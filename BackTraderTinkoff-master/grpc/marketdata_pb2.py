# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: marketdata.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10marketdata.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xf4\x04\n\x11MarketDataRequest\x12\x63\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequestH\x00\x12h\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequestH\x00\x12\x61\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequestH\x00\x12]\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequestH\x00\x12h\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequestH\x00\x12Y\n\x14get_my_subscriptions\x18\x06 \x01(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.GetMySubscriptionsH\x00\x42\t\n\x07payload\"\x94\x04\n!MarketDataServerSideStreamRequest\x12\x61\n\x19subscribe_candles_request\x18\x01 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeCandlesRequest\x12\x66\n\x1csubscribe_order_book_request\x18\x02 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookRequest\x12_\n\x18subscribe_trades_request\x18\x03 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.SubscribeTradesRequest\x12[\n\x16subscribe_info_request\x18\x04 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscribeInfoRequest\x12\x66\n\x1csubscribe_last_price_request\x18\x05 \x01(\x0b\x32@.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceRequest\"\xc0\x07\n\x12MarketDataResponse\x12\x65\n\x1asubscribe_candles_response\x18\x01 \x01(\x0b\x32?.tinkoff.public.invest.api.contract.v1.SubscribeCandlesResponseH\x00\x12j\n\x1dsubscribe_order_book_response\x18\x02 \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeOrderBookResponseH\x00\x12\x63\n\x19subscribe_trades_response\x18\x03 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.SubscribeTradesResponseH\x00\x12_\n\x17subscribe_info_response\x18\x04 \x01(\x0b\x32<.tinkoff.public.invest.api.contract.v1.SubscribeInfoResponseH\x00\x12?\n\x06\x63\x61ndle\x18\x05 \x01(\x0b\x32-.tinkoff.public.invest.api.contract.v1.CandleH\x00\x12=\n\x05trade\x18\x06 \x01(\x0b\x32,.tinkoff.public.invest.api.contract.v1.TradeH\x00\x12\x45\n\torderbook\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.OrderBookH\x00\x12N\n\x0etrading_status\x18\x08 \x01(\x0b\x32\x34.tinkoff.public.invest.api.contract.v1.TradingStatusH\x00\x12;\n\x04ping\x18\t \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x12j\n\x1dsubscribe_last_price_response\x18\n \x01(\x0b\x32\x41.tinkoff.public.invest.api.contract.v1.SubscribeLastPriceResponseH\x00\x12\x46\n\nlast_price\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPriceH\x00\x42\t\n\x07payload\"\xd6\x01\n\x17SubscribeCandlesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12L\n\x0binstruments\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.CandleInstrument\x12\x15\n\rwaiting_close\x18\x03 \x01(\x08\"\x86\x01\n\x10\x43\x61ndleInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\"\x89\x01\n\x18SubscribeCandlesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12X\n\x15\x63\x61ndles_subscriptions\x18\x02 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.CandleSubscription\"\xe1\x01\n\x12\x43\x61ndleSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x04 \x01(\t\"\xc4\x01\n\x19SubscribeOrderBookRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.OrderBookInstrument\"I\n\x13OrderBookInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\"\x91\x01\n\x1aSubscribeOrderBookResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18order_book_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.OrderBookSubscription\"\xa4\x01\n\x15OrderBookSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12V\n\x13subscription_status\x18\x03 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x04 \x01(\t\"\xbd\x01\n\x16SubscribeTradesRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12K\n\x0binstruments\x18\x02 \x03(\x0b\x32\x36.tinkoff.public.invest.api.contract.v1.TradeInstrument\"6\n\x0fTradeInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x85\x01\n\x17SubscribeTradesResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12U\n\x13trade_subscriptions\x18\x02 \x03(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.TradeSubscription\"\x91\x01\n\x11TradeSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\"\xba\x01\n\x14SubscribeInfoRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12J\n\x0binstruments\x18\x02 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.InfoInstrument\"5\n\x0eInfoInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x81\x01\n\x15SubscribeInfoResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12S\n\x12info_subscriptions\x18\x02 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.InfoSubscription\"\x90\x01\n\x10InfoSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\"\xc4\x01\n\x19SubscribeLastPriceRequest\x12V\n\x13subscription_action\x18\x01 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionAction\x12O\n\x0binstruments\x18\x02 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.LastPriceInstrument\":\n\x13LastPriceInstrument\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"\x91\x01\n\x1aSubscribeLastPriceResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12^\n\x18last_price_subscriptions\x18\x02 \x03(\x0b\x32<.tinkoff.public.invest.api.contract.v1.LastPriceSubscription\"\x95\x01\n\x15LastPriceSubscription\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12V\n\x13subscription_status\x18\x02 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.SubscriptionStatus\x12\x16\n\x0einstrument_uid\x18\x03 \x01(\t\"\xea\x03\n\x06\x43\x61ndle\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12M\n\x08interval\x18\x02 \x01(\x0e\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionInterval\x12>\n\x04open\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x07 \x01(\x03\x12(\n\x04time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rlast_trade_ts\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\n \x01(\t\"\x83\x03\n\tOrderBook\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\ris_consistent\x18\x03 \x01(\x08\x12:\n\x04\x62ids\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x05 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x16\n\x0einstrument_uid\x18\t \x01(\t\"Z\n\x05Order\x12?\n\x05price\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x02 \x01(\x03\"\xf4\x01\n\x05Trade\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12H\n\tdirection\x18\x02 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.TradeDirection\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12(\n\x04time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\"\xfe\x01\n\rTradingStatus\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x1alimit_order_available_flag\x18\x04 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x05 \x01(\x08\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\"\xd3\x01\n\x11GetCandlesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12G\n\x08interval\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.CandleInterval\x12\x15\n\rinstrument_id\x18\x05 \x01(\t\"\\\n\x12GetCandlesResponse\x12\x46\n\x07\x63\x61ndles\x18\x01 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.HistoricCandle\"\xdf\x02\n\x0eHistoricCandle\x12>\n\x04open\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12>\n\x04high\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03low\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12?\n\x05\x63lose\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0e\n\x06volume\x18\x05 \x01(\x03\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bis_complete\x18\x07 \x01(\x08\";\n\x14GetLastPricesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x03(\t\x12\x15\n\rinstrument_id\x18\x02 \x03(\t\"^\n\x15GetLastPricesResponse\x12\x45\n\x0blast_prices\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.LastPrice\"\x9c\x01\n\tLastPrice\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x0b \x01(\t\"I\n\x13GetOrderBookRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x15\n\rinstrument_id\x18\x03 \x01(\t\"\xf3\x04\n\x14GetOrderBookResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12:\n\x04\x62ids\x18\x03 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12:\n\x04\x61sks\x18\x04 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Order\x12\x44\n\nlast_price\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x45\n\x0b\x63lose_price\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x42\n\x08limit_up\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nlimit_down\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x31\n\rlast_price_ts\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0e\x63lose_price_ts\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0corderbook_ts\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\t \x01(\t\">\n\x17GetTradingStatusRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\"2\n\x19GetTradingStatusesRequest\x12\x15\n\rinstrument_id\x18\x01 \x03(\t\"w\n\x1aGetTradingStatusesResponse\x12Y\n\x10trading_statuses\x18\x01 \x03(\x0b\x32?.tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse\"\x81\x02\n\x18GetTradingStatusResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12T\n\x0etrading_status\x18\x02 \x01(\x0e\x32<.tinkoff.public.invest.api.contract.v1.SecurityTradingStatus\x12\"\n\x1alimit_order_available_flag\x18\x03 \x01(\x08\x12#\n\x1bmarket_order_available_flag\x18\x04 \x01(\x08\x12 \n\x18\x61pi_trade_available_flag\x18\x05 \x01(\x08\x12\x16\n\x0einstrument_uid\x18\x06 \x01(\t\"\x8d\x01\n\x14GetLastTradesRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rinstrument_id\x18\x04 \x01(\t\"U\n\x15GetLastTradesResponse\x12<\n\x06trades\x18\x01 \x03(\x0b\x32,.tinkoff.public.invest.api.contract.v1.Trade\"\x14\n\x12GetMySubscriptions\"p\n\x15GetClosePricesRequest\x12W\n\x0binstruments\x18\x01 \x03(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.InstrumentClosePriceRequest\"4\n\x1bInstrumentClosePriceRequest\x12\x15\n\rinstrument_id\x18\x01 \x01(\t\"s\n\x16GetClosePricesResponse\x12Y\n\x0c\x63lose_prices\x18\x01 \x03(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.InstrumentClosePriceResponse\"\xaf\x01\n\x1cInstrumentClosePriceResponse\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12?\n\x05price\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12(\n\x04time\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp*\x81\x01\n\x12SubscriptionAction\x12#\n\x1fSUBSCRIPTION_ACTION_UNSPECIFIED\x10\x00\x12!\n\x1dSUBSCRIPTION_ACTION_SUBSCRIBE\x10\x01\x12#\n\x1fSUBSCRIPTION_ACTION_UNSUBSCRIBE\x10\x02*\x8b\x01\n\x14SubscriptionInterval\x12%\n!SUBSCRIPTION_INTERVAL_UNSPECIFIED\x10\x00\x12$\n SUBSCRIPTION_INTERVAL_ONE_MINUTE\x10\x01\x12&\n\"SUBSCRIPTION_INTERVAL_FIVE_MINUTES\x10\x02*\x95\x03\n\x12SubscriptionStatus\x12#\n\x1fSUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12,\n(SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND\x10\x02\x12\x36\n2SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID\x10\x03\x12(\n$SUBSCRIPTION_STATUS_DEPTH_IS_INVALID\x10\x04\x12+\n\'SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID\x10\x05\x12)\n%SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED\x10\x06\x12&\n\"SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x07\x12)\n%SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS\x10\x08*d\n\x0eTradeDirection\x12\x1f\n\x1bTRADE_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13TRADE_DIRECTION_BUY\x10\x01\x12\x18\n\x14TRADE_DIRECTION_SELL\x10\x02*\x91\x03\n\x0e\x43\x61ndleInterval\x12\x1f\n\x1b\x43\x41NDLE_INTERVAL_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43\x41NDLE_INTERVAL_1_MIN\x10\x01\x12\x19\n\x15\x43\x41NDLE_INTERVAL_5_MIN\x10\x02\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_15_MIN\x10\x03\x12\x18\n\x14\x43\x41NDLE_INTERVAL_HOUR\x10\x04\x12\x17\n\x13\x43\x41NDLE_INTERVAL_DAY\x10\x05\x12\x19\n\x15\x43\x41NDLE_INTERVAL_2_MIN\x10\x06\x12\x19\n\x15\x43\x41NDLE_INTERVAL_3_MIN\x10\x07\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_10_MIN\x10\x08\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_30_MIN\x10\t\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_2_HOUR\x10\n\x12\x1a\n\x16\x43\x41NDLE_INTERVAL_4_HOUR\x10\x0b\x12\x18\n\x14\x43\x41NDLE_INTERVAL_WEEK\x10\x0c\x12\x19\n\x15\x43\x41NDLE_INTERVAL_MONTH\x10\r2\xfd\x07\n\x11MarketDataService\x12\x81\x01\n\nGetCandles\x12\x38.tinkoff.public.invest.api.contract.v1.GetCandlesRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetCandlesResponse\x12\x8a\x01\n\rGetLastPrices\x12;.tinkoff.public.invest.api.contract.v1.GetLastPricesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastPricesResponse\x12\x87\x01\n\x0cGetOrderBook\x12:.tinkoff.public.invest.api.contract.v1.GetOrderBookRequest\x1a;.tinkoff.public.invest.api.contract.v1.GetOrderBookResponse\x12\x93\x01\n\x10GetTradingStatus\x12>.tinkoff.public.invest.api.contract.v1.GetTradingStatusRequest\x1a?.tinkoff.public.invest.api.contract.v1.GetTradingStatusResponse\x12\x99\x01\n\x12GetTradingStatuses\x12@.tinkoff.public.invest.api.contract.v1.GetTradingStatusesRequest\x1a\x41.tinkoff.public.invest.api.contract.v1.GetTradingStatusesResponse\x12\x8a\x01\n\rGetLastTrades\x12;.tinkoff.public.invest.api.contract.v1.GetLastTradesRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetLastTradesResponse\x12\x8d\x01\n\x0eGetClosePrices\x12<.tinkoff.public.invest.api.contract.v1.GetClosePricesRequest\x1a=.tinkoff.public.invest.api.contract.v1.GetClosePricesResponse2\xcd\x02\n\x17MarketDataStreamService\x12\x8b\x01\n\x10MarketDataStream\x12\x38.tinkoff.public.invest.api.contract.v1.MarketDataRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse(\x01\x30\x01\x12\xa3\x01\n\x1aMarketDataServerSideStream\x12H.tinkoff.public.invest.api.contract.v1.MarketDataServerSideStreamRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.MarketDataResponse0\x01\x42\x61\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'marketdata_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _SUBSCRIPTIONACTION._serialized_start=9536
  _SUBSCRIPTIONACTION._serialized_end=9665
  _SUBSCRIPTIONINTERVAL._serialized_start=9668
  _SUBSCRIPTIONINTERVAL._serialized_end=9807
  _SUBSCRIPTIONSTATUS._serialized_start=9810
  _SUBSCRIPTIONSTATUS._serialized_end=10215
  _TRADEDIRECTION._serialized_start=10217
  _TRADEDIRECTION._serialized_end=10317
  _CANDLEINTERVAL._serialized_start=10320
  _CANDLEINTERVAL._serialized_end=10721
  _MARKETDATAREQUEST._serialized_start=107
  _MARKETDATAREQUEST._serialized_end=735
  _MARKETDATASERVERSIDESTREAMREQUEST._serialized_start=738
  _MARKETDATASERVERSIDESTREAMREQUEST._serialized_end=1270
  _MARKETDATARESPONSE._serialized_start=1273
  _MARKETDATARESPONSE._serialized_end=2233
  _SUBSCRIBECANDLESREQUEST._serialized_start=2236
  _SUBSCRIBECANDLESREQUEST._serialized_end=2450
  _CANDLEINSTRUMENT._serialized_start=2453
  _CANDLEINSTRUMENT._serialized_end=2587
  _SUBSCRIBECANDLESRESPONSE._serialized_start=2590
  _SUBSCRIBECANDLESRESPONSE._serialized_end=2727
  _CANDLESUBSCRIPTION._serialized_start=2730
  _CANDLESUBSCRIPTION._serialized_end=2955
  _SUBSCRIBEORDERBOOKREQUEST._serialized_start=2958
  _SUBSCRIBEORDERBOOKREQUEST._serialized_end=3154
  _ORDERBOOKINSTRUMENT._serialized_start=3156
  _ORDERBOOKINSTRUMENT._serialized_end=3229
  _SUBSCRIBEORDERBOOKRESPONSE._serialized_start=3232
  _SUBSCRIBEORDERBOOKRESPONSE._serialized_end=3377
  _ORDERBOOKSUBSCRIPTION._serialized_start=3380
  _ORDERBOOKSUBSCRIPTION._serialized_end=3544
  _SUBSCRIBETRADESREQUEST._serialized_start=3547
  _SUBSCRIBETRADESREQUEST._serialized_end=3736
  _TRADEINSTRUMENT._serialized_start=3738
  _TRADEINSTRUMENT._serialized_end=3792
  _SUBSCRIBETRADESRESPONSE._serialized_start=3795
  _SUBSCRIBETRADESRESPONSE._serialized_end=3928
  _TRADESUBSCRIPTION._serialized_start=3931
  _TRADESUBSCRIPTION._serialized_end=4076
  _SUBSCRIBEINFOREQUEST._serialized_start=4079
  _SUBSCRIBEINFOREQUEST._serialized_end=4265
  _INFOINSTRUMENT._serialized_start=4267
  _INFOINSTRUMENT._serialized_end=4320
  _SUBSCRIBEINFORESPONSE._serialized_start=4323
  _SUBSCRIBEINFORESPONSE._serialized_end=4452
  _INFOSUBSCRIPTION._serialized_start=4455
  _INFOSUBSCRIPTION._serialized_end=4599
  _SUBSCRIBELASTPRICEREQUEST._serialized_start=4602
  _SUBSCRIBELASTPRICEREQUEST._serialized_end=4798
  _LASTPRICEINSTRUMENT._serialized_start=4800
  _LASTPRICEINSTRUMENT._serialized_end=4858
  _SUBSCRIBELASTPRICERESPONSE._serialized_start=4861
  _SUBSCRIBELASTPRICERESPONSE._serialized_end=5006
  _LASTPRICESUBSCRIPTION._serialized_start=5009
  _LASTPRICESUBSCRIPTION._serialized_end=5158
  _CANDLE._serialized_start=5161
  _CANDLE._serialized_end=5651
  _ORDERBOOK._serialized_start=5654
  _ORDERBOOK._serialized_end=6041
  _ORDER._serialized_start=6043
  _ORDER._serialized_end=6133
  _TRADE._serialized_start=6136
  _TRADE._serialized_end=6380
  _TRADINGSTATUS._serialized_start=6383
  _TRADINGSTATUS._serialized_end=6637
  _GETCANDLESREQUEST._serialized_start=6640
  _GETCANDLESREQUEST._serialized_end=6851
  _GETCANDLESRESPONSE._serialized_start=6853
  _GETCANDLESRESPONSE._serialized_end=6945
  _HISTORICCANDLE._serialized_start=6948
  _HISTORICCANDLE._serialized_end=7299
  _GETLASTPRICESREQUEST._serialized_start=7301
  _GETLASTPRICESREQUEST._serialized_end=7360
  _GETLASTPRICESRESPONSE._serialized_start=7362
  _GETLASTPRICESRESPONSE._serialized_end=7456
  _LASTPRICE._serialized_start=7459
  _LASTPRICE._serialized_end=7615
  _GETORDERBOOKREQUEST._serialized_start=7617
  _GETORDERBOOKREQUEST._serialized_end=7690
  _GETORDERBOOKRESPONSE._serialized_start=7693
  _GETORDERBOOKRESPONSE._serialized_end=8320
  _GETTRADINGSTATUSREQUEST._serialized_start=8322
  _GETTRADINGSTATUSREQUEST._serialized_end=8384
  _GETTRADINGSTATUSESREQUEST._serialized_start=8386
  _GETTRADINGSTATUSESREQUEST._serialized_end=8436
  _GETTRADINGSTATUSESRESPONSE._serialized_start=8438
  _GETTRADINGSTATUSESRESPONSE._serialized_end=8557
  _GETTRADINGSTATUSRESPONSE._serialized_start=8560
  _GETTRADINGSTATUSRESPONSE._serialized_end=8817
  _GETLASTTRADESREQUEST._serialized_start=8820
  _GETLASTTRADESREQUEST._serialized_end=8961
  _GETLASTTRADESRESPONSE._serialized_start=8963
  _GETLASTTRADESRESPONSE._serialized_end=9048
  _GETMYSUBSCRIPTIONS._serialized_start=9050
  _GETMYSUBSCRIPTIONS._serialized_end=9070
  _GETCLOSEPRICESREQUEST._serialized_start=9072
  _GETCLOSEPRICESREQUEST._serialized_end=9184
  _INSTRUMENTCLOSEPRICEREQUEST._serialized_start=9186
  _INSTRUMENTCLOSEPRICEREQUEST._serialized_end=9238
  _GETCLOSEPRICESRESPONSE._serialized_start=9240
  _GETCLOSEPRICESRESPONSE._serialized_end=9355
  _INSTRUMENTCLOSEPRICERESPONSE._serialized_start=9358
  _INSTRUMENTCLOSEPRICERESPONSE._serialized_end=9533
  _MARKETDATASERVICE._serialized_start=10724
  _MARKETDATASERVICE._serialized_end=11745
  _MARKETDATASTREAMSERVICE._serialized_start=11748
  _MARKETDATASTREAMSERVICE._serialized_end=12081
# @@protoc_insertion_point(module_scope)
