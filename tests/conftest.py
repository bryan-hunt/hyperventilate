import pytest

from sphinx.testing.path import path

pytest_plugins = "sphinx.testing.fixtures"

# Exclude supporting directories
collect_ignore = ["mocks", "roots", "utils"]

@pytest.fixture(scope="session")
def rootdir():
    return path(__file__).parent.abspath() / "roots"
