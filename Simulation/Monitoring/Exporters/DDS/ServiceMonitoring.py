
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from ServiceMonitoring.idl
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


from RoutingServiceMonitoring import *
from RecordingServiceMonitoring import *

RTI = idl.get_module("RTI")

RTI_Service = idl.get_module("RTI_Service")

RTI.Service = RTI_Service

RTI_Service_Monitoring = idl.get_module("RTI_Service_Monitoring")

RTI.Service.Monitoring = RTI_Service_Monitoring
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::ConfigUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_Service_Monitoring_ConfigUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServiceConfig, RTI.RoutingService.Monitoring.DomainRouteConfig, RTI.RoutingService.Monitoring.SessionConfig, RTI.RoutingService.Monitoring.AutoRouteConfig, RTI.RoutingService.Monitoring.RouteConfig, RTI.RoutingService.Monitoring.InputConfig, RTI.RoutingService.Monitoring.OutputConfig, RTI.RecordingService.Monitoring.ServiceConfig, RTI.RecordingService.Monitoring.SessionConfig, RTI.RecordingService.Monitoring.TopicGroupConfig, RTI.RecordingService.Monitoring.TopicConfig] = field(default_factory = RTI.RoutingService.Monitoring.ServiceConfig)

    routing_service: RTI.RoutingService.Monitoring.ServiceConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RouteConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputConfig = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)
    recording_service: RTI.RecordingService.Monitoring.ServiceConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicConfig = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.Service.Monitoring.ConfigUnion = RTI_Service_Monitoring_ConfigUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::Config")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_Service_Monitoring_Config(RTI.Service.Monitoring.KeyedResource):
    value: RTI.Service.Monitoring.ConfigUnion = field(default_factory = RTI.Service.Monitoring.ConfigUnion)

RTI.Service.Monitoring.Config = RTI_Service_Monitoring_Config
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::EventUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_Service_Monitoring_EventUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServiceEvent, RTI.RoutingService.Monitoring.DomainRouteEvent, RTI.RoutingService.Monitoring.SessionEvent, RTI.RoutingService.Monitoring.AutoRouteEvent, RTI.RoutingService.Monitoring.RouteEvent, RTI.RoutingService.Monitoring.InputEvent, RTI.RoutingService.Monitoring.OutputEvent, RTI.RecordingService.Monitoring.ServiceEvent, RTI.RecordingService.Monitoring.SessionEvent, RTI.RecordingService.Monitoring.TopicGroupEvent, RTI.RecordingService.Monitoring.TopicEvent] = field(default_factory = RTI.RoutingService.Monitoring.ServiceEvent)

    routing_service: RTI.RoutingService.Monitoring.ServiceEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RouteEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputEvent = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)
    recording_service: RTI.RecordingService.Monitoring.ServiceEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicEvent = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.Service.Monitoring.EventUnion = RTI_Service_Monitoring_EventUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::Event")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_Service_Monitoring_Event(RTI.Service.Monitoring.KeyedResource):
    value: RTI.Service.Monitoring.EventUnion = field(default_factory = RTI.Service.Monitoring.EventUnion)

RTI.Service.Monitoring.Event = RTI_Service_Monitoring_Event
@idl.union(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::PeriodicUnion")],

    member_annotations = {
        'routing_service': [idl.id(135656345), ],
        'routing_domain_route': [idl.id(13105857), ],
        'routing_session': [idl.id(232603050), ],
        'routing_auto_route': [idl.id(58064840), ],
        'routing_route': [idl.id(60927627), ],
        'routing_input': [idl.id(25713616), ],
        'routing_output': [idl.id(227565324), ],
        'recording_service': [idl.id(99752846), ],
        'recording_session': [idl.id(145509639), ],
        'recording_topic_group': [idl.id(28098579), ],
        'recording_topic': [idl.id(123190568), ],
    }
)

class RTI_Service_Monitoring_PeriodicUnion:

    discriminator: RTI.Service.Monitoring.ResourceKind = RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE
    value: Union[RTI.RoutingService.Monitoring.ServicePeriodic, RTI.RoutingService.Monitoring.DomainRoutePeriodic, RTI.RoutingService.Monitoring.SessionPeriodic, RTI.RoutingService.Monitoring.AutoRoutePeriodic, RTI.RoutingService.Monitoring.RoutePeriodic, RTI.RoutingService.Monitoring.InputPeriodic, RTI.RoutingService.Monitoring.OutputPeriodic, RTI.RecordingService.Monitoring.ServicePeriodic, RTI.RecordingService.Monitoring.SessionPeriodic, RTI.RecordingService.Monitoring.TopicGroupPeriodic, RTI.RecordingService.Monitoring.TopicPeriodic] = field(default_factory = RTI.RoutingService.Monitoring.ServicePeriodic)

    routing_service: RTI.RoutingService.Monitoring.ServicePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SERVICE)
    routing_domain_route: RTI.RoutingService.Monitoring.DomainRoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_DOMAIN_ROUTE)
    routing_session: RTI.RoutingService.Monitoring.SessionPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_SESSION)
    routing_auto_route: RTI.RoutingService.Monitoring.AutoRoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_AUTO_ROUTE)
    routing_route: RTI.RoutingService.Monitoring.RoutePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_ROUTE)
    routing_input: RTI.RoutingService.Monitoring.InputPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_INPUT)
    routing_output: RTI.RoutingService.Monitoring.OutputPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.ROUTING_OUTPUT)
    recording_service: RTI.RecordingService.Monitoring.ServicePeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SERVICE)
    recording_session: RTI.RecordingService.Monitoring.SessionPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_SESSION)
    recording_topic_group: RTI.RecordingService.Monitoring.TopicGroupPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC_GROUP)
    recording_topic: RTI.RecordingService.Monitoring.TopicPeriodic = idl.case(RTI.Service.Monitoring.ResourceKind.RECORDING_TOPIC)

RTI.Service.Monitoring.PeriodicUnion = RTI_Service_Monitoring_PeriodicUnion

@idl.struct(
    type_annotations = [idl.mutable, idl.type_name("RTI::Service::Monitoring::Periodic")],

    member_annotations = {
        'value': [idl.id(12673824), ],
    }
)
class RTI_Service_Monitoring_Periodic(RTI.Service.Monitoring.KeyedResource):
    value: RTI.Service.Monitoring.PeriodicUnion = field(default_factory = RTI.Service.Monitoring.PeriodicUnion)

RTI.Service.Monitoring.Periodic = RTI_Service_Monitoring_Periodic
