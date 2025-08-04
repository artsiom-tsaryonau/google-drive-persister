from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Unit(str, Enum):
    """Unit enumeration for dimensions."""

    UNIT_UNSPECIFIED = "UNIT_UNSPECIFIED"
    PT = "PT"


class RgbColor(BaseModel):
    """Represents RGB color values."""

    red: float = Field(..., description="Red component (0.0-1.0)")
    green: float = Field(..., description="Green component (0.0-1.0)")
    blue: float = Field(..., description="Blue component (0.0-1.0)")


class Color(BaseModel):
    """Represents a color in the Google Docs API."""

    rgbColor: Optional[RgbColor] = Field(None, description="RGB color values")
    themeColor: Optional[str] = Field(None, description="Theme color name")


class OptionalColor(BaseModel):
    """Represents an optional color."""

    color: Optional[Color] = Field(None, description="The color")


class Dimension(BaseModel):
    """Represents a dimension with magnitude and unit."""

    magnitude: float = Field(..., description="The magnitude of the dimension")
    unit: Unit = Field(..., description="The unit of the dimension")


class TabStopAlignment(str, Enum):
    """Tab stop alignment enumeration."""

    TAB_STOP_ALIGNMENT_UNSPECIFIED = "TAB_STOP_ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"


class BaselineOffset(str, Enum):
    """Baseline offset enumeration."""

    BASELINE_OFFSET_UNSPECIFIED = "BASELINE_OFFSET_UNSPECIFIED"
    NONE = "NONE"
    SUPERSCRIPT = "SUPERSCRIPT"
    SUBSCRIPT = "SUBSCRIPT"


class AutoTextType(str, Enum):
    """Auto text type enumeration."""

    TYPE_UNSPECIFIED = "TYPE_UNSPECIFIED"
    PAGE_NUMBER = "PAGE_NUMBER"
    PAGE_COUNT = "PAGE_COUNT"


class NamedStyleType(str, Enum):
    """Named style type enumeration."""

    NAMED_STYLE_TYPE_UNSPECIFIED = "NAMED_STYLE_TYPE_UNSPECIFIED"
    NORMAL_TEXT = "NORMAL_TEXT"
    TITLE = "TITLE"
    SUBTITLE = "SUBTITLE"
    HEADING_1 = "HEADING_1"
    HEADING_2 = "HEADING_2"
    HEADING_3 = "HEADING_3"
    HEADING_4 = "HEADING_4"
    HEADING_5 = "HEADING_5"
    HEADING_6 = "HEADING_6"


class Alignment(str, Enum):
    """Alignment enumeration."""

    ALIGNMENT_UNSPECIFIED = "ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"
    JUSTIFIED = "JUSTIFIED"


class ContentDirection(str, Enum):
    """Content direction enumeration."""

    CONTENT_DIRECTION_UNSPECIFIED = "CONTENT_DIRECTION_UNSPECIFIED"
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"


class SpacingMode(str, Enum):
    """Spacing mode enumeration."""

    SPACING_MODE_UNSPECIFIED = "SPACING_MODE_UNSPECIFIED"
    NEVER_COLLAPSE = "NEVER_COLLAPSE"
    COLLAPSE_LISTS = "COLLAPSE_LISTS"
    COLLAPSE_WHITESPACE = "COLLAPSE_WHITESPACE"


class DashStyle(str, Enum):
    """Dash style enumeration."""

    DASH_STYLE_UNSPECIFIED = "DASH_STYLE_UNSPECIFIED"
    SOLID = "SOLID"
    DOT = "DOT"
    DASH = "DASH"


class BulletAlignment(str, Enum):
    """Bullet alignment enumeration."""

    BULLET_ALIGNMENT_UNSPECIFIED = "BULLET_ALIGNMENT_UNSPECIFIED"
    START = "START"
    CENTER = "CENTER"
    END = "END"


class GlyphType(str, Enum):
    """Glyph type enumeration."""

    GLYPH_TYPE_UNSPECIFIED = "GLYPH_TYPE_UNSPECIFIED"
    NONE = "NONE"
    BULLET = "BULLET"
    HOLLOW_BULLET = "HOLLOW_BULLET"
    SQUARE_BULLET = "SQUARE_BULLET"
    NUMBERS = "NUMBERS"
    UPPER_ALPHA = "UPPER_ALPHA"
    LOWER_ALPHA = "LOWER_ALPHA"
    UPPER_ROMAN = "UPPER_ROMAN"
    LOWER_ROMAN = "LOWER_ROMAN"


class ContentAlignment(str, Enum):
    """Content alignment enumeration."""

    CONTENT_ALIGNMENT_UNSPECIFIED = "CONTENT_ALIGNMENT_UNSPECIFIED"
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"


class WidthType(str, Enum):
    """Width type enumeration."""

    WIDTH_TYPE_UNSPECIFIED = "WIDTH_TYPE_UNSPECIFIED"
    EVENLY_DISTRIBUTED = "EVENLY_DISTRIBUTED"
    FIXED_WIDTH = "FIXED_WIDTH"


class ColumnSeparatorStyle(str, Enum):
    """Column separator style enumeration."""

    COLUMN_SEPARATOR_STYLE_UNSPECIFIED = "COLUMN_SEPARATOR_STYLE_UNSPECIFIED"
    NONE = "NONE"
    BETWEEN_EACH_COLUMN = "BETWEEN_EACH_COLUMN"
    BETWEEN_START_AND_END = "BETWEEN_START_AND_END"


class SectionType(str, Enum):
    """Section type enumeration."""

    SECTION_TYPE_UNSPECIFIED = "SECTION_TYPE_UNSPECIFIED"
    CONTINUOUS = "CONTINUOUS"
    NEW_PAGE = "NEW_PAGE"
    NEW_COLUMN = "NEW_COLUMN"


class PropertyState(str, Enum):
    """Property state enumeration."""

    PROPERTY_STATE_UNSPECIFIED = "PROPERTY_STATE_UNSPECIFIED"
    NOT_RENDERED = "NOT_RENDERED"
    RENDERED = "RENDERED"


class PageOrientation(str, Enum):
    """Page orientation enumeration."""

    PAGE_ORIENTATION_UNSPECIFIED = "PAGE_ORIENTATION_UNSPECIFIED"
    PORTRAIT = "PORTRAIT"
    LANDSCAPE = "LANDSCAPE"


class TabStop(BaseModel):
    """Represents a tab stop in a paragraph."""

    offset: Dimension = Field(..., description="The offset of the tab stop")
    alignment: TabStopAlignment = Field(
        ..., description="The alignment of the tab stop"
    )


class WeightedFontFamily(BaseModel):
    """Represents a weighted font family."""

    fontFamily: str = Field(..., description="The font family name")
    weight: Optional[int] = Field(None, description="The font weight")


class Link(BaseModel):
    """Represents a link."""

    url: str = Field(..., description="The URL")


class BookmarkLink(BaseModel):
    """Represents a bookmark link."""

    bookmarkId: str = Field(..., description="The bookmark ID")


class HeadingLink(BaseModel):
    """Represents a heading link."""

    documentId: str = Field(..., description="The document ID")
    headingId: str = Field(..., description="The heading ID")


class TextStyle(BaseModel):
    """Represents the styling of text."""

    bold: Optional[bool] = Field(None, description="Whether the text is bold")
    italic: Optional[bool] = Field(None, description="Whether the text is italic")
    underline: Optional[bool] = Field(
        None, description="Whether the text is underlined"
    )
    strikethrough: Optional[bool] = Field(
        None, description="Whether the text has a strikethrough"
    )
    smallCaps: Optional[bool] = Field(
        None, description="Whether the text is in small caps"
    )
    backgroundColor: Optional[Color] = Field(None, description="Background color")
    foregroundColor: Optional[Color] = Field(None, description="Foreground color")
    fontSize: Optional[Dimension] = Field(None, description="Font size")
    weightedFontFamily: Optional[WeightedFontFamily] = Field(
        None, description="Font family with weights"
    )
    baselineOffset: Optional[BaselineOffset] = Field(
        None, description="Baseline offset"
    )
    link: Optional[Link] = Field(None, description="Link information")


class TextStyleSuggestionState(BaseModel):
    """Represents the suggestion state of text style."""

    boldSuggested: Optional[bool] = Field(None, description="Whether bold is suggested")
    italicSuggested: Optional[bool] = Field(
        None, description="Whether italic is suggested"
    )
    underlineSuggested: Optional[bool] = Field(
        None, description="Whether underline is suggested"
    )
    strikethroughSuggested: Optional[bool] = Field(
        None, description="Whether strikethrough is suggested"
    )
    smallCapsSuggested: Optional[bool] = Field(
        None, description="Whether small caps is suggested"
    )
    backgroundColorSuggested: Optional[bool] = Field(
        None, description="Whether background color is suggested"
    )
    foregroundColorSuggested: Optional[bool] = Field(
        None, description="Whether foreground color is suggested"
    )
    fontSizeSuggested: Optional[bool] = Field(
        None, description="Whether font size is suggested"
    )
    weightedFontFamilySuggested: Optional[bool] = Field(
        None, description="Whether weighted font family is suggested"
    )
    baselineOffsetSuggested: Optional[bool] = Field(
        None, description="Whether baseline offset is suggested"
    )
    linkSuggested: Optional[bool] = Field(None, description="Whether link is suggested")


class SuggestedTextStyle(BaseModel):
    """Represents a suggested text style."""

    textStyle: Optional[TextStyle] = Field(None, description="The suggested text style")
    textStyleSuggestionState: Optional[TextStyleSuggestionState] = Field(
        None, description="The suggestion state"
    )


class ParagraphBorder(BaseModel):
    """Represents a paragraph border."""

    color: OptionalColor = Field(..., description="The border color")
    width: Optional[Dimension] = Field(None, description="The border width")
    dashStyle: Optional[DashStyle] = Field(None, description="The dash style")
    padding: Optional[Dimension] = Field(None, description="The padding")


class Shading(BaseModel):
    """Represents shading."""

    backgroundColor: OptionalColor = Field(..., description="The background color")


class ParagraphStyle(BaseModel):
    """Represents the styling of a paragraph."""

    alignment: Optional[Alignment] = Field(None, description="Text alignment")
    direction: Optional[ContentDirection] = Field(None, description="Text direction")
    indentFirstLine: Optional[Dimension] = Field(None, description="First line indent")
    indentStart: Optional[Dimension] = Field(None, description="Start indent")
    keepLinesTogether: Optional[bool] = Field(None, description="Keep lines together")
    keepWithNext: Optional[bool] = Field(None, description="Keep with next paragraph")
    spaceAbove: Optional[Dimension] = Field(None, description="Space above paragraph")
    spaceBelow: Optional[Dimension] = Field(None, description="Space below paragraph")
    spacingMode: Optional[SpacingMode] = Field(None, description="Spacing mode")
    tabStops: Optional[List[TabStop]] = Field(
        None, description="Tab stops in the paragraph"
    )
    paragraphBorder: Optional[ParagraphBorder] = Field(
        None, description="Paragraph border"
    )
    shading: Optional[Shading] = Field(None, description="Paragraph shading")


class ParagraphStyleSuggestionState(BaseModel):
    """Represents the suggestion state of paragraph style."""

    alignmentSuggested: Optional[bool] = Field(
        None, description="Whether alignment is suggested"
    )
    directionSuggested: Optional[bool] = Field(
        None, description="Whether direction is suggested"
    )
    indentFirstLineSuggested: Optional[bool] = Field(
        None, description="Whether first line indent is suggested"
    )
    indentStartSuggested: Optional[bool] = Field(
        None, description="Whether start indent is suggested"
    )
    keepLinesTogetherSuggested: Optional[bool] = Field(
        None, description="Whether keep lines together is suggested"
    )
    keepWithNextSuggested: Optional[bool] = Field(
        None, description="Whether keep with next is suggested"
    )
    spaceAboveSuggested: Optional[bool] = Field(
        None, description="Whether space above is suggested"
    )
    spaceBelowSuggested: Optional[bool] = Field(
        None, description="Whether space below is suggested"
    )
    spacingModeSuggested: Optional[bool] = Field(
        None, description="Whether spacing mode is suggested"
    )
    tabStopsSuggested: Optional[bool] = Field(
        None, description="Whether tab stops are suggested"
    )
    paragraphBorderSuggested: Optional[bool] = Field(
        None, description="Whether paragraph border is suggested"
    )
    shadingSuggested: Optional[bool] = Field(
        None, description="Whether shading is suggested"
    )


class SuggestedParagraphStyle(BaseModel):
    """Represents a suggested paragraph style."""

    paragraphStyle: Optional[ParagraphStyle] = Field(
        None, description="The suggested paragraph style"
    )
    paragraphStyleSuggestionState: Optional[ParagraphStyleSuggestionState] = Field(
        None, description="The suggestion state"
    )


class ShadingSuggestionState(BaseModel):
    """Represents the suggestion state of shading."""

    backgroundColorSuggested: Optional[bool] = Field(
        None, description="Whether background color is suggested"
    )


class Bullet(BaseModel):
    """Represents a bullet."""

    listId: str = Field(..., description="The list ID")
    nestingLevel: int = Field(..., description="The nesting level")
    textStyle: Optional[TextStyle] = Field(None, description="The text style")


class BulletSuggestionState(BaseModel):
    """Represents the suggestion state of bullet."""

    listIdSuggested: Optional[bool] = Field(
        None, description="Whether list ID is suggested"
    )
    nestingLevelSuggested: Optional[bool] = Field(
        None, description="Whether nesting level is suggested"
    )
    textStyleSuggested: Optional[bool] = Field(
        None, description="Whether text style is suggested"
    )


class SuggestedBullet(BaseModel):
    """Represents a suggested bullet."""

    bullet: Optional[Bullet] = Field(None, description="The suggested bullet")
    bulletSuggestionState: Optional[BulletSuggestionState] = Field(
        None, description="The suggestion state"
    )


class ObjectReferences(BaseModel):
    """Represents object references."""

    objectIds: List[str] = Field(..., description="The object IDs")


class Body(BaseModel):
    """Represents the body of a document."""

    content: List[Dict[str, Any]] = Field(..., description="The content of the body")


class Size(BaseModel):
    """Represents a size with width and height."""

    width: Dimension = Field(..., description="Width dimension")
    height: Dimension = Field(..., description="Height dimension")


class Location(BaseModel):
    """Represents a location in the document."""

    index: int = Field(..., description="The zero-based index of the location")
    segmentId: Optional[str] = Field(
        None, description="The ID of the header, footer, or footnote"
    )


class Range(BaseModel):
    """Represents a range in the document."""

    startIndex: int = Field(..., description="The start index of the range")
    endIndex: int = Field(..., description="The end index of the range")
    segmentId: Optional[str] = Field(
        None, description="The ID of the header, footer, or footnote"
    )


class ListProperties(BaseModel):
    """Represents list properties."""

    nestingLevel: int = Field(..., description="Nesting level of the list item")
    listId: str = Field(..., description="ID of the list")


class TextRun(BaseModel):
    """Represents a run of text."""

    content: str = Field(..., description="The text content")
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class InlineObjectElement(BaseModel):
    """Represents an inline object element."""

    inlineObjectId: str = Field(..., description="ID of the inline object")
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class PageBreak(BaseModel):
    """Represents a page break."""

    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class ColumnBreak(BaseModel):
    """Represents a column break."""

    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class HorizontalRule(BaseModel):
    """Represents a horizontal rule."""

    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class Equation(BaseModel):
    """Represents an equation."""

    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class FootnoteReference(BaseModel):
    """Represents a footnote reference."""

    footnoteId: str = Field(..., description="ID of the footnote")
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class AutoText(BaseModel):
    """Represents auto text."""

    type: AutoTextType = Field(..., description="Type of auto text")
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class RichLink(BaseModel):
    """Represents a rich link."""

    richLinkId: str = Field(..., description="ID of the rich link")
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class Person(BaseModel):
    """Represents a person."""

    personId: str = Field(..., description="ID of the person")
    textStyle: Optional[TextStyle] = Field(None, description="Text styling")


class ParagraphElement(BaseModel):
    """Represents an element within a paragraph."""

    startIndex: Optional[int] = Field(None, description="Start index of the element")
    endIndex: Optional[int] = Field(None, description="End index of the element")
    textRun: Optional[TextRun] = Field(None, description="Text run")
    autoText: Optional[AutoText] = Field(None, description="Auto text")
    pageBreak: Optional[PageBreak] = Field(None, description="Page break")
    columnBreak: Optional[ColumnBreak] = Field(None, description="Column break")
    footnoteReference: Optional[FootnoteReference] = Field(
        None, description="Footnote reference"
    )
    horizontalRule: Optional[HorizontalRule] = Field(
        None, description="Horizontal rule"
    )
    equation: Optional[Equation] = Field(None, description="Equation")
    inlineObjectElement: Optional[InlineObjectElement] = Field(
        None, description="Inline object"
    )
    richLink: Optional[RichLink] = Field(None, description="Rich link")
    person: Optional[Person] = Field(None, description="Person")


class Paragraph(BaseModel):
    """Represents a paragraph in the document."""

    elements: List[ParagraphElement] = Field(
        ..., description="Elements in the paragraph"
    )
    paragraphStyle: Optional[ParagraphStyle] = Field(
        None, description="Paragraph styling"
    )
    bullet: Optional[ListProperties] = Field(None, description="Bullet properties")
    positionedObjectIds: Optional[List[str]] = Field(
        None, description="Positioned object IDs"
    )
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )


class TableRow(BaseModel):
    """Represents a row in a table."""

    startIndex: int = Field(..., description="Start index of the row")
    endIndex: int = Field(..., description="End index of the row")
    tableCells: List[Dict[str, Any]] = Field(..., description="Table cells")
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )
    tableRowStyle: Optional[Dict[str, Any]] = Field(
        None, description="Table row styling"
    )


class Table(BaseModel):
    """Represents a table in the document."""

    rows: int = Field(..., description="Number of rows")
    columns: int = Field(..., description="Number of columns")
    tableRows: List[TableRow] = Field(..., description="Table rows")
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )
    tableStyle: Optional[Dict[str, Any]] = Field(None, description="Table styling")


class SectionBreak(BaseModel):
    """Represents a section break."""

    sectionStyle: Optional[Dict[str, Any]] = Field(None, description="Section styling")
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )


class Header(BaseModel):
    """Represents a header."""

    headerId: str = Field(..., description="ID of the header")
    content: List[Dict[str, Any]] = Field(..., description="Header content")


class Footer(BaseModel):
    """Represents a footer."""

    footerId: str = Field(..., description="ID of the footer")
    content: List[Dict[str, Any]] = Field(..., description="Footer content")


class Footnote(BaseModel):
    """Represents a footnote."""

    footnoteId: str = Field(..., description="ID of the footnote")
    content: List[Dict[str, Any]] = Field(..., description="Footnote content")


class InlineObject(BaseModel):
    """Represents an inline object."""

    inlineObjectId: str = Field(..., description="ID of the inline object")
    inlineObjectProperties: Dict[str, Any] = Field(
        ..., description="Inline object properties"
    )
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )


class PositionedObject(BaseModel):
    """Represents a positioned object."""

    objectId: str = Field(..., description="ID of the positioned object")
    positionedObjectProperties: Dict[str, Any] = Field(
        ..., description="Positioned object properties"
    )
    suggestedInsertionIds: Optional[List[str]] = Field(
        None, description="Suggested insertion IDs"
    )
    suggestedDeletionIds: Optional[List[str]] = Field(
        None, description="Suggested deletion IDs"
    )


class List(BaseModel):
    """Represents a list."""

    listId: str = Field(..., description="ID of the list")
    nestingLevels: Dict[str, Dict[str, Any]] = Field(..., description="Nesting levels")


class DocumentStyle(BaseModel):
    """Represents the styling of the document."""

    background: Optional[Dict[str, Any]] = Field(None, description="Background styling")
    defaultHeaderId: Optional[str] = Field(None, description="Default header ID")
    defaultFooterId: Optional[str] = Field(None, description="Default footer ID")
    evenPageHeaderId: Optional[str] = Field(None, description="Even page header ID")
    evenPageFooterId: Optional[str] = Field(None, description="Even page footer ID")
    firstPageHeaderId: Optional[str] = Field(None, description="First page header ID")
    firstPageFooterId: Optional[str] = Field(None, description="First page footer ID")
    useFirstPageHeaderFooter: Optional[bool] = Field(
        None, description="Use first page header/footer"
    )
    useEvenPageHeaderFooter: Optional[bool] = Field(
        None, description="Use even page header/footer"
    )
    pageNumberStart: Optional[int] = Field(None, description="Starting page number")
    marginTop: Optional[Dimension] = Field(None, description="Top margin")
    marginBottom: Optional[Dimension] = Field(None, description="Bottom margin")
    marginRight: Optional[Dimension] = Field(None, description="Right margin")
    marginLeft: Optional[Dimension] = Field(None, description="Left margin")
    pageSize: Optional[Size] = Field(None, description="Page size")
    pageOrientation: Optional[PageOrientation] = Field(
        None, description="Page orientation"
    )
    headerIds: Optional[List[str]] = Field(None, description="Header IDs")
    footerIds: Optional[List[str]] = Field(None, description="Footer IDs")
    footnoteIds: Optional[List[str]] = Field(None, description="Footnote IDs")


class NamedRanges(BaseModel):
    """Represents named ranges in the document."""

    namedRanges: Dict[str, Dict[str, Any]] = Field(..., description="Named ranges")


class NamedStyles(BaseModel):
    """Represents named styles in the document."""

    styles: Dict[str, Dict[str, Any]] = Field(..., description="Named styles")


class SuggestionsViewMode(str, Enum):
    """Suggestions view mode enumeration."""

    DEFAULT_FOR_CURRENT_ACCESS = "DEFAULT_FOR_CURRENT_ACCESS"
    SUGGESTIONS_INLINE = "SUGGESTIONS_INLINE"
    PREVIEW_SUGGESTIONS_ACCEPTED = "PREVIEW_SUGGESTIONS_ACCEPTED"
    PREVIEW_WITHOUT_SUGGESTIONS = "PREVIEW_WITHOUT_SUGGESTIONS"


class StructuralElement(BaseModel):
    """Represents a structural element in the document."""

    startIndex: Optional[int] = Field(None, description="Start index of the element")
    endIndex: Optional[int] = Field(None, description="End index of the element")
    paragraph: Optional[Paragraph] = Field(None, description="Paragraph element")
    table: Optional[Table] = Field(None, description="Table element")
    sectionBreak: Optional[SectionBreak] = Field(
        None, description="Section break element"
    )
    tableOfContents: Optional[Dict[str, Any]] = Field(
        None, description="Table of contents element"
    )


class Tab(BaseModel):
    """Represents a tab in the document."""

    tabId: str = Field(..., description="The ID of the tab")
    title: str = Field(..., description="The title of the tab")
    body: Optional[Dict[str, Any]] = Field(
        None, description="The body content of the tab"
    )
    headers: Optional[Dict[str, Header]] = Field(None, description="Headers in the tab")
    footers: Optional[Dict[str, Footer]] = Field(None, description="Footers in the tab")
    footnotes: Optional[Dict[str, Footnote]] = Field(
        None, description="Footnotes in the tab"
    )
    documentStyle: Optional[DocumentStyle] = Field(
        None, description="Document styling in the tab"
    )
    suggestedDocumentStyleChanges: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description="Suggested document style changes in the tab"
    )
    namedStyles: Optional[NamedStyles] = Field(
        None, description="Named styles in the tab"
    )
    suggestedNamedStylesChanges: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description="Suggested named styles changes in the tab"
    )
    lists: Optional[Dict[str, List]] = Field(None, description="Lists in the tab")
    namedRanges: Optional[NamedRanges] = Field(
        None, description="Named ranges in the tab"
    )
    inlineObjects: Optional[Dict[str, InlineObject]] = Field(
        None, description="Inline objects in the tab"
    )
    positionedObjects: Optional[Dict[str, PositionedObject]] = Field(
        None, description="Positioned objects in the tab"
    )


class Revision(BaseModel):
    """Represents a revision of the document."""

    id: str = Field(..., description="ID of the revision")
    mimeType: str = Field(..., description="MIME type of the revision")
    modifiedTime: datetime = Field(
        ..., description="Time when the revision was modified"
    )
    keepForever: bool = Field(..., description="Whether to keep the revision forever")
    autoRevision: bool = Field(..., description="Whether this is an auto revision")
    published: bool = Field(..., description="Whether the revision is published")
    publishedOutsideDomain: bool = Field(
        ..., description="Whether published outside domain"
    )
    publishedLink: Optional[str] = Field(None, description="Published link")


class Document(BaseModel):
    """Represents a complete Google Document structure."""

    documentId: str = Field(..., description="The ID of the document")
    title: str = Field(..., description="The title of the document")
    tabs: Optional[List[Tab]] = Field(None, description="Tabs in the document")
    revisionId: Optional[str] = Field(None, description="Revision ID")
    suggestionsViewMode: Optional[SuggestionsViewMode] = Field(
        None, description="Suggestions view mode"
    )
    body: Body = Field(..., description="The body content of the document")
    headers: Optional[Dict[str, Header]] = Field(None, description="Headers")
    footers: Optional[Dict[str, Footer]] = Field(None, description="Footers")
    footnotes: Optional[Dict[str, Footnote]] = Field(None, description="Footnotes")
    documentStyle: Optional[DocumentStyle] = Field(None, description="Document styling")
    suggestedDocumentStyleChanges: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description="Suggested document style changes"
    )
    namedStyles: Optional[NamedStyles] = Field(None, description="Named styles")
    suggestedNamedStylesChanges: Optional[Dict[str, Dict[str, Any]]] = Field(
        None, description="Suggested named styles changes"
    )
    lists: Optional[Dict[str, List]] = Field(None, description="Lists in the document")
    namedRanges: Optional[NamedRanges] = Field(None, description="Named ranges")
    inlineObjects: Optional[Dict[str, InlineObject]] = Field(
        None, description="Inline objects"
    )
    positionedObjects: Optional[Dict[str, PositionedObject]] = Field(
        None, description="Positioned objects"
    )
