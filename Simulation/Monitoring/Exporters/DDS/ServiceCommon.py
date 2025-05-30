
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from ServiceCommon.idl
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



RTI = idl.get_module("RTI")

RTI_Service = idl.get_module("RTI_Service")

RTI.Service = RTI_Service

RTI_Service_BOUNDED_STRING_LENGTH_MAX = 1024

RTI.Service.BOUNDED_STRING_LENGTH_MAX = RTI_Service_BOUNDED_STRING_LENGTH_MAX

RTI_Service_BoundedString = str

RTI.Service.BoundedString = RTI_Service_BoundedString

RTI_Service_FILE_PATH_MAX_LENGTH = 1024

RTI.Service.FILE_PATH_MAX_LENGTH = RTI_Service_FILE_PATH_MAX_LENGTH

RTI_Service_FilePath = str

RTI.Service.FilePath = RTI_Service_FilePath

RTI_Service_RESOURCE_IDENTIFIER_LENGTH_MAX = 2048

RTI.Service.RESOURCE_IDENTIFIER_LENGTH_MAX = RTI_Service_RESOURCE_IDENTIFIER_LENGTH_MAX

RTI_Service_ResourceId = str

RTI.Service.ResourceId = RTI_Service_ResourceId

RTI_Service_XmlString = str

RTI.Service.XmlString = RTI_Service_XmlString

@idl.enum
class RTI_Service_EntityStateKind(IntEnum):
    INVALID = 0
    ENABLED = 1
    DISABLED = 2
    STARTED = 3
    STOPPED = 4
    RUNNING = 5
    PAUSED = 6

RTI.Service.EntityStateKind = RTI_Service_EntityStateKind

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::EntityState")],

    member_annotations = {
        'state': [idl.id(245289886), idl.default(0),],
    }
)
class RTI_Service_EntityState:
    state: RTI.Service.EntityStateKind = RTI.Service.EntityStateKind.INVALID

RTI.Service.EntityState = RTI_Service_EntityState

RTI_Service_BUILTIN_TOPIC_KEY_VALUE_LENGTH = 4

RTI.Service.BUILTIN_TOPIC_KEY_VALUE_LENGTH = RTI_Service_BUILTIN_TOPIC_KEY_VALUE_LENGTH

@idl.struct(
    type_annotations = [idl.final, idl.type_name("RTI::Service::BuiltinTopicKey")],

    member_annotations = {
        'value': [idl.id(12673824), idl.array([RTI.Service.BUILTIN_TOPIC_KEY_VALUE_LENGTH])],
    }
)
class RTI_Service_BuiltinTopicKey:
    value: Sequence[idl.uint32] = field(default_factory = idl.array_factory(idl.uint32, [RTI.Service.BUILTIN_TOPIC_KEY_VALUE_LENGTH]))

RTI.Service.BuiltinTopicKey = RTI_Service_BuiltinTopicKey

RTI_Service_Monitoring = idl.get_module("RTI_Service_Monitoring")

RTI.Service.Monitoring = RTI_Service_Monitoring

RTI_Service_Monitoring_RESOURCE_GUID_VALUE_LENGTH = 16

RTI.Service.Monitoring.RESOURCE_GUID_VALUE_LENGTH = RTI_Service_Monitoring_RESOURCE_GUID_VALUE_LENGTH

@idl.struct(
    type_annotations = [idl.final, idl.type_name("RTI::Service::Monitoring::ResourceGuid")],

    member_annotations = {
        'value': [idl.id(12673824), idl.array([RTI.Service.Monitoring.RESOURCE_GUID_VALUE_LENGTH])],
    }
)
class RTI_Service_Monitoring_ResourceGuid:
    value: Sequence[idl.uint8] = field(default_factory = idl.array_factory(idl.uint8, [RTI.Service.Monitoring.RESOURCE_GUID_VALUE_LENGTH]))

RTI.Service.Monitoring.ResourceGuid = RTI_Service_Monitoring_ResourceGuid

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::KeyedResource")],

    member_annotations = {
        'object_guid': [idl.key, idl.id(40060539), ],
        'owner_guid': [idl.id(165202898), ],
    }
)
class RTI_Service_Monitoring_KeyedResource:
    object_guid: RTI.Service.Monitoring.ResourceGuid = field(default_factory = RTI.Service.Monitoring.ResourceGuid)
    owner_guid: RTI.Service.Monitoring.ResourceGuid = field(default_factory = RTI.Service.Monitoring.ResourceGuid)

RTI.Service.Monitoring.KeyedResource = RTI_Service_Monitoring_KeyedResource

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::StatisticMetrics")],

    member_annotations = {
        'period_ms': [idl.id(165434195), ],
        'count': [idl.id(69899490), ],
        'mean': [idl.id(145833401), ],
        'minimum': [idl.id(203654115), ],
        'maximum': [idl.id(149074021), ],
        'std_dev': [idl.id(136822783), ],
    }
)
class RTI_Service_Monitoring_StatisticMetrics:
    period_ms: idl.uint64 = 0
    count: int = 0
    mean: idl.float32 = 0.0
    minimum: idl.float32 = 0.0
    maximum: idl.float32 = 0.0
    std_dev: idl.float32 = 0.0

RTI.Service.Monitoring.StatisticMetrics = RTI_Service_Monitoring_StatisticMetrics

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::StatisticVariable")],

    member_annotations = {
        'publication_period_metrics': [idl.id(232134331), ],
    }
)
class RTI_Service_Monitoring_StatisticVariable:
    publication_period_metrics: RTI.Service.Monitoring.StatisticMetrics = field(default_factory = RTI.Service.Monitoring.StatisticMetrics)

RTI.Service.Monitoring.StatisticVariable = RTI_Service_Monitoring_StatisticVariable

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::CountStatus")],

    member_annotations = {
        'total_count': [idl.id(52314676), ],
        'current_count': [idl.id(210848979), ],
        'current_count_peak': [idl.id(130880564), ],
    }
)
class RTI_Service_Monitoring_CountStatus:
    total_count: int = 0
    current_count: int = 0
    current_count_peak: int = 0

RTI.Service.Monitoring.CountStatus = RTI_Service_Monitoring_CountStatus

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::ProcessConfig")],

    member_annotations = {
        'id': [idl.id(79104952), ],
    }
)
class RTI_Service_Monitoring_ProcessConfig:
    id: idl.uint64 = 0

RTI.Service.Monitoring.ProcessConfig = RTI_Service_Monitoring_ProcessConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ProcessPeriodic")],

    member_annotations = {
        'cpu_usage_percentage': [idl.id(22539634), ],
        'physical_memory_kb': [idl.id(128452345), ],
        'total_memory_kb': [idl.id(89601480), ],
        'uptime_sec': [idl.id(233937351), ],
    }
)
class RTI_Service_Monitoring_ProcessPeriodic:
    cpu_usage_percentage: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    physical_memory_kb: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    total_memory_kb: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    uptime_sec: idl.int32 = 0

RTI.Service.Monitoring.ProcessPeriodic = RTI_Service_Monitoring_ProcessPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ThreadPeriodic")],

    member_annotations = {
        'id': [idl.id(79104952), ],
        'cpu_usage_percentage': [idl.id(22539634), ],
    }
)
class RTI_Service_Monitoring_ThreadPeriodic:
    id: idl.uint64 = 0
    cpu_usage_percentage: Optional[RTI.Service.Monitoring.StatisticVariable] = None

RTI.Service.Monitoring.ThreadPeriodic = RTI_Service_Monitoring_ThreadPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ThreadPoolPeriodic")],

    member_annotations = {
        'threads': [idl.id(83761417), idl.bound(100)],
    }
)
class RTI_Service_Monitoring_ThreadPoolPeriodic:
    threads: Optional[Sequence[RTI.Service.Monitoring.ThreadPeriodic]] = None

RTI.Service.Monitoring.ThreadPoolPeriodic = RTI_Service_Monitoring_ThreadPoolPeriodic

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::HostPeriodic")],

    member_annotations = {
        'cpu_usage_percentage': [idl.id(22539634), ],
        'free_memory_kb': [idl.id(226325808), ],
        'free_swap_memory_kb': [idl.id(225988660), ],
        'uptime_sec': [idl.id(233937351), ],
    }
)
class RTI_Service_Monitoring_HostPeriodic:
    cpu_usage_percentage: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    free_memory_kb: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    free_swap_memory_kb: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    uptime_sec: idl.int32 = 0

RTI.Service.Monitoring.HostPeriodic = RTI_Service_Monitoring_HostPeriodic

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::HostConfig")],

    member_annotations = {
        'name': [idl.id(210987184), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'id': [idl.id(79104952), ],
        'total_memory_kb': [idl.id(89601480), ],
        'total_swap_memory_kb': [idl.id(153693844), ],
        'target': [idl.id(251375170), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
    }
)
class RTI_Service_Monitoring_HostConfig:
    name: str = ""
    id: idl.uint32 = 0
    total_memory_kb: int = 0
    total_swap_memory_kb: int = 0
    target: str = ""

RTI.Service.Monitoring.HostConfig = RTI_Service_Monitoring_HostConfig

@idl.struct(
    type_annotations = [idl.type_name("RTI::Service::Monitoring::NetworkPerformance")],

    member_annotations = {
        'samples_per_sec': [idl.id(56607360), ],
        'bytes_per_sec': [idl.id(172643302), ],
        'latency_millisec': [idl.id(25379405), ],
    }
)
class RTI_Service_Monitoring_NetworkPerformance:
    samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    latency_millisec: Optional[RTI.Service.Monitoring.StatisticVariable] = None

RTI.Service.Monitoring.NetworkPerformance = RTI_Service_Monitoring_NetworkPerformance

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::EntityConfig")],

    member_annotations = {
        'resource_id': [idl.id(200274914), idl.bound(RTI.Service.RESOURCE_IDENTIFIER_LENGTH_MAX),],
        'configuration': [idl.id(50778572), idl.bound(RTI.Service.RESOURCE_IDENTIFIER_LENGTH_MAX),],
    }
)
class RTI_Service_Monitoring_EntityConfig:
    resource_id: str = ""
    configuration: str = ""

RTI.Service.Monitoring.EntityConfig = RTI_Service_Monitoring_EntityConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::EntityEvent")],

    member_annotations = {
        'state': [idl.id(245289886), idl.default(0),],
    }
)
class RTI_Service_Monitoring_EntityEvent:
    state: RTI.Service.EntityStateKind = RTI.Service.EntityStateKind.INVALID

RTI.Service.Monitoring.EntityEvent = RTI_Service_Monitoring_EntityEvent

@idl.enum
class RTI_Service_Monitoring_DistributionTopicKind(IntEnum):
    CONFIG = 0
    EVENT = 1
    PERIODIC = 2

RTI.Service.Monitoring.DistributionTopicKind = RTI_Service_Monitoring_DistributionTopicKind

@idl.enum(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ResourceKindIndex")])
class RTI_Service_Monitoring_ResourceKindIndex(IntEnum):
    DDS_INDEX = 1
    ROUTING_INDEX = 10000
    RECORDING_INDEX = 20000
    CDS_INDEX = 30000

RTI.Service.Monitoring.ResourceKindIndex = RTI_Service_Monitoring_ResourceKindIndex

@idl.enum(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ResourceKind")])
class RTI_Service_Monitoring_ResourceKind(IntEnum):
    UNKNOWN = 0
    ROUTING_SERVICE = 10000
    ROUTING_DOMAIN_ROUTE = 10001
    ROUTING_SESSION = 10002
    ROUTING_AUTO_ROUTE = 10003
    ROUTING_ROUTE = 10004
    ROUTING_INPUT = 10005
    ROUTING_OUTPUT = 10006
    RECORDING_SERVICE = 20000
    RECORDING_SESSION = 20001
    RECORDING_TOPIC_GROUP = 20002
    RECORDING_TOPIC = 20003
    CDS_SERVICE = 30000
    CDS_FORWARDER = 30001
    CDS_DATABASE = 30002
    CDS_RECEIVER = 30003
    CDS_SENDER = 30004

RTI.Service.Monitoring.ResourceKind = RTI_Service_Monitoring_ResourceKind

RTI_Service_Monitoring_CONFIG_TOPIC_NAME = "rti/service/monitoring/config"

RTI.Service.Monitoring.CONFIG_TOPIC_NAME = RTI_Service_Monitoring_CONFIG_TOPIC_NAME

RTI_Service_Monitoring_EVENT_TOPIC_NAME = "rti/service/monitoring/event"

RTI.Service.Monitoring.EVENT_TOPIC_NAME = RTI_Service_Monitoring_EVENT_TOPIC_NAME

RTI_Service_Monitoring_PERIODIC_TOPIC_NAME = "rti/service/monitoring/periodic"

RTI.Service.Monitoring.PERIODIC_TOPIC_NAME = RTI_Service_Monitoring_PERIODIC_TOPIC_NAME

RTI_Service_Monitoring_CONFIG_REGISTERED_TYPE_NAME = "RTI::Service::Monitoring::Config"

RTI.Service.Monitoring.CONFIG_REGISTERED_TYPE_NAME = RTI_Service_Monitoring_CONFIG_REGISTERED_TYPE_NAME

RTI_Service_Monitoring_EVENT_REGISTERED_TYPE_NAME = "RTI::Service::Monitoring::Event"

RTI.Service.Monitoring.EVENT_REGISTERED_TYPE_NAME = RTI_Service_Monitoring_EVENT_REGISTERED_TYPE_NAME

RTI_Service_Monitoring_PERIODIC_REGISTERED_TYPE_NAME = "RTI::Service::Monitoring::Periodic"

RTI.Service.Monitoring.PERIODIC_REGISTERED_TYPE_NAME = RTI_Service_Monitoring_PERIODIC_REGISTERED_TYPE_NAME
