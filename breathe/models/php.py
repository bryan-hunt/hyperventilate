
from .base import BaseObject, DirectiveMapBase


try:
    from sphinxcontrib import phpdomain as php

    # ----------------------------------------------------------------------------

    # Create multi-inheritance classes to merge BaseObject from Breathe with
    # classes from phpdomain.
    # We use capitalization (and the namespace) to differentiate between the two

    class PHPNamespaceLevel(BaseObject, php.PhpNamespacelevel):
        """Description of a PHP item *in* a namespace (not the space itself)."""

        pass

    class PHPClassLike(BaseObject, php.PhpClasslike):
        pass

    class PHPClassMember(BaseObject, php.PhpClassmember):
        pass

    class PHPGlobalLevel(BaseObject, php.PhpGloballevel):
        pass


    class PhpDirectiveMap(DirectiveMapBase):
        def get(self, name: str, signature: Sequence[str]) -> Sequence[Any, str]:
            separators = php.separators
            if any([separators["method"] in n for n in signature]):
                if any([separators["attr"] in n for n in signature]):
                    name = "attr"
                else:
                    name = "method"
            else:
                if name in ["variable"]:
                    name = "global"

            return self._map.get(name, self._default)


    # A mapping from node kinds to domain directives and their names.
    _BREATHE_CLASS_MAP_PHP = PhpDirectiveMap({
        "function": (PHPNamespaceLevel, "function"),
        "class": (PHPClassLike, "class"),
        "attr": (PHPClassMember, "attr"),
        "method": (PHPClassMember, "method"),
        "global": (PHPGlobalLevel, "global"),
    }, (PHPClassLike, "class"))

except ImportError:
    class PhpDirectiveMap(DirectiveMapBase):
        pass

    _BREATHE_CLASS_MAP_PHP = PhpDirectiveMap({})
