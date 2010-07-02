# ./_m.py
# PyXB bindings for NamespaceModule
# NSM:5efc25b18958ca665491f7bd74832d9a9691ccbf
# Generated 2010-07-02 14:32:29.363874 by PyXB version 1.1.2
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

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/officeDocument/2006/math', create_if_missing=True)
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

from _nsgroup import oMathPara # {http://schemas.openxmlformats.org/officeDocument/2006/math}oMathPara
from _nsgroup import oMath # {http://schemas.openxmlformats.org/officeDocument/2006/math}oMath
from _nsgroup import mathPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}mathPr
from _nsgroup import ST_Char # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Char
from _nsgroup import CT_Char # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Char
from _nsgroup import CT_Func # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Func
from _nsgroup import CT_CtrlPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_CtrlPr
from _nsgroup import CT_OMathArg # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMathArg
from _nsgroup import CT_OMath # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMath
from _nsgroup import ST_UnSignedInteger # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_UnSignedInteger
from _nsgroup import CT_UnSignedInteger # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_UnSignedInteger
from _nsgroup import CT_OnOff_ as CT_OnOff # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OnOff
from _nsgroup import ST_SpacingRule # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_SpacingRule
from _nsgroup import CT_SpacingRule # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SpacingRule
from _nsgroup import CT_OMathPara # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMathPara
from _nsgroup import CT_SSubSup # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSubSup
from _nsgroup import CT_Nary # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Nary
from _nsgroup import ST_Script # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Script
from _nsgroup import CT_Script # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Script
from _nsgroup import CT_GroupChrPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_GroupChrPr
from _nsgroup import CT_BoxPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BoxPr
from _nsgroup import ST_TopBot # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_TopBot
from _nsgroup import CT_TopBot # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_TopBot
from _nsgroup import CT_R # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_R
from _nsgroup import CT_DPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_DPr
from _nsgroup import CT_TwipsMeasure # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_TwipsMeasure
from _nsgroup import CT_LimUpp # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_LimUpp
from _nsgroup import ST_Jc # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Jc
from _nsgroup import CT_OMathJc # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMathJc
from _nsgroup import ST_Shp # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Shp
from _nsgroup import CT_Shp # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Shp
from _nsgroup import CT_MPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MPr
from _nsgroup import CT_Rad # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Rad
from _nsgroup import CT_Acc # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Acc
from _nsgroup import CT_Box # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Box
from _nsgroup import CT_BorderBox # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BorderBox
from _nsgroup import CT_FPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_FPr
from _nsgroup import CT_YAlign # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_YAlign
from _nsgroup import CT_MC # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MC
from _nsgroup import ST_Integer2 # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Integer2
from _nsgroup import CT_Integer2 # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Integer2
from _nsgroup import CT_Phant # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Phant
from _nsgroup import CT_M # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_M
from _nsgroup import CT_GroupChr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_GroupChr
from _nsgroup import CT_SSup # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSup
from _nsgroup import CT_String_ as CT_String # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_String
from _nsgroup import CT_D # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_D
from _nsgroup import CT_EqArr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_EqArr
from _nsgroup import CT_F # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_F
from _nsgroup import CT_Bar # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Bar
from _nsgroup import ST_FType # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_FType
from _nsgroup import CT_FType # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_FType
from _nsgroup import CT_SSub # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSub
from _nsgroup import CT_BorderBoxPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BorderBoxPr
from _nsgroup import CT_SPre # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SPre
from _nsgroup import CT_XAlign # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_XAlign
from _nsgroup import CT_LimLow # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_LimLow
from _nsgroup import ST_Integer255 # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Integer255
from _nsgroup import CT_ManualBreak # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_ManualBreak
from _nsgroup import CT_LimUppPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_LimUppPr
from _nsgroup import CT_LimLowPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_LimLowPr
from _nsgroup import CT_Text_ as CT_Text # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Text
from _nsgroup import CT_Integer255 # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Integer255
from _nsgroup import CT_SSupPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSupPr
from _nsgroup import CT_EqArrPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_EqArrPr
from _nsgroup import CT_MathPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MathPr
from _nsgroup import CT_SSubSupPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSubSupPr
from _nsgroup import ST_LimLoc # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_LimLoc
from _nsgroup import CT_LimLoc # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_LimLoc
from _nsgroup import CT_SSubPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SSubPr
from _nsgroup import ST_BreakBinSub # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_BreakBinSub
from _nsgroup import CT_BreakBinSub # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BreakBinSub
from _nsgroup import CT_OMathParaPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMathParaPr
from _nsgroup import CT_MCPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MCPr
from _nsgroup import CT_OMathArgPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_OMathArgPr
from _nsgroup import CT_MR # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MR
from _nsgroup import CT_MCS # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_MCS
from _nsgroup import CT_RPR # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_RPR
from _nsgroup import CT_SPrePr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_SPrePr
from _nsgroup import CT_RadPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_RadPr
from _nsgroup import CT_PhantPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_PhantPr
from _nsgroup import CT_NaryPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_NaryPr
from _nsgroup import CT_BarPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BarPr
from _nsgroup import CT_AccPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_AccPr
from _nsgroup import ST_Style # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_Style
from _nsgroup import CT_Style_ as CT_Style # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_Style
from _nsgroup import ST_BreakBin # {http://schemas.openxmlformats.org/officeDocument/2006/math}ST_BreakBin
from _nsgroup import CT_BreakBin # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_BreakBin
from _nsgroup import CT_FuncPr # {http://schemas.openxmlformats.org/officeDocument/2006/math}CT_FuncPr
