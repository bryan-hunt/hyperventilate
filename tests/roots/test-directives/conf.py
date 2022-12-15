import os
import breathe


exclude_patterns = ['_build']
extensions = [
    'breathe'
]

project_root = os.path.abspath(os.path.join(os.path.dirname(breathe.__file__),"../"))

breathe_projects = {
	"class": f"{project_root}/examples/doxygen/class/xml/",
    "concept": f"{project_root}/examples/doxygen/concept/xml/",
    "define": f"{project_root}/examples/doxygen/define/xml/",
    "enum": f"{project_root}/examples/doxygen/enum/xml/",
    "manual": f"{project_root}/examples/doxygen/manual/xml/",
    "file": f"{project_root}/examples/doxygen/file/xml/",
    "group": f"{project_root}/examples/doxygen/group/xml/",
    "interface": f"{project_root}/examples/doxygen/interface/xml/",
    "page": f"{project_root}/examples/doxygen/page/xml/",
    "typedef": f"{project_root}/examples/doxygen/restypedef/xml/"
}
breathe_default_project = "manual"

breathe_projects_source = {
    "auto" : ( f"{project_root}/examples/specific", ["auto_function.h", "auto_class.h"] )
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'
