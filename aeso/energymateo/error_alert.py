from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


@dataclass
class ErrorAlertType:
    trading_partner_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TradingPartnerID",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
        }
    )
    facility: Optional[str] = field(
        default=None,
        metadata={
            "name": "Facility",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
        }
    )
    timestamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
            "pattern": r"\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ",
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionID",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "max_length": 255,
        }
    )
    error_alert_detail: Optional["ErrorAlertType.ErrorAlertDetail"] = field(
        default=None,
        metadata={
            "name": "ErrorAlertDetail",
            "type": "Element",
            "namespace": "http://windforecasting.public.aeso.ca",
            "required": True,
        }
    )

    @dataclass
    class ErrorAlertDetail:
        alert_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AlertCode",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )
        message: Optional[str] = field(
            default=None,
            metadata={
                "name": "Message",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
                "required": True,
            }
        )
        transaction_data: Optional[str] = field(
            default=None,
            metadata={
                "name": "TransactionData",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )
        dump_analysis: Optional[str] = field(
            default=None,
            metadata={
                "name": "DumpAnalysis",
                "type": "Element",
                "namespace": "http://windforecasting.public.aeso.ca",
            }
        )


@dataclass
class ErrorAlert(ErrorAlertType):
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"
