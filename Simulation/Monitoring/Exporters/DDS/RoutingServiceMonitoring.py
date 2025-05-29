
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from RoutingServiceMonitoring.idl
# using RTI Code Generator (rtiddsgen) version 4.5.0.
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

RTI_RoutingService = idl.get_module("RTI_RoutingService")

RTI.RoutingService = RTI_RoutingService

RTI_RoutingService_Monitoring = idl.get_module("RTI_RoutingService_Monitoring")

RTI.RoutingService.Monitoring = RTI_RoutingService_Monitoring

RTI_RoutingService_Monitoring_BoundedString = str

RTI.RoutingService.Monitoring.BoundedString = RTI_RoutingService_Monitoring_BoundedString

RTI_RoutingService_Monitoring_FilePath = str

RTI.RoutingService.Monitoring.FilePath = RTI_RoutingService_Monitoring_FilePath

RTI_RoutingService_Monitoring_XmlString = str

RTI.RoutingService.Monitoring.XmlString = RTI_RoutingService_Monitoring_XmlString

RTI_RoutingService_Monitoring_DistributionTopicKind = RTI.Service.Monitoring.DistributionTopicKind

RTI.RoutingService.Monitoring.DistributionTopicKind = RTI_RoutingService_Monitoring_DistributionTopicKind

@idl.enum
class RTI_RoutingService_Monitoring_AdapterClassKind(IntEnum):
    GENERIC = 0
    DDS = 1

RTI.RoutingService.Monitoring.AdapterClassKind = RTI_RoutingService_Monitoring_AdapterClassKind

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::TransformationInfo")],

    member_annotations = {
        'plugin_name': [idl.id(210719575), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'configuration': [idl.id(50778572), idl.bound(255),],
    }
)
class RTI_RoutingService_Monitoring_TransformationInfo:
    plugin_name: str = ""
    configuration: str = ""

RTI.RoutingService.Monitoring.TransformationInfo = RTI_RoutingService_Monitoring_TransformationInfo

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::StreamPortConfig")],

    member_annotations = {
        'stream_name': [idl.id(244573051), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'registered_type_name': [idl.id(190898267), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'connection_name': [idl.id(248778389), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'transformation': [idl.id(251147577), ],
    }
)
class RTI_RoutingService_Monitoring_StreamPortConfig(RTI.Service.Monitoring.EntityConfig):
    stream_name: str = ""
    registered_type_name: str = ""
    connection_name: str = ""
    transformation: Optional[RTI.RoutingService.Monitoring.TransformationInfo] = None

RTI.RoutingService.Monitoring.StreamPortConfig = RTI_RoutingService_Monitoring_StreamPortConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::StreamPortEvent")],

    member_annotations = {
        'endpoint_key': [idl.id(136948497), ],
    }
)
class RTI_RoutingService_Monitoring_StreamPortEvent(RTI.Service.Monitoring.EntityEvent):
    endpoint_key: Optional[RTI.Service.BuiltinTopicKey] = None

RTI.RoutingService.Monitoring.StreamPortEvent = RTI_RoutingService_Monitoring_StreamPortEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::StreamPortPeriodic")],

    member_annotations = {
        'samples_per_sec': [idl.id(56607360), ],
        'bytes_per_sec': [idl.id(172643302), ],
    }
)
class RTI_RoutingService_Monitoring_StreamPortPeriodic:
    samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None

RTI.RoutingService.Monitoring.StreamPortPeriodic = RTI_RoutingService_Monitoring_StreamPortPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::InputConfig")])
class RTI_RoutingService_Monitoring_InputConfig(RTI.RoutingService.Monitoring.StreamPortConfig):
    pass

RTI.RoutingService.Monitoring.InputConfig = RTI_RoutingService_Monitoring_InputConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::InputEvent")])
class RTI_RoutingService_Monitoring_InputEvent(RTI.RoutingService.Monitoring.StreamPortEvent):
    pass

RTI.RoutingService.Monitoring.InputEvent = RTI_RoutingService_Monitoring_InputEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::InputPeriodic")])
class RTI_RoutingService_Monitoring_InputPeriodic(RTI.RoutingService.Monitoring.StreamPortPeriodic):
    pass

RTI.RoutingService.Monitoring.InputPeriodic = RTI_RoutingService_Monitoring_InputPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::OutputConfig")])
class RTI_RoutingService_Monitoring_OutputConfig(RTI.RoutingService.Monitoring.StreamPortConfig):
    pass

RTI.RoutingService.Monitoring.OutputConfig = RTI_RoutingService_Monitoring_OutputConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::OutputEvent")])
class RTI_RoutingService_Monitoring_OutputEvent(RTI.RoutingService.Monitoring.StreamPortEvent):
    pass

RTI.RoutingService.Monitoring.OutputEvent = RTI_RoutingService_Monitoring_OutputEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::OutputPeriodic")])
class RTI_RoutingService_Monitoring_OutputPeriodic(RTI.RoutingService.Monitoring.StreamPortPeriodic):
    pass

RTI.RoutingService.Monitoring.OutputPeriodic = RTI_RoutingService_Monitoring_OutputPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::RouteConfig")],

    member_annotations = {
        'auto_route_guid': [idl.id(31409865), ],
    }
)
class RTI_RoutingService_Monitoring_RouteConfig(RTI.Service.Monitoring.EntityConfig):
    auto_route_guid: Optional[RTI.Service.Monitoring.ResourceGuid] = None

RTI.RoutingService.Monitoring.RouteConfig = RTI_RoutingService_Monitoring_RouteConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::RouteEvent")])
class RTI_RoutingService_Monitoring_RouteEvent(RTI.Service.Monitoring.EntityEvent):
    pass

RTI.RoutingService.Monitoring.RouteEvent = RTI_RoutingService_Monitoring_RouteEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::RoutePeriodic")],

    member_annotations = {
        'in_samples_per_sec': [idl.id(7043531), ],
        'in_bytes_per_sec': [idl.id(127450418), ],
        'out_samples_per_sec': [idl.id(207273174), ],
        'out_bytes_per_sec': [idl.id(43897310), ],
        'latency_millisec': [idl.id(25379405), ],
    }
)
class RTI_RoutingService_Monitoring_RoutePeriodic:
    in_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    in_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    latency_millisec: Optional[RTI.Service.Monitoring.StatisticVariable] = None

RTI.RoutingService.Monitoring.RoutePeriodic = RTI_RoutingService_Monitoring_RoutePeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::AutoRouteStreamPortInfo")],

    member_annotations = {
        'configuration': [idl.id(50778572), idl.bound(255),],
    }
)
class RTI_RoutingService_Monitoring_AutoRouteStreamPortInfo:
    configuration: str = ""

RTI.RoutingService.Monitoring.AutoRouteStreamPortInfo = RTI_RoutingService_Monitoring_AutoRouteStreamPortInfo

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::AutoRouteConfig")],

    member_annotations = {
        'input': [idl.id(169557156), ],
        'output': [idl.id(253945464), ],
    }
)
class RTI_RoutingService_Monitoring_AutoRouteConfig(RTI.Service.Monitoring.EntityConfig):
    input: Optional[RTI.RoutingService.Monitoring.AutoRouteStreamPortInfo] = None
    output: Optional[RTI.RoutingService.Monitoring.AutoRouteStreamPortInfo] = None

RTI.RoutingService.Monitoring.AutoRouteConfig = RTI_RoutingService_Monitoring_AutoRouteConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::AutoRouteEvent")])
class RTI_RoutingService_Monitoring_AutoRouteEvent(RTI.Service.Monitoring.EntityEvent):
    pass

RTI.RoutingService.Monitoring.AutoRouteEvent = RTI_RoutingService_Monitoring_AutoRouteEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::AutoRoutePeriodic")],

    member_annotations = {
        'in_samples_per_sec': [idl.id(7043531), ],
        'in_bytes_per_sec': [idl.id(127450418), ],
        'out_samples_per_sec': [idl.id(207273174), ],
        'out_bytes_per_sec': [idl.id(43897310), ],
        'latency_millisec': [idl.id(25379405), ],
        'route_count': [idl.id(182346748), ],
    }
)
class RTI_RoutingService_Monitoring_AutoRoutePeriodic:
    in_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    in_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    latency_millisec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    route_count: int = 0

RTI.RoutingService.Monitoring.AutoRoutePeriodic = RTI_RoutingService_Monitoring_AutoRoutePeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::SessionConfig")])
class RTI_RoutingService_Monitoring_SessionConfig(RTI.Service.Monitoring.EntityConfig):
    pass

RTI.RoutingService.Monitoring.SessionConfig = RTI_RoutingService_Monitoring_SessionConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::SessionEvent")])
class RTI_RoutingService_Monitoring_SessionEvent(RTI.Service.Monitoring.EntityEvent):
    pass

RTI.RoutingService.Monitoring.SessionEvent = RTI_RoutingService_Monitoring_SessionEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::SessionPeriodic")],

    member_annotations = {
        'in_samples_per_sec': [idl.id(7043531), ],
        'in_bytes_per_sec': [idl.id(127450418), ],
        'out_samples_per_sec': [idl.id(207273174), ],
        'out_bytes_per_sec': [idl.id(43897310), ],
        'latency_millisec': [idl.id(25379405), ],
        'thread_pool': [idl.id(14967618), ],
    }
)
class RTI_RoutingService_Monitoring_SessionPeriodic:
    in_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    in_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    latency_millisec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    thread_pool: Optional[RTI.Service.Monitoring.ThreadPoolPeriodic] = None

RTI.RoutingService.Monitoring.SessionPeriodic = RTI_RoutingService_Monitoring_SessionPeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ConnectionConfigInfo")],

    member_annotations = {
        'name': [idl.id(210987184), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        '_py_class': [idl.id(267252386), idl.default(0),],
        'plugin_name': [idl.id(210719575), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'configuration': [idl.id(50778572), idl.bound(255),],
    }
)
class RTI_RoutingService_Monitoring_ConnectionConfigInfo:
    name: str = ""
    _py_class: RTI.RoutingService.Monitoring.AdapterClassKind = RTI.RoutingService.Monitoring.AdapterClassKind.GENERIC
    plugin_name: str = ""
    configuration: str = ""

RTI.RoutingService.Monitoring.ConnectionConfigInfo = RTI_RoutingService_Monitoring_ConnectionConfigInfo

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ConnectionEventInfo")],

    member_annotations = {
        'name': [idl.id(210987184), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'participant_key': [idl.id(132084097), ],
    }
)
class RTI_RoutingService_Monitoring_ConnectionEventInfo:
    name: str = ""
    participant_key: Optional[RTI.Service.BuiltinTopicKey] = None

RTI.RoutingService.Monitoring.ConnectionEventInfo = RTI_RoutingService_Monitoring_ConnectionEventInfo

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::DomainRouteConfig")],

    member_annotations = {
        'connections': [idl.id(235556382), idl.bound(100)],
    }
)
class RTI_RoutingService_Monitoring_DomainRouteConfig(RTI.Service.Monitoring.EntityConfig):
    connections: Optional[Sequence[RTI.RoutingService.Monitoring.ConnectionConfigInfo]] = None

RTI.RoutingService.Monitoring.DomainRouteConfig = RTI_RoutingService_Monitoring_DomainRouteConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::DomainRouteEvent")],

    member_annotations = {
        'connections': [idl.id(235556382), idl.bound(100)],
    }
)
class RTI_RoutingService_Monitoring_DomainRouteEvent(RTI.Service.Monitoring.EntityEvent):
    connections: Optional[Sequence[RTI.RoutingService.Monitoring.ConnectionEventInfo]] = None

RTI.RoutingService.Monitoring.DomainRouteEvent = RTI_RoutingService_Monitoring_DomainRouteEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::DomainRoutePeriodic")],

    member_annotations = {
        'in_samples_per_sec': [idl.id(7043531), ],
        'in_bytes_per_sec': [idl.id(127450418), ],
        'out_samples_per_sec': [idl.id(207273174), ],
        'out_bytes_per_sec': [idl.id(43897310), ],
        'latency_millisec': [idl.id(25379405), ],
    }
)
class RTI_RoutingService_Monitoring_DomainRoutePeriodic:
    in_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    in_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_samples_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    out_bytes_per_sec: Optional[RTI.Service.Monitoring.StatisticVariable] = None
    latency_millisec: Optional[RTI.Service.Monitoring.StatisticVariable] = None

RTI.RoutingService.Monitoring.DomainRoutePeriodic = RTI_RoutingService_Monitoring_DomainRoutePeriodic

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ServiceConfig")],

    member_annotations = {
        'application_name': [idl.id(20524100), idl.bound(RTI.Service.BOUNDED_STRING_LENGTH_MAX),],
        'application_guid': [idl.id(217559336), ],
        'host': [idl.id(148616039), ],
        'process': [idl.id(135558480), ],
    }
)
class RTI_RoutingService_Monitoring_ServiceConfig(RTI.Service.Monitoring.EntityConfig):
    application_name: str = ""
    application_guid: RTI.Service.Monitoring.ResourceGuid = field(default_factory = RTI.Service.Monitoring.ResourceGuid)
    host: Optional[RTI.Service.Monitoring.HostConfig] = None
    process: Optional[RTI.Service.Monitoring.ProcessConfig] = None

RTI.RoutingService.Monitoring.ServiceConfig = RTI_RoutingService_Monitoring_ServiceConfig

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ServiceEvent")])
class RTI_RoutingService_Monitoring_ServiceEvent(RTI.Service.Monitoring.EntityEvent):
    pass

RTI.RoutingService.Monitoring.ServiceEvent = RTI_RoutingService_Monitoring_ServiceEvent

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ServicePeriodic")],

    member_annotations = {
        'host': [idl.id(148616039), ],
        'process': [idl.id(135558480), ],
    }
)
class RTI_RoutingService_Monitoring_ServicePeriodic:
    host: Optional[RTI.Service.Monitoring.HostPeriodic] = None
    process: Optional[RTI.Service.Monitoring.ProcessPeriodic] = None

RTI.RoutingService.Monitoring.ServicePeriodic = RTI_RoutingService_Monitoring_ServicePeriodic
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::ConfigUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
    }
)

class RTI_RoutingService_Monitoring_ConfigUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServiceConfig, RTI.RoutingService.Monitoring.DomainRouteConfig, RTI.RoutingService.Monitoring.SessionConfig, RTI.RoutingService.Monitoring.AutoRouteConfig, RTI.RoutingService.Monitoring.RouteConfig, RTI.RoutingService.Monitoring.InputConfig, RTI.RoutingService.Monitoring.OutputConfig] = field(default_factory = RTI.RoutingService.Monitoring.ServiceConfig)

    routing_service: RTI.RoutingService.Monitoring.ServiceConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)

RTI.RoutingService.Monitoring.ConfigUnion = RTI_RoutingService_Monitoring_ConfigUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::Config")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RoutingService_Monitoring_Config(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RoutingService.Monitoring.ConfigUnion = field(default_factory = RTI.RoutingService.Monitoring.ConfigUnion)

RTI.RoutingService.Monitoring.Config = RTI_RoutingService_Monitoring_Config
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::EventUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
    }
)

class RTI_RoutingService_Monitoring_EventUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServiceEvent, RTI.RoutingService.Monitoring.DomainRouteEvent, RTI.RoutingService.Monitoring.SessionEvent, RTI.RoutingService.Monitoring.AutoRouteEvent, RTI.RoutingService.Monitoring.RouteEvent, RTI.RoutingService.Monitoring.InputEvent, RTI.RoutingService.Monitoring.OutputEvent] = field(default_factory = RTI.RoutingService.Monitoring.ServiceEvent)

    routing_service: RTI.RoutingService.Monitoring.ServiceEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)

RTI.RoutingService.Monitoring.EventUnion = RTI_RoutingService_Monitoring_EventUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::Event")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RoutingService_Monitoring_Event(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RoutingService.Monitoring.EventUnion = field(default_factory = RTI.RoutingService.Monitoring.EventUnion)

RTI.RoutingService.Monitoring.Event = RTI_RoutingService_Monitoring_Event
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::PeriodicUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
    }
)

class RTI_RoutingService_Monitoring_PeriodicUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServicePeriodic, RTI.RoutingService.Monitoring.DomainRoutePeriodic, RTI.RoutingService.Monitoring.SessionPeriodic, RTI.RoutingService.Monitoring.AutoRoutePeriodic, RTI.RoutingService.Monitoring.RoutePeriodic, RTI.RoutingService.Monitoring.InputPeriodic, RTI.RoutingService.Monitoring.OutputPeriodic] = field(default_factory = RTI.RoutingService.Monitoring.ServicePeriodic)

    routing_service: RTI.RoutingService.Monitoring.ServicePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)

RTI.RoutingService.Monitoring.PeriodicUnion = RTI_RoutingService_Monitoring_PeriodicUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::RoutingService::Monitoring::Periodic")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_RoutingService_Monitoring_Periodic(RTI.Service.Monitoring.KeyedResource):
    value: RTI.RoutingService.Monitoring.PeriodicUnion = field(default_factory = RTI.RoutingService.Monitoring.PeriodicUnion)

RTI.RoutingService.Monitoring.Periodic = RTI_RoutingService_Monitoring_Periodic
