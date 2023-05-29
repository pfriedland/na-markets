from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://windforecasting.public.aeso.ca"


class WindSolarResponseReturnCode(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class WindSolarResponse:
    class Meta:
        namespace = "http://windforecasting.public.aeso.ca"

    return_code: Optional[WindSolarResponseReturnCode] = field(
        default=None,
        metadata={
            "name": "ReturnCode",
            "type": "Element",
            "required": True,
        }
    )
    transaction_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionID",
            "type": "Element",
            "required": True,
            "max_length": 255,
        }
    )
    error_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "ErrorLevel",
            "type": "Element",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Element",
        }
    )
