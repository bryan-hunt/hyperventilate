import pytest

from docutils import nodes
from sphinx import addnodes
from sphinx.io import create_publisher
from sphinx.util.docutils import sphinx_domains


def _doctree_for_test(builder, docname: str) -> nodes.document:
    builder.env.prepare_settings(docname)
    publisher = create_publisher(builder.app, 'restructuredtext')
    with sphinx_domains(builder.env):
        publisher.set_source(source_path=builder.env.doc2path(docname))
        publisher.publish()
        return publisher.document


@pytest.mark.sphinx(testroot='directives')
def test_doxygenindex(app):
    app.builder.build_all()

    doctree = app.env.get_doctree('directives/doxygenindex')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_autodoxygenindex(app):
    doctree = _doctree_for_test(app.builder, 'directives/autoindex')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenfunction(app):
    doctree = _doctree_for_test(app.builder, 'directives/function')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)
    assert isinstance(doctree[2][1][0], nodes.paragraph)
    assert doctree[2][1][0][0] == "Starts the vehicle. "


@pytest.mark.sphinx(testroot='directives')
def test_doxygenstruct(app):
    doctree = _doctree_for_test(app.builder, 'directives/struct')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenclass(app):
    doctree = _doctree_for_test(app.builder, 'directives/class')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygeninterface(app):
    doctree = _doctree_for_test(app.builder, 'directives/interface')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenvariable(app):
    doctree = _doctree_for_test(app.builder, 'directives/variable')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygendefine(app):
    doctree = _doctree_for_test(app.builder, 'directives/define')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenconcept(app):
    doctree = _doctree_for_test(app.builder, 'directives/concept')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenenum(app):
    doctree = _doctree_for_test(app.builder, 'directives/enum')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenenumvalue(app):
    doctree = _doctree_for_test(app.builder, 'directives/enumvalue')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygentypedef(app):
    doctree = _doctree_for_test(app.builder, 'directives/typedef')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenunion(app):
    doctree = _doctree_for_test(app.builder, 'directives/union')
   
    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygennamespace(app):
    doctree = _doctree_for_test(app.builder, 'directives/namespace')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygengroup(app):
    doctree = _doctree_for_test(app.builder, 'directives/group')

    assert isinstance(doctree[1], addnodes.desc)
    assert isinstance(doctree[1][0], addnodes.desc_signature)
    assert isinstance(doctree[1][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenfile(app):
    doctree = _doctree_for_test(app.builder, 'directives/file')

    assert isinstance(doctree[2], nodes.container)
    assert isinstance(doctree[2][1], addnodes.index)
    assert isinstance(doctree[2][2], addnodes.desc)
    assert isinstance(doctree[2][2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_autodoxygenfile(app):
    doctree = _doctree_for_test(app.builder, 'directives/autofile')

    assert isinstance(doctree[1], addnodes.index)
    assert isinstance(doctree[2], addnodes.desc)
    assert isinstance(doctree[2][0], addnodes.desc_signature)
    assert isinstance(doctree[2][1], addnodes.desc_content)


@pytest.mark.sphinx(testroot='directives')
def test_doxygenpage(app):
    doctree = _doctree_for_test(app.builder, 'directives/page')
   
    assert isinstance(doctree[1], addnodes.desc)
    assert isinstance(doctree[1][0], addnodes.desc_signature)
    assert isinstance(doctree[1][1], addnodes.desc_content)
