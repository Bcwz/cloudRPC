# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: assignment_prototype.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='assignment_prototype.proto',
  package='assignment_prototype',
  syntax='proto3',
  serialized_options=b'\n%io.grpc.examples.assignment_prototypeB\030AssignmentPrototypeProtoP\001\242\002\003APP',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1a\x61ssignment_prototype.proto\x12\x14\x61ssignment_prototype\"/\n\x0bRequestCall\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\nRequestMsg\x18\x02 \x01(\t\"&\n\x0fRequestResponse\x12\x13\n\x0bResponseMsg\x18\x01 \x01(\t2i\n\x0c\x63ommunicator\x12Y\n\x0bmakerequest\x12!.assignment_prototype.RequestCall\x1a%.assignment_prototype.RequestResponse\"\x00\x42I\n%io.grpc.examples.assignment_prototypeB\x18\x41ssignmentPrototypeProtoP\x01\xa2\x02\x03\x41PPb\x06proto3'
)




_REQUESTCALL = _descriptor.Descriptor(
  name='RequestCall',
  full_name='assignment_prototype.RequestCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='assignment_prototype.RequestCall.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RequestMsg', full_name='assignment_prototype.RequestCall.RequestMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=99,
)


_REQUESTRESPONSE = _descriptor.Descriptor(
  name='RequestResponse',
  full_name='assignment_prototype.RequestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ResponseMsg', full_name='assignment_prototype.RequestResponse.ResponseMsg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['RequestCall'] = _REQUESTCALL
DESCRIPTOR.message_types_by_name['RequestResponse'] = _REQUESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestCall = _reflection.GeneratedProtocolMessageType('RequestCall', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCALL,
  '__module__' : 'assignment_prototype_pb2'
  # @@protoc_insertion_point(class_scope:assignment_prototype.RequestCall)
  })
_sym_db.RegisterMessage(RequestCall)

RequestResponse = _reflection.GeneratedProtocolMessageType('RequestResponse', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRESPONSE,
  '__module__' : 'assignment_prototype_pb2'
  # @@protoc_insertion_point(class_scope:assignment_prototype.RequestResponse)
  })
_sym_db.RegisterMessage(RequestResponse)


DESCRIPTOR._options = None

_COMMUNICATOR = _descriptor.ServiceDescriptor(
  name='communicator',
  full_name='assignment_prototype.communicator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=141,
  serialized_end=246,
  methods=[
  _descriptor.MethodDescriptor(
    name='makerequest',
    full_name='assignment_prototype.communicator.makerequest',
    index=0,
    containing_service=None,
    input_type=_REQUESTCALL,
    output_type=_REQUESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMUNICATOR)

DESCRIPTOR.services_by_name['communicator'] = _COMMUNICATOR

# @@protoc_insertion_point(module_scope)
