from dataclasses import dataclass, field
from typing import List, Optional
from .error_alert import ErrorAlertType
from .gross_real_power_capability_data import GrossRealPowerCapabilityDataType
from .power_data import PowerDataType
from .wind_facility_data import WindFacilityDataType
from .wind_facility_met_data import WindFacilityMetDataType

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


@dataclass
class WindSolarComLayerType:
    """
    :ivar access_key:
    :ivar gzip_data:
    :ivar by_date_nposition_nfacility: A wrapper element to hold the
        Power, MET and Facility data for "a date", within "a position"
        and for  "a facility".
    """
    access_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccessKey",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "max_length": 255,
        }
    )
    gzip_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "GzipData",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "max_length": 100000,
        }
    )
    by_date_nposition_nfacility: List["WindSolarComLayerType.ByDateNpositionNfacility"] = field(
        default_factory=list,
        metadata={
            "name": "ByDateNPositionNFacility",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
        }
    )

    @dataclass
    class ByDateNpositionNfacility:
        wind_facility_met_data: List[WindFacilityMetDataType] = field(
            default_factory=list,
            metadata={
                "name": "WindFacilityMetData",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )
        power_data: List[PowerDataType] = field(
            default_factory=list,
            metadata={
                "name": "PowerData",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )
        gross_real_power_capability_data: List[GrossRealPowerCapabilityDataType] = field(
            default_factory=list,
            metadata={
                "name": "GrossRealPowerCapabilityData",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )
        wind_facility_data: List[WindFacilityDataType] = field(
            default_factory=list,
            metadata={
                "name": "WindFacilityData",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )
        error_alert: List[ErrorAlertType] = field(
            default_factory=list,
            metadata={
                "name": "ErrorAlert",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )


@dataclass
class WindSolarComLayer(WindSolarComLayerType):
    """Element that packages the MET, Power and Facility data.

    The three kind of data must be sorted by Date : PositionID : FacilityID : Power Data : Met Data : Fac Data
    """
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
