from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


class TimeStampsActivity(Enum):
    SEND = "Send"
    RECEIVE = "Receive"
    PROCESS = "Process"


class TimeStampsSource(Enum):
    WIND_FACILITY = "Wind Facility"
    WIND_FORECASTER = "Wind Forecaster"
    B2_B_PROVIDER = "B2B Provider"


@dataclass
class WindFacilityMetDataType:
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
    time_stamps: List["WindFacilityMetDataType.TimeStamps"] = field(
        default_factory=list,
        metadata={
            "name": "TimeStamps",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
        }
    )
    met_tower_data: List["WindFacilityMetDataType.MetTowerData"] = field(
        default_factory=list,
        metadata={
            "name": "MetTowerData",
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
    class MetTowerData:
        meteorological_tower_unique_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "MeteorologicalTowerUniqueID",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_length": 0,
                "max_length": 90,
            }
        )
        wind_speed: Optional[float] = field(
            default=None,
            metadata={
                "name": "WindSpeed",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50.0,
            }
        )
        wind_direction: Optional[float] = field(
            default=None,
            metadata={
                "name": "WindDirection",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 360.0,
            }
        )
        barometric_pressure: Optional[float] = field(
            default=None,
            metadata={
                "name": "BarometricPressure",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 800.0,
                "max_inclusive": 1000.0,
            }
        )
        ambient_temperature: Optional[float] = field(
            default=None,
            metadata={
                "name": "AmbientTemperature",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -50.0,
                "max_inclusive": 50.0,
            }
        )
        dew_point: Optional[float] = field(
            default=None,
            metadata={
                "name": "DewPoint",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -50.0,
                "max_inclusive": 50.0,
            }
        )
        relative_humidity: Optional[float] = field(
            default=None,
            metadata={
                "name": "RelativeHumidity",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 101.0,
            }
        )
        iceup_parameter: Optional[float] = field(
            default=None,
            metadata={
                "name": "IceupParameter",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1.0,
            }
        )
        precipitation: Optional[float] = field(
            default=None,
            metadata={
                "name": "Precipitation",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 11.0,
            }
        )


@dataclass
class WindFacilityMetData(WindFacilityMetDataType):
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
