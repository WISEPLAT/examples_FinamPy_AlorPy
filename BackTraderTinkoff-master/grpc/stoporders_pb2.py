# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stoporders.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10stoporders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\x8f\x04\n\x14PostStopOrderRequest\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x44\n\nstop_price\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12L\n\tdirection\x18\x05 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12W\n\x0f\x65xpiration_type\x18\x07 \x01(\x0e\x32>.tinkoff.public.invest.api.contract.v1.StopOrderExpirationType\x12M\n\x0fstop_order_type\x18\x08 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x65xpire_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rinstrument_id\x18\n \x01(\t\".\n\x15PostStopOrderResponse\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\"*\n\x14GetStopOrdersRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"^\n\x15GetStopOrdersResponse\x12\x45\n\x0bstop_orders\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.StopOrder\"C\n\x16\x43\x61ncelStopOrderRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rstop_order_id\x18\x02 \x01(\t\"C\n\x17\x43\x61ncelStopOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb3\x04\n\tStopOrder\x12\x15\n\rstop_order_id\x18\x01 \x01(\t\x12\x16\n\x0elots_requested\x18\x02 \x01(\x03\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12L\n\tdirection\x18\x04 \x01(\x0e\x32\x39.tinkoff.public.invest.api.contract.v1.StopOrderDirection\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12H\n\norder_type\x18\x06 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.StopOrderType\x12/\n\x0b\x63reate_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x38\n\x14\x61\x63tivation_date_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x33\n\x0f\x65xpiration_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12@\n\x05price\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x45\n\nstop_price\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x16\n\x0einstrument_uid\x18\x0c \x01(\t*w\n\x12StopOrderDirection\x12$\n STOP_ORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x1c\n\x18STOP_ORDER_DIRECTION_BUY\x10\x01\x12\x1d\n\x19STOP_ORDER_DIRECTION_SELL\x10\x02*\xa5\x01\n\x17StopOrderExpirationType\x12*\n&STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED\x10\x00\x12/\n+STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL\x10\x01\x12-\n)STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE\x10\x02*\x90\x01\n\rStopOrderType\x12\x1f\n\x1bSTOP_ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bSTOP_ORDER_TYPE_TAKE_PROFIT\x10\x01\x12\x1d\n\x19STOP_ORDER_TYPE_STOP_LOSS\x10\x02\x12\x1e\n\x1aSTOP_ORDER_TYPE_STOP_LIMIT\x10\x03\x32\xc0\x03\n\x11StopOrdersService\x12\x8a\x01\n\rPostStopOrder\x12;.tinkoff.public.invest.api.contract.v1.PostStopOrderRequest\x1a<.tinkoff.public.invest.api.contract.v1.PostStopOrderResponse\x12\x8a\x01\n\rGetStopOrders\x12;.tinkoff.public.invest.api.contract.v1.GetStopOrdersRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetStopOrdersResponse\x12\x90\x01\n\x0f\x43\x61ncelStopOrder\x12=.tinkoff.public.invest.api.contract.v1.CancelStopOrderRequest\x1a>.tinkoff.public.invest.api.contract.v1.CancelStopOrderResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stoporders_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _STOPORDERDIRECTION._serialized_start=1528
  _STOPORDERDIRECTION._serialized_end=1647
  _STOPORDEREXPIRATIONTYPE._serialized_start=1650
  _STOPORDEREXPIRATIONTYPE._serialized_end=1815
  _STOPORDERTYPE._serialized_start=1818
  _STOPORDERTYPE._serialized_end=1962
  _POSTSTOPORDERREQUEST._serialized_start=107
  _POSTSTOPORDERREQUEST._serialized_end=634
  _POSTSTOPORDERRESPONSE._serialized_start=636
  _POSTSTOPORDERRESPONSE._serialized_end=682
  _GETSTOPORDERSREQUEST._serialized_start=684
  _GETSTOPORDERSREQUEST._serialized_end=726
  _GETSTOPORDERSRESPONSE._serialized_start=728
  _GETSTOPORDERSRESPONSE._serialized_end=822
  _CANCELSTOPORDERREQUEST._serialized_start=824
  _CANCELSTOPORDERREQUEST._serialized_end=891
  _CANCELSTOPORDERRESPONSE._serialized_start=893
  _CANCELSTOPORDERRESPONSE._serialized_end=960
  _STOPORDER._serialized_start=963
  _STOPORDER._serialized_end=1526
  _STOPORDERSSERVICE._serialized_start=1965
  _STOPORDERSSERVICE._serialized_end=2413
# @@protoc_insertion_point(module_scope)
