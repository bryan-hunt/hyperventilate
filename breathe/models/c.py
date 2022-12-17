
from sphinx.domains import c
from .base import BaseObject, DirectiveMapBase

# ----------------------------------------------------------------------------

class CStructObject(BaseObject, c.CStructObject):
    pass


class CUnionObject(BaseObject, c.CUnionObject):
    pass


class CFunctionObject(BaseObject, c.CFunctionObject):
    pass


class CMemberObject(BaseObject, c.CMemberObject):
    pass


class CTypeObject(BaseObject, c.CTypeObject):
    pass


class CEnumObject(BaseObject, c.CEnumObject):
    pass


class CEnumeratorObject(BaseObject, c.CEnumeratorObject):
    pass


class CMacroObject(BaseObject, c.CMacroObject):
    pass


class CDirectiveMap(DirectiveMapBase):
    pass

# A mapping from node kinds to domain directives and their names.
_BREATHE_CLASS_MAP_C = CDirectiveMap({
    "variable": (CMemberObject, "var"),
    "function": (CFunctionObject, "function"),
    "define": (CMacroObject, "macro"),
    "struct": (CStructObject, "struct"),
    "union": (CUnionObject, "union"),
    "enum": (CEnumObject, "enum"),
    "enumvalue": (CEnumeratorObject, "enumerator"),
    "typedef": (CTypeObject, "type"),
})
