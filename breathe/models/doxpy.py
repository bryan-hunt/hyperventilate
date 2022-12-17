
from sphinx.domains import python
from .base import BaseObject, DirectiveMapBase


class DoxPythonDirectiveMap(DirectiveMapBase):
    pass


class PyFunction(BaseObject, python.PyFunction):
    pass


class PyAttribute(BaseObject, python.PyAttribute):
    pass


class PyClasslike(BaseObject, python.PyClasslike):
    pass


_BREATHE_CLASS_MAP_PYTHON = DoxPythonDirectiveMap({
    # TODO: PyFunction is meant for module-level functions
    #       and PyAttribute is meant for class attributes, not module-level variables.
    #       Somehow there should be made a distinction at some point to get the correct
    #       index-text and whatever other things are different.
    "function": (PyFunction, "function"),
    "variable": (PyAttribute, "attribute"),
    "class": (PyClasslike, "class"),
    "namespace": (PyClasslike, "class"),
})
