from unittest import TestCase
from xml.dom import minidom

from breathe.renderer.sphinxrenderer import get_param_decl, get_definition_without_template_args
#from breathe.parser import memberdefType
from breathe import path_handler

from docutils import nodes
from .utils import find_node, find_nodes

# class TestUtils(TestCase):
#     def test_param_decl(self):

#         # From xml from: examples/specific/parameters.h
#         xml = """
#         <memberdef>
#         <param>
#           <type>int</type>
#           <declname>a</declname>
#         </param>
#         <param>
#           <type>float</type>
#           <declname>b</declname>
#         </param>
#         <param>
#           <type>int *</type>
#           <declname>c</declname>
#         </param>
#         <param>
#           <type>int(**)</type>
#           <declname>p</declname>
#           <array>[3]</array>
#         </param>
#         <param>
#           <type><ref refid="class_my_class" kindref="compound">MyClass</ref></type>
#           <declname>a</declname>
#         </param>
#         <param>
#           <type><ref refid="class_my_class" kindref="compound">MyClass</ref> *</type>
#           <declname>b</declname>
#         </param>
#         <param>
#           <type>int(&amp;)</type>
#           <declname>r</declname>
#           <array>[3]</array>
#         </param>
#         </memberdef>
#         """

#         doc = minidom.parseString(xml)

#         memberdef = memberdefType()
#         for child in doc.documentElement.childNodes:
#             memberdef.buildChildren(child, "param")

#         self.assertEqual(get_param_decl(memberdef.param[0]), "int a")
#         self.assertEqual(get_param_decl(memberdef.param[1]), "float b")
#         self.assertEqual(get_param_decl(memberdef.param[2]), "int * c")
#         self.assertEqual(get_param_decl(memberdef.param[3]), "int(**p)[3]")
#         self.assertEqual(get_param_decl(memberdef.param[4]), "MyClass a")
#         self.assertEqual(get_param_decl(memberdef.param[5]), "MyClass  * b")
#         self.assertEqual(get_param_decl(memberdef.param[6]), "int(&r)[3]")

#     def test_definition_without_template_args(self):
#         def get_definition(definition, name, bitfield=""):
#             class MockDataObject:
#                 def __init__(self, definition, name, bitfield):
#                     self.definition = definition
#                     self.name = name
#                     self.bitfield = bitfield

#             return get_definition_without_template_args(MockDataObject(definition, name, bitfield))

#         self.assertEqual("void A::foo", get_definition("void A<T>::foo", "foo"))
#         # Template arguments in the return type should be preserved:
#         self.assertEqual("Result<T> A::f", get_definition("Result<T> A::f", "f"))
#         # Nested template arguments:
#         self.assertEqual("Result<T> A::f", get_definition("Result<T> A< B<C> >::f", "f"))

#         # Bit fields
#         self.assertEqual("int f : 3", get_definition("int f", "f", "3"))


class TestPathHandler(TestCase):
    def test_path_handler(self):
        self.assertEqual(path_handler.includes_directory("directory/file.h"), True)
        self.assertEqual(path_handler.includes_directory("directory\\file.h"), True)
        self.assertEqual(path_handler.includes_directory("file.h"), False)


def test_find_nodes():
    section = nodes.section()
    foo = nodes.Text("foo")
    desc = nodes.description()
    bar = nodes.Text("bar")
    section.children = [foo, desc, bar]
    assert find_nodes(section, "description") == [desc]
    assert find_nodes([section, desc], "description") == [desc, desc]
    assert find_nodes([], "description") == []
    assert find_nodes(section, "unknown") == []
    assert find_nodes(section, "Text") == [foo, bar]


def check_exception(func, message):
    """Check if func() throws an exception with the specified message."""
    exception = None
    try:
        func()
    except Exception as e:
        exception = e
    print(str(exception))
    assert exception and str(exception) == message


def test_find_node():
    section = nodes.section()
    foo = nodes.Text("foo")
    desc = nodes.description()
    bar = nodes.Text("bar")
    section.children = [foo, desc, bar]
    assert find_node(section, "description") == desc
    check_exception(
        lambda: find_node([section, desc], "description"), "the number of nodes description is 2"
    )
    check_exception(lambda: find_node([], "description"), "the number of nodes description is 0")
    check_exception(lambda: find_node([section], "unknown"), "the number of nodes unknown is 0")
    check_exception(lambda: find_node([section], "Text"), "the number of nodes Text is 2")
