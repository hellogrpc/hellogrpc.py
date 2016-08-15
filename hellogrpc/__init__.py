# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hellogrpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hellogrpc.proto',
  package='hellogrpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0fhellogrpc.proto\x12\thellogrpc\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2G\n\x07Greeter\x12<\n\x08SayHello\x12\x17.hellogrpc.HelloRequest\x1a\x15.hellogrpc.HelloReply\"\x00\x42\x34\n\x1a\x63om.stackmachine.hellogrpcB\x0eHelloGRPCProtoP\x01\xa2\x02\x03HLGb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='hellogrpc.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='hellogrpc.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=58,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='hellogrpc.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='hellogrpc.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'hellogrpc_pb2'
  # @@protoc_insertion_point(class_scope:hellogrpc.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'hellogrpc_pb2'
  # @@protoc_insertion_point(class_scope:hellogrpc.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.stackmachine.hellogrpcB\016HelloGRPCProtoP\001\242\002\003HLG'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/hellogrpc.Greeter/SayHello',
        request_serializer=HelloRequest.SerializeToString,
        response_deserializer=HelloReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=HelloRequest.FromString,
          response_serializer=HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'hellogrpc.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaGreeterServicer(object):
  """The greeting service definition.
  """
  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaGreeterStub(object):
  """The greeting service definition.
  """
  def SayHello(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends a greeting
    """
    raise NotImplementedError()
  SayHello.future = None


def beta_create_Greeter_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('hellogrpc.Greeter', 'SayHello'): HelloRequest.FromString,
  }
  response_serializers = {
    ('hellogrpc.Greeter', 'SayHello'): HelloReply.SerializeToString,
  }
  method_implementations = {
    ('hellogrpc.Greeter', 'SayHello'): face_utilities.unary_unary_inline(servicer.SayHello),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Greeter_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('hellogrpc.Greeter', 'SayHello'): HelloRequest.SerializeToString,
  }
  response_deserializers = {
    ('hellogrpc.Greeter', 'SayHello'): HelloReply.FromString,
  }
  cardinalities = {
    'SayHello': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'hellogrpc.Greeter', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
