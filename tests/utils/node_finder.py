
from docutils import nodes

from tests.mocks import MockDocument

class NodeFinder(nodes.NodeVisitor):
    """Find node with specified class name."""

    def __init__(self, name, document):
        super().__init__(document)
        self.name = name
        self.found_nodes = []

    def unknown_visit(self, node):
        if node.__class__.__name__ == self.name:
            self.found_nodes.append(node)


def find_nodes(nodes, name):
    """Find all docutils nodes with specified class name in *nodes*."""
    finder = NodeFinder(name, MockDocument())
    for node in nodes:
        node.walk(finder)
    return finder.found_nodes


def find_node(nodes, name):
    """
    Find a single docutils node with specified class name in *nodes*.
    Throw an exception if there isn't exactly one such node.
    """
    found_nodes = find_nodes(nodes, name)
    if len(found_nodes) != 1:
        raise Exception("the number of nodes {0} is {1}".format(name, len(found_nodes)))
    return found_nodes[0]
