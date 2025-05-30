
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from RecordingServiceMonitoring.idl
# using RTI Code Generator (rtiddsgen) version 4.5.0.1.
# The rtiddsgen tool is part of the RTI Connext DDS distribution.
# For more information, type 'rtiddsgen -help' at a command shell
# or consult the Code Generator User's Manual.

from dataclasses import field
from typing import Union, Sequence, Optional
import rti.idl as idl
import rti.rpc as rpc
from enum import IntEnum
import sys
import os
from abc import ABC


from ServiceCommon import *

RTI = idl.get_module("RTI")

RTI_RecordingService = idl.get_module("RTI_RecordingService")

RTI.RecordingService = RTI_RecordingService

RTI_RecordingService_Monitoring = idl.get_module("RTI_RecordingService_Monitoring")

RTI.RecordingService.Monitoring = RTI_RecordingService_Monitoring

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicConfig")],

    member_annotations = {
        'topic_name': [idl.id(86271723), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'registered_type_name': [idl.id(190898267), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'participant_name': [idl.id(39253971), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'topic_group': [idl.id(150052247), ],
    }
)
class RTI_RecordingService_Monitoring_TopicConfig(RTI.Service.Monitoring.EntityConfig):
    topic_name: str = ""
    registered_type_name: str = ""
    participant_name: str = ""
    topic_group: RTI.Service.Monitoring.ResourceGuid = field(default_factory = RTI.Service.Monitoring.ResourceGuid)

RTI.RecordingService.Monitoring.TopicConfig = RTI_RecordingService_Monitoring_TopicConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicEvent")],

    member_annotations = {
        '_dummy': [idl.id(231408241), ],
    }
)
class RTI_RecordingService_Monitoring_TopicEvent(RTI.Service.Monitoring.EntityEvent):
    _dummy: idl.int32 = 0

RTI.RecordingService.Monitoring.TopicEvent = RTI_RecordingService_Monitoring_TopicEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicPeriodic")],

    member_annotations = {
        'network_performance': [idl.id(53037858), ],
        'matched_status': [idl.id(184706801), ],
    }
)
class RTI_RecordingService_Monitoring_TopicPeriodic:
    network_performance: Optional[RTI.Service.Monitoring.NetworkPerformance] = None
    matched_status: Optional[RTI.Service.Monitoring.CountStatus] = None

RTI.RecordingService.Monitoring.TopicPeriodic = RTI_RecordingService_Monitoring_TopicPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicGroupConfig")],

    member_annotations = {
        'participant_name': [idl.id(39253971), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
    }
)
class RTI_RecordingService_Monitoring_TopicGroupConfig(RTI.Service.Monitoring.EntityConfig):
    participant_name: str = ""

RTI.RecordingService.Monitoring.TopicGroupConfig = RTI_RecordingService_Monitoring_TopicGroupConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicGroupEvent")],

    member_annotations = {
        '_dummy': [idl.id(231408241), ],
    }
)
class RTI_RecordingService_Monitoring_TopicGroupEvent(RTI.Service.Monitoring.EntityEvent):
    _dummy: idl.int32 = 0

RTI.RecordingService.Monitoring.TopicGroupEvent = RTI_RecordingService_Monitoring_TopicGroupEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::TopicGroupPeriodic")],

    member_annotations = {
        'network_performance': [idl.id(53037858), ],
        'topic_count': [idl.id(48236934), ],
    }
)
class RTI_RecordingService_Monitoring_TopicGroupPeriodic:
    network_performance: Optional[RTI.Service.Monitoring.NetworkPerformance] = None
    topic_count: int = 0

RTI.RecordingService.Monitoring.TopicGroupPeriodic = RTI_RecordingService_Monitoring_TopicGroupPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SessionConfig")],

    member_annotations = {
        'default_participant_name': [idl.id(209495964), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
    }
)
class RTI_RecordingService_Monitoring_SessionConfig(RTI.Service.Monitoring.EntityConfig):
    default_participant_name: str = ""

RTI.RecordingService.Monitoring.SessionConfig = RTI_RecordingService_Monitoring_SessionConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SessionEvent")],

    member_annotations = {
        '_dummy': [idl.id(231408241), ],
    }
)
class RTI_RecordingService_Monitoring_SessionEvent(RTI.Service.Monitoring.EntityEvent):
    _dummy: idl.int32 = 0

RTI.RecordingService.Monitoring.SessionEvent = RTI_RecordingService_Monitoring_SessionEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SessionPeriodic")],

    member_annotations = {
        'network_performance': [idl.id(53037858), ],
        'thread_pool': [idl.id(14967618), ],
    }
)
class RTI_RecordingService_Monitoring_SessionPeriodic:
    network_performance: Optional[RTI.Service.Monitoring.NetworkPerformance] = None
    thread_pool: Optional[RTI.Service.Monitoring.ThreadPoolPeriodic] = None

RTI.RecordingService.Monitoring.SessionPeriodic = RTI_RecordingService_Monitoring_SessionPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SqliteDatabaseConfig")],

    member_annotations = {
        'db_directory': [idl.id(245637612), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
        'execution_directory_expression': [idl.id(164393944), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
        'user_data_file_expression': [idl.id(198600638), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
    }
)
class RTI_RecordingService_Monitoring_SqliteDatabaseConfig:
    db_directory: str = ""
    execution_directory_expression: Optional[str] = None
    user_data_file_expression: Optional[str] = None

RTI.RecordingService.Monitoring.SqliteDatabaseConfig = RTI_RecordingService_Monitoring_SqliteDatabaseConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SqliteDatabaseEvent")],

    member_annotations = {
        'current_db_directory': [idl.id(238001274), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
        'current_file': [idl.id(5676753), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
        'rollover_count': [idl.id(168090855), ],
    }
)
class RTI_RecordingService_Monitoring_SqliteDatabaseEvent:
    current_db_directory: Optional[str] = None
    current_file: Optional[str] = None
    rollover_count: Optional[idl.int32] = None

RTI.RecordingService.Monitoring.SqliteDatabaseEvent = RTI_RecordingService_Monitoring_SqliteDatabaseEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::SqliteDatabasePeriodic")],

    member_annotations = {
        'current_file': [idl.id(5676753), idl.bound(RTI.Service.FILE_PATH_MAX_LENGTH),],
        'current_file_size': [idl.id(158098344), ],
        'current_timestamp_sec': [idl.id(114132813), ],
        'current_timestamp_nanosec': [idl.id(60585440), ],
    }
)
class RTI_RecordingService_Monitoring_SqliteDatabasePeriodic:
    current_file: Optional[str] = None
    current_file_size: Optional[idl.uint64] = None
    current_timestamp_sec: idl.int32 = 0
    current_timestamp_nanosec: idl.uint32 = 0

RTI.RecordingService.Monitoring.SqliteDatabasePeriodic = RTI_RecordingService_Monitoring_SqliteDatabasePeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::ParticipantInfo")],

    member_annotations = {
        'name': [idl.id(210987184), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
    }
)
class RTI_RecordingService_Monitoring_ParticipantInfo:
    name: str = ""

RTI.RecordingService.Monitoring.ParticipantInfo = RTI_RecordingService_Monitoring_ParticipantInfo

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::ServiceConfig")],

    member_annotations = {
        'application_name': [idl.id(20524100), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'application_guid': [idl.id(217559336), ],
        'host': [idl.id(148616039), ],
        'process': [idl.id(135558480), ],
        'builtin_sqlite': [idl.id(151085104), ],
        'participants': [idl.id(78010457), idl.bound(100)],
    }
)
class RTI_RecordingService_Monitoring_ServiceConfig(RTI.Service.Monitoring.EntityConfig):
    application_name: str = ""
    application_guid: RTI.Service.Monitoring.ResourceGuid = field(default_factory = RTI.Service.Monitoring.ResourceGuid)
    host: Optional[RTI.Service.Monitoring.HostConfig] = None
    process: Optional[RTI.Service.Monitoring.ProcessConfig] = None
    builtin_sqlite: Optional[RTI.RecordingService.Monitoring.SqliteDatabaseConfig] = None
    participants: Optional[Sequence[RTI.RecordingService.Monitoring.ParticipantInfo]] = None

RTI.RecordingService.Monitoring.ServiceConfig = RTI_RecordingService_Monitoring_ServiceConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::ServiceEvent")],

    member_annotations = {
        'builtin_sqlite': [idl.id(151085104), ],
    }
)
class RTI_RecordingService_Monitoring_ServiceEvent(RTI.Service.Monitoring.EntityEvent):
    builtin_sqlite: Optional[RTI.RecordingService.Monitoring.SqliteDatabaseEvent] = None

RTI.RecordingService.Monitoring.ServiceEvent = RTI_RecordingService_Monitoring_ServiceEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::ServicePeriodic")],

    member_annotations = {
        'host': [idl.id(148616039), ],
        'process': [idl.id(135558480), ],
        'current_timestamp_nanos': [idl.id(229515784), ],
        'builtin_sqlite': [idl.id(151085104), ],
    }
)
class RTI_RecordingService_Monitoring_ServicePeriodic:
    host: Optional[RTI.Service.Monitoring.HostPeriodic] = None
    process: Optional[RTI.Service.Monitoring.ProcessPeriodic] = None
    current_timestamp_nanos: int = 0
    builtin_sqlite: Optional[RTI.RecordingService.Monitoring.SqliteDatabasePeriodic] = None

RTI.RecordingService.Monitoring.ServicePeriodic = RTI_RecordingService_Monitoring_ServicePeriodic
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::ConfigUnion")],

    member_annotations = {
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_RecordingService_Monitoring_ConfigUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE
    value: Union[RTI.RecordingService.Monitoring.ServiceConfig, RTI.RecordingService.Monitoring.SessionConfig, RTI.RecordingService.Monitoring.TopicGroupConfig, RTI.RecordingService.Monitoring.TopicConfig] = field(default_factory = RTI.RecordingService.Monitoring.ServiceConfig)

    recording_service: RTI.RecordingService.Monitoring.ServiceConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.RecordingService.Monitoring.ConfigUnion = RTI_RecordingService_Monitoring_ConfigUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::Config")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RecordingService_Monitoring_Config(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RecordingService.Monitoring.ConfigUnion = field(default_factory = RTI.RecordingService.Monitoring.ConfigUnion)

RTI.RecordingService.Monitoring.Config = RTI_RecordingService_Monitoring_Config
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::EventUnion")],

    member_annotations = {
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_RecordingService_Monitoring_EventUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE
    value: Union[RTI.RecordingService.Monitoring.ServiceEvent, RTI.RecordingService.Monitoring.SessionEvent, RTI.RecordingService.Monitoring.TopicGroupEvent, RTI.RecordingService.Monitoring.TopicEvent] = field(default_factory = RTI.RecordingService.Monitoring.ServiceEvent)

    recording_service: RTI.RecordingService.Monitoring.ServiceEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.RecordingService.Monitoring.EventUnion = RTI_RecordingService_Monitoring_EventUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::Event")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RecordingService_Monitoring_Event(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RecordingService.Monitoring.EventUnion = field(default_factory = RTI.RecordingService.Monitoring.EventUnion)

RTI.RecordingService.Monitoring.Event = RTI_RecordingService_Monitoring_Event
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::PeriodicUnion")],

    member_annotations = {
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_RecordingService_Monitoring_PeriodicUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE
    value: Union[RTI.RecordingService.Monitoring.ServicePeriodic, RTI.RecordingService.Monitoring.SessionPeriodic, RTI.RecordingService.Monitoring.TopicGroupPeriodic, RTI.RecordingService.Monitoring.TopicPeriodic] = field(default_factory = RTI.RecordingService.Monitoring.ServicePeriodic)

    recording_service: RTI.RecordingService.Monitoring.ServicePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.RecordingService.Monitoring.PeriodicUnion = RTI_RecordingService_Monitoring_PeriodicUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RecordingService::Monitoring::Periodic")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RecordingService_Monitoring_Periodic(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RecordingService.Monitoring.PeriodicUnion = field(default_factory = RTI.RecordingService.Monitoring.PeriodicUnion)

RTI.RecordingService.Monitoring.Periodic = RTI_RecordingService_Monitoring_Periodic
