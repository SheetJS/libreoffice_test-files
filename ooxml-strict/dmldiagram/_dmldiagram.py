# ./_dmldiagram.py
# PyXB bindings for NamespaceModule
# NSM:f21916f780c9134594597370f6699cf6386d205f
# Generated 2010-07-02 14:32:14.161486 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d5fab9fc-85d5-11df-8aeb-0026b9799156')

# Import bindings for namespaces imported into schema
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/diagram', create_if_missing=True)
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

from _nsgroup import colorsDefHdr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}colorsDefHdr
from _nsgroup import relIds # {http://schemas.openxmlformats.org/drawingml/2006/diagram}relIds
from _nsgroup import layoutDefHdr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}layoutDefHdr
from _nsgroup import colorsDef # {http://schemas.openxmlformats.org/drawingml/2006/diagram}colorsDef
from _nsgroup import styleDefHdrLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}styleDefHdrLst
from _nsgroup import layoutDefHdrLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}layoutDefHdrLst
from _nsgroup import styleDefHdr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}styleDefHdr
from _nsgroup import styleDef # {http://schemas.openxmlformats.org/drawingml/2006/diagram}styleDef
from _nsgroup import layoutDef # {http://schemas.openxmlformats.org/drawingml/2006/diagram}layoutDef
from _nsgroup import colorsDefHdrLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}colorsDefHdrLst
from _nsgroup import dataModel # {http://schemas.openxmlformats.org/drawingml/2006/diagram}dataModel
from _nsgroup import CT_SDCategories # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_SDCategories
from _nsgroup import CT_OrgChart # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_OrgChart
from _nsgroup import ST_OutputShapeType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_OutputShapeType
from _nsgroup import ST_LayoutShapeType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_LayoutShapeType
from _nsgroup import CT_Shape # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Shape
from _nsgroup import CT_Choose # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Choose
from _nsgroup import CT_SDDescription # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_SDDescription
from _nsgroup import CT_Name # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Name
from _nsgroup import CT_Description # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Description
from _nsgroup import ST_HueDir # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_HueDir
from _nsgroup import ST_ClrAppMethod # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ClrAppMethod
from _nsgroup import CT_Colors # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Colors
from _nsgroup import CT_StyleDefinitionHeader # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_StyleDefinitionHeader
from _nsgroup import ST_AlgorithmType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AlgorithmType
from _nsgroup import CT_Algorithm # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Algorithm
from _nsgroup import CT_DiagramDefinitionHeader # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_DiagramDefinitionHeader
from _nsgroup import ST_ModelId # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ModelId
from _nsgroup import ST_CxnType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_CxnType
from _nsgroup import CT_Cxn # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Cxn
from _nsgroup import ST_ConstraintType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ConstraintType
from _nsgroup import ST_ConstraintRelationship # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ConstraintRelationship
from _nsgroup import ST_ElementType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ElementType
from _nsgroup import CT_NumericRule # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_NumericRule
from _nsgroup import ST_AxisType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AxisType
from _nsgroup import ST_AxisTypes # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AxisTypes
from _nsgroup import ST_ElementTypes # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ElementTypes
from _nsgroup import ST_Booleans # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Booleans
from _nsgroup import ST_UnsignedInts # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_UnsignedInts
from _nsgroup import ST_Ints # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Ints
from _nsgroup import CT_ForEach # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ForEach
from _nsgroup import ST_ChildOrderType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ChildOrderType
from _nsgroup import CT_LayoutNode # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_LayoutNode
from _nsgroup import CT_SampleData # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_SampleData
from _nsgroup import CT_Constraints # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Constraints
from _nsgroup import CT_LayoutVariablePropertySet # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_LayoutVariablePropertySet
from _nsgroup import CT_ColorTransformHeader # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ColorTransformHeader
from _nsgroup import CT_RelIds # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_RelIds
from _nsgroup import ST_Index1 # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Index1
from _nsgroup import CT_Adj # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Adj
from _nsgroup import CT_SDCategory # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_SDCategory
from _nsgroup import ST_BoolOperator # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_BoolOperator
from _nsgroup import CT_Constraint # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Constraint
from _nsgroup import CT_DataModel # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_DataModel
from _nsgroup import CT_SDName # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_SDName
from _nsgroup import CT_ElemPropSet # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ElemPropSet
from _nsgroup import CT_Otherwise # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Otherwise
from _nsgroup import CT_CTCategory # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CTCategory
from _nsgroup import ST_ParameterId # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ParameterId
from _nsgroup import ST_DiagramHorizontalAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_DiagramHorizontalAlignment
from _nsgroup import ST_VerticalAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_VerticalAlignment
from _nsgroup import ST_ChildDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ChildDirection
from _nsgroup import ST_ContinueDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ContinueDirection
from _nsgroup import ST_LinearDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_LinearDirection
from _nsgroup import ST_SecondaryLinearDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_SecondaryLinearDirection
from _nsgroup import ST_StartingElement # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_StartingElement
from _nsgroup import ST_SecondaryChildAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_SecondaryChildAlignment
from _nsgroup import ST_CenterShapeMapping # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_CenterShapeMapping
from _nsgroup import ST_BendPoint # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_BendPoint
from _nsgroup import ST_ConnectorRouting # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ConnectorRouting
from _nsgroup import ST_ArrowheadStyle # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ArrowheadStyle
from _nsgroup import ST_ConnectorDimension # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ConnectorDimension
from _nsgroup import ST_ConnectorPoint # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ConnectorPoint
from _nsgroup import ST_NodeHorizontalAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_NodeHorizontalAlignment
from _nsgroup import ST_NodeVerticalAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_NodeVerticalAlignment
from _nsgroup import ST_FallbackDimension # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FallbackDimension
from _nsgroup import ST_TextDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_TextDirection
from _nsgroup import ST_PyramidAccentPosition # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_PyramidAccentPosition
from _nsgroup import ST_RotationPath # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_RotationPath
from _nsgroup import ST_TextBlockDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_TextBlockDirection
from _nsgroup import ST_TextAnchorHorizontal # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_TextAnchorHorizontal
from _nsgroup import ST_TextAnchorVertical # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_TextAnchorVertical
from _nsgroup import ST_DiagramTextAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_DiagramTextAlignment
from _nsgroup import ST_ChildAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ChildAlignment
from _nsgroup import ST_AutoTextRotation # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AutoTextRotation
from _nsgroup import ST_GrowDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_GrowDirection
from _nsgroup import ST_FlowDirection # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FlowDirection
from _nsgroup import ST_Breakpoint # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Breakpoint
from _nsgroup import ST_Offset # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Offset
from _nsgroup import ST_PyramidAccentTextMargin # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_PyramidAccentTextMargin
from _nsgroup import ST_HierarchyAlignment # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_HierarchyAlignment
from _nsgroup import ST_ParameterVal # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ParameterVal
from _nsgroup import CT_Parameter # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Parameter
from _nsgroup import ST_AnimOneStr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AnimOneStr
from _nsgroup import CT_AnimOne # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_AnimOne
from _nsgroup import CT_ColorTransform # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ColorTransform
from _nsgroup import ST_NodeCount # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_NodeCount
from _nsgroup import CT_ChildPref # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ChildPref
from _nsgroup import CT_PresentationOf # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_PresentationOf
from _nsgroup import CT_CTDescription # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CTDescription
from _nsgroup import CT_Rules # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Rules
from _nsgroup import CT_Categories # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Categories
from _nsgroup import ST_ResizeHandlesStr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_ResizeHandlesStr
from _nsgroup import CT_ResizeHandles # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ResizeHandles
from _nsgroup import CT_CTStyleLabel # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CTStyleLabel
from _nsgroup import CT_PtList # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_PtList
from _nsgroup import CT_CxnList # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CxnList
from _nsgroup import CT_Category # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Category
from _nsgroup import CT_StyleDefinitionHeaderLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_StyleDefinitionHeaderLst
from _nsgroup import CT_DiagramDefinitionHeaderLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_DiagramDefinitionHeaderLst
from _nsgroup import CT_AdjLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_AdjLst
from _nsgroup import ST_HierBranchStyle # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_HierBranchStyle
from _nsgroup import ST_Direction # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_Direction
from _nsgroup import ST_AnimLvlStr # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_AnimLvlStr
from _nsgroup import ST_FunctionValue # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FunctionValue
from _nsgroup import ST_VariableType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_VariableType
from _nsgroup import ST_FunctionArgument # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FunctionArgument
from _nsgroup import ST_FunctionType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FunctionType
from _nsgroup import ST_FunctionOperator # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_FunctionOperator
from _nsgroup import CT_When # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_When
from _nsgroup import ST_PtType # {http://schemas.openxmlformats.org/drawingml/2006/diagram}ST_PtType
from _nsgroup import CT_Pt # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Pt
from _nsgroup import CT_CTName # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CTName
from _nsgroup import CT_TextProps # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_TextProps
from _nsgroup import CT_CTCategories # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_CTCategories
from _nsgroup import CT_StyleDefinition # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_StyleDefinition
from _nsgroup import CT_DiagramDefinition # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_DiagramDefinition
from _nsgroup import CT_Direction # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_Direction
from _nsgroup import CT_ChildMax # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ChildMax
from _nsgroup import CT_BulletEnabled # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_BulletEnabled
from _nsgroup import CT_ColorTransformHeaderLst # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_ColorTransformHeaderLst
from _nsgroup import CT_StyleLabel # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_StyleLabel
from _nsgroup import CT_HierBranchStyle # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_HierBranchStyle
from _nsgroup import CT_AnimLvl # {http://schemas.openxmlformats.org/drawingml/2006/diagram}CT_AnimLvl
