# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc/tradeapi/v1/stops.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from FinamPy.proto.tradeapi.v1 import stops_pb2 as proto_dot_tradeapi_dot_v1_dot_stops__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cgrpc/tradeapi/v1/stops.proto\x12\x10grpc.tradeapi.v1\x1a\x1dproto/tradeapi/v1/stops.proto2\x83\x02\n\x05Stops\x12Q\n\x08GetStops\x12\".proto.tradeapi.v1.GetStopsRequest\x1a!.proto.tradeapi.v1.GetStopsResult\x12W\n\nCancelStop\x12$.proto.tradeapi.v1.CancelStopRequest\x1a#.proto.tradeapi.v1.CancelStopResult\x12N\n\x07NewStop\x12!.proto.tradeapi.v1.NewStopRequest\x1a .proto.tradeapi.v1.NewStopResultB\x19\xaa\x02\x16\x46inam.TradeApi.Grpc.V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc.tradeapi.v1.stops_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\026Finam.TradeApi.Grpc.V1'
  _globals['_STOPS']._serialized_start=82
  _globals['_STOPS']._serialized_end=341
# @@protoc_insertion_point(module_scope)
