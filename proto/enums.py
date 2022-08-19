from ast import Pass
from enum import Enum
from tkinter import E
import numpy as numpy

class MessageType(Enum):
    Request_Data        = 0x50
    Reply_Data          = 0x41
    Request_Settings    = 0x03
    Reply_Settings      = 0x43

class ErrorType(Enum):
    No_Error             = 0xF0
    Invalid_Addres       = 0xF1
    Invalid_CMD          = 0xF2
    Invalid_Data         = 0xF3
    Addres_Is_Identified = 0xF4

class ErrorType(Enum):
    Online_Info              = 0x0202
    Group_Online_Info_1      = 0xffff
    Group_Online_Info_2      = 0xfffe
    Module_ONOFF_1_31        = 0x0230
    Module_ONOFF_32_63       = 0x0232
    Voltage_Mode             = 0x0233
    Set_Output_Voltage_Limit = 0x0021
    Set_Output_Current_Limit = 0x0022
    Modify_Group_Number      = 0x001a

class DCOperatingStatusType(Enum):
    Init_Status                     = 0x0000
    PFC_soft_start_initialization_1 = 0x0001  
    PFC_soft_start_initialization_2 = 0x0002  
    PFC_soft_start                  = 0x0003
    DCDC_soft_start_initialization  = 0x0004
    DCDC_soft_start_widening_stage  = 0x0005
    DCDC_soft_start_FM_stage        = 0x0006
    DCDC_soft_start_is_completed    = 0x0007
    Shutdown_is_failed              = 0x0020

class ACOperatingStatusType(Enum):
    Initialization      = 0
    Standby             = 1 
    ACDC_soft_start     = 2
    Normal_operation    = 3
    Alarm               = 4 
    Monitor_shutdown    = 5

# DC status / fault 1

class OutputOvervoltageType(Enum):
    normal = 0
    overvoltage = 1

class OverTemperatureProtection(Enum):
    normal = 0
    overtemprerature = 1

class HardwareFailureType(Enum):
    normal = 0
    fault = 1

class OperatingModeType(Enum):
    manual = 0
    automatic = 1

class FanFailureType(Enum):
    normal = 0
    fault = 1

class ACPowerLimitStateType(Enum):
    valid = 1

class TemperatureDeratingState(Enum):
    valid = 1

class PowerLimitedState(Enum):
    valid = 1

class OnOffStateType(Enum):
    on = 0
    off = 1

class OutputUndervoltageType(Enum):
    normal = 0
    undervoltage = 1

class ModuleAddressConflictType(Enum):
    normal = 0
    conflict = 1

class CurrentImbalanceType(Enum):
    normal = 0
    unbalanced = 1

class CANCommunicationFailed(Enum):
    normal = 0
    failed = 1

# DC status / fault 2

class ShortCircuitCurrentLimitingStateType(Enum):
    normal = 0
    retraction = 1 

class PFCFailureType(Enum):
    normal = 0
    fault = 1
    
class ReadyBootType(Enum):
     invalid = 0
     valid = 1

# AC Status / Fault 1

class ACInputCurrentPhaseLossType(Enum):
    normal = 0
    fault = 1

class ACInputPhaseALossType(Enum):
    normal = 0
    fault = 1

class ACInputPhaseBLossType(Enum):
    normal = 0
    fault = 1

class ACInputPhaseCLossType(Enum):
    normal = 0
    fault = 1

class BUSVoltageOvervoltageType(Enum):
    normal = 0
    overvoltage = 1

class BUSVoltageUndervoltageType(Enum):
    normal = 0
    undervoltage = 1

class BUSVoltageImbalance(Enum):
    normal = 0
    unbalanced = 1

class BUSVoltageImbalanceLimitExceededType(Enum):
    normal = 0
    exceeded = 1

class ACInputOverloadType(Enum):
    normal = 0
    overload = 1

class ACInputOverloadExceededType(Enum):
    normal = 0
    exceeded = 1

class ACInputOverCurrentType(Enum):
    normal = 0
    fault = 1

# AC Status / Fault 2:

class ACInputVoltageOvervoltage(Enum):
    normal = 0
    alarm = 1

class ACInputVoltageUndervoltageType(Enum):
    normal = 0
    alarm = 1

class ACInputFrequencyOverfrequencyType(Enum):
    normal = 0
    alarm = 1

class ACInputFrequencUunderfrequencyType(Enum):
    normal = 0
    alarm = 1

class ACVoltageImbalanceType(Enum):
    normal = 0
    alarm = 1

class ACPhaseLockFailureType(Enum):
    normal = 0
    alarm = 1

class ACVoltageFastPowerDownType(Enum):
    normal = 0
    alarm = 1

class AbnormalACInputType(Enum):
    normal = 0
    alarm = 1
