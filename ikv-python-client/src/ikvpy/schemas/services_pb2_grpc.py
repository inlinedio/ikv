# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import services_pb2 as services__pb2


class InlineKVWriteServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.helloWorld = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/helloWorld',
                request_serializer=services__pb2.HelloWorldRequest.SerializeToString,
                response_deserializer=services__pb2.HelloWorldResponse.FromString,
                )
        self.upsertFieldValues = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/upsertFieldValues',
                request_serializer=services__pb2.UpsertFieldValuesRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.batchUpsertFieldValues = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/batchUpsertFieldValues',
                request_serializer=services__pb2.BatchUpsertFieldValuesRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.deleteFieldValues = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/deleteFieldValues',
                request_serializer=services__pb2.DeleteFieldValueRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.batchDeleteFieldValues = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/batchDeleteFieldValues',
                request_serializer=services__pb2.BatchDeleteFieldValuesRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.deleteDocument = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/deleteDocument',
                request_serializer=services__pb2.DeleteDocumentRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.batchDeleteDocuments = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/batchDeleteDocuments',
                request_serializer=services__pb2.BatchDeleteDocumentsRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.dropFields = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/dropFields',
                request_serializer=services__pb2.DropFieldsRequest.SerializeToString,
                response_deserializer=services__pb2.Status.FromString,
                )
        self.getUserStoreConfig = channel.unary_unary(
                '/ikvschemas.InlineKVWriteService/getUserStoreConfig',
                request_serializer=services__pb2.GetUserStoreConfigRequest.SerializeToString,
                response_deserializer=services__pb2.GetUserStoreConfigResponse.FromString,
                )


class InlineKVWriteServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def helloWorld(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upsertFieldValues(self, request, context):
        """Write methods
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def batchUpsertFieldValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteFieldValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def batchDeleteFieldValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteDocument(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def batchDeleteDocuments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dropFields(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getUserStoreConfig(self, request, context):
        """Gateway-specified configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InlineKVWriteServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'helloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.helloWorld,
                    request_deserializer=services__pb2.HelloWorldRequest.FromString,
                    response_serializer=services__pb2.HelloWorldResponse.SerializeToString,
            ),
            'upsertFieldValues': grpc.unary_unary_rpc_method_handler(
                    servicer.upsertFieldValues,
                    request_deserializer=services__pb2.UpsertFieldValuesRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'batchUpsertFieldValues': grpc.unary_unary_rpc_method_handler(
                    servicer.batchUpsertFieldValues,
                    request_deserializer=services__pb2.BatchUpsertFieldValuesRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'deleteFieldValues': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteFieldValues,
                    request_deserializer=services__pb2.DeleteFieldValueRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'batchDeleteFieldValues': grpc.unary_unary_rpc_method_handler(
                    servicer.batchDeleteFieldValues,
                    request_deserializer=services__pb2.BatchDeleteFieldValuesRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'deleteDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteDocument,
                    request_deserializer=services__pb2.DeleteDocumentRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'batchDeleteDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.batchDeleteDocuments,
                    request_deserializer=services__pb2.BatchDeleteDocumentsRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'dropFields': grpc.unary_unary_rpc_method_handler(
                    servicer.dropFields,
                    request_deserializer=services__pb2.DropFieldsRequest.FromString,
                    response_serializer=services__pb2.Status.SerializeToString,
            ),
            'getUserStoreConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.getUserStoreConfig,
                    request_deserializer=services__pb2.GetUserStoreConfigRequest.FromString,
                    response_serializer=services__pb2.GetUserStoreConfigResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ikvschemas.InlineKVWriteService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InlineKVWriteService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def helloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/helloWorld',
            services__pb2.HelloWorldRequest.SerializeToString,
            services__pb2.HelloWorldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upsertFieldValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/upsertFieldValues',
            services__pb2.UpsertFieldValuesRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def batchUpsertFieldValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/batchUpsertFieldValues',
            services__pb2.BatchUpsertFieldValuesRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteFieldValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/deleteFieldValues',
            services__pb2.DeleteFieldValueRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def batchDeleteFieldValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/batchDeleteFieldValues',
            services__pb2.BatchDeleteFieldValuesRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/deleteDocument',
            services__pb2.DeleteDocumentRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def batchDeleteDocuments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/batchDeleteDocuments',
            services__pb2.BatchDeleteDocumentsRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dropFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/dropFields',
            services__pb2.DropFieldsRequest.SerializeToString,
            services__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getUserStoreConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.InlineKVWriteService/getUserStoreConfig',
            services__pb2.GetUserStoreConfigRequest.SerializeToString,
            services__pb2.GetUserStoreConfigResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AdminServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.healthCheck = channel.unary_unary(
                '/ikvschemas.AdminService/healthCheck',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=services__pb2.HealthCheckResponse.FromString,
                )


class AdminServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def healthCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'healthCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.healthCheck,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=services__pb2.HealthCheckResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ikvschemas.AdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdminService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def healthCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ikvschemas.AdminService/healthCheck',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            services__pb2.HealthCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
