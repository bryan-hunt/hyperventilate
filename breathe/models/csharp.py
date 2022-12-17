
from .base import BaseObject, DirectiveMapBase


class CsharpDirectiveMap(DirectiveMapBase):
    pass


try:
    from sphinx_csharp import csharp as cs  # type: ignore


    class CSharpCurrentNamespace(BaseObject, cs.CSharpCurrentNamespace):
        pass


    class CSharpNamespacePlain(BaseObject, cs.CSharpNamespacePlain):
        pass


    class CSharpClass(BaseObject, cs.CSharpClass):
        pass


    class CSharpStruct(BaseObject, cs.CSharpStruct):
        pass


    class CSharpInterface(BaseObject, cs.CSharpInterface):
        pass


    class CSharpInherits(BaseObject, cs.CSharpInherits):
        pass


    class CSharpMethod(BaseObject, cs.CSharpMethod):
        pass


    class CSharpVariable(BaseObject, cs.CSharpVariable):
        pass


    class CSharpProperty(BaseObject, cs.CSharpProperty):
        pass


    class CSharpEvent(BaseObject, cs.CSharpEvent):
        pass


    class CSharpEnum(BaseObject, cs.CSharpEnum):
        pass


    class CSharpEnumValue(BaseObject, cs.CSharpEnumValue):
        pass


    class CSharpAttribute(BaseObject, cs.CSharpAttribute):
        pass


    class CSharpIndexer(BaseObject, cs.CSharpIndexer):
        pass


    class CSharpXRefRole(BaseObject, cs.CSharpXRefRole):
        pass


    _BREATHE_CLASS_MAP_CSHARP = CsharpDirectiveMap({
        # 'doxygen-name': (CSharp class, key in CSharpDomain.object_types)
        "namespace": (CSharpNamespacePlain, "namespace"),
        "class": (CSharpClass, "class"),
        "struct": (CSharpStruct, "struct"),
        "interface": (CSharpInterface, "interface"),
        "function": (CSharpMethod, "function"),
        "method": (CSharpMethod, "method"),
        "variable": (CSharpVariable, "var"),
        "property": (CSharpProperty, "property"),
        "event": (CSharpEvent, "event"),
        "enum": (CSharpEnum, "enum"),
        "enumvalue": (CSharpEnumValue, "enumerator"),
        "attribute": (CSharpAttribute, "attr"),
        # Fallback to cpp domain
        "typedef": (CPPTypeObject, "type"),
    })

except ImportError:
    _BREATHE_CLASS_MAP_CSHARP = CsharpDirectiveMap({})
