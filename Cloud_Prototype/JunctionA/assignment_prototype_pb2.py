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
  serialized_pb=b'\n\x1a\x61ssignment_prototype.proto\x12\x14\x61ssignment_prototype\"/\n\x0bRequestCall\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x12\n\nRequestMsg\x18\x02 \x01(\t\"&\n\x0fRequestResponse\x12\x13\n\x0bResponseMsg\x18\x01 \x01(\t\"\x1b\n\nRequestLog\x12\r\n\x05types\x18\x01 \x01(\x05\"0\n\x0blogResponse\x12\x0f\n\x07\x43ontent\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t2\xbb\x01\n\x0c\x63ommunicator\x12Y\n\x0bmakerequest\x12!.assignment_prototype.RequestCall\x1a%.assignment_prototype.RequestResponse\"\x00\x12P\n\x07getLogs\x12 .assignment_prototype.RequestLog\x1a!.assignment_prototype.logResponse\"\x00\x42I\n%io.grpc.examples.assignment_prototypeB\x18\x41ssignmentPrototypeProtoP\x01\xa2\x02\x03\x41PPb\x06proto3'
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


_REQUESTLOG = _descriptor.Descriptor(
  name='RequestLog',
  full_name='assignment_prototype.RequestLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='types', full_name='assignment_prototype.RequestLog.types', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=141,
  serialized_end=168,
)


_LOGRESPONSE = _descriptor.Descriptor(
  name='logResponse',
  full_name='assignment_prototype.logResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Content', full_name='assignment_prototype.logResponse.Content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filename', full_name='assignment_prototype.logResponse.filename', index=1,
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
  serialized_start=170,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['RequestCall'] = _REQUESTCALL
DESCRIPTOR.message_types_by_name['RequestResponse'] = _REQUESTRESPONSE
DESCRIPTOR.message_types_by_name['RequestLog'] = _REQUESTLOG
DESCRIPTOR.message_types_by_name['logResponse'] = _LOGRESPONSE
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

RequestLog = _reflection.GeneratedProtocolMessageType('RequestLog', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTLOG,
  '__module__' : 'assignment_prototype_pb2'
  # @@protoc_insertion_point(class_scope:assignment_prototype.RequestLog)
  })
_sym_db.RegisterMessage(RequestLog)

logResponse = _reflection.GeneratedProtocolMessageType('logResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGRESPONSE,
  '__module__' : 'assignment_prototype_pb2'
  # @@protoc_insertion_point(class_scope:assignment_prototype.logResponse)
  })
_sym_db.RegisterMessage(logResponse)


DESCRIPTOR._options = None

_COMMUNICATOR = _descriptor.ServiceDescriptor(
  name='communicator',
  full_name='assignment_prototype.communicator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=221,
  serialized_end=408,
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
  _descriptor.MethodDescriptor(
    name='getLogs',
    full_name='assignment_prototype.communicator.getLogs',
    index=1,
    containing_service=None,
    input_type=_REQUESTLOG,
    output_type=_LOGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COMMUNICATOR)

DESCRIPTOR.services_by_name['communicator'] = _COMMUNICATOR

# @@protoc_insertion_point(module_scope)
