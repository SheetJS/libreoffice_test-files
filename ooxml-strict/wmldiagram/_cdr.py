# ./_cdr.py
# PyXB bindings for NamespaceModule
# NSM:9fb7786fa089a8a11964db761e62c6c348f9f59c
# Generated 2010-07-02 14:32:29.362835 by PyXB version 1.1.2
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
import pyxb.binding.datatypes
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/chartDrawing', create_if_missing=True)
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


# Atomic SimpleTypeDefinition
class ST_MarkerCoordinate (pyxb.binding.datatypes.double):

    """Chart Marker Coordinate Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_MarkerCoordinate')
    _Documentation = u'Chart Marker Coordinate Value'
ST_MarkerCoordinate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_MarkerCoordinate, value=pyxb.binding.datatypes.double(0.0))
ST_MarkerCoordinate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_MarkerCoordinate, value=pyxb.binding.datatypes.double(1.0))
ST_MarkerCoordinate._InitializeFacetMap(ST_MarkerCoordinate._CF_minInclusive,
   ST_MarkerCoordinate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_MarkerCoordinate', ST_MarkerCoordinate)

# Complex type CT_Shape with content type ELEMENT_ONLY
class CT_Shape (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Shape')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}txBody uses Python identifier txBody
    __txBody = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txBody'), 'txBody', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingtxBody', False)

    
    txBody = property(__txBody.value, __txBody.set, None, u'Shape Text Body')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}nvSpPr uses Python identifier nvSpPr
    __nvSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr'), 'nvSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingnvSpPr', False)

    
    nvSpPr = property(__nvSpPr.value, __nvSpPr.set, None, u'Non-Visual Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, u'Shape Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Shape Properties')

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server')

    
    # Attribute fLocksText uses Python identifier fLocksText
    __fLocksText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fLocksText'), 'fLocksText', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_fLocksText', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    fLocksText = property(__fLocksText.value, __fLocksText.set, None, u'Lock Text')

    
    # Attribute textlink uses Python identifier textlink
    __textlink = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'textlink'), 'textlink', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Shape_textlink', pyxb.binding.datatypes.string)
    
    textlink = property(__textlink.value, __textlink.set, None, u'Text Link')


    _ElementMap = {
        __txBody.name() : __txBody,
        __nvSpPr.name() : __nvSpPr,
        __style.name() : __style,
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished,
        __fLocksText.name() : __fLocksText,
        __textlink.name() : __textlink
    }
Namespace.addCategoryObject('typeBinding', u'CT_Shape', CT_Shape)


# Complex type CT_Marker with content type ELEMENT_ONLY
class CT_Marker (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Marker')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}y uses Python identifier y
    __y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'y'), 'y', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartDrawingy', False)

    
    y = property(__y.value, __y.set, None, u'Relative Y Coordinate')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}x uses Python identifier x
    __x = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'x'), 'x', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartDrawingx', False)

    
    x = property(__x.value, __x.set, None, u'Relative X Coordinate')


    _ElementMap = {
        __y.name() : __y,
        __x.name() : __x
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Marker', CT_Marker)


# Complex type CT_GraphicFrame with content type ELEMENT_ONLY
class CT_GraphicFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GraphicFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/main}graphic uses Python identifier graphic
    __graphic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), 'graphic', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrame_httpschemas_openxmlformats_orgdrawingml2006maingraphic', False)

    
    graphic = property(__graphic.value, __graphic.set, None, u'Graphic Object')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}nvGraphicFramePr uses Python identifier nvGraphicFramePr
    __nvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr'), 'nvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrame_httpschemas_openxmlformats_orgdrawingml2006chartDrawingnvGraphicFramePr', False)

    
    nvGraphicFramePr = property(__nvGraphicFramePr.value, __nvGraphicFramePr.set, None, u'Non-Visual Graphic Frame Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}xfrm uses Python identifier xfrm
    __xfrm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'xfrm'), 'xfrm', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrame_httpschemas_openxmlformats_orgdrawingml2006chartDrawingxfrm', False)

    
    xfrm = property(__xfrm.value, __xfrm.set, None, u'Graphic Frame Transform')

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrame_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrame_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish To Server')


    _ElementMap = {
        __graphic.name() : __graphic,
        __nvGraphicFramePr.name() : __nvGraphicFramePr,
        __xfrm.name() : __xfrm
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished
    }
Namespace.addCategoryObject('typeBinding', u'CT_GraphicFrame', CT_GraphicFrame)


# Complex type CT_AbsSizeAnchor with content type ELEMENT_ONLY
class CT_AbsSizeAnchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AbsSizeAnchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}from uses Python identifier from_
    __from = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingfrom', False)

    
    from_ = property(__from.value, __from.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggrpSp', False)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}ext uses Python identifier ext
    __ext = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ext'), 'ext', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingext', False)

    
    ext = property(__ext.value, __ext.set, None, u'Shape Extent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcxnSp', False)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingsp', False)

    
    sp = property(__sp.value, __sp.set, None, u'Shape Definition')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingpic', False)

    
    pic = property(__pic.value, __pic.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_AbsSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggraphicFrame', False)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')


    _ElementMap = {
        __from.name() : __from,
        __grpSp.name() : __grpSp,
        __ext.name() : __ext,
        __cxnSp.name() : __cxnSp,
        __sp.name() : __sp,
        __pic.name() : __pic,
        __graphicFrame.name() : __graphicFrame
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_AbsSizeAnchor', CT_AbsSizeAnchor)


# Complex type CT_Connector with content type ELEMENT_ONLY
class CT_Connector (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Connector')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006chartDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, u'Connection Shape Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}nvCxnSpPr uses Python identifier nvCxnSpPr
    __nvCxnSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr'), 'nvCxnSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006chartDrawingnvCxnSpPr', False)

    
    nvCxnSpPr = property(__nvCxnSpPr.value, __nvCxnSpPr.set, None, u'Connector Non Visual Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006chartDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Shape Properties')

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Connector_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Connector_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server')


    _ElementMap = {
        __style.name() : __style,
        __nvCxnSpPr.name() : __nvCxnSpPr,
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished
    }
Namespace.addCategoryObject('typeBinding', u'CT_Connector', CT_Connector)


# Complex type CT_GraphicFrameNonVisual with content type ELEMENT_ONLY
class CT_GraphicFrameNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GraphicFrameNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvGraphicFramePr uses Python identifier cNvGraphicFramePr
    __cNvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), 'cNvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrameNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvGraphicFramePr', False)

    
    cNvGraphicFramePr = property(__cNvGraphicFramePr.value, __cNvGraphicFramePr.set, None, u'Non-Visual Graphic Frame Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GraphicFrameNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Non-Visual Drawing Properties')


    _ElementMap = {
        __cNvGraphicFramePr.name() : __cNvGraphicFramePr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GraphicFrameNonVisual', CT_GraphicFrameNonVisual)


# Complex type CT_RelSizeAnchor with content type ELEMENT_ONLY
class CT_RelSizeAnchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RelSizeAnchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingpic', False)

    
    pic = property(__pic.value, __pic.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}from uses Python identifier from_
    __from = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingfrom', False)

    
    from_ = property(__from.value, __from.set, None, u'Starting Anchor Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggrpSp', False)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingsp', False)

    
    sp = property(__sp.value, __sp.set, None, u'Shape Definition')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggraphicFrame', False)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}to uses Python identifier to
    __to = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingto', False)

    
    to = property(__to.value, __to.set, None, u'Ending Anchor Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_RelSizeAnchor_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcxnSp', False)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')


    _ElementMap = {
        __pic.name() : __pic,
        __from.name() : __from,
        __grpSp.name() : __grpSp,
        __sp.name() : __sp,
        __graphicFrame.name() : __graphicFrame,
        __to.name() : __to,
        __cxnSp.name() : __cxnSp
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_RelSizeAnchor', CT_RelSizeAnchor)


# Complex type CT_PictureNonVisual with content type ELEMENT_ONLY
class CT_PictureNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPicPr uses Python identifier cNvPicPr
    __cNvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), 'cNvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPicPr', False)

    
    cNvPicPr = property(__cNvPicPr.value, __cNvPicPr.set, None, u'Non-Visual Picture Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, None)


    _ElementMap = {
        __cNvPicPr.name() : __cNvPicPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureNonVisual', CT_PictureNonVisual)


# Complex type CT_GroupShape with content type ELEMENT_ONLY
class CT_GroupShape (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GroupShape')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}grpSpPr uses Python identifier grpSpPr
    __grpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSpPr'), 'grpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggrpSpPr', False)

    
    grpSpPr = property(__grpSpPr.value, __grpSpPr.set, None, u'Group Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingpic', True)

    
    pic = property(__pic.value, __pic.set, None, u'Picture')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingsp', True)

    
    sp = property(__sp.value, __sp.set, None, u'Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcxnSp', True)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connector Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggrpSp', True)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawinggraphicFrame', True)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}nvGrpSpPr uses Python identifier nvGrpSpPr
    __nvGrpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvGrpSpPr'), 'nvGrpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006chartDrawingnvGrpSpPr', False)

    
    nvGrpSpPr = property(__nvGrpSpPr.value, __nvGrpSpPr.set, None, u'Non-Visual Group Shape Properties')


    _ElementMap = {
        __grpSpPr.name() : __grpSpPr,
        __pic.name() : __pic,
        __sp.name() : __sp,
        __cxnSp.name() : __cxnSp,
        __grpSp.name() : __grpSp,
        __graphicFrame.name() : __graphicFrame,
        __nvGrpSpPr.name() : __nvGrpSpPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GroupShape', CT_GroupShape)


# Complex type CT_ShapeNonVisual with content type ELEMENT_ONLY
class CT_ShapeNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ShapeNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvSpPr uses Python identifier cNvSpPr
    __cNvSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr'), 'cNvSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_ShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvSpPr', False)

    
    cNvSpPr = property(__cNvSpPr.value, __cNvSpPr.set, None, u'Non-Visual Shape Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_ShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Chart Non Visual Properties')


    _ElementMap = {
        __cNvSpPr.name() : __cNvSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ShapeNonVisual', CT_ShapeNonVisual)


# Complex type CT_Picture with content type ELEMENT_ONLY
class CT_Picture (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Picture')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006chartDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}nvPicPr uses Python identifier nvPicPr
    __nvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), 'nvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006chartDrawingnvPicPr', False)

    
    nvPicPr = property(__nvPicPr.value, __nvPicPr.set, None, u'Non-Visual Picture Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}blipFill uses Python identifier blipFill
    __blipFill = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), 'blipFill', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006chartDrawingblipFill', False)

    
    blipFill = property(__blipFill.value, __blipFill.set, None, u'Picture Fill')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006chartDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_macro', pyxb.binding.datatypes.string, unicode_default=u'')
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Picture_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server')


    _ElementMap = {
        __style.name() : __style,
        __nvPicPr.name() : __nvPicPr,
        __blipFill.name() : __blipFill,
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished
    }
Namespace.addCategoryObject('typeBinding', u'CT_Picture', CT_Picture)


# Complex type CT_GroupShapeNonVisual with content type ELEMENT_ONLY
class CT_GroupShapeNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GroupShapeNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvGrpSpPr uses Python identifier cNvGrpSpPr
    __cNvGrpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr'), 'cNvGrpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvGrpSpPr', False)

    
    cNvGrpSpPr = property(__cNvGrpSpPr.value, __cNvGrpSpPr.set, None, u'Non-Visual Group Shape Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_GroupShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Chart Non Visual Properties')


    _ElementMap = {
        __cNvGrpSpPr.name() : __cNvGrpSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GroupShapeNonVisual', CT_GroupShapeNonVisual)


# Complex type CT_ConnectorNonVisual with content type ELEMENT_ONLY
class CT_ConnectorNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ConnectorNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvCxnSpPr uses Python identifier cNvCxnSpPr
    __cNvCxnSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr'), 'cNvCxnSpPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_ConnectorNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvCxnSpPr', False)

    
    cNvCxnSpPr = property(__cNvCxnSpPr.value, __cNvCxnSpPr.set, None, u'Non-Visual Connection Shape Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_ConnectorNonVisual_httpschemas_openxmlformats_orgdrawingml2006chartDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Chart Non Visual Properties')


    _ElementMap = {
        __cNvCxnSpPr.name() : __cNvCxnSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ConnectorNonVisual', CT_ConnectorNonVisual)


# Complex type CT_Drawing with content type ELEMENT_ONLY
class CT_Drawing (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Drawing')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}absSizeAnchor uses Python identifier absSizeAnchor
    __absSizeAnchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'absSizeAnchor'), 'absSizeAnchor', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Drawing_httpschemas_openxmlformats_orgdrawingml2006chartDrawingabsSizeAnchor', True)

    
    absSizeAnchor = property(__absSizeAnchor.value, __absSizeAnchor.set, None, u'Absolute Anchor Shape Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chartDrawing}relSizeAnchor uses Python identifier relSizeAnchor
    __relSizeAnchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'relSizeAnchor'), 'relSizeAnchor', '__httpschemas_openxmlformats_orgdrawingml2006chartDrawing_CT_Drawing_httpschemas_openxmlformats_orgdrawingml2006chartDrawingrelSizeAnchor', True)

    
    relSizeAnchor = property(__relSizeAnchor.value, __relSizeAnchor.set, None, u'Relative Anchor Shape Size')


    _ElementMap = {
        __absSizeAnchor.name() : __absSizeAnchor,
        __relSizeAnchor.name() : __relSizeAnchor
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Drawing', CT_Drawing)




CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txBody'), _nsgroup.CT_TextBody, scope=CT_Shape, documentation=u'Shape Text Body'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr'), CT_ShapeNonVisual, scope=CT_Shape, documentation=u'Non-Visual Shape Properties'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Shape, documentation=u'Shape Style'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Shape, documentation=u'Shape Properties'))
CT_Shape._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txBody')), min_occurs=0L, max_occurs=1L)
    )
CT_Shape._ContentModel = pyxb.binding.content.ParticleModel(CT_Shape._GroupModel, min_occurs=1, max_occurs=1)



CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'y'), ST_MarkerCoordinate, scope=CT_Marker, documentation=u'Relative Y Coordinate'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'x'), ST_MarkerCoordinate, scope=CT_Marker, documentation=u'Relative X Coordinate'))
CT_Marker._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'x')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'y')), min_occurs=1L, max_occurs=1L)
    )
CT_Marker._ContentModel = pyxb.binding.content.ParticleModel(CT_Marker._GroupModel, min_occurs=1, max_occurs=1)



CT_GraphicFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), _nsgroup.CT_GraphicalObject, scope=CT_GraphicFrame, documentation=u'Graphic Object'))

CT_GraphicFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr'), CT_GraphicFrameNonVisual, scope=CT_GraphicFrame, documentation=u'Non-Visual Graphic Frame Properties'))

CT_GraphicFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xfrm'), _nsgroup.CT_Transform2D, scope=CT_GraphicFrame, documentation=u'Graphic Frame Transform'))
CT_GraphicFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GraphicFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xfrm')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic')), min_occurs=1L, max_occurs=1L)
    )
CT_GraphicFrame._ContentModel = pyxb.binding.content.ParticleModel(CT_GraphicFrame._GroupModel, min_occurs=1, max_occurs=1)



CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), CT_Marker, scope=CT_AbsSizeAnchor))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_AbsSizeAnchor, documentation=u'Group Shape'))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ext'), _nsgroup.CT_PositiveSize2D, scope=CT_AbsSizeAnchor, documentation=u'Shape Extent'))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_AbsSizeAnchor, documentation=u'Connection Shape'))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_AbsSizeAnchor, documentation=u'Shape Definition'))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_AbsSizeAnchor))

CT_AbsSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicFrame, scope=CT_AbsSizeAnchor, documentation=u'Graphic Frame'))
CT_AbsSizeAnchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1)
    )
CT_AbsSizeAnchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_AbsSizeAnchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ext')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._GroupModel_, min_occurs=1, max_occurs=1)
    )
CT_AbsSizeAnchor._ContentModel = pyxb.binding.content.ParticleModel(CT_AbsSizeAnchor._GroupModel, min_occurs=1, max_occurs=1)



CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Connector, documentation=u'Connection Shape Style'))

CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr'), CT_ConnectorNonVisual, scope=CT_Connector, documentation=u'Connector Non Visual Properties'))

CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Connector, documentation=u'Shape Properties'))
CT_Connector._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L)
    )
CT_Connector._ContentModel = pyxb.binding.content.ParticleModel(CT_Connector._GroupModel, min_occurs=1, max_occurs=1)



CT_GraphicFrameNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), _nsgroup.CT_NonVisualGraphicFrameProperties, scope=CT_GraphicFrameNonVisual, documentation=u'Non-Visual Graphic Frame Drawing Properties'))

CT_GraphicFrameNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_GraphicFrameNonVisual, documentation=u'Non-Visual Drawing Properties'))
CT_GraphicFrameNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GraphicFrameNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicFrameNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr')), min_occurs=1L, max_occurs=1L)
    )
CT_GraphicFrameNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_GraphicFrameNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_RelSizeAnchor))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), CT_Marker, scope=CT_RelSizeAnchor, documentation=u'Starting Anchor Point'))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_RelSizeAnchor, documentation=u'Group Shape'))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_RelSizeAnchor, documentation=u'Shape Definition'))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicFrame, scope=CT_RelSizeAnchor, documentation=u'Graphic Frame'))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'to'), CT_Marker, scope=CT_RelSizeAnchor, documentation=u'Ending Anchor Point'))

CT_RelSizeAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_RelSizeAnchor, documentation=u'Connection Shape'))
CT_RelSizeAnchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1)
    )
CT_RelSizeAnchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_RelSizeAnchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'to')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._GroupModel_, min_occurs=1, max_occurs=1)
    )
CT_RelSizeAnchor._ContentModel = pyxb.binding.content.ParticleModel(CT_RelSizeAnchor._GroupModel, min_occurs=1, max_occurs=1)



CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), _nsgroup.CT_NonVisualPictureProperties, scope=CT_PictureNonVisual, documentation=u'Non-Visual Picture Drawing Properties'))

CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_PictureNonVisual))
CT_PictureNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr')), min_occurs=1L, max_occurs=1L)
    )
CT_PictureNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_PictureNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSpPr'), _nsgroup.CT_GroupShapeProperties, scope=CT_GroupShape, documentation=u'Group Shape Properties'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_GroupShape, documentation=u'Picture'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_GroupShape, documentation=u'Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_GroupShape, documentation=u'Connector Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_GroupShape, documentation=u'Group Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicFrame, scope=CT_GroupShape, documentation=u'Graphic Frame'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvGrpSpPr'), CT_GroupShapeNonVisual, scope=CT_GroupShape, documentation=u'Non-Visual Group Shape Properties'))
CT_GroupShape._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1)
    )
CT_GroupShape._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvGrpSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GroupShape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GroupShape._GroupModel_, min_occurs=0L, max_occurs=None)
    )
CT_GroupShape._ContentModel = pyxb.binding.content.ParticleModel(CT_GroupShape._GroupModel, min_occurs=1, max_occurs=1)



CT_ShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr'), _nsgroup.CT_NonVisualDrawingShapeProps, scope=CT_ShapeNonVisual, documentation=u'Non-Visual Shape Drawing Properties'))

CT_ShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_ShapeNonVisual, documentation=u'Chart Non Visual Properties'))
CT_ShapeNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_ShapeNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Picture))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), CT_PictureNonVisual, scope=CT_Picture, documentation=u'Non-Visual Picture Properties'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), _nsgroup.CT_BlipFillProperties, scope=CT_Picture, documentation=u'Picture Fill'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Picture))
CT_Picture._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blipFill')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L)
    )
CT_Picture._ContentModel = pyxb.binding.content.ParticleModel(CT_Picture._GroupModel, min_occurs=1, max_occurs=1)



CT_GroupShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr'), _nsgroup.CT_NonVisualGroupDrawingShapeProps, scope=CT_GroupShapeNonVisual, documentation=u'Non-Visual Group Shape Drawing Properties'))

CT_GroupShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_GroupShapeNonVisual, documentation=u'Chart Non Visual Properties'))
CT_GroupShapeNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_GroupShapeNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_ConnectorNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr'), _nsgroup.CT_NonVisualConnectorProperties, scope=CT_ConnectorNonVisual, documentation=u'Non-Visual Connection Shape Drawing Properties'))

CT_ConnectorNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_ConnectorNonVisual, documentation=u'Chart Non Visual Properties'))
CT_ConnectorNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_ConnectorNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absSizeAnchor'), CT_AbsSizeAnchor, scope=CT_Drawing, documentation=u'Absolute Anchor Shape Size'))

CT_Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'relSizeAnchor'), CT_RelSizeAnchor, scope=CT_Drawing, documentation=u'Relative Anchor Shape Size'))
CT_Drawing._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_Drawing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'relSizeAnchor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Drawing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absSizeAnchor')), min_occurs=1, max_occurs=1)
    )
CT_Drawing._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Drawing._GroupModel_, min_occurs=0L, max_occurs=None)
    )
CT_Drawing._ContentModel = pyxb.binding.content.ParticleModel(CT_Drawing._GroupModel, min_occurs=1, max_occurs=1)
