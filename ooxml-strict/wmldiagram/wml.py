# ./wml.py
# PyXB bindings for NamespaceModule
# NSM:19646aec388215c989fb75ede3f402ff063ba490
# Generated 2010-07-02 14:32:29.363722 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dd24c2f4-85d5-11df-8277-0026b9799156')

# Import bindings for namespaces imported into schema
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/wordprocessingml/2006/main', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a Python instance."""
    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=Namespace.fallbackNamespace(), location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, _fallback_namespace=default_namespace)

from _nsgroup import endnotes # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}endnotes
from _nsgroup import fonts # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}fonts
from _nsgroup import document # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}document
from _nsgroup import footnotes # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}footnotes
from _nsgroup import webSettings # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}webSettings
from _nsgroup import recipients # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}recipients
from _nsgroup import comments # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}comments
from _nsgroup import txbxContent # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}txbxContent
from _nsgroup import settings # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}settings
from _nsgroup import numbering # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}numbering
from _nsgroup import ftr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ftr
from _nsgroup import glossaryDocument # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}glossaryDocument
from _nsgroup import styles # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}styles
from _nsgroup import hdr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}hdr
from _nsgroup import ST_DecimalNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DecimalNumber
from _nsgroup import CT_Markup # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Markup
from _nsgroup import ST_DateTime # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DateTime
from _nsgroup import CT_TrackChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrackChange
from _nsgroup import CT_FFCheckBox # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFCheckBox
from _nsgroup import ST_SignedTwipsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_SignedTwipsMeasure
from _nsgroup import CT_PageMar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PageMar
from _nsgroup import CT_AltChunk # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_AltChunk
from _nsgroup import CT_OnOff # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_OnOff
from _nsgroup import CT_SdtRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtRun
from _nsgroup import CT_RunTrackChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RunTrackChange
from _nsgroup import CT_CustomXmlRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CustomXmlRun
from _nsgroup import ST_UcharHexNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_UcharHexNumber
from _nsgroup import ST_PointMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PointMeasure
from _nsgroup import ST_Border # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Border
from _nsgroup import ST_ThemeColor # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ThemeColor
from _nsgroup import ST_HexColorAuto # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HexColorAuto
from _nsgroup import ST_HexColor # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HexColor
from _nsgroup import ST_EighthPointMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_EighthPointMeasure
from _nsgroup import CT_Border # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Border
from _nsgroup import CT_SmartTagRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SmartTagRun
from _nsgroup import ST_ProofErr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ProofErr
from _nsgroup import CT_ProofErr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ProofErr
from _nsgroup import ST_DisplacedByCustomXml # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DisplacedByCustomXml
from _nsgroup import CT_MarkupRange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MarkupRange
from _nsgroup import CT_SignedTwipsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SignedTwipsMeasure
from _nsgroup import CT_String # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_String
from _nsgroup import CT_Perm # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Perm
from _nsgroup import CT_Hyperlink # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Hyperlink
from _nsgroup import CT_Empty # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Empty
from _nsgroup import CT_Drawing # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Drawing
from _nsgroup import ST_PixelsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PixelsMeasure
from _nsgroup import CT_PixelsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PixelsMeasure
from _nsgroup import ST_EdGrp # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_EdGrp
from _nsgroup import CT_PermStart # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PermStart
from _nsgroup import CT_FtnEdnRef # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnEdnRef
from _nsgroup import ST_CombineBrackets # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_CombineBrackets
from _nsgroup import CT_EastAsianLayout # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_EastAsianLayout
from _nsgroup import CT_SdtPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtPr
from _nsgroup import CT_TblGridBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblGridBase
from _nsgroup import CT_TblGrid # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblGrid
from _nsgroup import ST_LongHexNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_LongHexNumber
from _nsgroup import CT_P # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_P
from _nsgroup import CT_DocPartCategory # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartCategory
from _nsgroup import CT_CustomXmlCell # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CustomXmlCell
from _nsgroup import ST_HpsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HpsMeasure
from _nsgroup import CT_HpsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_HpsMeasure
from _nsgroup import ST_JcTable # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_JcTable
from _nsgroup import CT_JcTable # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_JcTable
from _nsgroup import CT_BookmarkRange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_BookmarkRange
from _nsgroup import CT_Bookmark # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Bookmark
from _nsgroup import CT_MoveBookmark # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MoveBookmark
from _nsgroup import ST_TblWidth # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TblWidth
from _nsgroup import ST_UnqualifiedPercentage # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_UnqualifiedPercentage
from _nsgroup import ST_DecimalNumberOrPercent # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DecimalNumberOrPercent
from _nsgroup import CT_TblWidth # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblWidth
from _nsgroup import ST_LineNumberRestart # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_LineNumberRestart
from _nsgroup import CT_LineNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LineNumber
from _nsgroup import ST_Shd # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Shd
from _nsgroup import CT_Shd # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Shd
from _nsgroup import ST_Direction # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Direction
from _nsgroup import CT_DirContentRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DirContentRun
from _nsgroup import CT_DocRsids # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocRsids
from _nsgroup import CT_RPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RPr
from _nsgroup import CT_VerticalAlignRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_VerticalAlignRun
from _nsgroup import CT_Frame # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Frame
from _nsgroup import CT_SdtEndPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtEndPr
from _nsgroup import CT_BdoContentRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_BdoContentRun
from _nsgroup import ST_RestartNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_RestartNumber
from _nsgroup import CT_NumRestart # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_NumRestart
from _nsgroup import ST_Underline # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Underline
from _nsgroup import CT_Underline # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Underline
from _nsgroup import CT_Captions # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Captions
from _nsgroup import CT_Ind # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Ind
from _nsgroup import CT_SdtListItem # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtListItem
from _nsgroup import CT_Rel # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Rel
from _nsgroup import CT_SdtDocPart # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtDocPart
from _nsgroup import CT_Body # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Body
from _nsgroup import CT_Columns # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Columns
from _nsgroup import CT_ShapeDefaults # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ShapeDefaults
from _nsgroup import CT_Tbl # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Tbl
from _nsgroup import ST_Theme # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Theme
from _nsgroup import ST_Hint # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Hint
from _nsgroup import CT_Fonts # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Fonts
from _nsgroup import CT_Endnotes # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Endnotes
from _nsgroup import ST_ShortHexNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ShortHexNumber
from _nsgroup import CT_TblLook # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblLook
from _nsgroup import CT_DecimalNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DecimalNumber
from _nsgroup import CT_SdtBlock # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtBlock
from _nsgroup import CT_PPrBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PPrBase
from _nsgroup import CT_PPrGeneral # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PPrGeneral
from _nsgroup import ST_Cnf # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Cnf
from _nsgroup import CT_Cnf # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Cnf
from _nsgroup import CT_RPrDefault # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RPrDefault
from _nsgroup import CT_SdtDropDownList # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtDropDownList
from _nsgroup import CT_DocDefaults # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocDefaults
from _nsgroup import CT_FtnProps # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnProps
from _nsgroup import CT_CustomXmlPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CustomXmlPr
from _nsgroup import CT_Color # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Color
from _nsgroup import ST_InfoTextType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_InfoTextType
from _nsgroup import ST_FFHelpTextVal # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FFHelpTextVal
from _nsgroup import CT_FFHelpText # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFHelpText
from _nsgroup import CT_Tc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Tc
from _nsgroup import CT_SdtRow # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtRow
from _nsgroup import CT_SectPrBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SectPrBase
from _nsgroup import CT_TblPrBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPrBase
from _nsgroup import ST_PTabAlignment # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PTabAlignment
from _nsgroup import ST_PTabLeader # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PTabLeader
from _nsgroup import ST_PTabRelativeTo # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PTabRelativeTo
from _nsgroup import CT_PTab # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PTab
from _nsgroup import CT_TwipsMeasure_ as CT_TwipsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TwipsMeasure
from _nsgroup import CT_Sym # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Sym
from _nsgroup import CT_StylePaneFilter # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_StylePaneFilter
from _nsgroup import CT_SectPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SectPr
from _nsgroup import CT_UnsignedDecimalNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_UnsignedDecimalNumber
from _nsgroup import CT_R_ as CT_R # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_R
from _nsgroup import ST_Em # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Em
from _nsgroup import CT_Em # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Em
from _nsgroup import CT_Picture # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Picture
from _nsgroup import CT_PageBorder # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PageBorder
from _nsgroup import CT_BottomPageBorder # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_BottomPageBorder
from _nsgroup import CT_Text # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Text
from _nsgroup import CT_FontsList # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FontsList
from _nsgroup import CT_CustomXmlRow # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CustomXmlRow
from _nsgroup import CT_Panose # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Panose
from _nsgroup import ST_BrClear # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_BrClear
from _nsgroup import ST_BrType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_BrType
from _nsgroup import CT_Br # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Br
from _nsgroup import CT_Language # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Language
from _nsgroup import CT_Kinsoku # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Kinsoku
from _nsgroup import CT_FitText # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FitText
from _nsgroup import CT_Lang # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Lang
from _nsgroup import ST_VAnchor # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_VAnchor
from _nsgroup import ST_HAnchor # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HAnchor
from _nsgroup import CT_TblPPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPPr
from _nsgroup import ST_HighlightColor # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HighlightColor
from _nsgroup import CT_Highlight # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Highlight
from _nsgroup import CT_TcBorders # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcBorders
from _nsgroup import ST_FFTextType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FFTextType
from _nsgroup import CT_FFTextType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFTextType
from _nsgroup import ST_DocProtect # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocProtect
from _nsgroup import CT_DocProtect # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocProtect
from _nsgroup import CT_DocumentBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocumentBase
from _nsgroup import CT_Document # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Document
from _nsgroup import ST_VerticalJc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_VerticalJc
from _nsgroup import CT_VerticalJc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_VerticalJc
from _nsgroup import CT_SdtText # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtText
from _nsgroup import CT_CustomXmlBlock # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CustomXmlBlock
from _nsgroup import CT_Background # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Background
from _nsgroup import CT_EdnProps # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_EdnProps
from _nsgroup import ST_TextEffect # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TextEffect
from _nsgroup import CT_TextEffect # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TextEffect
from _nsgroup import CT_RPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RPrChange
from _nsgroup import ST_Jc_ as ST_Jc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Jc
from _nsgroup import CT_Jc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Jc
from _nsgroup import CT_SectPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SectPrChange
from _nsgroup import CT_TblCellMar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblCellMar
from _nsgroup import CT_TcPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcPrChange
from _nsgroup import ST_TextDirection # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TextDirection
from _nsgroup import CT_TextDirection # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TextDirection
from _nsgroup import ST_SignedHpsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_SignedHpsMeasure
from _nsgroup import CT_SignedHpsMeasure # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SignedHpsMeasure
from _nsgroup import ST_WmlColorSchemeIndex # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_WmlColorSchemeIndex
from _nsgroup import CT_ColorSchemeMapping # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ColorSchemeMapping
from _nsgroup import CT_SmartTagPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SmartTagPr
from _nsgroup import CT_Column # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Column
from _nsgroup import CT_Object # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Object
from _nsgroup import CT_Footnotes # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Footnotes
from _nsgroup import CT_SimpleField # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SimpleField
from _nsgroup import CT_RPrOriginal # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RPrOriginal
from _nsgroup import CT_SaveThroughXslt # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SaveThroughXslt
from _nsgroup import CT_LatentStyles # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LatentStyles
from _nsgroup import ST_TblLayoutType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TblLayoutType
from _nsgroup import CT_TblLayoutType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblLayoutType
from _nsgroup import ST_StyleSort # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_StyleSort
from _nsgroup import CT_StyleSort # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_StyleSort
from _nsgroup import ST_View # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_View
from _nsgroup import CT_View # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_View
from _nsgroup import CT_TrackChangeNumbering # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrackChangeNumbering
from _nsgroup import CT_NumLvl # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_NumLvl
from _nsgroup import CT_FontSig # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FontSig
from _nsgroup import CT_TcPrBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcPrBase
from _nsgroup import CT_TcPrInner # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcPrInner
from _nsgroup import CT_TcPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcPr
from _nsgroup import CT_PaperSource # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PaperSource
from _nsgroup import ST_MailMergeOdsoFMDFieldType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MailMergeOdsoFMDFieldType
from _nsgroup import CT_MailMergeOdsoFMDFieldType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMergeOdsoFMDFieldType
from _nsgroup import ST_PageOrientation # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PageOrientation
from _nsgroup import CT_PageSz # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PageSz
from _nsgroup import CT_LongHexNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LongHexNumber
from _nsgroup import CT_WebSettings # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_WebSettings
from _nsgroup import CT_TrPrBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrPrBase
from _nsgroup import CT_TrPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrPr
from _nsgroup import CT_Recipients # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Recipients
from _nsgroup import CT_WritingStyle # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_WritingStyle
from _nsgroup import ST_Pitch # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Pitch
from _nsgroup import CT_Pitch # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Pitch
from _nsgroup import ST_TblStyleOverrideType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TblStyleOverrideType
from _nsgroup import CT_TblStylePr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblStylePr
from _nsgroup import ST_TabTlc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TabTlc
from _nsgroup import ST_TabJc # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TabJc
from _nsgroup import CT_TabStop # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TabStop
from _nsgroup import ST_FontFamily # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FontFamily
from _nsgroup import CT_FontFamily # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FontFamily
from _nsgroup import CT_SdtCell # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtCell
from _nsgroup import ST_PageBorderDisplay # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PageBorderDisplay
from _nsgroup import ST_PageBorderZOrder # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PageBorderZOrder
from _nsgroup import ST_PageBorderOffset # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_PageBorderOffset
from _nsgroup import CT_PageBorders # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PageBorders
from _nsgroup import CT_Div # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Div
from _nsgroup import ST_Merge # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Merge
from _nsgroup import CT_VMerge # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_VMerge
from _nsgroup import CT_Frameset # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Frameset
from _nsgroup import CT_TblPrExChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPrExChange
from _nsgroup import ST_LineSpacingRule # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_LineSpacingRule
from _nsgroup import CT_Spacing # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Spacing
from _nsgroup import CT_DocPart # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPart
from _nsgroup import ST_TextboxTightWrap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TextboxTightWrap
from _nsgroup import CT_TextboxTightWrap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TextboxTightWrap
from _nsgroup import ST_ObjectDrawAspect # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ObjectDrawAspect
from _nsgroup import CT_ObjectEmbed # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ObjectEmbed
from _nsgroup import CT_FtnEdnSepRef # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnEdnSepRef
from _nsgroup import CT_TrPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrPrChange
from _nsgroup import CT_FontRel # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FontRel
from _nsgroup import CT_Comments # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Comments
from _nsgroup import ST_MailMergeDocType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MailMergeDocType
from _nsgroup import CT_MailMergeDocType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMergeDocType
from _nsgroup import ST_FldCharType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FldCharType
from _nsgroup import CT_FldChar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FldChar
from _nsgroup import CT_TrackChangesView # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrackChangesView
from _nsgroup import ST_LevelSuffix # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_LevelSuffix
from _nsgroup import CT_LevelSuffix # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LevelSuffix
from _nsgroup import ST_DocGrid # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocGrid
from _nsgroup import CT_DocGrid # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocGrid
from _nsgroup import CT_FFTextInput # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFTextInput
from _nsgroup import CT_Font # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Font
from _nsgroup import CT_TcMar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TcMar
from _nsgroup import ST_MacroName # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MacroName
from _nsgroup import CT_MacroName # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MacroName
from _nsgroup import CT_DivBdr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DivBdr
from _nsgroup import ST_TextScale # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TextScale
from _nsgroup import CT_TextScale # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TextScale
from _nsgroup import ST_TblOverlap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TblOverlap
from _nsgroup import CT_TblOverlap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblOverlap
from _nsgroup import ST_MailMergeSourceType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MailMergeSourceType
from _nsgroup import CT_MailMergeSourceType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMergeSourceType
from _nsgroup import ST_ChapterSep # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ChapterSep
from _nsgroup import ST_NumberFormat # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_NumberFormat
from _nsgroup import CT_PageNumber # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PageNumber
from _nsgroup import CT_PPrDefault # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PPrDefault
from _nsgroup import ST_HdrFtr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HdrFtr
from _nsgroup import CT_HdrFtrRef # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_HdrFtrRef
from _nsgroup import ST_RubyAlign # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_RubyAlign
from _nsgroup import CT_RubyAlign # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RubyAlign
from _nsgroup import ST_SectionMark # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_SectionMark
from _nsgroup import CT_SectType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SectType
from _nsgroup import CT_TxbxContent # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TxbxContent
from _nsgroup import CT_Settings # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Settings
from _nsgroup import CT_Tabs # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Tabs
from _nsgroup import CT_EdnDocProps # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_EdnDocProps
from _nsgroup import CT_DocPartBehaviors # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartBehaviors
from _nsgroup import CT_NumFmt # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_NumFmt
from _nsgroup import CT_SmartTagType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SmartTagType
from _nsgroup import CT_TblBorders # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblBorders
from _nsgroup import CT_PPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PPrChange
from _nsgroup import CT_Numbering # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Numbering
from _nsgroup import CT_Divs # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Divs
from _nsgroup import CT_AbstractNum # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_AbstractNum
from _nsgroup import CT_Guid # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Guid
from _nsgroup import CT_SdtComboBox # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtComboBox
from _nsgroup import ST_FrameScrollbar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FrameScrollbar
from _nsgroup import CT_FrameScrollbar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FrameScrollbar
from _nsgroup import CT_DecimalNumberOrPrecent # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DecimalNumberOrPrecent
from _nsgroup import CT_Lvl # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Lvl
from _nsgroup import CT_FFData # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFData
from _nsgroup import CT_AutoCaptions # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_AutoCaptions
from _nsgroup import CT_HdrFtr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_HdrFtr
from _nsgroup import CT_DocPartPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartPr
from _nsgroup import ST_EdnPos # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_EdnPos
from _nsgroup import CT_EdnPos # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_EdnPos
from _nsgroup import CT_CalendarType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CalendarType
from _nsgroup import CT_Control # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Control
from _nsgroup import CT_DocPartName # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartName
from _nsgroup import CT_ParaRPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ParaRPr
from _nsgroup import CT_Row # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Row
from _nsgroup import CT_TblGridCol # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblGridCol
from _nsgroup import ST_AnnotationVMerge # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_AnnotationVMerge
from _nsgroup import CT_CellMergeTrackChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CellMergeTrackChange
from _nsgroup import CT_ParaRPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ParaRPrChange
from _nsgroup import ST_FtnEdn # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FtnEdn
from _nsgroup import CT_FtnEdn # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnEdn
from _nsgroup import ST_ObjectUpdateMode # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_ObjectUpdateMode
from _nsgroup import CT_ObjectLink # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ObjectLink
from _nsgroup import CT_LevelText # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LevelText
from _nsgroup import CT_RubyContent # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RubyContent
from _nsgroup import ST_DocPartBehavior # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocPartBehavior
from _nsgroup import CT_DocPartBehavior # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartBehavior
from _nsgroup import CT_GlossaryDocument # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_GlossaryDocument
from _nsgroup import CT_TblGridChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblGridChange
from _nsgroup import CT_Attr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Attr
from _nsgroup import CT_NumPicBullet # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_NumPicBullet
from _nsgroup import ST_FrameLayout # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FrameLayout
from _nsgroup import CT_FrameLayout # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FrameLayout
from _nsgroup import ST_MailMergeDest # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MailMergeDest
from _nsgroup import CT_MailMergeDest # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMergeDest
from _nsgroup import CT_Num # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Num
from _nsgroup import CT_FFDDList # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFDDList
from _nsgroup import CT_SdtContentRow # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtContentRow
from _nsgroup import CT_Styles # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Styles
from _nsgroup import CT_LsdException # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LsdException
from _nsgroup import CT_LvlLegacy # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_LvlLegacy
from _nsgroup import CT_ParaRPrOriginal # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ParaRPrOriginal
from _nsgroup import CT_Ruby # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Ruby
from _nsgroup import CT_Charset # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Charset
from _nsgroup import CT_SdtContentCell # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtContentCell
from _nsgroup import CT_SdtContentBlock # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtContentBlock
from _nsgroup import CT_DocParts # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocParts
from _nsgroup import ST_HeightRule # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_HeightRule
from _nsgroup import CT_Height # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Height
from _nsgroup import CT_TopPageBorder # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TopPageBorder
from _nsgroup import ST_DocPartGallery # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocPartGallery
from _nsgroup import CT_DocPartGallery # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartGallery
from _nsgroup import CT_SdtContentRun # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtContentRun
from _nsgroup import CT_Comment # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Comment
from _nsgroup import ST_DocPartType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocPartType
from _nsgroup import CT_DocPartType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartType
from _nsgroup import CT_TrackChangeRange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TrackChangeRange
from _nsgroup import ST_DropCap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DropCap
from _nsgroup import ST_Wrap # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Wrap
from _nsgroup import CT_FramePr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FramePr
from _nsgroup import ST_StyleType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_StyleType
from _nsgroup import CT_Style # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Style
from _nsgroup import ST_MailMergeDataType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MailMergeDataType
from _nsgroup import CT_MailMergeDataType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMergeDataType
from _nsgroup import ST_FtnPos # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FtnPos
from _nsgroup import CT_FtnPos # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnPos
from _nsgroup import ST_Zoom # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Zoom
from _nsgroup import CT_Zoom # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Zoom
from _nsgroup import ST_TextAlignment # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TextAlignment
from _nsgroup import CT_TextAlignment # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TextAlignment
from _nsgroup import CT_HMerge # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_HMerge
from _nsgroup import CT_NumPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_NumPr
from _nsgroup import ST_FFStatusTextVal # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FFStatusTextVal
from _nsgroup import CT_FFStatusText # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFStatusText
from _nsgroup import CT_TblPrChange # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPrChange
from _nsgroup import ST_Proof # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Proof
from _nsgroup import CT_Proof # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Proof
from _nsgroup import CT_Headers # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Headers
from _nsgroup import CT_RubyPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RubyPr
from _nsgroup import CT_PPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PPr
from _nsgroup import CT_TblPrExBase # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPrExBase
from _nsgroup import CT_OdsoFieldMapData # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_OdsoFieldMapData
from _nsgroup import ST_SdtDateMappingType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_SdtDateMappingType
from _nsgroup import CT_SdtDateMappingType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtDateMappingType
from _nsgroup import CT_FramesetSplitbar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FramesetSplitbar
from _nsgroup import CT_ReadingModeInkLockDown # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_ReadingModeInkLockDown
from _nsgroup import CT_TblPrEx # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPrEx
from _nsgroup import ST_CharacterSpacing # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_CharacterSpacing
from _nsgroup import CT_CharacterSpacing # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CharacterSpacing
from _nsgroup import ST_MultiLevelType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_MultiLevelType
from _nsgroup import CT_MultiLevelType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MultiLevelType
from _nsgroup import ST_TargetScreenSz # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_TargetScreenSz
from _nsgroup import CT_TargetScreenSz # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TargetScreenSz
from _nsgroup import CT_SdtDate # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_SdtDate
from _nsgroup import CT_PBdr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_PBdr
from _nsgroup import CT_DocVars # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocVars
from _nsgroup import ST_FFName # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_FFName
from _nsgroup import CT_FFName # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FFName
from _nsgroup import CT_Compat # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Compat
from _nsgroup import CT_AltChunkPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_AltChunkPr
from _nsgroup import CT_AutoCaption # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_AutoCaption
from _nsgroup import CT_OptimizeForBrowser # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_OptimizeForBrowser
from _nsgroup import CT_MailMerge # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_MailMerge
from _nsgroup import CT_Odso # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Odso
from _nsgroup import CT_WriteProtection # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_WriteProtection
from _nsgroup import CT_DocVar # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocVar
from _nsgroup import CT_RecipientData # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_RecipientData
from _nsgroup import CT_Placeholder # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Placeholder
from _nsgroup import CT_FtnDocProps # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_FtnDocProps
from _nsgroup import ST_CaptionPos # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_CaptionPos
from _nsgroup import CT_Caption # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Caption
from _nsgroup import CT_DataBinding # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DataBinding
from _nsgroup import CT_DocPartTypes # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocPartTypes
from _nsgroup import CT_CompatSetting # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_CompatSetting
from _nsgroup import ST_Lock # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_Lock
from _nsgroup import CT_Lock # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_Lock
from _nsgroup import ST_DocType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}ST_DocType
from _nsgroup import CT_DocType # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_DocType
from _nsgroup import CT_TblPr # {http://schemas.openxmlformats.org/wordprocessingml/2006/main}CT_TblPr
