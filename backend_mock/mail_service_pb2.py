# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail-service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12mail-service.proto\"<\n\x0fScheduleRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x05\x12\x10\n\x08\x64\x65\x61\x64line\x18\x02 \x01(\t\"&\n\x10ScheduleResponse\x12\x12\n\nadd_status\x18\x01 \x01(\x05\"2\n\x17NotificationInfoRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x05\"\xa1\x01\n\x18NotificationInfoResponse\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x05\x12\x15\n\rproject_title\x18\x02 \x01(\t\x12\x15\n\rsection_title\x18\x03 \x01(\t\x12\x1a\n\x12notification_title\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\r\n\x05\x65mail\x18\x06 \x03(\t\"O\n\x1fUpdateNotificationStatusRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x05\x12\x13\n\x0bsend_status\x18\x02 \x01(\x05\"7\n UpdateNotificationStatusResponse\x12\x13\n\x0bsend_status\x18\x01 \x01(\x05\"4\n\x19\x43\x61ncelNotificationRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\x05\"1\n\x1a\x43\x61ncelNotificationResponse\x12\x13\n\x0bsend_status\x18\x01 \x01(\x05\x32\x9c\x01\n\x0eMailingService\x12;\n\x14ScheduleNotification\x12\x10.ScheduleRequest\x1a\x11.ScheduleResponse\x12M\n\x12\x43\x61ncelNotification\x12\x1a.CancelNotificationRequest\x1a\x1b.CancelNotificationResponse2\xc1\x01\n\x0e\x42\x61\x63kendService\x12N\n\x17GetFullNotificationInfo\x12\x18.NotificationInfoRequest\x1a\x19.NotificationInfoResponse\x12_\n\x18UpdateNotificationStatus\x12 .UpdateNotificationStatusRequest\x1a!.UpdateNotificationStatusResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mail_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SCHEDULEREQUEST._serialized_start=22
  _SCHEDULEREQUEST._serialized_end=82
  _SCHEDULERESPONSE._serialized_start=84
  _SCHEDULERESPONSE._serialized_end=122
  _NOTIFICATIONINFOREQUEST._serialized_start=124
  _NOTIFICATIONINFOREQUEST._serialized_end=174
  _NOTIFICATIONINFORESPONSE._serialized_start=177
  _NOTIFICATIONINFORESPONSE._serialized_end=338
  _UPDATENOTIFICATIONSTATUSREQUEST._serialized_start=340
  _UPDATENOTIFICATIONSTATUSREQUEST._serialized_end=419
  _UPDATENOTIFICATIONSTATUSRESPONSE._serialized_start=421
  _UPDATENOTIFICATIONSTATUSRESPONSE._serialized_end=476
  _CANCELNOTIFICATIONREQUEST._serialized_start=478
  _CANCELNOTIFICATIONREQUEST._serialized_end=530
  _CANCELNOTIFICATIONRESPONSE._serialized_start=532
  _CANCELNOTIFICATIONRESPONSE._serialized_end=581
  _MAILINGSERVICE._serialized_start=584
  _MAILINGSERVICE._serialized_end=740
  _BACKENDSERVICE._serialized_start=743
  _BACKENDSERVICE._serialized_end=936
# @@protoc_insertion_point(module_scope)
