from dataclasses import field
try:
    from pydantic.dataclasses import dataclass
except ImportError:
    from dataclasses import dataclass

from enum import Enum
from typing import List, Optional


class defaultType(Enum):
    yes = "yes"
    no = "no"


class typeType(Enum):
    int_value = "int"
    bool_value = "bool"
    string = "string"
    stringlist = "stringlist"


@dataclass
class OptionType:
    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    default: Optional[defaultType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[typeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DoxygenFileType:
    option: List[OptionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )


@dataclass
class doxyfile(DoxygenFileType):
    pass
