from dataclasses import field
try:
    from pydantic.dataclasses import dataclass
except ImportError:
    from dataclasses import dataclass

from enum import Enum
from typing import Dict, List, Optional, Type


class DoxAccessor(Enum):
    retain = "retain"
    copy = "copy"
    assign = "assign"
    weak = "weak"
    strong = "strong"
    unretained = "unretained"


class DoxAlign(Enum):
    left = "left"
    right = "right"
    center = "center"


class DoxBool(Enum):
    yes = "yes"
    no = "no"


class DoxCompoundKind(Enum):
    class_value = "class"
    struct = "struct"
    union = "union"
    interface = "interface"
    protocol = "protocol"
    category = "category"
    exception = "exception"
    service = "service"
    singleton = "singleton"
    module = "module"
    type = "type"
    file = "file"
    namespace = "namespace"
    group = "group"
    page = "page"
    example = "example"
    dir = "dir"
    concept = "concept"


class DoxGraphRelation(Enum):
    include = "include"
    usage = "usage"
    template_instance = "template-instance"
    public_inheritance = "public-inheritance"
    protected_inheritance = "protected-inheritance"
    private_inheritance = "private-inheritance"
    type_constraint = "type-constraint"


class DoxHighlightType(Enum):
    comment = "comment"
    normal = "normal"
    preprocessor = "preprocessor"
    keyword = "keyword"
    keywordtype = "keywordtype"
    keywordflow = "keywordflow"
    stringliteral = "stringliteral"
    charliteral = "charliteral"
    vhdlkeyword = "vhdlkeyword"
    vhdllogic = "vhdllogic"
    vhdlchar = "vhdlchar"
    vhdldigit = "vhdldigit"


class DoxImageKind(Enum):
    html = "html"
    latex = "latex"
    docbook = "docbook"
    rtf = "rtf"
    xml = "xml"


class DoxLanguage(Enum):
    unknown = "Unknown"
    idl = "IDL"
    java = "Java"
    c = "C#"
    d = "D"
    php = "PHP"
    objective_c = "Objective-C"
    c_1 = "C++"
    java_script = "JavaScript"
    python = "Python"
    fortran = "Fortran"
    vhdl = "VHDL"
    xml = "XML"
    sql = "SQL"
    markdown = "Markdown"
    slice = "Slice"
    lex = "Lex"


class DoxMemberKind(Enum):
    define = "define"
    property = "property"
    event = "event"
    variable = "variable"
    typedef = "typedef"
    enum = "enum"
    function = "function"
    signal = "signal"
    prototype = "prototype"
    friend = "friend"
    dcop = "dcop"
    slot = "slot"
    interface = "interface"
    service = "service"


class DoxOlType(Enum):
    value_1 = "1"
    a = "a"
    a_1 = "A"
    i = "i"
    i_1 = "I"


class DoxParamDir(Enum):
    in_value = "in"
    out = "out"
    inout = "inout"


class DoxParamListKind(Enum):
    param = "param"
    retval = "retval"
    exception = "exception"
    templateparam = "templateparam"


class DoxPlantumlEngine(Enum):
    uml = "uml"
    bpm = "bpm"
    wire = "wire"
    dot = "dot"
    ditaa = "ditaa"
    salt = "salt"
    math = "math"
    latex = "latex"
    gantt = "gantt"
    mindmap = "mindmap"
    wbs = "wbs"
    yaml = "yaml"
    creole = "creole"
    json = "json"
    flow = "flow"
    board = "board"
    git = "git"


class DoxProtectionKind(Enum):
    public = "public"
    protected = "protected"
    private = "private"
    package = "package"


class DoxRefKind(Enum):
    compound = "compound"
    member = "member"


class DoxRefQualifierKind(Enum):
    lvalue = "lvalue"
    rvalue = "rvalue"


class DoxSectionKind(Enum):
    user_defined = "user-defined"
    public_type = "public-type"
    public_func = "public-func"
    public_attrib = "public-attrib"
    public_slot = "public-slot"
    signal = "signal"
    dcop_func = "dcop-func"
    property = "property"
    event = "event"
    public_static_func = "public-static-func"
    public_static_attrib = "public-static-attrib"
    protected_type = "protected-type"
    protected_func = "protected-func"
    protected_attrib = "protected-attrib"
    protected_slot = "protected-slot"
    protected_static_func = "protected-static-func"
    protected_static_attrib = "protected-static-attrib"
    package_type = "package-type"
    package_func = "package-func"
    package_attrib = "package-attrib"
    package_static_func = "package-static-func"
    package_static_attrib = "package-static-attrib"
    private_type = "private-type"
    private_func = "private-func"
    private_attrib = "private-attrib"
    private_slot = "private-slot"
    private_static_func = "private-static-func"
    private_static_attrib = "private-static-attrib"
    friend = "friend"
    related = "related"
    define = "define"
    prototype = "prototype"
    typedef = "typedef"
    enum = "enum"
    func = "func"
    var = "var"


class DoxSimpleSectKind(Enum):
    see = "see"
    return_value = "return"
    author = "author"
    authors = "authors"
    version = "version"
    since = "since"
    date = "date"
    note = "note"
    warning = "warning"
    pre = "pre"
    post = "post"
    copyright = "copyright"
    invariant = "invariant"
    remark = "remark"
    attention = "attention"
    par = "par"
    rcs = "rcs"


class DoxVerticalAlign(Enum):
    bottom = "bottom"
    top = "top"
    middle = "middle"


class DoxVirtualKind(Enum):
    non_virtual = "non-virtual"
    virtual = "virtual"
    pure_virtual = "pure-virtual"


@dataclass
class docAnchorType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class docBlockQuoteType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class docDetailsType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class docEmojiType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    unicode: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docEmptyType:
    pass


@dataclass
class docFormulaType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class docHtmlOnlyType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    block: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docIndexEntryType:
    primaryie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    secondaryie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class docInternalS4Type:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docLanguageType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    langid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docListItemType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docParBlockType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class docXRefSectType:
    xreftitle: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    xrefdescription: Optional["descriptionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class linkType:
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class locationType:
    file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    line: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    column: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declfile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    declcolumn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodyfile: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodystart: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bodyend: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class referenceType:
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    compoundref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    startline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    endline: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class reimplementType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class spType:
    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )


@dataclass
class tableofcontentsKindType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    tableofcontents: List["tableofcontentsType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class childnodeType:
    edgelabel: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    relation: Optional[DoxGraphRelation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class compoundRefType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docEntryType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    thead: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    colspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rowspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[DoxAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[DoxVerticalAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class docListType:
    listitem: List[docListItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    type: Optional[DoxOlType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docRefTextType:
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kindref: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["docImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": Type["docPlantumlType"],
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": Type["docRefTextType"],
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docSect4Type:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": docInternalS4Type,
                    "namespace": "",
                },
            ),
        }
    )



@dataclass
class incType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    local: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class memberRefType:
    scope: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ambiguityscope: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class refTextType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kindref: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tooltip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class refType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class tableofcontentsType:
    tocsect: List[tableofcontentsKindType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class docInternalS3Type:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": docSect4Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParamName:
    direction: Optional[DoxParamDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": refTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParamType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": refTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docPlantumlType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    engine: Optional[DoxPlantumlEngine] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["docImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": Type["docPlantumlType"],
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docRowType:
    entry: List[docEntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class highlightType:
    class_value: Optional[DoxHighlightType] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "sp",
                    "type": spType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": refTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class linkedTextType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": refTextType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class listofallmembersType:
    member: List[memberRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class nodeType:
    label: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    link: Optional[linkType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    childnode: List[childnodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class codelineType:
    highlight: List[highlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    lineno: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refkind: Optional[DoxRefKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    external: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docDotMscType:
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["docImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": Type["docDotMscType"],
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParamNameList:
    parametertype: List[docParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parametername: List[docParamName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class docSect3Type:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect4",
                    "type": docSect4Type,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": docInternalS3Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class graphType:
    node: List[nodeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class docImageType:
    type: Optional[DoxImageKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caption: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": Type["docImageType"],
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docInternalS2Type:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": docSect3Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParamListItem:
    parameternamelist: List[docParamNameList] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    parameterdescription: Optional["descriptionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class listingType:
    codeline: List[codelineType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docCaptionType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docHeadingType:
    level: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docImageFileType:
    """
    :ivar name: The mentioned file will be located in the directory as
        specified by XML_OUTPUT
    :ivar width:
    :ivar height:
    :ivar content:
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParamListType:
    parameteritem: List[docParamListItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxParamListKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docSect2Type:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect3",
                    "type": docSect3Type,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": docInternalS2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docTitleType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docTocItemType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docInternalS1Type:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect2",
                    "type": docSect2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docSimpleSectType:
    title: Optional[docTitleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxSimpleSectKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docTableType:
    caption: Optional[docCaptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    row: List[docRowType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    rows: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cols: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docTocListType:
    tocitem: List[docTocItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class docVarListEntryType:
    term: Optional[docTitleType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class docSect1Type:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": docInternalS1Type,
                    "namespace": "",
                },
                {
                    "name": "sect2",
                    "type": docSect2Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docVariableListType:
    varlistentry: List[docVarListEntryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )
    listitem: List[docListItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "sequential": True,
        }
    )


@dataclass
class docInternalType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "para",
                    "type": Type["docParaType"],
                    "namespace": "",
                },
                {
                    "name": "sect1",
                    "type": docSect1Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docCopyType:
    para: List["docParaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sect1: List[docSect1Type] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    internal: Optional[docInternalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class docMarkupType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hruler",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "preformatted",
                    "type": Type["docMarkupType"],
                    "namespace": "",
                },
                {
                    "name": "programlisting",
                    "type": listingType,
                    "namespace": "",
                },
                {
                    "name": "verbatim",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadocliteral",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadoccode",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "indexentry",
                    "type": docIndexEntryType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": docListType,
                    "namespace": "",
                },
                {
                    "name": "itemizedlist",
                    "type": docListType,
                    "namespace": "",
                },
                {
                    "name": "simplesect",
                    "type": docSimpleSectType,
                    "namespace": "",
                },
                {
                    "name": "title",
                    "type": docTitleType,
                    "namespace": "",
                },
                {
                    "name": "variablelist",
                    "type": docVariableListType,
                    "namespace": "",
                },
                {
                    "name": "table",
                    "type": docTableType,
                    "namespace": "",
                },
                {
                    "name": "heading",
                    "type": docHeadingType,
                    "namespace": "",
                },
                {
                    "name": "dotfile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "mscfile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "diafile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "toclist",
                    "type": docTocListType,
                    "namespace": "",
                },
                {
                    "name": "language",
                    "type": docLanguageType,
                    "namespace": "",
                },
                {
                    "name": "parameterlist",
                    "type": docParamListType,
                    "namespace": "",
                },
                {
                    "name": "xrefsect",
                    "type": docXRefSectType,
                    "namespace": "",
                },
                {
                    "name": "copydoc",
                    "type": docCopyType,
                    "namespace": "",
                },
                {
                    "name": "details",
                    "type": docDetailsType,
                    "namespace": "",
                },
                {
                    "name": "blockquote",
                    "type": docBlockQuoteType,
                    "namespace": "",
                },
                {
                    "name": "parblock",
                    "type": docParBlockType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docURLLink:
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": Type["docURLLink"],
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class docParaType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ulink",
                    "type": docURLLink,
                    "namespace": "",
                },
                {
                    "name": "bold",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "s",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "strike",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "underline",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "emphasis",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "computeroutput",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "subscript",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "superscript",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "center",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "small",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "cite",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "del",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "ins",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "summary",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "htmlonly",
                    "type": docHtmlOnlyType,
                    "namespace": "",
                },
                {
                    "name": "manonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "xmlonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "rtfonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "latexonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "docbookonly",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "image",
                    "type": docImageType,
                    "namespace": "",
                },
                {
                    "name": "dot",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "msc",
                    "type": docDotMscType,
                    "namespace": "",
                },
                {
                    "name": "plantuml",
                    "type": docPlantumlType,
                    "namespace": "",
                },
                {
                    "name": "anchor",
                    "type": docAnchorType,
                    "namespace": "",
                },
                {
                    "name": "formula",
                    "type": docFormulaType,
                    "namespace": "",
                },
                {
                    "name": "ref",
                    "type": docRefTextType,
                    "namespace": "",
                },
                {
                    "name": "emoji",
                    "type": docEmojiType,
                    "namespace": "",
                },
                {
                    "name": "linebreak",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nonbreakablespace",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iexcl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cent",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pound",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "curren",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yen",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "brvbar",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sect",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "umlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "copy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "laquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "not",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "shy",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "registered",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "macr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "deg",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "plusmn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup2",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup3",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "micro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "middot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup1",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ordm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "raquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac14",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac12",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frac34",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iquest",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "AElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ETH",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "times",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "THORN",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "szlig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "agrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "acirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "atilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aring",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "aelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ccedil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "egrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ecirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "igrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "icirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eth",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ntilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ograve",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ocirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "divide",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oslash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ugrave",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ucirc",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yacute",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thorn",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "fnof",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alpha",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "beta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "gamma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "delta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "epsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zeta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "eta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "theta",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "iota",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "kappa",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lambda",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nu",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "xi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omicron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "pi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rho",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigmaf",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sigma",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tau",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsilon",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "phi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "chi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "psi",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "omega",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thetasym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "upsih",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "piv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bull",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hellip",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Prime",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oline",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "frasl",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "weierp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "imaginary",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "real",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "trademark",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "alefsym",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "larr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "darr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "harr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "crarr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "uArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hArr",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "forall",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "part",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "exist",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "empty",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nabla",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "isin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "notin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ni",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prod",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sum",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "minus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lowast",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "radic",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "prop",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "infin",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "and",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "or",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cap",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "int",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "there4",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sim",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "cong",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "asymp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ne",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "equiv",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "le",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ge",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sup",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "nsub",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sube",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "supe",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oplus",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "otimes",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "perp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sdot",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rceil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rfloor",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rang",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "loz",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "spades",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "clubs",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hearts",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "diams",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "OElig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "oelig",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "scaron",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Yumlaut",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "circ",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tilde",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ensp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "emsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "thinsp",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwnj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "zwj",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lrm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rlm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ndash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "mdash",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "sbquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "ldquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "bdquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "Dagger",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "permil",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "lsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "rsaquo",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "euro",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "tm",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "hruler",
                    "type": docEmptyType,
                    "namespace": "",
                },
                {
                    "name": "preformatted",
                    "type": docMarkupType,
                    "namespace": "",
                },
                {
                    "name": "programlisting",
                    "type": listingType,
                    "namespace": "",
                },
                {
                    "name": "verbatim",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadocliteral",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "javadoccode",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "indexentry",
                    "type": docIndexEntryType,
                    "namespace": "",
                },
                {
                    "name": "orderedlist",
                    "type": docListType,
                    "namespace": "",
                },
                {
                    "name": "itemizedlist",
                    "type": docListType,
                    "namespace": "",
                },
                {
                    "name": "simplesect",
                    "type": docSimpleSectType,
                    "namespace": "",
                },
                {
                    "name": "title",
                    "type": docTitleType,
                    "namespace": "",
                },
                {
                    "name": "variablelist",
                    "type": docVariableListType,
                    "namespace": "",
                },
                {
                    "name": "table",
                    "type": docTableType,
                    "namespace": "",
                },
                {
                    "name": "heading",
                    "type": docHeadingType,
                    "namespace": "",
                },
                {
                    "name": "dotfile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "mscfile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "diafile",
                    "type": docImageFileType,
                    "namespace": "",
                },
                {
                    "name": "toclist",
                    "type": docTocListType,
                    "namespace": "",
                },
                {
                    "name": "language",
                    "type": docLanguageType,
                    "namespace": "",
                },
                {
                    "name": "parameterlist",
                    "type": docParamListType,
                    "namespace": "",
                },
                {
                    "name": "xrefsect",
                    "type": docXRefSectType,
                    "namespace": "",
                },
                {
                    "name": "copydoc",
                    "type": docCopyType,
                    "namespace": "",
                },
                {
                    "name": "details",
                    "type": docDetailsType,
                    "namespace": "",
                },
                {
                    "name": "blockquote",
                    "type": docBlockQuoteType,
                    "namespace": "",
                },
                {
                    "name": "parblock",
                    "type": docParBlockType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class descriptionType:
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "title",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "para",
                    "type": docParaType,
                    "namespace": "",
                },
                {
                    "name": "internal",
                    "type": docInternalType,
                    "namespace": "",
                },
                {
                    "name": "sect1",
                    "type": docSect1Type,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class enumvalueType:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "name",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "initializer",
                    "type": linkedTextType,
                    "namespace": "",
                },
                {
                    "name": "briefdescription",
                    "type": descriptionType,
                    "namespace": "",
                },
                {
                    "name": "detaileddescription",
                    "type": descriptionType,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class paramType:
    attributes: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    type: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    declname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    defname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    array: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    defval: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    typeconstraint: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class templateparamlistType:
    param: List[paramType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class memberdefType:
    templateparamlist: Optional[templateparamlistType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    type: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    definition: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    argsstring: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    name: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    qualifiedname: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    read: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    write: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    bitfield: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    reimplements: List[reimplementType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    reimplementedby: List[reimplementType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    param: List[paramType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    enumvalue: List[enumvalueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    requiresclause: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    initializer: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    exceptions: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detaileddescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inbodydescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    location: Optional[locationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    references: List[referenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    referencedby: List[referenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    kind: Optional[DoxMemberKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    static: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    strong: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    const: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    explicit: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    refqual: Optional[DoxRefQualifierKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    virt: Optional[DoxVirtualKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    volatile: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mutable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    noexcept: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    constexpr: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    readable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    writable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    initonly: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    settable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    privatesettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    protectedsettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    privategettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    protectedgettable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sealed: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    new: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    add: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    remove: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    raise_value: Optional[DoxBool] = field(
        default=None,
        metadata={
            "name": "raise",
            "type": "Attribute",
        }
    )
    optional: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    required: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accessor: Optional[DoxAccessor] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attribute: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    property: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    readonly: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    bound: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    removable: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    constrained: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    transient: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybevoid: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybedefault: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maybeambiguous: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class sectiondefType:
    header: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    description: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    memberdef: List[memberdefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    kind: Optional[DoxSectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class compounddefType:
    compoundname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    basecompoundref: List[compoundRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    derivedcompoundref: List[compoundRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    includes: List[incType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    includedby: List[incType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    incdepgraph: Optional[graphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    invincdepgraph: Optional[graphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerdir: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerfile: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerclass: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innernamespace: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innerpage: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    innergroup: List[refType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    templateparamlist: Optional[templateparamlistType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    sectiondef: List[sectiondefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    tableofcontents: Optional[tableofcontentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    requiresclause: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    initializer: Optional[linkedTextType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    briefdescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    detaileddescription: Optional[descriptionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    inheritancegraph: Optional[graphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    collaborationgraph: Optional[graphType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    programlisting: Optional[listingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    location: Optional[locationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    listofallmembers: Optional[listofallmembersType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    kind: Optional[DoxCompoundKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    language: Optional[DoxLanguage] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    prot: Optional[DoxProtectionKind] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    inline: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sealed: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    abstract: Optional[DoxBool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DoxygenType:
    compounddef: List[compounddefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class doxygen(DoxygenType):
    pass

docSimpleSectType.__pydantic_model__.update_forward_refs()
