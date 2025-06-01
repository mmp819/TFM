
# WARNING: THIS FILE IS AUTO-GENERATED. DO NOT MODIFY.

# This file was generated from vehicle_data.idl
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



VehicleSimulation = idl.get_module("VehicleSimulation")

@idl.struct(
    type_annotations = [idl.final, idl.type_name("VehicleSimulation::VehicleState")],

    member_annotations = {
        'vehicle_id': [idl.key, idl.bound(6),],
    }
)
class VehicleSimulation_VehicleState:
    vehicle_id: str = ""
    timestamp: float = 0.0
    gps_latitude: float = 0.0
    gps_longitude: float = 0.0
    gps_altitude: float = 0.0
    gps_hdop: float = 0.0
    gps_pdop: float = 0.0
    gps_vdop: float = 0.0
    speed: float = 0.0

VehicleSimulation.VehicleState = VehicleSimulation_VehicleState

@idl.struct(
    type_annotations = [idl.final, idl.type_name("VehicleSimulation::AggregatedVehicleData")],

    member_annotations = {
        'sector_id': [idl.key, idl.bound(2),],
    }
)
class VehicleSimulation_AggregatedVehicleData:
    sector_id: str = ""
    timestamp: float = 0.0
    avg_speed: float = 0.0
    vehicle_count: idl.int32 = 0
    congestion_lvl: float = 0.0

VehicleSimulation.AggregatedVehicleData = VehicleSimulation_AggregatedVehicleData
