# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AxisSystemPositionController.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import sila2lib.framework.SiLAFramework_pb2 as SiLAFramework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AxisSystemPositionController.proto',
  package='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"AxisSystemPositionController.proto\x12\x42sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1\x1a\x13SiLAFramework.proto\"\xf1\x01\n\x11\x44\x61taType_Position\x12w\n\x08Position\x18\x01 \x01(\x0b\x32\x65.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position_Struct\x1a\x63\n\x0fPosition_Struct\x12\'\n\x01X\x18\x01 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real\x12\'\n\x01Y\x18\x02 \x01(\x0b\x32\x1c.sila2.org.silastandard.Real\"\xb7\x01\n\x19MoveToPosition_Parameters\x12g\n\x08Position\x18\x01 \x01(\x0b\x32U.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position\x12\x31\n\x08Velocity\x18\x02 \x01(\x0b\x32\x1f.sila2.org.silastandard.Integer\"\x1a\n\x18MoveToPosition_Responses\"\x1f\n\x1dMoveToHomePosition_Parameters\"\x1e\n\x1cMoveToHomePosition_Responses\"\x17\n\x15StopMoving_Parameters\"\x16\n\x14StopMoving_Responses\"\x1f\n\x1dSubscribe_Position_Parameters\"\x87\x01\n\x1cSubscribe_Position_Responses\x12g\n\x08Position\x18\x01 \x01(\x0b\x32U.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position2\xdb\x08\n\x1c\x41xisSystemPositionController\x12\x9e\x01\n\x0eMoveToPosition\x12].sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Parameters\x1a+.sila2.org.silastandard.CommandConfirmation\"\x00\x12n\n\x13MoveToPosition_Info\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a%.sila2.org.silastandard.ExecutionInfo\"\x00\x30\x01\x12\xa5\x01\n\x15MoveToPosition_Result\x12,.sila2.org.silastandard.CommandExecutionUUID\x1a\\.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Responses\"\x00\x12\xdb\x01\n\x12MoveToHomePosition\x12\x61.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Parameters\x1a`.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Responses\"\x00\x12\xc3\x01\n\nStopMoving\x12Y.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Parameters\x1aX.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Responses\"\x00\x12\xdd\x01\n\x12Subscribe_Position\x12\x61.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Parameters\x1a`.sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Responses\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[SiLAFramework__pb2.DESCRIPTOR,])




_DATATYPE_POSITION_POSITION_STRUCT = _descriptor.Descriptor(
  name='Position_Struct',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position_Struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position_Struct.X', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Y', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position_Struct.Y', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=270,
  serialized_end=369,
)

_DATATYPE_POSITION = _descriptor.Descriptor(
  name='DataType_Position',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Position', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATATYPE_POSITION_POSITION_STRUCT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=369,
)


_MOVETOPOSITION_PARAMETERS = _descriptor.Descriptor(
  name='MoveToPosition_Parameters',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Position', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Parameters.Position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Velocity', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Parameters.Velocity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=372,
  serialized_end=555,
)


_MOVETOPOSITION_RESPONSES = _descriptor.Descriptor(
  name='MoveToPosition_Responses',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=557,
  serialized_end=583,
)


_MOVETOHOMEPOSITION_PARAMETERS = _descriptor.Descriptor(
  name='MoveToHomePosition_Parameters',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=585,
  serialized_end=616,
)


_MOVETOHOMEPOSITION_RESPONSES = _descriptor.Descriptor(
  name='MoveToHomePosition_Responses',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=618,
  serialized_end=648,
)


_STOPMOVING_PARAMETERS = _descriptor.Descriptor(
  name='StopMoving_Parameters',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=650,
  serialized_end=673,
)


_STOPMOVING_RESPONSES = _descriptor.Descriptor(
  name='StopMoving_Responses',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=675,
  serialized_end=697,
)


_SUBSCRIBE_POSITION_PARAMETERS = _descriptor.Descriptor(
  name='Subscribe_Position_Parameters',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=699,
  serialized_end=730,
)


_SUBSCRIBE_POSITION_RESPONSES = _descriptor.Descriptor(
  name='Subscribe_Position_Responses',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Responses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Position', full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Responses.Position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=733,
  serialized_end=868,
)

_DATATYPE_POSITION_POSITION_STRUCT.fields_by_name['X'].message_type = SiLAFramework__pb2._REAL
_DATATYPE_POSITION_POSITION_STRUCT.fields_by_name['Y'].message_type = SiLAFramework__pb2._REAL
_DATATYPE_POSITION_POSITION_STRUCT.containing_type = _DATATYPE_POSITION
_DATATYPE_POSITION.fields_by_name['Position'].message_type = _DATATYPE_POSITION_POSITION_STRUCT
_MOVETOPOSITION_PARAMETERS.fields_by_name['Position'].message_type = _DATATYPE_POSITION
_MOVETOPOSITION_PARAMETERS.fields_by_name['Velocity'].message_type = SiLAFramework__pb2._INTEGER
_SUBSCRIBE_POSITION_RESPONSES.fields_by_name['Position'].message_type = _DATATYPE_POSITION
DESCRIPTOR.message_types_by_name['DataType_Position'] = _DATATYPE_POSITION
DESCRIPTOR.message_types_by_name['MoveToPosition_Parameters'] = _MOVETOPOSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['MoveToPosition_Responses'] = _MOVETOPOSITION_RESPONSES
DESCRIPTOR.message_types_by_name['MoveToHomePosition_Parameters'] = _MOVETOHOMEPOSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['MoveToHomePosition_Responses'] = _MOVETOHOMEPOSITION_RESPONSES
DESCRIPTOR.message_types_by_name['StopMoving_Parameters'] = _STOPMOVING_PARAMETERS
DESCRIPTOR.message_types_by_name['StopMoving_Responses'] = _STOPMOVING_RESPONSES
DESCRIPTOR.message_types_by_name['Subscribe_Position_Parameters'] = _SUBSCRIBE_POSITION_PARAMETERS
DESCRIPTOR.message_types_by_name['Subscribe_Position_Responses'] = _SUBSCRIBE_POSITION_RESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataType_Position = _reflection.GeneratedProtocolMessageType('DataType_Position', (_message.Message,), {

  'Position_Struct' : _reflection.GeneratedProtocolMessageType('Position_Struct', (_message.Message,), {
    'DESCRIPTOR' : _DATATYPE_POSITION_POSITION_STRUCT,
    '__module__' : 'AxisSystemPositionController_pb2'
    # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position.Position_Struct)
    })
  ,
  'DESCRIPTOR' : _DATATYPE_POSITION,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.DataType_Position)
  })
_sym_db.RegisterMessage(DataType_Position)
_sym_db.RegisterMessage(DataType_Position.Position_Struct)

MoveToPosition_Parameters = _reflection.GeneratedProtocolMessageType('MoveToPosition_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOPOSITION_PARAMETERS,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Parameters)
  })
_sym_db.RegisterMessage(MoveToPosition_Parameters)

MoveToPosition_Responses = _reflection.GeneratedProtocolMessageType('MoveToPosition_Responses', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOPOSITION_RESPONSES,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToPosition_Responses)
  })
_sym_db.RegisterMessage(MoveToPosition_Responses)

MoveToHomePosition_Parameters = _reflection.GeneratedProtocolMessageType('MoveToHomePosition_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOHOMEPOSITION_PARAMETERS,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Parameters)
  })
_sym_db.RegisterMessage(MoveToHomePosition_Parameters)

MoveToHomePosition_Responses = _reflection.GeneratedProtocolMessageType('MoveToHomePosition_Responses', (_message.Message,), {
  'DESCRIPTOR' : _MOVETOHOMEPOSITION_RESPONSES,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.MoveToHomePosition_Responses)
  })
_sym_db.RegisterMessage(MoveToHomePosition_Responses)

StopMoving_Parameters = _reflection.GeneratedProtocolMessageType('StopMoving_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _STOPMOVING_PARAMETERS,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Parameters)
  })
_sym_db.RegisterMessage(StopMoving_Parameters)

StopMoving_Responses = _reflection.GeneratedProtocolMessageType('StopMoving_Responses', (_message.Message,), {
  'DESCRIPTOR' : _STOPMOVING_RESPONSES,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.StopMoving_Responses)
  })
_sym_db.RegisterMessage(StopMoving_Responses)

Subscribe_Position_Parameters = _reflection.GeneratedProtocolMessageType('Subscribe_Position_Parameters', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_POSITION_PARAMETERS,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Parameters)
  })
_sym_db.RegisterMessage(Subscribe_Position_Parameters)

Subscribe_Position_Responses = _reflection.GeneratedProtocolMessageType('Subscribe_Position_Responses', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBE_POSITION_RESPONSES,
  '__module__' : 'AxisSystemPositionController_pb2'
  # @@protoc_insertion_point(class_scope:sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.Subscribe_Position_Responses)
  })
_sym_db.RegisterMessage(Subscribe_Position_Responses)



_AXISSYSTEMPOSITIONCONTROLLER = _descriptor.ServiceDescriptor(
  name='AxisSystemPositionController',
  full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=871,
  serialized_end=1986,
  methods=[
  _descriptor.MethodDescriptor(
    name='MoveToPosition',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.MoveToPosition',
    index=0,
    containing_service=None,
    input_type=_MOVETOPOSITION_PARAMETERS,
    output_type=SiLAFramework__pb2._COMMANDCONFIRMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveToPosition_Info',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.MoveToPosition_Info',
    index=1,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=SiLAFramework__pb2._EXECUTIONINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveToPosition_Result',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.MoveToPosition_Result',
    index=2,
    containing_service=None,
    input_type=SiLAFramework__pb2._COMMANDEXECUTIONUUID,
    output_type=_MOVETOPOSITION_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveToHomePosition',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.MoveToHomePosition',
    index=3,
    containing_service=None,
    input_type=_MOVETOHOMEPOSITION_PARAMETERS,
    output_type=_MOVETOHOMEPOSITION_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StopMoving',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.StopMoving',
    index=4,
    containing_service=None,
    input_type=_STOPMOVING_PARAMETERS,
    output_type=_STOPMOVING_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe_Position',
    full_name='sila2.de.cetoni.motioncontrol.axis.axissystempositioncontroller.v1.AxisSystemPositionController.Subscribe_Position',
    index=5,
    containing_service=None,
    input_type=_SUBSCRIBE_POSITION_PARAMETERS,
    output_type=_SUBSCRIBE_POSITION_RESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AXISSYSTEMPOSITIONCONTROLLER)

DESCRIPTOR.services_by_name['AxisSystemPositionController'] = _AXISSYSTEMPOSITIONCONTROLLER

# @@protoc_insertion_point(module_scope)