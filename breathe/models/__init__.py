
from sphinx.directives import ObjectDescription
from typing import Mapping, Optional
from breathe.exception import UnknownClassType

from .base import DirectiveMapBase, BaseObject
from .c import _BREATHE_CLASS_MAP_C
from .cpp import _BREATHE_CLASS_MAP_CPP
from .csharp import _BREATHE_CLASS_MAP_CSHARP
from .doxpy import _BREATHE_CLASS_MAP_PYTHON
from .php import _BREATHE_CLASS_MAP_PHP


class DomainDirectiveFactory:
    _maps: Mapping[str, DirectiveMapBase] = {
        "c": _BREATHE_CLASS_MAP_C,
        "cpp": _BREATHE_CLASS_MAP_CPP,
        "cs": _BREATHE_CLASS_MAP_CSHARP,
        "php": _BREATHE_CLASS_MAP_PHP,
        "python": _BREATHE_CLASS_MAP_PYTHON
    }

    @staticmethod
    def create(domain: str, identifier: str, *args: Optional[str]) -> ObjectDescription:
        if domain is None:
            domain = "cpp"

        cls, name = DomainDirectiveFactory._maps.get(domain, _BREATHE_CLASS_MAP_CPP).get(identifier, *args)

        if cls:
            # Replace the directive name because domain directives don't know how to handle
            # Breathe's "doxygen" directives.
            assert ":" not in name
            return cls(domain + ":" + name, *args)
        else:
            raise UnknownClassType(f"No mapping found for {identifier} in {domain}")

__all__ = ["BaseObject", "DomainDirectiveFactory"]
