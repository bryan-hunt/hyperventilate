
from sphinx.domains import cpp
from .base import BaseObject, DirectiveMapBase
from .c import CMacroObject

# ----------------------------------------------------------------------------

class CPPClassObject(BaseObject, cpp.CPPClassObject):
    pass


class CPPUnionObject(BaseObject, cpp.CPPUnionObject):
    pass


class CPPFunctionObject(BaseObject, cpp.CPPFunctionObject):
    pass


class CPPMemberObject(BaseObject, cpp.CPPMemberObject):
    pass


class CPPTypeObject(BaseObject, cpp.CPPTypeObject):
    pass


class CPPConceptObject(BaseObject, cpp.CPPConceptObject):
    pass


class CPPEnumObject(BaseObject, cpp.CPPEnumObject):
    pass


class CPPEnumeratorObject(BaseObject, cpp.CPPEnumeratorObject):
    pass


class CppDirectiveMap(DirectiveMapBase):
    pass


# A mapping from node kinds to domain directives and their names.
_BREATHE_CLASS_MAP_CPP = CppDirectiveMap({
    "variable": (CPPMemberObject, "var"),
    "class": (CPPClassObject, "class"),
    "struct": (CPPClassObject, "struct"),
    "interface": (CPPClassObject, "class"),
    "function": (CPPFunctionObject, "function"),
    "friend": (CPPFunctionObject, "function"),
    "signal": (CPPFunctionObject, "function"),
    "slot": (CPPFunctionObject, "function"),
    "concept": (CPPConceptObject, "concept"),
    "enum": (CPPEnumObject, "enum"),
    "enum-class": (CPPEnumObject, "enum-class"),
    "typedef": (CPPTypeObject, "type"),
    "using": (CPPTypeObject, "type"),
    "union": (CPPUnionObject, "union"),
    "namespace": (CPPTypeObject, "type"),
    "enumvalue": (CPPEnumeratorObject, "enumerator"),
    "define": (CMacroObject, "macro"),
})
