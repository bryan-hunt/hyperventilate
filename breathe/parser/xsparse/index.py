from dataclasses import field

try:
    from pydantic.dataclasses import dataclass
except ImportError:
    from dataclasses import dataclass

from enum import Enum
from typing import List, Optional


class CompoundKind(Enum):
    class_value = "class"
    struct = "struct"
    union = "union"
    interface = "interface"
    protocol = "protocol"
    category = "category"
    exception = "exception"
    file = "file"
    namespace = "namespace"
    group = "group"
    page = "page"
    example = "example"
    dir = "dir"
    type = "type"
    concept = "concept"


class MemberKind(Enum):
    define = "define"
    property = "property"
    event = "event"
    variable = "variable"
    typedef = "typedef"
    enum = "enum"
    enumvalue = "enumvalue"
    function = "function"
    signal = "signal"
    prototype = "prototype"
    friend = "friend"
    dcop = "dcop"
    slot = "slot"


@dataclass
class MemberType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    kind: Optional[MemberKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CompoundType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    member: List[MemberType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    kind: Optional[CompoundKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class DoxygenType:
    compound: List[CompoundType] = field(
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
class doxygenindex(DoxygenType):
    pass
