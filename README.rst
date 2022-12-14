Hyperventilate is a fork of `Breathe <https://github.com/breathe-doc/breathe>`_ to demonstrate experimental updates.

Project Goals
-------------

* Maintain the existing external breathe interfaces (include module name)
* Preserve existing `Sphinx <https://github.com/sphinx-doc/sphinx>`_ directives
* Improve speed and memory usage especially when used with other projects
  such as `exhale <https://github.com/svenevs/exhale>`_.
* Provide a framework for quick and easy additions of new features from
  Doxygen and Sphinx
* Provide a python level configuration interface to extend and modify
  rendering operations.

If these goals are satisfactorily accomplished all reasonable attempts to
submit them to the Breathe mainline will be made. 

Download
--------

Because Hyperventilate uses the same module name as Breathe they may not be
installed simulateously. It is recommended that one uses a python virtual
environment::

    python -m venv .venv

Hyperventilate is available from github and `PyPI, the Python Package Index
<http://pypi.python.org/pypi/hyperventilate>`_. It can be installed with::

    pip install hyperventilate

Documentation
-------------

Because this project is meant to be compatible with Breathe the existing Breathe
documentation will serve as both the documentation and specification

The documentation is available `here <http://breathe.readthedocs.org/>`__.
