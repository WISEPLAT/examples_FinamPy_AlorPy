# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from FinamPy.proto.tradeapi.v1 import candles_pb2 as proto_dot_tradeapi_dot_v1_dot_candles__pb2


class CandlesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDayCandles = channel.unary_unary(
                '/grpc.tradeapi.v1.Candles/GetDayCandles',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesResult.FromString,
                )
        self.GetIntradayCandles = channel.unary_unary(
                '/grpc.tradeapi.v1.Candles/GetIntradayCandles',
                request_serializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesRequest.SerializeToString,
                response_deserializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesResult.FromString,
                )


class CandlesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDayCandles(self, request, context):
        """Returns the list of day candles.
        Возвращает дневные свечи.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIntradayCandles(self, request, context):
        """Returns the list of intraday candles.
        Возвращает внутридневные свечи.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CandlesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetDayCandles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDayCandles,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesResult.SerializeToString,
            ),
            'GetIntradayCandles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIntradayCandles,
                    request_deserializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesRequest.FromString,
                    response_serializer=proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.tradeapi.v1.Candles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Candles(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDayCandles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Candles/GetDayCandles',
            proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetDayCandlesResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIntradayCandles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.tradeapi.v1.Candles/GetIntradayCandles',
            proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesRequest.SerializeToString,
            proto_dot_tradeapi_dot_v1_dot_candles__pb2.GetIntradayCandlesResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
