from .xsparse import doxygen, doxygenindex
from xsdata.formats.dataclass.parsers import XmlParser

from breathe import file_state_cache, path_handler
from breathe.project import ProjectInfo

from sphinx.application import Sphinx
from typing import Any, Sequence

class ParserError(Exception):
    def __init__(self, error: Exception, filename: str):
        super().__init__(error)

        self.error = error
        self.filename = filename

    def __str__(self):
        return ("file %s: %s" % (self.filename, self.error))


class FileIOError(Exception):
    def __init__(self, error: Exception, filename: str):
        super().__init__(error)

        self.error = error
        self.filename = filename


class Parser:
    def __init__(self, app: Sphinx, cache):
        self.app = app
        self.cache = cache
        self.parser = XmlParser()


class DoxygenIndexParser(Parser):
    def parse(self, project_info: ProjectInfo):
        filename = path_handler.resolve_path(self.app, project_info.project_path(), "index.xml")
        file_state_cache.update(self.app, filename)

        try:
            # Try to get from our cache
            return self.cache[filename]
        except KeyError:
            # If that fails, parse it afresh
            try:
                result = self.parser.parse(open(filename, "rb"), doxygenindex)
                # result = index.parse(filename)
                self.cache[filename] = result
                return result
            except Exception as e:
                raise ParserError(e, filename)
            # except index.ParseError as e:
            #     raise ParserError(e, filename)
            # except index.FileIOError as e:
            #     raise FileIOError(e, filename)


class DoxygenCompoundParser(Parser):
    def __init__(self, app: Sphinx, cache,
                 project_info: ProjectInfo) -> None:
        super().__init__(app, cache)

        self.project_info = project_info

    def parse(self, refid: str):
        filename = path_handler.resolve_path(
            self.app,
            self.project_info.project_path(),
            "%s.xml" % refid
        )

        file_state_cache.update(self.app, filename)

        try:
            # Try to get from our cache
            return self.cache[filename]
        except KeyError:
            # If that fails, parse it afresh
            try:
                result = self.parser.parse(open(filename, "rb"), doxygen)
                #result = compound.parse(filename)
                self.cache[filename] = result
                return result
            except Exception as e:
                raise ParserError(e, filename)
            # except compound.ParseError as e:
            #     raise ParserError(e, filename)
            # except compound.FileIOError as e:
            #     raise FileIOError(e, filename)


class DoxygenParserFactory:
    def __init__(self, app: Sphinx) -> None:
        self.app = app
        # TODO: do we have a base class for all the Doxygen XML node types
        #       that we can use for typing?
        self.cache = {}  # type: ignore

    def create_index_parser(self) -> DoxygenIndexParser:
        return DoxygenIndexParser(self.app, self.cache)

    def create_compound_parser(self, project_info: ProjectInfo) -> DoxygenCompoundParser:
        return DoxygenCompoundParser(self.app, self.cache, project_info)


def DoxygenFindWildcardContent(node: Any, qname: str) -> Any:
    result = getattr(node, qname, None)
    if result is None:
        content = getattr(node, 'content', [])
        for item in content:
            name = getattr(item, 'qname', None)
            if name == qname:
                return item
