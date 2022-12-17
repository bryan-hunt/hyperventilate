import os
import pytest

import sphinx.addnodes
import sphinx.environment
from breathe.parser.xsparse import (
    compounddefType,
    linkedTextType,
    descriptionType,
    memberdefType,
    paramType,
    refType
)
from breathe.renderer.sphinxrenderer import SphinxRenderer
from breathe.renderer.filter import OpenFilter
from docutils import frontend, parsers, utils

from .mocks import MockReporter
from .utils import find_node


class MockMemo:
    def __init__(self):
        self.title_styles = ""
        self.section_level = ""


class MockState:
    def __init__(self, app):
        from breathe.project import ProjectInfoFactory
        from breathe.parser import DoxygenParserFactory

        env = sphinx.environment.BuildEnvironment(app)
        env.setup(app)
        env.temp_data["docname"] = "mock-doc"
        env.temp_data["breathe_project_info_factory"] = ProjectInfoFactory(app)
        env.temp_data["breathe_parser_factory"] = DoxygenParserFactory(app)
        settings = frontend.OptionParser(components=(parsers.rst.Parser,)).get_default_values()
        settings.env = env
        self.document = utils.new_document("", settings)

        # In sphinx 5.3.0 the method state.nested_parse is not called directly
        # so this memo object should exists here
        self.memo = MockMemo()

    def nested_parse(self, content, content_offset, contentnode, match_titles=1):
        pass


class MockStateMachine:
    def __init__(self):
        self.reporter = MockReporter()

    def get_source_and_line(self, lineno: int):
        if lineno is None:
            lineno = 42
        return "mock-doc", lineno


class MockMaskFactory:
    def __init__(self):
        pass

    def mask(self, node):
        return node


class MockContext:
    def __init__(self, app, node_stack, domain=None, options=[]):
        self.domain = domain
        self.node_stack = node_stack
        self.directive_args = [
            None,  # name
            None,  # arguments
            options,  # options
            None,  # content
            None,  # lineno
            None,  # content_offset
            None,  # block_text
            MockState(app),
            MockStateMachine(),
        ]
        self.child = None
        self.mask_factory = MockMaskFactory()

    def create_child_context(self, attribute):
        return self


class MockTargetHandler:
    def __init__(self):
        pass

    def create_target(self, refid):
        pass


class MockCompoundParser:
    """
    A compound parser reads a doxygen XML file from disk; this mock implements
    a mapping of what would be the file name on disk to data using a dict.
    """

    def __init__(self, compound_dict):
        self.compound_dict = compound_dict

    class MockFileData:
        def __init__(self, compounddef):
            self.compounddef = compounddef

    def parse(self, compoundname):
        compounddef = self.compound_dict[compoundname]
        return self.MockFileData(compounddef)


def render(
    app, member_def, domain=None, show_define_initializer=False, compound_parser=None, options=[]
):
    """Render Doxygen *member_def* with *renderer_class*."""

    app.config.breathe_separate_member_pages = False
    app.config.breathe_use_project_refids = False
    app.config.breathe_show_define_initializer = show_define_initializer
    app.config.breathe_order_parameters_first = False
    app.config.breathe_debug_trace_directives = False
    app.config.breathe_debug_trace_doxygen_ids = False
    app.config.breathe_debug_trace_qualification = False
    renderer = SphinxRenderer(
        app,
        None,  # project_info
        [],  # node_stack
        None,  # state
        None,  # document
        MockTargetHandler(),
        compound_parser,
        OpenFilter(),
    )
    renderer.context = MockContext(app, [member_def], domain, options)
    return renderer.render(member_def)


@pytest.mark.sphinx(testroot="empty")
def test_render_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void foo",
        type=linkedTextType(content=["void"]),
        name="foo",
        argsstring="(int)",
        virt="non-virtual",
        param=[
            paramType(type=linkedTextType(content=["int"]))
        ],
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext().startswith("void")
    if sphinx.version_info[0] < 4:
        assert find_node(signature, "desc_name")[0] == "foo"
    else:
        n = find_node(signature, "desc_name")[0]
        assert isinstance(n, sphinx.addnodes.desc_sig_name)
        assert len(n) == 1
        assert n[0] == "foo"
    params = find_node(signature, "desc_parameterlist")
    assert len(params) == 1
    param = params[0]
    if sphinx.version_info[0] < 4:
        assert param[0] == "int"
    else:
        assert isinstance(param[0], sphinx.addnodes.desc_sig_keyword_type)
        assert param[0][0] == "int"


@pytest.mark.sphinx(testroot="empty")
def test_render_typedef(app):
    member_def = memberdefType(
        kind="typedef", 
        definition="typedef int foo", 
        type=linkedTextType(content=["int"]), 
        name="foo"
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext() == "typedef int foo"


@pytest.mark.sphinx(testroot="empty")
def test_render_c_typedef(app):
    member_def = memberdefType(
        kind="typedef", 
        definition="typedef unsigned int bar", 
        type=linkedTextType(content=["unsigned int"]), 
        name="bar"
    )
    signature = find_node(render(app, member_def, domain="c"), "desc_signature")
    assert signature.astext() == "typedef unsigned int bar"


@pytest.mark.sphinx(testroot="empty")
def test_render_c_function_typedef(app):
    member_def = memberdefType(
        kind="typedef",
        definition="typedef void* (*voidFuncPtr)(float, int)",
        type=linkedTextType(content=["void* (*"]),
        name="voidFuncPtr",
        argsstring=")(float, int)",
    )
    signature = find_node(render(app, member_def, domain="c"), "desc_signature")
    assert signature.astext().startswith("typedef void *")
    if sphinx.version_info[0] < 4:
        params = find_node(signature, "desc_parameterlist")
        assert len(params) == 2
        assert params[0].astext() == "float"
        assert params[1].astext() == "int"
    else:
        # the use of desc_parameterlist in this case was not correct,
        # it should only be used for a top-level function
        pass


@pytest.mark.sphinx(testroot="empty")
def test_render_using_alias(app):
    member_def = memberdefType(
        kind="typedef",
        definition="using foo = int",
        type=linkedTextType(content=["int"]),
        name="foo"
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext() == "using foo = int"


@pytest.mark.sphinx(testroot="empty")
def test_render_const_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void f",
        type=linkedTextType(content=["void"]),
        name="f",
        argsstring="() const",
        virt="non-virtual",
        const="yes",
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert "_CPPv2NK1fEv" in signature["ids"]


@pytest.mark.sphinx(testroot="empty")
def test_render_lvalue_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void f",
        type=linkedTextType(content=["void"]),
        name="f",
        argsstring="() &",
        virt="non-virtual",
        refqual="lvalue",
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext().endswith("&")


@pytest.mark.sphinx(testroot="empty")
def test_render_rvalue_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void f",
        type=linkedTextType(content=["void"]),
        name="f",
        argsstring="() &&",
        virt="non-virtual",
        refqual="rvalue",
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext().endswith("&&")


@pytest.mark.sphinx(testroot="empty")
def test_render_const_lvalue_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void f",
        type=linkedTextType(content=["void"]),
        name="f",
        argsstring="() const &",
        virt="non-virtual",
        const="yes",
        refqual="lvalue",
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext().endswith("const &")


@pytest.mark.sphinx(testroot="empty")
def test_render_const_rvalue_func(app):
    member_def = memberdefType(
        kind="function",
        definition="void f",
        type=linkedTextType(content=["void"]),
        name="f",
        argsstring="() const &&",
        virt="non-virtual",
        const="yes",
        refqual="rvalue",
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext().endswith("const &&")


@pytest.mark.sphinx(testroot="empty")
def test_render_variable_initializer(app):
    member_def = memberdefType(
        kind="variable",
        definition="const int EOF",
        type=linkedTextType(content=["const int"]),
        name="EOF",
        initializer=linkedTextType(content=["= -1"]),
    )
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext() == "const int EOF = -1"


@pytest.mark.sphinx(testroot="empty")
def test_render_define_initializer(app):
    member_def = memberdefType(
        kind="define",
        name="MAX_LENGTH",
        initializer=linkedTextType(content=["100"]),
    )
    signature_w_initializer = find_node(
        render(app, member_def, show_define_initializer=True), "desc_signature"
    )
    assert signature_w_initializer.astext() == "MAX_LENGTH 100"

    member_def_no_show = memberdefType(
        kind="define",
        name="MAX_LENGTH_NO_INITIALIZER",
        initializer=linkedTextType(content=["100"]),
    )

    signature_wo_initializer = find_node(
        render(app, member_def_no_show, show_define_initializer=False), "desc_signature"
    )
    assert signature_wo_initializer.astext() == "MAX_LENGTH_NO_INITIALIZER"


@pytest.mark.sphinx(testroot="empty")
def test_render_define_no_initializer(app):
    sphinx.addnodes.setup(app)
    member_def = memberdefType(kind="define", name="USE_MILK")
    signature = find_node(render(app, member_def), "desc_signature")
    assert signature.astext() == "USE_MILK"


@pytest.mark.sphinx(testroot="empty")
def test_render_innergroup(app):
    refid = "group__innergroup"
    mock_compound_parser = MockCompoundParser(
        {
            refid: compounddefType(
                kind="group", 
                compoundname="InnerGroup",
                briefdescription=descriptionType(content=["InnerGroup"])
            )
        }
    )
    ref = refType("InnerGroup", refid=refid)
    compound_def = compounddefType(
        kind="group", 
        compoundname="OuterGroup", 
        briefdescription=descriptionType(content=["OuterGroup"]),
        innergroup=[ref]
    )
    assert all(
        el.astext() != "InnerGroup"
        for el in render(app, compound_def, compound_parser=mock_compound_parser)
    )
    assert any(
        el.astext() == "InnerGroup"
        for el in render(app, compound_def, compound_parser=mock_compound_parser, options=["inner"])
    )


def get_directive(app):
    from breathe.directives.function import DoxygenFunctionDirective
    from docutils.statemachine import StringList

    app.config.breathe_separate_member_pages = False
    app.config.breathe_default_project = "test_project"
    app.config.breathe_domain_by_extension = {}
    app.config.breathe_domain_by_file_pattern = {}
    app.config.breathe_use_project_refids = False
    cls_args = (
        "doxygenclass",
        ["at::Tensor"],
        {"members": "", "protected-members": None, "undoc-members": None},
        StringList([], items=[]),
        20,
        24,
        (
            ".. doxygenclass:: at::Tensor\n   :members:\n"
            "   :protected-members:\n   :undoc-members:"
        ),
        MockState(app),
        MockStateMachine(),
    )
    return DoxygenFunctionDirective(*cls_args)
