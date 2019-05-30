# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: devmodel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='devmodel.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\037com.zededa.cloud.uservice.protoZ$github.com/lf-edge/eve/api/go/config'),
  serialized_pb=_b('\n\x0e\x64\x65vmodel.proto\"n\n\x0fsWAdapterParams\x12\x1d\n\x05\x61Type\x18\x01 \x01(\x0e\x32\x0e.sWAdapterType\x12\x19\n\x11underlayInterface\x18\x08 \x01(\t\x12\x0e\n\x06vlanId\x18\t \x01(\r\x12\x11\n\tbondgroup\x18\n \x03(\t\"\xa1\x01\n\rSystemAdapter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x0c\x61llocDetails\x18\x14 \x01(\x0b\x32\x10.sWAdapterParams\x12\x12\n\nfreeUplink\x18\x02 \x01(\x08\x12\x0e\n\x06uplink\x18\x03 \x01(\x08\x12\x13\n\x0bnetworkUUID\x18\x04 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x05 \x01(\t\x12\x13\n\x0blogicalName\x18\x06 \x01(\t\"&\n\x10PhyIOUsagePolicy\x12\x12\n\nfreeUplink\x18\x01 \x01(\x08\"\xe2\x02\n\nPhysicalIO\x12\x19\n\x05ptype\x18\x01 \x01(\x0e\x32\n.PhyIoType\x12\x10\n\x08phylabel\x18\x02 \x01(\t\x12+\n\x08phyaddrs\x18\x03 \x03(\x0b\x32\x19.PhysicalIO.PhyaddrsEntry\x12\x14\n\x0clogicallabel\x18\x04 \x01(\t\x12\x11\n\tassigngrp\x18\x05 \x01(\t\x12 \n\x05usage\x18\x06 \x01(\x0e\x32\x11.PhyIoMemberUsage\x12&\n\x0busagePolicy\x18\x07 \x01(\x0b\x32\x11.PhyIOUsagePolicy\x12\'\n\x06\x63\x62\x61ttr\x18\x08 \x03(\x0b\x32\x17.PhysicalIO.CbattrEntry\x1a/\n\rPhyaddrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0b\x43\x62\x61ttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*\\\n\x08ZCioType\x12\x0b\n\x07ZCioNop\x10\x00\x12\x0b\n\x07ZCioEth\x10\x01\x12\x0b\n\x07ZCioUSB\x10\x02\x12\x0b\n\x07ZCioCOM\x10\x03\x12\x0c\n\x08ZCioHDMI\x10\x04\x12\x0e\n\tZCioOther\x10\xff\x01*/\n\rsWAdapterType\x12\n\n\x06IGNORE\x10\x00\x12\x08\n\x04VLAN\x10\x01\x12\x08\n\x04\x42OND\x10\x02*\x9b\x01\n\tPhyIoType\x12\r\n\tPhyIoNoop\x10\x00\x12\x0f\n\x0bPhyIoNetEth\x10\x01\x12\x0c\n\x08PhyIoUSB\x10\x02\x12\x0c\n\x08PhyIoCOM\x10\x03\x12\x0e\n\nPhyIoAudio\x10\x04\x12\x10\n\x0cPhyIoNetWLAN\x10\x05\x12\x10\n\x0cPhyIoNetWWAN\x10\x06\x12\r\n\tPhyIoHDMI\x10\x07\x12\x0f\n\nPhyIoOther\x10\xff\x01*i\n\x10PhyIoMemberUsage\x12\x12\n\x0ePhyIoUsageNone\x10\x00\x12\x12\n\x0ePhyIoUsageMgmt\x10\x01\x12\x14\n\x10PhyIoUsageShared\x10\x02\x12\x17\n\x13PhyIoUsageDedicated\x10\x03\x42G\n\x1f\x63om.zededa.cloud.uservice.protoZ$github.com/lf-edge/eve/api/go/configb\x06proto3')
)

_ZCIOTYPE = _descriptor.EnumDescriptor(
  name='ZCioType',
  full_name='ZCioType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZCioNop', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioEth', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioUSB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioCOM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioHDMI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZCioOther', index=5, number=255,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=691,
  serialized_end=783,
)
_sym_db.RegisterEnumDescriptor(_ZCIOTYPE)

ZCioType = enum_type_wrapper.EnumTypeWrapper(_ZCIOTYPE)
_SWADAPTERTYPE = _descriptor.EnumDescriptor(
  name='sWAdapterType',
  full_name='sWAdapterType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IGNORE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VLAN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOND', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=785,
  serialized_end=832,
)
_sym_db.RegisterEnumDescriptor(_SWADAPTERTYPE)

sWAdapterType = enum_type_wrapper.EnumTypeWrapper(_SWADAPTERTYPE)
_PHYIOTYPE = _descriptor.EnumDescriptor(
  name='PhyIoType',
  full_name='PhyIoType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PhyIoNoop', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoNetEth', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoUSB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoCOM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoAudio', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoNetWLAN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoNetWWAN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoHDMI', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoOther', index=8, number=255,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=835,
  serialized_end=990,
)
_sym_db.RegisterEnumDescriptor(_PHYIOTYPE)

PhyIoType = enum_type_wrapper.EnumTypeWrapper(_PHYIOTYPE)
_PHYIOMEMBERUSAGE = _descriptor.EnumDescriptor(
  name='PhyIoMemberUsage',
  full_name='PhyIoMemberUsage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PhyIoUsageNone', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoUsageMgmt', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoUsageShared', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PhyIoUsageDedicated', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=992,
  serialized_end=1097,
)
_sym_db.RegisterEnumDescriptor(_PHYIOMEMBERUSAGE)

PhyIoMemberUsage = enum_type_wrapper.EnumTypeWrapper(_PHYIOMEMBERUSAGE)
ZCioNop = 0
ZCioEth = 1
ZCioUSB = 2
ZCioCOM = 3
ZCioHDMI = 4
ZCioOther = 255
IGNORE = 0
VLAN = 1
BOND = 2
PhyIoNoop = 0
PhyIoNetEth = 1
PhyIoUSB = 2
PhyIoCOM = 3
PhyIoAudio = 4
PhyIoNetWLAN = 5
PhyIoNetWWAN = 6
PhyIoHDMI = 7
PhyIoOther = 255
PhyIoUsageNone = 0
PhyIoUsageMgmt = 1
PhyIoUsageShared = 2
PhyIoUsageDedicated = 3



_SWADAPTERPARAMS = _descriptor.Descriptor(
  name='sWAdapterParams',
  full_name='sWAdapterParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aType', full_name='sWAdapterParams.aType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underlayInterface', full_name='sWAdapterParams.underlayInterface', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vlanId', full_name='sWAdapterParams.vlanId', index=2,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bondgroup', full_name='sWAdapterParams.bondgroup', index=3,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=18,
  serialized_end=128,
)


_SYSTEMADAPTER = _descriptor.Descriptor(
  name='SystemAdapter',
  full_name='SystemAdapter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SystemAdapter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allocDetails', full_name='SystemAdapter.allocDetails', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freeUplink', full_name='SystemAdapter.freeUplink', index=2,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uplink', full_name='SystemAdapter.uplink', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='networkUUID', full_name='SystemAdapter.networkUUID', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='SystemAdapter.addr', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logicalName', full_name='SystemAdapter.logicalName', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=131,
  serialized_end=292,
)


_PHYIOUSAGEPOLICY = _descriptor.Descriptor(
  name='PhyIOUsagePolicy',
  full_name='PhyIOUsagePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='freeUplink', full_name='PhyIOUsagePolicy.freeUplink', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=294,
  serialized_end=332,
)


_PHYSICALIO_PHYADDRSENTRY = _descriptor.Descriptor(
  name='PhyaddrsEntry',
  full_name='PhysicalIO.PhyaddrsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PhysicalIO.PhyaddrsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PhysicalIO.PhyaddrsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=642,
)

_PHYSICALIO_CBATTRENTRY = _descriptor.Descriptor(
  name='CbattrEntry',
  full_name='PhysicalIO.CbattrEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PhysicalIO.CbattrEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PhysicalIO.CbattrEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=644,
  serialized_end=689,
)

_PHYSICALIO = _descriptor.Descriptor(
  name='PhysicalIO',
  full_name='PhysicalIO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ptype', full_name='PhysicalIO.ptype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phylabel', full_name='PhysicalIO.phylabel', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phyaddrs', full_name='PhysicalIO.phyaddrs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logicallabel', full_name='PhysicalIO.logicallabel', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assigngrp', full_name='PhysicalIO.assigngrp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usage', full_name='PhysicalIO.usage', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usagePolicy', full_name='PhysicalIO.usagePolicy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cbattr', full_name='PhysicalIO.cbattr', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PHYSICALIO_PHYADDRSENTRY, _PHYSICALIO_CBATTRENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=335,
  serialized_end=689,
)

_SWADAPTERPARAMS.fields_by_name['aType'].enum_type = _SWADAPTERTYPE
_SYSTEMADAPTER.fields_by_name['allocDetails'].message_type = _SWADAPTERPARAMS
_PHYSICALIO_PHYADDRSENTRY.containing_type = _PHYSICALIO
_PHYSICALIO_CBATTRENTRY.containing_type = _PHYSICALIO
_PHYSICALIO.fields_by_name['ptype'].enum_type = _PHYIOTYPE
_PHYSICALIO.fields_by_name['phyaddrs'].message_type = _PHYSICALIO_PHYADDRSENTRY
_PHYSICALIO.fields_by_name['usage'].enum_type = _PHYIOMEMBERUSAGE
_PHYSICALIO.fields_by_name['usagePolicy'].message_type = _PHYIOUSAGEPOLICY
_PHYSICALIO.fields_by_name['cbattr'].message_type = _PHYSICALIO_CBATTRENTRY
DESCRIPTOR.message_types_by_name['sWAdapterParams'] = _SWADAPTERPARAMS
DESCRIPTOR.message_types_by_name['SystemAdapter'] = _SYSTEMADAPTER
DESCRIPTOR.message_types_by_name['PhyIOUsagePolicy'] = _PHYIOUSAGEPOLICY
DESCRIPTOR.message_types_by_name['PhysicalIO'] = _PHYSICALIO
DESCRIPTOR.enum_types_by_name['ZCioType'] = _ZCIOTYPE
DESCRIPTOR.enum_types_by_name['sWAdapterType'] = _SWADAPTERTYPE
DESCRIPTOR.enum_types_by_name['PhyIoType'] = _PHYIOTYPE
DESCRIPTOR.enum_types_by_name['PhyIoMemberUsage'] = _PHYIOMEMBERUSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

sWAdapterParams = _reflection.GeneratedProtocolMessageType('sWAdapterParams', (_message.Message,), dict(
  DESCRIPTOR = _SWADAPTERPARAMS,
  __module__ = 'devmodel_pb2'
  # @@protoc_insertion_point(class_scope:sWAdapterParams)
  ))
_sym_db.RegisterMessage(sWAdapterParams)

SystemAdapter = _reflection.GeneratedProtocolMessageType('SystemAdapter', (_message.Message,), dict(
  DESCRIPTOR = _SYSTEMADAPTER,
  __module__ = 'devmodel_pb2'
  # @@protoc_insertion_point(class_scope:SystemAdapter)
  ))
_sym_db.RegisterMessage(SystemAdapter)

PhyIOUsagePolicy = _reflection.GeneratedProtocolMessageType('PhyIOUsagePolicy', (_message.Message,), dict(
  DESCRIPTOR = _PHYIOUSAGEPOLICY,
  __module__ = 'devmodel_pb2'
  # @@protoc_insertion_point(class_scope:PhyIOUsagePolicy)
  ))
_sym_db.RegisterMessage(PhyIOUsagePolicy)

PhysicalIO = _reflection.GeneratedProtocolMessageType('PhysicalIO', (_message.Message,), dict(

  PhyaddrsEntry = _reflection.GeneratedProtocolMessageType('PhyaddrsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PHYSICALIO_PHYADDRSENTRY,
    __module__ = 'devmodel_pb2'
    # @@protoc_insertion_point(class_scope:PhysicalIO.PhyaddrsEntry)
    ))
  ,

  CbattrEntry = _reflection.GeneratedProtocolMessageType('CbattrEntry', (_message.Message,), dict(
    DESCRIPTOR = _PHYSICALIO_CBATTRENTRY,
    __module__ = 'devmodel_pb2'
    # @@protoc_insertion_point(class_scope:PhysicalIO.CbattrEntry)
    ))
  ,
  DESCRIPTOR = _PHYSICALIO,
  __module__ = 'devmodel_pb2'
  # @@protoc_insertion_point(class_scope:PhysicalIO)
  ))
_sym_db.RegisterMessage(PhysicalIO)
_sym_db.RegisterMessage(PhysicalIO.PhyaddrsEntry)
_sym_db.RegisterMessage(PhysicalIO.CbattrEntry)


DESCRIPTOR._options = None
_PHYSICALIO_PHYADDRSENTRY._options = None
_PHYSICALIO_CBATTRENTRY._options = None
# @@protoc_insertion_point(module_scope)
