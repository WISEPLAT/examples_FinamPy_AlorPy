import collections
from datetime import timedelta

from backtrader.metabase import MetaParams
from backtrader.utils.py3 import with_metaclass
from backtrader import TimeFrame

from AlorPy import AlorPy


class MetaSingleton(MetaParams):
    """Метакласс для создания Singleton классов"""
    def __init__(cls, *args, **kwargs):
        """Инициализация класса"""
        super(MetaSingleton, cls).__init__(*args, **kwargs)
        cls._singleton = None  # Экземпляра класса еще нет

    def __call__(cls, *args, **kwargs):
        """Вызов класса"""
        if cls._singleton is None:  # Если класса нет в экземплярах класса
            cls._singleton = super(MetaSingleton, cls).__call__(*args, **kwargs)  # то создаем зкземпляр класса
        return cls._singleton  # Возвращаем экземпляр класса


class ALStore(with_metaclass(MetaSingleton, object)):
    """Хранилище Алор. Работает с мультисчетами и мультипортфелями

    В параметр providers передавать список счетов в виде словаря с ключами:
    - provider_name - Название провайдера. Должно быть уникальным
    - demo - Режим демо торговли. Можно не указывать. Тогда будет выбран режим реальной торговли
    - username - Имя пользователя из Config
    - refresh_token - Токен из Config

    Пример использования:
    provider1 = dict(provider_name='alor_trade', username=Config.UserName, demo=False, refresh_token=Config.RefreshToken)  # Торговый счет Алор
    provider2 = dict(provider_name='alor_iia', username=ConfigIIA.UserName, demo=False, refresh_token=ConfigIIA.RefreshToken)  # ИИС Алор
    store = ALStore(providers=[provider1, provider2])  # Мультисчет
    """
    params = (
        ('providers', None),  # Список провайдеров счетов в виде словаря
    )

    BrokerCls = None  # Класс брокера будет задан из брокера
    DataCls = None  # Класс данных будет задан из данных

    @classmethod
    def getdata(cls, *args, **kwargs):
        """Возвращает новый экземпляр класса данных с заданными параметрами"""
        return cls.DataCls(*args, **kwargs)

    @classmethod
    def getbroker(cls, *args, **kwargs):
        """Возвращает новый экземпляр класса брокера с заданными параметрами"""
        return cls.BrokerCls(*args, **kwargs)

    def __init__(self, **kwargs):
        super(ALStore, self).__init__()
        if 'providers' in kwargs:  # Если хранилище создаем из данных/брокера (не рекомендуется)
            self.p.providers = kwargs['providers']  # то список провайдеров берем из переданного ключа providers
        self.notifs = collections.deque()  # Уведомления хранилища
        self.providers = {}  # Справочник провайдеров
        for provider in self.p.providers:  # Пробегаемся по всем провайдерам
            demo = provider['demo'] if 'demo' in provider else False  # Признак демо счета или реальный счет
            provider_name = provider['provider_name'] if 'provider_name' in provider else 'default'  # Название провайдера или название по умолчанию
            self.providers[provider_name] = AlorPy(provider['username'], provider['refresh_token'], demo)  # Работа с Alor OpenAPI V2 из Python https://alor.dev/docs с именем пользователя и токеном
        self.provider = list(self.providers.values())[0]  # Провайдер по умолчанию для работы со справочниками. Первый счет по ключу name
        self.new_bars = []  # Новые бары по всем подпискам на тикеры из Алор

    def start(self):
        for name, provider in self.providers.items():  # Пробегаемся по всем провайдерам
            # События WebSocket Thread/Task для понимания, что происходит с провайдером
            provider.OnEntering = lambda n=name: print(f'- WebSocket Thread({n}): Запуск')
            provider.OnEnter = lambda n=name: print(f'- WebSocket Thread({n}): Запущен')
            provider.OnConnect = lambda n=name: print(f'- WebSocket Task({n}): Подключен к серверу')
            provider.OnResubscribe = lambda n=name: print(f'- WebSocket Task({n}): Возобновление подписок ({len(provider.subscriptions)})')
            provider.OnReady = lambda n=name: print(f'- WebSocket Task({n}): Готов')
            provider.OnDisconnect = lambda n=name: print(f'- WebSocket Task({n}): Отключен от сервера')
            provider.OnTimeout = lambda n=name: print(f'- WebSocket Task({n}): Таймаут')
            provider.OnError = lambda response,  n=name: print(f'- WebSocket Task({n}): {response}')
            provider.OnCancel = lambda n=name: print(f'- WebSocket Task({n}): Отмена')
            provider.OnExit = lambda n=name: print(f'- WebSocket Thread({n}): Завершение')
            provider.OnNewBar = lambda response, n=name: self.new_bars.append(dict(provider_name=n, response=response))  # Обработчик новых баров по подписке из Алор

    def put_notification(self, msg, *args, **kwargs):
        self.notifs.append((msg, args, kwargs))

    def get_notifications(self):
        """Выдача уведомлений хранилища"""
        self.notifs.append(None)
        return [x for x in iter(self.notifs.popleft, None)]

    def stop(self):
        for provider in self.providers.values():  # Пробегаемся по всем значениям провайдеров
            provider.OnNewBar = provider.default_handler  # Возвращаем обработчик по умолчанию
            provider.close_web_socket()  # Перед выходом закрываем соединение с WebSocket

    # Функции конвертации

    @staticmethod
    def timeframe_to_alor_timeframe(timeframe, compression) -> str:
        """Перевод временнОго интервала во временной интервал Алор

        :param TimeFrame timeframe: Временной интервал
        :param int compression: Размер временнОго интервала
        :return: Временной интервал Алор
        """
        if timeframe == TimeFrame.Days:  # Дневной временной интервал (по умолчанию)
            return 'D'
        elif timeframe == TimeFrame.Weeks:  # Недельный временной интервал
            return 'W'
        elif timeframe == TimeFrame.Months:  # Месячный временной интервал
            return 'M'
        elif timeframe == TimeFrame.Years:  # Годовой временной интервал
            return 'Y'
        elif timeframe == TimeFrame.Minutes:  # Минутный временной интервал
            return str(compression * 60)  # Переводим в секунды
        elif timeframe == TimeFrame.Seconds:  # Секундный временной интервал
            return str(compression)

    @staticmethod
    def timeframe_to_timedelta(timeframe, compression) -> timedelta:
        """Перевод временнОго интервала в разницу во времени

        :param TimeFrame timeframe: Временной интервал
        :param int compression: Размер временнОго интервала
        :return: Разница во времени
        """
        if timeframe == TimeFrame.Days:  # Дневной временной интервал (по умолчанию)
            return timedelta(days=1)
        elif timeframe == TimeFrame.Weeks:  # Недельный временной интервал
            return timedelta(weeks=1)
        elif timeframe == TimeFrame.Months:  # Месячный временной интервал
            raise NotImplementedError  # TODO В месяце разное кол-во дней
        elif timeframe == TimeFrame.Years:  # Годовой временной интервал
            raise NotImplementedError  # TODO В году разное кол-во дней
        elif timeframe == TimeFrame.Minutes:  # Минутный временной интервал
            return timedelta(minutes=compression)
        elif timeframe == TimeFrame.Seconds:  # Секундный временной интервал
            return timedelta(seconds=compression)
