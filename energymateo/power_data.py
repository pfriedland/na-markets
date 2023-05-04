from dataclasses import dataclass, field
from typing import List, Optional
from .wind_facility_met_data import (
    TimeStampsActivity,
    TimeStampsSource,
)

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


@dataclass
class PowerDataType:
    facility: Optional[str] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "max_length": 255,
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionID",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "max_length": 255,
        }
    )
    position_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "PositionID",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 6,
        }
    )
    sub_interval: Optional[int] = field(
        default=None,
        metadata={
            "name": "SubInterval",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 9,
        }
    )
    time_stamps: List["PowerDataType.TimeStamps"] = field(
        default_factory=list,
        metadata={
            "name": "TimeStamps",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
        }
    )
    real_power_limit: Optional[float] = field(
        default=None,
        metadata={
            "name": "RealPowerLimit",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "min_inclusive": -1.0,
        }
    )
    net_to_grid: Optional[float] = field(
        default=None,
        metadata={
            "name": "NetToGrid",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "min_inclusive": -1.0,
        }
    )

    @dataclass
    class TimeStamps:
        source: Optional[TimeStampsSource] = field(
            default=None,
            metadata={
                "name": "Source",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )
        activity: Optional[TimeStampsActivity] = field(
            default=None,
            metadata={
                "name": "Activity",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )
        time_stamp: Optional[str] = field(
            default=None,
            metadata={
                "name": "TimeStamp",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "pattern": r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ",
            }
        )


@dataclass
class PowerData(PowerDataType):
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
