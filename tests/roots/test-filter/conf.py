import os
import breathe


exclude_patterns = ['_build']
extensions = [
    'breathe'
]

project_root = os.path.abspath(os.path.join(os.path.dirname(breathe.__file__),"../"))

breathe_projects = {
    "manual": f"{project_root}/examples/doxygen/manual/xml/"
}
breathe_default_project = "manual"

breathe_projects_source = {
    "auto" : ( f"{project_root}/examples/specific", ["auto_function.h", "auto_class.h"] )
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'
