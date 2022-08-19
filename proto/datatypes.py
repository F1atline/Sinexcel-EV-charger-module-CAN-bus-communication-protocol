from dataclasses import dataclass
import numpy as numpy
from enum import Enum
from proto.enums import *

@dataclass
class SourceAdr:
    Group: numpy.uint8
    SubAdr: numpy.uint8

@dataclass
class DCStatusFault1Type:
    Output_overvoltage: OutputOvervoltageType
    Over_temperature_protection: OverTemperatureProtection
    Module_hardware_failure: HardwareFailureType
    Operating_mode: OperatingModeType
    Fan_failure: FanFailureType
    Reserved: None
    AC_power_limited_state: ACPowerLimitStateType
    Temperature_derating_state: TemperatureDeratingState
    Power_limited_state: PowerLimitedState
    Module_onoff_state: OnOffStateType
    Reserved: None
    Reserved: None
    Output_undervoltage: OutputUndervoltageType
    Module_address_conflict: ModuleAddressConflictType
    Current_imbalance: CurrentImbalanceType
    CAN_communication_failed: CANCommunicationFailed

@dataclass
class DCStatusFault2Type:
    Short_circuit_current_limiting_retraction: ShortCircuitCurrentLimitingStateType
    Reserved: None
    Reserved: None
    PFC_failure: PFCFailureType
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Charger_ready_boot: ReadyBootType
    Reserved: None
    Reserved: None

@dataclass
class ACStatusFault1Type:
    AC_input_current_phase_loss: ACInputCurrentPhaseLossType
    AC_input_phase_A_phase_loss: ACInputPhaseALossType
    AC_input_phase_B_phase_loss: ACInputPhaseBLossType
    AC_input_phase_C_phase_loss: ACInputPhaseCLossType
    BUS_voltage_overvoltage: BUSVoltageOvervoltageType
    BUS_voltage_undervoltage: BUSVoltageUndervoltageType
    BUS_voltage_imbalance: BUSVoltageImbalance
    BUS_voltage_imbalance_limit_exceeded: BUSVoltageImbalanceLimitExceededType
    AC_input_overload:ACInputOverloadType
    AC_input_overload_limit_exceeded: ACInputOverloadExceededType
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    AC_input_overcurrent: ACInputOverCurrentType

@dataclass
class ACStatusFault2Type:
    AC_input_voltage_overvoltage: ACInputVoltageOvervoltage
    AC_input_voltage_undervoltage: ACInputVoltageUndervoltageType
    AC_input_frequency_overfrequency: ACInputFrequencyOverfrequencyType
    AC_input_frequency_underfrequency: ACInputFrequencUunderfrequencyType
    AC_voltage_imbalance: ACVoltageImbalanceType
    AC_side_Phase_lock_failure: ACPhaseLockFailureType
    AC_voltage_fast_power_down: ACVoltageFastPowerDownType
    Abnormal_AC_input: AbnormalACInputType
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None
    Reserved: None