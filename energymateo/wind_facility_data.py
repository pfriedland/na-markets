from dataclasses import dataclass, field
from typing import List, Optional
from tests.fixtures.primer.wind_facility_met_data import (
    TimeStampsActivity,
    TimeStampsSource,
)

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


@dataclass
class WindFacilityDataType:
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
    time_stamps: List["WindFacilityDataType.TimeStamps"] = field(
        default_factory=list,
        metadata={
            "name": "TimeStamps",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
        }
    )
    power_curve: List["WindFacilityDataType.PowerCurve"] = field(
        default_factory=list,
        metadata={
            "name": "PowerCurve",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "min_occurs": 1,
        }
    )
    meteorological_tower_data: List["WindFacilityDataType.MeteorologicalTowerData"] = field(
        default_factory=list,
        metadata={
            "name": "MeteorologicalTowerData",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
        }
    )
    turbine_land_data: List["WindFacilityDataType.TurbineLandData"] = field(
        default_factory=list,
        metadata={
            "name": "TurbineLandData",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
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
    class PowerCurve:
        wind_speed: Optional[float] = field(
            default=None,
            metadata={
                "name": "WindSpeed",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
            }
        )
        mega_watts: Optional[float] = field(
            default=None,
            metadata={
                "name": "MegaWatts",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
            }
        )

    @dataclass
    class MeteorologicalTowerData:
        meteorological_tower_unique_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "MeteorologicalTowerUniqueId",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_length": 0,
                "max_length": 90,
            }
        )
        meteorological_tower_data_collection_height: Optional[float] = field(
            default=None,
            metadata={
                "name": "MeteorologicalTowerDataCollectionHeight",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )

    @dataclass
    class TurbineLandData:
        turbine_model_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "TurbineModelName",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )
        turbine_model_capacity: Optional[float] = field(
            default=None,
            metadata={
                "name": "TurbineModelCapacity",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.1,
                "max_inclusive": 20.0,
            }
        )
        turbine_wind_speed_cut_in: Optional[float] = field(
            default=None,
            metadata={
                "name": "TurbineWindSpeedCutIn",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 50.0,
            }
        )
        turbine_wind_speed_cut_out: Optional[float] = field(
            default=None,
            metadata={
                "name": "TurbineWindSpeedCutOut",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 99.0,
            }
        )
        turbine_temperature_cut_out_lower: Optional[float] = field(
            default=None,
            metadata={
                "name": "TurbineTemperatureCutOutLower",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -50.0,
                "max_inclusive": 50.0,
            }
        )
        turbine_temperature_cut_out_upper: Optional[float] = field(
            default=None,
            metadata={
                "name": "TurbineTemperatureCutOutUpper",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -50.0,
                "max_inclusive": 50.0,
            }
        )
        latitude: Optional[float] = field(
            default=None,
            metadata={
                "name": "Latitude",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": 48.0,
                "max_inclusive": 65.0,
            }
        )
        longitude: Optional[float] = field(
            default=None,
            metadata={
                "name": "Longitude",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
                "min_inclusive": -125.0,
                "max_inclusive": -98.0,
            }
        )


@dataclass
class WindFacilityData(WindFacilityDataType):
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
