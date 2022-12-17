
import pytest

from breathe.finder.factory import FinderFactory
from breathe.parser import DoxygenParserFactory


def _init_finder(app):
    return FinderFactory(app, DoxygenParserFactory(app))


@pytest.mark.sphinx(testroot='finder')
def test_finder(app):
    node_finder = _init_finder(app)
