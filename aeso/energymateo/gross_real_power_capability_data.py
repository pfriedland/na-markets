from dataclasses import dataclass, field
from typing import List, Optional
from .wind_facility_met_data import (
    TimeStampsActivity,
    TimeStampsSource,
)

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


@dataclass
class GrossRealPowerCapabilityDataType:
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
    time_stamps: List["GrossRealPowerCapabilityDataType.TimeStamps"] = field(
        default_factory=list,
        metadata={
            "name": "TimeStamps",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
        }
    )
    gross_real_power_capability: List["GrossRealPowerCapabilityDataType.GrossRealPowerCapability"] = field(
        default_factory=list,
        metadata={
            "name": "GrossRealPowerCapability",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
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
    class GrossRealPowerCapability:
        time_stamp_begin: Optional[str] = field(
            default=None,
            metadata={
                "name": "TimeStampBegin",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "pattern": r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ",
            }
        )
        time_stamp_end: Optional[str] = field(
            default=None,
            metadata={
                "name": "TimeStampEnd",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "pattern": r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ",
            }
        )
        capacity_average: Optional[float] = field(
            default=None,
            metadata={
                "name": "CapacityAverage",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -1.0,
            }
        )


@dataclass
class GrossRealPowerCapabilityData(GrossRealPowerCapabilityDataType):
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
