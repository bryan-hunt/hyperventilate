
import pytest

from breathe.renderer.filter import FilterFactory

def _init_filter(app):
    return FilterFactory(app)


@pytest.mark.sphinx(testroot='filter')
def test_filter(app):
    node_filter = _init_filter(app)
