
from abc import ABC
from typing import Any, Mapping, Tuple

from sphinx import addnodes

class BaseObject:
    # Use this class as the first base class to make sure the overrides are used.
    # Set the content_callback attribute to a function taking a docutils node.

    def transform_content(self, contentnode: addnodes.desc_content) -> None:
        super().transform_content(contentnode)  # type: ignore
        callback = getattr(self, "breathe_content_callback", None)
        if callback is None:
            return
        callback(contentnode)


class DirectiveMapBase(ABC):
    def __init__(self, map: Mapping[str, Tuple[Any, str]], default: Tuple[Any, str] = []) -> None:
        self._map = map
        self._default = default

    def get(self, name: str, *args: Any) -> Tuple[Any, str]:
        return self._map.get(name, self._default)
