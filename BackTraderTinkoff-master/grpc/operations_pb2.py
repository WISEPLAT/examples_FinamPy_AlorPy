# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10operations.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\xcd\x01\n\x11OperationsRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x44\n\x05state\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x0c\n\x04\x66igi\x18\x05 \x01(\t\"Z\n\x12OperationsResponse\x12\x44\n\noperations\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Operation\"\xf0\x04\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1b\n\x13parent_operation_id\x18\x02 \x01(\t\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\x12\x42\n\x07payment\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\x05state\x18\x06 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x10\n\x08quantity\x18\x07 \x01(\x03\x12\x15\n\rquantity_rest\x18\x08 \x01(\x03\x12\x0c\n\x04\x66igi\x18\t \x01(\t\x12\x17\n\x0finstrument_type\x18\n \x01(\t\x12(\n\x04\x64\x61te\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x0c \x01(\t\x12L\n\x0eoperation_type\x18\r \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12\x45\n\x06trades\x18\x0e \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.OperationTrade\x12\x11\n\tasset_uid\x18\x10 \x01(\t\x12\x14\n\x0cposition_uid\x18\x11 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x12 \x01(\t\"\xa5\x01\n\x0eOperationTrade\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12-\n\tdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12@\n\x05price\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xaf\x01\n\x10PortfolioRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12Y\n\x08\x63urrency\x18\x02 \x01(\x0e\x32G.tinkoff.public.invest.api.contract.v1.PortfolioRequest.CurrencyRequest\",\n\x0f\x43urrencyRequest\x12\x07\n\x03RUB\x10\x00\x12\x07\n\x03USD\x10\x01\x12\x07\n\x03\x45UR\x10\x02\"\x9b\x07\n\x11PortfolioResponse\x12N\n\x13total_amount_shares\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_amount_bonds\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12K\n\x10total_amount_etf\x18\x03 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12R\n\x17total_amount_currencies\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14total_amount_futures\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12K\n\tpositions\x18\x07 \x03(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.PortfolioPosition\x12\x12\n\naccount_id\x18\x08 \x01(\t\x12O\n\x14total_amount_options\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0ftotal_amount_sp\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16total_amount_portfolio\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Z\n\x11virtual_positions\x18\x0c \x03(\x0b\x32?.tinkoff.public.invest.api.contract.v1.VirtualPortfolioPosition\"&\n\x10PositionsRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\xa1\x03\n\x11PositionsResponse\x12@\n\x05money\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x42\n\x07\x62locked\x18\x02 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\nsecurities\x18\x03 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.PositionsSecurities\x12\"\n\x1alimits_loading_in_progress\x18\x04 \x01(\x08\x12H\n\x07\x66utures\x18\x05 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsFutures\x12H\n\x07options\x18\x06 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsOptions\"+\n\x15WithdrawLimitsRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\xec\x01\n\x16WithdrawLimitsResponse\x12@\n\x05money\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x42\n\x07\x62locked\x18\x02 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12L\n\x11\x62locked_guarantee\x18\x03 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xc0\x07\n\x11PortfolioPosition\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x42\n\x08quantity\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12Q\n\x16\x61verage_position_price\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x46\n\x0b\x63urrent_nkd\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12S\n\x19\x61verage_position_price_pt\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\rcurrent_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12V\n\x1b\x61verage_position_price_fifo\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12G\n\rquantity_lots\x18\n \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x0f\n\x07\x62locked\x18\x15 \x01(\x08\x12\x46\n\x0c\x62locked_lots\x18\x16 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x14\n\x0cposition_uid\x18\x18 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x19 \x01(\t\x12\x45\n\nvar_margin\x18\x1a \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x13\x65xpected_yield_fifo\x18\x1b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"\xf2\x04\n\x18VirtualPortfolioPosition\x12\x14\n\x0cposition_uid\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12\x17\n\x0finstrument_type\x18\x04 \x01(\t\x12\x42\n\x08quantity\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12Q\n\x16\x61verage_position_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x13\x65xpected_yield_fifo\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12/\n\x0b\x65xpire_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\rcurrent_price\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12V\n\x1b\x61verage_position_price_fifo\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xa6\x01\n\x13PositionsSecurities\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x14\n\x0cposition_uid\x18\x04 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x05 \x01(\t\x12\x18\n\x10\x65xchange_blocked\x18\x0b \x01(\x08\x12\x17\n\x0finstrument_type\x18\x10 \x01(\t\"p\n\x10PositionsFutures\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x14\n\x0cposition_uid\x18\x04 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x05 \x01(\t\"b\n\x10PositionsOptions\x12\x14\n\x0cposition_uid\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12\x0f\n\x07\x62locked\x18\x0b \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x15 \x01(\x03\"\xf2\x01\n\x13\x42rokerReportRequest\x12l\n\x1egenerate_broker_report_request\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.GenerateBrokerReportRequestH\x00\x12\x62\n\x19get_broker_report_request\x18\x02 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.GetBrokerReportRequestH\x00\x42\t\n\x07payload\"\xf7\x01\n\x14\x42rokerReportResponse\x12n\n\x1fgenerate_broker_report_response\x18\x01 \x01(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.GenerateBrokerReportResponseH\x00\x12\x64\n\x1aget_broker_report_response\x18\x02 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.GetBrokerReportResponseH\x00\x42\t\n\x07payload\"\x83\x01\n\x1bGenerateBrokerReportRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"/\n\x1cGenerateBrokerReportResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"7\n\x16GetBrokerReportRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\"\x9b\x01\n\x17GetBrokerReportResponse\x12J\n\rbroker_report\x18\x01 \x03(\x0b\x32\x33.tinkoff.public.invest.api.contract.v1.BrokerReport\x12\x12\n\nitemsCount\x18\x02 \x01(\x05\x12\x12\n\npagesCount\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\"\xda\x08\n\x0c\x42rokerReport\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12\x14\n\x0c\x65xecute_sign\x18\x04 \x01(\t\x12\x32\n\x0etrade_datetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x65xchange\x18\x06 \x01(\t\x12\x12\n\nclass_code\x18\x07 \x01(\t\x12\x11\n\tdirection\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06ticker\x18\n \x01(\t\x12@\n\x05price\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x0c \x01(\x03\x12G\n\x0corder_amount\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x43\n\taci_value\x18\x0e \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x12total_order_amount\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12L\n\x11\x62roker_commission\x18\x10 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xchange_commission\x18\x11 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12W\n\x1c\x65xchange_clearing_commission\x18\x12 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x43\n\trepo_rate\x18\x13 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\r\n\x05party\x18\x14 \x01(\t\x12\x34\n\x10\x63lear_value_date\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0esec_value_date\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rbroker_status\x18\x17 \x01(\t\x12\x1f\n\x17separate_agreement_type\x18\x18 \x01(\t\x12!\n\x19separate_agreement_number\x18\x19 \x01(\t\x12\x1f\n\x17separate_agreement_date\x18\x1a \x01(\t\x12\x15\n\rdelivery_type\x18\x1b \x01(\t\"\xa8\x02\n GetDividendsForeignIssuerRequest\x12\x80\x01\n\"generate_div_foreign_issuer_report\x18\x01 \x01(\x0b\x32R.tinkoff.public.invest.api.contract.v1.GenerateDividendsForeignIssuerReportRequestH\x00\x12v\n\x1dget_div_foreign_issuer_report\x18\x02 \x01(\x0b\x32M.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerReportRequestH\x00\x42\t\n\x07payload\"\xb0\x02\n!GetDividendsForeignIssuerResponse\x12\x8a\x01\n+generate_div_foreign_issuer_report_response\x18\x01 \x01(\x0b\x32S.tinkoff.public.invest.api.contract.v1.GenerateDividendsForeignIssuerReportResponseH\x00\x12s\n\x19\x64iv_foreign_issuer_report\x18\x02 \x01(\x0b\x32N.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerReportResponseH\x00\x42\t\n\x07payload\"\x93\x01\n+GenerateDividendsForeignIssuerReportRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12(\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"G\n&GetDividendsForeignIssuerReportRequest\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\"?\n,GenerateDividendsForeignIssuerReportResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"\xcd\x01\n\'GetDividendsForeignIssuerReportResponse\x12l\n\x1f\x64ividends_foreign_issuer_report\x18\x01 \x03(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.DividendsForeignIssuerReport\x12\x12\n\nitemsCount\x18\x02 \x01(\x05\x12\x12\n\npagesCount\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\"\xc9\x04\n\x1c\x44ividendsForeignIssuerReport\x12/\n\x0brecord_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpayment_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rsecurity_name\x18\x03 \x01(\t\x12\x0c\n\x04isin\x18\x04 \x01(\t\x12\x16\n\x0eissuer_country\x18\x05 \x01(\t\x12\x10\n\x08quantity\x18\x06 \x01(\x03\x12\x42\n\x08\x64ividend\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x13\x65xternal_commission\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\x0e\x64ividend_gross\x18\t \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03tax\x18\n \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12I\n\x0f\x64ividend_amount\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08\x63urrency\x18\x0c \x01(\t\"*\n\x16PortfolioStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\x8d\x02\n\x17PortfolioStreamResponse\x12[\n\rsubscriptions\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PortfolioSubscriptionResultH\x00\x12M\n\tportfolio\x18\x02 \x01(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponseH\x00\x12;\n\x04ping\x18\x03 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"q\n\x1bPortfolioSubscriptionResult\x12R\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32@.tinkoff.public.invest.api.contract.v1.AccountSubscriptionStatus\"\x90\x01\n\x19\x41\x63\x63ountSubscriptionStatus\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12_\n\x13subscription_status\x18\x06 \x01(\x0e\x32\x42.tinkoff.public.invest.api.contract.v1.PortfolioSubscriptionStatus\"\xa0\x03\n\x1cGetOperationsByCursorRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12(\n\x04\x66rom\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x02to\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x63ursor\x18\x0b \x01(\t\x12\r\n\x05limit\x18\x0c \x01(\x05\x12M\n\x0foperation_types\x18\r \x03(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12\x44\n\x05state\x18\x0e \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x1b\n\x13without_commissions\x18\x0f \x01(\x08\x12\x16\n\x0ewithout_trades\x18\x10 \x01(\x08\x12\x1a\n\x12without_overnights\x18\x11 \x01(\x08\"\x8b\x01\n\x1dGetOperationsByCursorResponse\x12\x10\n\x08has_next\x18\x01 \x01(\x08\x12\x13\n\x0bnext_cursor\x18\x02 \x01(\t\x12\x43\n\x05items\x18\x06 \x03(\x0b\x32\x34.tinkoff.public.invest.api.contract.v1.OperationItem\"\xf1\x08\n\rOperationItem\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x19\n\x11\x62roker_account_id\x18\x06 \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\x12\x1b\n\x13parent_operation_id\x18\x11 \x01(\t\x12\x0c\n\x04name\x18\x12 \x01(\t\x12(\n\x04\x64\x61te\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x04type\x18\x16 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12\x13\n\x0b\x64\x65scription\x18\x17 \x01(\t\x12\x44\n\x05state\x18\x18 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x16\n\x0einstrument_uid\x18\x1f \x01(\t\x12\x0c\n\x04\x66igi\x18  \x01(\t\x12\x17\n\x0finstrument_type\x18! \x01(\t\x12N\n\x0finstrument_kind\x18\" \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.InstrumentType\x12\x14\n\x0cposition_uid\x18# \x01(\t\x12\x42\n\x07payment\x18) \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05price\x18* \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x45\n\ncommission\x18+ \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05yield\x18, \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0eyield_relative\x18- \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x46\n\x0b\x61\x63\x63rued_int\x18. \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x33 \x01(\x03\x12\x15\n\rquantity_rest\x18\x34 \x01(\x03\x12\x15\n\rquantity_done\x18\x35 \x01(\x03\x12\x34\n\x10\x63\x61ncel_date_time\x18\x38 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rcancel_reason\x18\x39 \x01(\t\x12O\n\x0btrades_info\x18= \x01(\x0b\x32:.tinkoff.public.invest.api.contract.v1.OperationItemTrades\x12\x11\n\tasset_uid\x18@ \x01(\t\"`\n\x13OperationItemTrades\x12I\n\x06trades\x18\x06 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.OperationItemTrade\"\xab\x02\n\x12OperationItemTrade\x12\x0b\n\x03num\x18\x01 \x01(\t\x12(\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x0b \x01(\x03\x12@\n\x05price\x18\x10 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05yield\x18\x15 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0eyield_relative\x18\x16 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"*\n\x16PositionsStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\x87\x02\n\x17PositionsStreamResponse\x12[\n\rsubscriptions\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PositionsSubscriptionResultH\x00\x12G\n\x08position\x18\x02 \x01(\x0b\x32\x33.tinkoff.public.invest.api.contract.v1.PositionDataH\x00\x12;\n\x04ping\x18\x03 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"s\n\x1bPositionsSubscriptionResult\x12T\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PositionsSubscriptionStatus\"\x99\x01\n\x1bPositionsSubscriptionStatus\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x66\n\x13subscription_status\x18\x06 \x01(\x0e\x32I.tinkoff.public.invest.api.contract.v1.PositionsAccountSubscriptionStatus\"\xf6\x02\n\x0cPositionData\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x44\n\x05money\x18\x02 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.PositionsMoney\x12N\n\nsecurities\x18\x03 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.PositionsSecurities\x12H\n\x07\x66utures\x18\x04 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsFutures\x12H\n\x07options\x18\x05 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsOptions\x12(\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa6\x01\n\x0ePositionsMoney\x12J\n\x0f\x61vailable_value\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\rblocked_value\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue*\x8b\x01\n\x0eOperationState\x12\x1f\n\x1bOPERATION_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18OPERATION_STATE_EXECUTED\x10\x01\x12\x1c\n\x18OPERATION_STATE_CANCELED\x10\x02\x12\x1c\n\x18OPERATION_STATE_PROGRESS\x10\x03*\xba\x10\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14OPERATION_TYPE_INPUT\x10\x01\x12\x1b\n\x17OPERATION_TYPE_BOND_TAX\x10\x02\x12$\n OPERATION_TYPE_OUTPUT_SECURITIES\x10\x03\x12\x1c\n\x18OPERATION_TYPE_OVERNIGHT\x10\x04\x12\x16\n\x12OPERATION_TYPE_TAX\x10\x05\x12&\n\"OPERATION_TYPE_BOND_REPAYMENT_FULL\x10\x06\x12\x1c\n\x18OPERATION_TYPE_SELL_CARD\x10\x07\x12\x1f\n\x1bOPERATION_TYPE_DIVIDEND_TAX\x10\x08\x12\x19\n\x15OPERATION_TYPE_OUTPUT\x10\t\x12!\n\x1dOPERATION_TYPE_BOND_REPAYMENT\x10\n\x12!\n\x1dOPERATION_TYPE_TAX_CORRECTION\x10\x0b\x12\x1e\n\x1aOPERATION_TYPE_SERVICE_FEE\x10\x0c\x12\x1e\n\x1aOPERATION_TYPE_BENEFIT_TAX\x10\r\x12\x1d\n\x19OPERATION_TYPE_MARGIN_FEE\x10\x0e\x12\x16\n\x12OPERATION_TYPE_BUY\x10\x0f\x12\x1b\n\x17OPERATION_TYPE_BUY_CARD\x10\x10\x12#\n\x1fOPERATION_TYPE_INPUT_SECURITIES\x10\x11\x12\x1e\n\x1aOPERATION_TYPE_SELL_MARGIN\x10\x12\x12\x1d\n\x19OPERATION_TYPE_BROKER_FEE\x10\x13\x12\x1d\n\x19OPERATION_TYPE_BUY_MARGIN\x10\x14\x12\x1b\n\x17OPERATION_TYPE_DIVIDEND\x10\x15\x12\x17\n\x13OPERATION_TYPE_SELL\x10\x16\x12\x19\n\x15OPERATION_TYPE_COUPON\x10\x17\x12\x1e\n\x1aOPERATION_TYPE_SUCCESS_FEE\x10\x18\x12$\n OPERATION_TYPE_DIVIDEND_TRANSFER\x10\x19\x12%\n!OPERATION_TYPE_ACCRUING_VARMARGIN\x10\x1a\x12(\n$OPERATION_TYPE_WRITING_OFF_VARMARGIN\x10\x1b\x12\x1f\n\x1bOPERATION_TYPE_DELIVERY_BUY\x10\x1c\x12 \n\x1cOPERATION_TYPE_DELIVERY_SELL\x10\x1d\x12\x1d\n\x19OPERATION_TYPE_TRACK_MFEE\x10\x1e\x12\x1d\n\x19OPERATION_TYPE_TRACK_PFEE\x10\x1f\x12\"\n\x1eOPERATION_TYPE_TAX_PROGRESSIVE\x10 \x12\'\n#OPERATION_TYPE_BOND_TAX_PROGRESSIVE\x10!\x12+\n\'OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE\x10\"\x12*\n&OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE\x10#\x12-\n)OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE\x10$\x12\'\n#OPERATION_TYPE_TAX_REPO_PROGRESSIVE\x10%\x12\x1b\n\x17OPERATION_TYPE_TAX_REPO\x10&\x12 \n\x1cOPERATION_TYPE_TAX_REPO_HOLD\x10\'\x12\"\n\x1eOPERATION_TYPE_TAX_REPO_REFUND\x10(\x12,\n(OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE\x10)\x12.\n*OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE\x10*\x12\x1a\n\x16OPERATION_TYPE_DIV_EXT\x10+\x12(\n$OPERATION_TYPE_TAX_CORRECTION_COUPON\x10,\x12\x1b\n\x17OPERATION_TYPE_CASH_FEE\x10-\x12\x1a\n\x16OPERATION_TYPE_OUT_FEE\x10.\x12!\n\x1dOPERATION_TYPE_OUT_STAMP_DUTY\x10/\x12\x1f\n\x1bOPERATION_TYPE_OUTPUT_SWIFT\x10\x32\x12\x1e\n\x1aOPERATION_TYPE_INPUT_SWIFT\x10\x33\x12#\n\x1fOPERATION_TYPE_OUTPUT_ACQUIRING\x10\x35\x12\"\n\x1eOPERATION_TYPE_INPUT_ACQUIRING\x10\x36\x12!\n\x1dOPERATION_TYPE_OUTPUT_PENALTY\x10\x37\x12\x1d\n\x19OPERATION_TYPE_ADVICE_FEE\x10\x38\x12\x1f\n\x1bOPERATION_TYPE_TRANS_IIS_BS\x10\x39\x12\x1e\n\x1aOPERATION_TYPE_TRANS_BS_BS\x10:\x12\x1c\n\x18OPERATION_TYPE_OUT_MULTI\x10;\x12\x1c\n\x18OPERATION_TYPE_INP_MULTI\x10<\x12!\n\x1dOPERATION_TYPE_OVER_PLACEMENT\x10=\x12\x1b\n\x17OPERATION_TYPE_OVER_COM\x10>\x12\x1e\n\x1aOPERATION_TYPE_OVER_INCOME\x10?\x12$\n OPERATION_TYPE_OPTION_EXPIRATION\x10@*\xde\x01\n\x1bPortfolioSubscriptionStatus\x12-\n)PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12)\n%PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12\x33\n/PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND\x10\x02\x12\x30\n,PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x03*\xe5\x01\n\"PositionsAccountSubscriptionStatus\x12-\n)POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12)\n%POSITIONS_SUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12\x33\n/POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND\x10\x02\x12\x30\n,POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x03\x32\x98\x08\n\x11OperationsService\x12\x84\x01\n\rGetOperations\x12\x38.tinkoff.public.invest.api.contract.v1.OperationsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.OperationsResponse\x12\x81\x01\n\x0cGetPortfolio\x12\x37.tinkoff.public.invest.api.contract.v1.PortfolioRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponse\x12\x81\x01\n\x0cGetPositions\x12\x37.tinkoff.public.invest.api.contract.v1.PositionsRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PositionsResponse\x12\x90\x01\n\x11GetWithdrawLimits\x12<.tinkoff.public.invest.api.contract.v1.WithdrawLimitsRequest\x1a=.tinkoff.public.invest.api.contract.v1.WithdrawLimitsResponse\x12\x8a\x01\n\x0fGetBrokerReport\x12:.tinkoff.public.invest.api.contract.v1.BrokerReportRequest\x1a;.tinkoff.public.invest.api.contract.v1.BrokerReportResponse\x12\xae\x01\n\x19GetDividendsForeignIssuer\x12G.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerRequest\x1aH.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerResponse\x12\xa2\x01\n\x15GetOperationsByCursor\x12\x43.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorRequest\x1a\x44.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorResponse2\xc3\x02\n\x17OperationsStreamService\x12\x92\x01\n\x0fPortfolioStream\x12=.tinkoff.public.invest.api.contract.v1.PortfolioStreamRequest\x1a>.tinkoff.public.invest.api.contract.v1.PortfolioStreamResponse0\x01\x12\x92\x01\n\x0fPositionsStream\x12=.tinkoff.public.invest.api.contract.v1.PositionsStreamRequest\x1a>.tinkoff.public.invest.api.contract.v1.PositionsStreamResponse0\x01\x42\x61\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operations_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _OPERATIONSTATE._serialized_start=12533
  _OPERATIONSTATE._serialized_end=12672
  _OPERATIONTYPE._serialized_start=12675
  _OPERATIONTYPE._serialized_end=14781
  _PORTFOLIOSUBSCRIPTIONSTATUS._serialized_start=14784
  _PORTFOLIOSUBSCRIPTIONSTATUS._serialized_end=15006
  _POSITIONSACCOUNTSUBSCRIPTIONSTATUS._serialized_start=15009
  _POSITIONSACCOUNTSUBSCRIPTIONSTATUS._serialized_end=15238
  _OPERATIONSREQUEST._serialized_start=107
  _OPERATIONSREQUEST._serialized_end=312
  _OPERATIONSRESPONSE._serialized_start=314
  _OPERATIONSRESPONSE._serialized_end=404
  _OPERATION._serialized_start=407
  _OPERATION._serialized_end=1031
  _OPERATIONTRADE._serialized_start=1034
  _OPERATIONTRADE._serialized_end=1199
  _PORTFOLIOREQUEST._serialized_start=1202
  _PORTFOLIOREQUEST._serialized_end=1377
  _PORTFOLIOREQUEST_CURRENCYREQUEST._serialized_start=1333
  _PORTFOLIOREQUEST_CURRENCYREQUEST._serialized_end=1377
  _PORTFOLIORESPONSE._serialized_start=1380
  _PORTFOLIORESPONSE._serialized_end=2303
  _POSITIONSREQUEST._serialized_start=2305
  _POSITIONSREQUEST._serialized_end=2343
  _POSITIONSRESPONSE._serialized_start=2346
  _POSITIONSRESPONSE._serialized_end=2763
  _WITHDRAWLIMITSREQUEST._serialized_start=2765
  _WITHDRAWLIMITSREQUEST._serialized_end=2808
  _WITHDRAWLIMITSRESPONSE._serialized_start=2811
  _WITHDRAWLIMITSRESPONSE._serialized_end=3047
  _PORTFOLIOPOSITION._serialized_start=3050
  _PORTFOLIOPOSITION._serialized_end=4010
  _VIRTUALPORTFOLIOPOSITION._serialized_start=4013
  _VIRTUALPORTFOLIOPOSITION._serialized_end=4639
  _POSITIONSSECURITIES._serialized_start=4642
  _POSITIONSSECURITIES._serialized_end=4808
  _POSITIONSFUTURES._serialized_start=4810
  _POSITIONSFUTURES._serialized_end=4922
  _POSITIONSOPTIONS._serialized_start=4924
  _POSITIONSOPTIONS._serialized_end=5022
  _BROKERREPORTREQUEST._serialized_start=5025
  _BROKERREPORTREQUEST._serialized_end=5267
  _BROKERREPORTRESPONSE._serialized_start=5270
  _BROKERREPORTRESPONSE._serialized_end=5517
  _GENERATEBROKERREPORTREQUEST._serialized_start=5520
  _GENERATEBROKERREPORTREQUEST._serialized_end=5651
  _GENERATEBROKERREPORTRESPONSE._serialized_start=5653
  _GENERATEBROKERREPORTRESPONSE._serialized_end=5700
  _GETBROKERREPORTREQUEST._serialized_start=5702
  _GETBROKERREPORTREQUEST._serialized_end=5757
  _GETBROKERREPORTRESPONSE._serialized_start=5760
  _GETBROKERREPORTRESPONSE._serialized_end=5915
  _BROKERREPORT._serialized_start=5918
  _BROKERREPORT._serialized_end=7032
  _GETDIVIDENDSFOREIGNISSUERREQUEST._serialized_start=7035
  _GETDIVIDENDSFOREIGNISSUERREQUEST._serialized_end=7331
  _GETDIVIDENDSFOREIGNISSUERRESPONSE._serialized_start=7334
  _GETDIVIDENDSFOREIGNISSUERRESPONSE._serialized_end=7638
  _GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST._serialized_start=7641
  _GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST._serialized_end=7788
  _GETDIVIDENDSFOREIGNISSUERREPORTREQUEST._serialized_start=7790
  _GETDIVIDENDSFOREIGNISSUERREPORTREQUEST._serialized_end=7861
  _GENERATEDIVIDENDSFOREIGNISSUERREPORTRESPONSE._serialized_start=7863
  _GENERATEDIVIDENDSFOREIGNISSUERREPORTRESPONSE._serialized_end=7926
  _GETDIVIDENDSFOREIGNISSUERREPORTRESPONSE._serialized_start=7929
  _GETDIVIDENDSFOREIGNISSUERREPORTRESPONSE._serialized_end=8134
  _DIVIDENDSFOREIGNISSUERREPORT._serialized_start=8137
  _DIVIDENDSFOREIGNISSUERREPORT._serialized_end=8722
  _PORTFOLIOSTREAMREQUEST._serialized_start=8724
  _PORTFOLIOSTREAMREQUEST._serialized_end=8766
  _PORTFOLIOSTREAMRESPONSE._serialized_start=8769
  _PORTFOLIOSTREAMRESPONSE._serialized_end=9038
  _PORTFOLIOSUBSCRIPTIONRESULT._serialized_start=9040
  _PORTFOLIOSUBSCRIPTIONRESULT._serialized_end=9153
  _ACCOUNTSUBSCRIPTIONSTATUS._serialized_start=9156
  _ACCOUNTSUBSCRIPTIONSTATUS._serialized_end=9300
  _GETOPERATIONSBYCURSORREQUEST._serialized_start=9303
  _GETOPERATIONSBYCURSORREQUEST._serialized_end=9719
  _GETOPERATIONSBYCURSORRESPONSE._serialized_start=9722
  _GETOPERATIONSBYCURSORRESPONSE._serialized_end=9861
  _OPERATIONITEM._serialized_start=9864
  _OPERATIONITEM._serialized_end=11001
  _OPERATIONITEMTRADES._serialized_start=11003
  _OPERATIONITEMTRADES._serialized_end=11099
  _OPERATIONITEMTRADE._serialized_start=11102
  _OPERATIONITEMTRADE._serialized_end=11401
  _POSITIONSSTREAMREQUEST._serialized_start=11403
  _POSITIONSSTREAMREQUEST._serialized_end=11445
  _POSITIONSSTREAMRESPONSE._serialized_start=11448
  _POSITIONSSTREAMRESPONSE._serialized_end=11711
  _POSITIONSSUBSCRIPTIONRESULT._serialized_start=11713
  _POSITIONSSUBSCRIPTIONRESULT._serialized_end=11828
  _POSITIONSSUBSCRIPTIONSTATUS._serialized_start=11831
  _POSITIONSSUBSCRIPTIONSTATUS._serialized_end=11984
  _POSITIONDATA._serialized_start=11987
  _POSITIONDATA._serialized_end=12361
  _POSITIONSMONEY._serialized_start=12364
  _POSITIONSMONEY._serialized_end=12530
  _OPERATIONSSERVICE._serialized_start=15241
  _OPERATIONSSERVICE._serialized_end=16289
  _OPERATIONSSTREAMSERVICE._serialized_start=16292
  _OPERATIONSSTREAMSERVICE._serialized_end=16615
# @@protoc_insertion_point(module_scope)