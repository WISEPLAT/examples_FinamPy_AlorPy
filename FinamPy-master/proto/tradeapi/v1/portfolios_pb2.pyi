"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import proto.tradeapi.v1.common_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class PortfolioContent(google.protobuf.message.Message):
    """What kind of data the response contains.
    Какие данные будут в ответе.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCLUDE_CURRENCIES_FIELD_NUMBER: builtins.int
    INCLUDE_MONEY_FIELD_NUMBER: builtins.int
    INCLUDE_POSITIONS_FIELD_NUMBER: builtins.int
    INCLUDE_MAX_BUY_SELL_FIELD_NUMBER: builtins.int
    include_currencies: builtins.bool
    """Currency positions.
    Валютные позиции.
    """
    include_money: builtins.bool
    """Money positions.
    Денежные позиции.
    """
    include_positions: builtins.bool
    """DEPO positions.
    Позиции DEPO.
    """
    include_max_buy_sell: builtins.bool
    """Buy and Sell limits.
    Лимиты покупки и продажи.
    """
    def __init__(
        self,
        *,
        include_currencies: builtins.bool = ...,
        include_money: builtins.bool = ...,
        include_positions: builtins.bool = ...,
        include_max_buy_sell: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["include_currencies", b"include_currencies", "include_max_buy_sell", b"include_max_buy_sell", "include_money", b"include_money", "include_positions", b"include_positions"]) -> None: ...

global___PortfolioContent = PortfolioContent

@typing_extensions.final
class PositionRow(google.protobuf.message.Message):
    """DEPO position.
    Позиция DEPO.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SECURITY_CODE_FIELD_NUMBER: builtins.int
    MARKET_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    CURRENT_PRICE_FIELD_NUMBER: builtins.int
    EQUITY_FIELD_NUMBER: builtins.int
    AVERAGE_PRICE_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    ACCUMULATED_PROFIT_FIELD_NUMBER: builtins.int
    TODAY_PROFIT_FIELD_NUMBER: builtins.int
    UNREALIZED_PROFIT_FIELD_NUMBER: builtins.int
    PROFIT_FIELD_NUMBER: builtins.int
    MAX_BUY_FIELD_NUMBER: builtins.int
    MAX_SELL_FIELD_NUMBER: builtins.int
    PRICE_CURRENCY_FIELD_NUMBER: builtins.int
    AVERAGE_PRICE_CURRENCY_FIELD_NUMBER: builtins.int
    AVERAGE_RATE_FIELD_NUMBER: builtins.int
    security_code: builtins.str
    """Security Code.
    Тикер инструмента.
    """
    market: proto.tradeapi.v1.common_pb2.Market.ValueType
    """Security market.
    Рынок инструмента.
    """
    balance: builtins.int
    """Current position, items.
    Текущая позиция, шт.
    """
    current_price: builtins.float
    """Current price in price_currency.
    Текущая цена в валюте цены инструмента.
    """
    equity: builtins.float
    """Positions equity.
    Оценка позиции по инструменту в валюте риска.
    """
    average_price: builtins.float
    """Balanced price of security in price_currency.
    Балансовая цена в валюте цены инструмента.
    """
    currency: builtins.str
    """Risk currency.
    Валюта риска.
    """
    accumulated_profit: builtins.float
    """P/L for initial position, in risk currency.
    Прибыль/убыток по входящей позиции, в валюте риска.
    """
    today_profit: builtins.float
    """Daily P/L, in risk currency.
    Прибыль/убыток по сделкам за день, в валюте риска.
    """
    unrealized_profit: builtins.float
    """Unrealized P/L, in average_price_currency.
    Нереализованные прибыль/убытки по балансовой цене в валюте инструмента.
    """
    profit: builtins.float
    """P/L in price_currency.
    Прибыль/убытки в валюте цены инструмента.
    """
    max_buy: builtins.int
    """Max lots to buy.
    Максимальное кол-во лотов, доступных для покупки.
    """
    max_sell: builtins.int
    """Max lots to sell.
    Максимальное кол-во лотов, доступных для продажи.
    """
    price_currency: builtins.str
    """Security price currency.
    Валюта цены инструмента.
    """
    average_price_currency: builtins.str
    """Balanced price currency.
    Валюта балансовой цены.
    """
    average_rate: builtins.float
    """Risk Currency to Price currency Cross rate.
    Кросс-курс валюты балансовой цены к валюте риска.
    """
    def __init__(
        self,
        *,
        security_code: builtins.str = ...,
        market: proto.tradeapi.v1.common_pb2.Market.ValueType = ...,
        balance: builtins.int = ...,
        current_price: builtins.float = ...,
        equity: builtins.float = ...,
        average_price: builtins.float = ...,
        currency: builtins.str = ...,
        accumulated_profit: builtins.float = ...,
        today_profit: builtins.float = ...,
        unrealized_profit: builtins.float = ...,
        profit: builtins.float = ...,
        max_buy: builtins.int = ...,
        max_sell: builtins.int = ...,
        price_currency: builtins.str = ...,
        average_price_currency: builtins.str = ...,
        average_rate: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["accumulated_profit", b"accumulated_profit", "average_price", b"average_price", "average_price_currency", b"average_price_currency", "average_rate", b"average_rate", "balance", b"balance", "currency", b"currency", "current_price", b"current_price", "equity", b"equity", "market", b"market", "max_buy", b"max_buy", "max_sell", b"max_sell", "price_currency", b"price_currency", "profit", b"profit", "security_code", b"security_code", "today_profit", b"today_profit", "unrealized_profit", b"unrealized_profit"]) -> None: ...

global___PositionRow = PositionRow

@typing_extensions.final
class CurrencyRow(google.protobuf.message.Message):
    """Currency position.
    Валютная позиция.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    CROSS_RATE_FIELD_NUMBER: builtins.int
    EQUITY_FIELD_NUMBER: builtins.int
    UNREALIZED_PROFIT_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Currency code.
    Код валюты.
    """
    balance: builtins.float
    """Current position.
    Текущая позиция.
    """
    cross_rate: builtins.float
    """Currency rate for RUB.
    Курс валюты к рублю.
    """
    equity: builtins.float
    """Equity in RUB.
    Оценка в рублях.
    """
    unrealized_profit: builtins.float
    """Unrealized P/L, in RUB.
    Нереализованные прибыль/убытки в рублях.
    """
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        balance: builtins.float = ...,
        cross_rate: builtins.float = ...,
        equity: builtins.float = ...,
        unrealized_profit: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance", b"balance", "cross_rate", b"cross_rate", "equity", b"equity", "name", b"name", "unrealized_profit", b"unrealized_profit"]) -> None: ...

global___CurrencyRow = CurrencyRow

@typing_extensions.final
class MoneyRow(google.protobuf.message.Message):
    """Money position.
    Денежная позиция.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MARKET_FIELD_NUMBER: builtins.int
    CURRENCY_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    market: proto.tradeapi.v1.common_pb2.Market.ValueType
    """Position market.
    Рынок позиции.
    """
    currency: builtins.str
    """Currency code.
    Код валюты.
    """
    balance: builtins.float
    """Current position.
    Текущая позиция.
    """
    def __init__(
        self,
        *,
        market: proto.tradeapi.v1.common_pb2.Market.ValueType = ...,
        currency: builtins.str = ...,
        balance: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance", b"balance", "currency", b"currency", "market", b"market"]) -> None: ...

global___MoneyRow = MoneyRow

@typing_extensions.final
class GetPortfolioRequest(google.protobuf.message.Message):
    """Get Portfolio Request.
    Запрос портфеля.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    @property
    def content(self) -> global___PortfolioContent:
        """What data to return by request.
        Какие данные возвращать в ответе.
        """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        content: global___PortfolioContent | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content", b"content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["client_id", b"client_id", "content", b"content"]) -> None: ...

global___GetPortfolioRequest = GetPortfolioRequest

@typing_extensions.final
class GetPortfolioResult(google.protobuf.message.Message):
    """GetPortfolioRequest result.
    Результат GetPortfolioRequest.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_ID_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    EQUITY_FIELD_NUMBER: builtins.int
    BALANCE_FIELD_NUMBER: builtins.int
    POSITIONS_FIELD_NUMBER: builtins.int
    CURRENCIES_FIELD_NUMBER: builtins.int
    MONEY_FIELD_NUMBER: builtins.int
    client_id: builtins.str
    """Trade Account ID.
    Идентификатор торгового счёта.
    """
    @property
    def content(self) -> global___PortfolioContent:
        """What kind of data the response contains.
        Какие данные будут в ответе.
        """
    equity: builtins.float
    """Current equity, RUB.
    Текущая оценка портфеля в рублях.
    """
    balance: builtins.float
    """Open Equity, RUB.
    Входящая оценка портфеля в рублях.
    """
    @property
    def positions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PositionRow]:
        """DEPO positions.
        Позиции DEPO.
        """
    @property
    def currencies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CurrencyRow]:
        """Currency positions.
        Валютные позиции.
        """
    @property
    def money(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MoneyRow]:
        """Money positions.
        Денежные позиции.
        """
    def __init__(
        self,
        *,
        client_id: builtins.str = ...,
        content: global___PortfolioContent | None = ...,
        equity: builtins.float = ...,
        balance: builtins.float = ...,
        positions: collections.abc.Iterable[global___PositionRow] | None = ...,
        currencies: collections.abc.Iterable[global___CurrencyRow] | None = ...,
        money: collections.abc.Iterable[global___MoneyRow] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["content", b"content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["balance", b"balance", "client_id", b"client_id", "content", b"content", "currencies", b"currencies", "equity", b"equity", "money", b"money", "positions", b"positions"]) -> None: ...

global___GetPortfolioResult = GetPortfolioResult
