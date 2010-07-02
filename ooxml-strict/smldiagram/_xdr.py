# ./_xdr.py
# PyXB bindings for NamespaceModule
# NSM:49495484aa854302d08892401f85fced20a7bd90
# Generated 2010-07-02 14:32:40.122779 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e3950400-85d5-11df-91df-0026b9799156')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import _nsgroup
import _r

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing', create_if_missing=True)
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
class ST_ColID (pyxb.binding.datatypes.int):

    """Column ID"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ColID')
    _Documentation = u'Column ID'
ST_ColID._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_ColID, value=pyxb.binding.datatypes.int(0))
ST_ColID._InitializeFacetMap(ST_ColID._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_ColID', ST_ColID)

# Atomic SimpleTypeDefinition
class ST_EditAs (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Resizing Behaviors"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_EditAs')
    _Documentation = u'Resizing Behaviors'
ST_EditAs._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_EditAs, enum_prefix=None)
ST_EditAs.twoCell = ST_EditAs._CF_enumeration.addEnumeration(unicode_value=u'twoCell')
ST_EditAs.oneCell = ST_EditAs._CF_enumeration.addEnumeration(unicode_value=u'oneCell')
ST_EditAs.absolute = ST_EditAs._CF_enumeration.addEnumeration(unicode_value=u'absolute')
ST_EditAs._InitializeFacetMap(ST_EditAs._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_EditAs', ST_EditAs)

# Atomic SimpleTypeDefinition
class ST_RowID (pyxb.binding.datatypes.int):

    """Row ID"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RowID')
    _Documentation = u'Row ID'
ST_RowID._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_RowID, value=pyxb.binding.datatypes.int(0))
ST_RowID._InitializeFacetMap(ST_RowID._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_RowID', ST_RowID)

# Complex type CT_Marker with content type ELEMENT_ONLY
class CT_Marker (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Marker')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}rowOff uses Python identifier rowOff
    __rowOff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rowOff'), 'rowOff', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingrowOff', False)

    
    rowOff = property(__rowOff.value, __rowOff.set, None, u'Row Offset')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}col uses Python identifier col
    __col = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'col'), 'col', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcol', False)

    
    col = property(__col.value, __col.set, None, u'Column)')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}colOff uses Python identifier colOff
    __colOff = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'colOff'), 'colOff', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcolOff', False)

    
    colOff = property(__colOff.value, __colOff.set, None, u'Column Offset')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}row uses Python identifier row
    __row = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'row'), 'row', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingrow', False)

    
    row = property(__row.value, __row.set, None, u'Row')


    _ElementMap = {
        __rowOff.name() : __rowOff,
        __col.name() : __col,
        __colOff.name() : __colOff,
        __row.name() : __row
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Marker', CT_Marker)


# Complex type CT_GroupShape with content type ELEMENT_ONLY
class CT_GroupShape (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GroupShape')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggrpSp', True)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}nvGrpSpPr uses Python identifier nvGrpSpPr
    __nvGrpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvGrpSpPr'), 'nvGrpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingnvGrpSpPr', False)

    
    nvGrpSpPr = property(__nvGrpSpPr.value, __nvGrpSpPr.set, None, u'Non-Visual Properties for a Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcxnSp', True)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggraphicFrame', True)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingpic', True)

    
    pic = property(__pic.value, __pic.set, None, u'Picture')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}grpSpPr uses Python identifier grpSpPr
    __grpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSpPr'), 'grpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggrpSpPr', False)

    
    grpSpPr = property(__grpSpPr.value, __grpSpPr.set, None, u'Group Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingsp', True)

    
    sp = property(__sp.value, __sp.set, None, u'Shape')


    _ElementMap = {
        __grpSp.name() : __grpSp,
        __nvGrpSpPr.name() : __nvGrpSpPr,
        __cxnSp.name() : __cxnSp,
        __graphicFrame.name() : __graphicFrame,
        __pic.name() : __pic,
        __grpSpPr.name() : __grpSpPr,
        __sp.name() : __sp
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GroupShape', CT_GroupShape)


# Complex type CT_AnchorClientData with content type EMPTY
class CT_AnchorClientData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AnchorClientData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute fPrintsWithSheet uses Python identifier fPrintsWithSheet
    __fPrintsWithSheet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPrintsWithSheet'), 'fPrintsWithSheet', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AnchorClientData_fPrintsWithSheet', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    fPrintsWithSheet = property(__fPrintsWithSheet.value, __fPrintsWithSheet.set, None, u'Prints With Sheet Flag')

    
    # Attribute fLocksWithSheet uses Python identifier fLocksWithSheet
    __fLocksWithSheet = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fLocksWithSheet'), 'fLocksWithSheet', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AnchorClientData_fLocksWithSheet', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    fLocksWithSheet = property(__fLocksWithSheet.value, __fLocksWithSheet.set, None, u'Locks With Sheet Flag')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __fPrintsWithSheet.name() : __fPrintsWithSheet,
        __fLocksWithSheet.name() : __fLocksWithSheet
    }
Namespace.addCategoryObject('typeBinding', u'CT_AnchorClientData', CT_AnchorClientData)


# Complex type CT_Shape with content type ELEMENT_ONLY
class CT_Shape (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Shape')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}txBody uses Python identifier txBody
    __txBody = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txBody'), 'txBody', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingtxBody', False)

    
    txBody = property(__txBody.value, __txBody.set, None, u'Shape Text Body')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}nvSpPr uses Python identifier nvSpPr
    __nvSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr'), 'nvSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingnvSpPr', False)

    
    nvSpPr = property(__nvSpPr.value, __nvSpPr.set, None, u'Non-Visual Properties for a Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, None)

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server Flag')

    
    # Attribute fLocksText uses Python identifier fLocksText
    __fLocksText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fLocksText'), 'fLocksText', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_fLocksText', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    fLocksText = property(__fLocksText.value, __fLocksText.set, None, u'Lock Text Flag')

    
    # Attribute textlink uses Python identifier textlink
    __textlink = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'textlink'), 'textlink', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Shape_textlink', pyxb.binding.datatypes.string)
    
    textlink = property(__textlink.value, __textlink.set, None, u'Text Link')


    _ElementMap = {
        __txBody.name() : __txBody,
        __nvSpPr.name() : __nvSpPr,
        __spPr.name() : __spPr,
        __style.name() : __style
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished,
        __fLocksText.name() : __fLocksText,
        __textlink.name() : __textlink
    }
Namespace.addCategoryObject('typeBinding', u'CT_Shape', CT_Shape)


# Complex type CT_Picture with content type ELEMENT_ONLY
class CT_Picture (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Picture')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, u'Shape Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}nvPicPr uses Python identifier nvPicPr
    __nvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), 'nvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingnvPicPr', False)

    
    nvPicPr = property(__nvPicPr.value, __nvPicPr.set, None, u'Non-Visual Properties for a Picture')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}blipFill uses Python identifier blipFill
    __blipFill = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), 'blipFill', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingblipFill', False)

    
    blipFill = property(__blipFill.value, __blipFill.set, None, u'Picture Fill')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_macro', pyxb.binding.datatypes.string, unicode_default=u'')
    
    macro = property(__macro.value, __macro.set, None, u'Reference To Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Picture_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server Flag')


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


# Complex type CT_Connector with content type ELEMENT_ONLY
class CT_Connector (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Connector')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingstyle', False)

    
    style = property(__style.value, __style.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}nvCxnSpPr uses Python identifier nvCxnSpPr
    __nvCxnSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr'), 'nvCxnSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingnvCxnSpPr', False)

    
    nvCxnSpPr = property(__nvCxnSpPr.value, __nvCxnSpPr.set, None, u'Non-Visual Properties for a Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Connector_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Connector Shape Properties')

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Connector_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference to Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Connector_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server Flag')


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


# Complex type CT_OneCellAnchor with content type ELEMENT_ONLY
class CT_OneCellAnchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_OneCellAnchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggrpSp', False)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}from uses Python identifier from_
    __from = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingfrom', False)

    
    from_ = property(__from.value, __from.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}contentPart uses Python identifier contentPart
    __contentPart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), 'contentPart', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcontentPart', False)

    
    contentPart = property(__contentPart.value, __contentPart.set, None, u'Content Part')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggraphicFrame', False)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcxnSp', False)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}clientData uses Python identifier clientData
    __clientData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'clientData'), 'clientData', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingclientData', False)

    
    clientData = property(__clientData.value, __clientData.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingpic', False)

    
    pic = property(__pic.value, __pic.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingsp', False)

    
    sp = property(__sp.value, __sp.set, None, u'Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}ext uses Python identifier ext
    __ext = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ext'), 'ext', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_OneCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingext', False)

    
    ext = property(__ext.value, __ext.set, None, None)


    _ElementMap = {
        __grpSp.name() : __grpSp,
        __from.name() : __from,
        __contentPart.name() : __contentPart,
        __graphicFrame.name() : __graphicFrame,
        __cxnSp.name() : __cxnSp,
        __clientData.name() : __clientData,
        __pic.name() : __pic,
        __sp.name() : __sp,
        __ext.name() : __ext
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_OneCellAnchor', CT_OneCellAnchor)


# Complex type CT_GraphicalObjectFrameNonVisual with content type ELEMENT_ONLY
class CT_GraphicalObjectFrameNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GraphicalObjectFrameNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvGraphicFramePr uses Python identifier cNvGraphicFramePr
    __cNvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), 'cNvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrameNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvGraphicFramePr', False)

    
    cNvGraphicFramePr = property(__cNvGraphicFramePr.value, __cNvGraphicFramePr.set, None, u'Non-Visual Graphic Frame Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrameNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Connection Non-Visual Properties')


    _ElementMap = {
        __cNvGraphicFramePr.name() : __cNvGraphicFramePr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GraphicalObjectFrameNonVisual', CT_GraphicalObjectFrameNonVisual)


# Complex type CT_GroupShapeNonVisual with content type ELEMENT_ONLY
class CT_GroupShapeNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GroupShapeNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvGrpSpPr uses Python identifier cNvGrpSpPr
    __cNvGrpSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr'), 'cNvGrpSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvGrpSpPr', False)

    
    cNvGrpSpPr = property(__cNvGrpSpPr.value, __cNvGrpSpPr.set, None, u'Non-Visual Group Shape Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GroupShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Connection Non-Visual Properties')


    _ElementMap = {
        __cNvGrpSpPr.name() : __cNvGrpSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_GroupShapeNonVisual', CT_GroupShapeNonVisual)


# Complex type CT_Drawing with content type ELEMENT_ONLY
class CT_Drawing (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Drawing')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}absoluteAnchor uses Python identifier absoluteAnchor
    __absoluteAnchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'absoluteAnchor'), 'absoluteAnchor', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Drawing_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingabsoluteAnchor', True)

    
    absoluteAnchor = property(__absoluteAnchor.value, __absoluteAnchor.set, None, u'Absolute Anchor Shape Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}oneCellAnchor uses Python identifier oneCellAnchor
    __oneCellAnchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'oneCellAnchor'), 'oneCellAnchor', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Drawing_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingoneCellAnchor', True)

    
    oneCellAnchor = property(__oneCellAnchor.value, __oneCellAnchor.set, None, u'One Cell Anchor Shape Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}twoCellAnchor uses Python identifier twoCellAnchor
    __twoCellAnchor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'twoCellAnchor'), 'twoCellAnchor', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Drawing_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingtwoCellAnchor', True)

    
    twoCellAnchor = property(__twoCellAnchor.value, __twoCellAnchor.set, None, u'Two Cell Anchor Shape Size')


    _ElementMap = {
        __absoluteAnchor.name() : __absoluteAnchor,
        __oneCellAnchor.name() : __oneCellAnchor,
        __twoCellAnchor.name() : __twoCellAnchor
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Drawing', CT_Drawing)


# Complex type CT_GraphicalObjectFrame with content type ELEMENT_ONLY
class CT_GraphicalObjectFrame (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GraphicalObjectFrame')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/main}graphic uses Python identifier graphic
    __graphic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), 'graphic', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrame_httpschemas_openxmlformats_orgdrawingml2006maingraphic', False)

    
    graphic = property(__graphic.value, __graphic.set, None, u'Graphic Object')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}nvGraphicFramePr uses Python identifier nvGraphicFramePr
    __nvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr'), 'nvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrame_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingnvGraphicFramePr', False)

    
    nvGraphicFramePr = property(__nvGraphicFramePr.value, __nvGraphicFramePr.set, None, u'Non-Visual Properties for a Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}xfrm uses Python identifier xfrm
    __xfrm = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'xfrm'), 'xfrm', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrame_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingxfrm', False)

    
    xfrm = property(__xfrm.value, __xfrm.set, None, u'2D Transform for Graphic Frames')

    
    # Attribute macro uses Python identifier macro
    __macro = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'macro'), 'macro', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrame_macro', pyxb.binding.datatypes.string)
    
    macro = property(__macro.value, __macro.set, None, u'Reference To Custom Function')

    
    # Attribute fPublished uses Python identifier fPublished
    __fPublished = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'fPublished'), 'fPublished', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_GraphicalObjectFrame_fPublished', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    fPublished = property(__fPublished.value, __fPublished.set, None, u'Publish to Server Flag')


    _ElementMap = {
        __graphic.name() : __graphic,
        __nvGraphicFramePr.name() : __nvGraphicFramePr,
        __xfrm.name() : __xfrm
    }
    _AttributeMap = {
        __macro.name() : __macro,
        __fPublished.name() : __fPublished
    }
Namespace.addCategoryObject('typeBinding', u'CT_GraphicalObjectFrame', CT_GraphicalObjectFrame)


# Complex type CT_TwoCellAnchor with content type ELEMENT_ONLY
class CT_TwoCellAnchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TwoCellAnchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}from uses Python identifier from_
    __from = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingfrom', False)

    
    from_ = property(__from.value, __from.set, None, u'Starting Anchor Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}to uses Python identifier to
    __to = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingto', False)

    
    to = property(__to.value, __to.set, None, u'Ending Anchor Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggraphicFrame', False)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcxnSp', False)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}clientData uses Python identifier clientData
    __clientData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'clientData'), 'clientData', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingclientData', False)

    
    clientData = property(__clientData.value, __clientData.set, None, u'Client Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingpic', False)

    
    pic = property(__pic.value, __pic.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggrpSp', False)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}contentPart uses Python identifier contentPart
    __contentPart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), 'contentPart', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcontentPart', False)

    
    contentPart = property(__contentPart.value, __contentPart.set, None, u'Content Part')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingsp', False)

    
    sp = property(__sp.value, __sp.set, None, u'Shape')

    
    # Attribute editAs uses Python identifier editAs
    __editAs = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'editAs'), 'editAs', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_TwoCellAnchor_editAs', ST_EditAs, unicode_default=u'twoCell')
    
    editAs = property(__editAs.value, __editAs.set, None, u'Positioning and Resizing Behaviors')


    _ElementMap = {
        __from.name() : __from,
        __to.name() : __to,
        __graphicFrame.name() : __graphicFrame,
        __cxnSp.name() : __cxnSp,
        __clientData.name() : __clientData,
        __pic.name() : __pic,
        __grpSp.name() : __grpSp,
        __contentPart.name() : __contentPart,
        __sp.name() : __sp
    }
    _AttributeMap = {
        __editAs.name() : __editAs
    }
Namespace.addCategoryObject('typeBinding', u'CT_TwoCellAnchor', CT_TwoCellAnchor)


# Complex type CT_Rel with content type EMPTY
class CT_Rel (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Rel')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://schemas.openxmlformats.org/officeDocument/2006/relationships}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/officeDocument/2006/relationships'), u'id'), 'id', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_Rel_httpschemas_openxmlformats_orgofficeDocument2006relationshipsid', _r.ST_RelationshipId, required=True)
    
    id = property(__id.value, __id.set, None, u'Relationship ID')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'CT_Rel', CT_Rel)


# Complex type CT_PictureNonVisual with content type ELEMENT_ONLY
class CT_PictureNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPicPr uses Python identifier cNvPicPr
    __cNvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), 'cNvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPicPr', False)

    
    cNvPicPr = property(__cNvPicPr.value, __cNvPicPr.set, None, u'Non-Visual Picture Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, None)


    _ElementMap = {
        __cNvPicPr.name() : __cNvPicPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureNonVisual', CT_PictureNonVisual)


# Complex type CT_ShapeNonVisual with content type ELEMENT_ONLY
class CT_ShapeNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ShapeNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvSpPr uses Python identifier cNvSpPr
    __cNvSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr'), 'cNvSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_ShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvSpPr', False)

    
    cNvSpPr = property(__cNvSpPr.value, __cNvSpPr.set, None, u'Connection Non-Visual Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_ShapeNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Non-Visual Drawing Properties')


    _ElementMap = {
        __cNvSpPr.name() : __cNvSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ShapeNonVisual', CT_ShapeNonVisual)


# Complex type CT_AbsoluteAnchor with content type ELEMENT_ONLY
class CT_AbsoluteAnchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AbsoluteAnchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}pos uses Python identifier pos
    __pos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pos'), 'pos', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingpos', False)

    
    pos = property(__pos.value, __pos.set, None, u'Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}graphicFrame uses Python identifier graphicFrame
    __graphicFrame = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), 'graphicFrame', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggraphicFrame', False)

    
    graphicFrame = property(__graphicFrame.value, __graphicFrame.set, None, u'Graphic Frame')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cxnSp uses Python identifier cxnSp
    __cxnSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), 'cxnSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcxnSp', False)

    
    cxnSp = property(__cxnSp.value, __cxnSp.set, None, u'Connection Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}clientData uses Python identifier clientData
    __clientData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'clientData'), 'clientData', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingclientData', False)

    
    clientData = property(__clientData.value, __clientData.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}ext uses Python identifier ext
    __ext = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ext'), 'ext', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingext', False)

    
    ext = property(__ext.value, __ext.set, None, u'Shape Extent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}contentPart uses Python identifier contentPart
    __contentPart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), 'contentPart', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcontentPart', False)

    
    contentPart = property(__contentPart.value, __contentPart.set, None, u'Content Part')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}pic uses Python identifier pic
    __pic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pic'), 'pic', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingpic', False)

    
    pic = property(__pic.value, __pic.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}sp uses Python identifier sp
    __sp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sp'), 'sp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingsp', False)

    
    sp = property(__sp.value, __sp.set, None, u'Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}grpSp uses Python identifier grpSp
    __grpSp = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), 'grpSp', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_AbsoluteAnchor_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawinggrpSp', False)

    
    grpSp = property(__grpSp.value, __grpSp.set, None, u'Group Shape')


    _ElementMap = {
        __pos.name() : __pos,
        __graphicFrame.name() : __graphicFrame,
        __cxnSp.name() : __cxnSp,
        __clientData.name() : __clientData,
        __ext.name() : __ext,
        __contentPart.name() : __contentPart,
        __pic.name() : __pic,
        __sp.name() : __sp,
        __grpSp.name() : __grpSp
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_AbsoluteAnchor', CT_AbsoluteAnchor)


# Complex type CT_ConnectorNonVisual with content type ELEMENT_ONLY
class CT_ConnectorNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ConnectorNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvCxnSpPr uses Python identifier cNvCxnSpPr
    __cNvCxnSpPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr'), 'cNvCxnSpPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_ConnectorNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvCxnSpPr', False)

    
    cNvCxnSpPr = property(__cNvCxnSpPr.value, __cNvCxnSpPr.set, None, u'Non-Visual Connector Shape Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawing_CT_ConnectorNonVisual_httpschemas_openxmlformats_orgdrawingml2006spreadsheetDrawingcNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Connection Non-Visual Properties')


    _ElementMap = {
        __cNvCxnSpPr.name() : __cNvCxnSpPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ConnectorNonVisual', CT_ConnectorNonVisual)


from_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), CT_Marker)
Namespace.addCategoryObject('elementBinding', from_.name().localName(), from_)

wsDr = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wsDr'), CT_Drawing, documentation=u'Worksheet Drawing')
Namespace.addCategoryObject('elementBinding', wsDr.name().localName(), wsDr)

to = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'to'), CT_Marker)
Namespace.addCategoryObject('elementBinding', to.name().localName(), to)



CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rowOff'), _nsgroup.ST_Coordinate, scope=CT_Marker, documentation=u'Row Offset'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'col'), ST_ColID, scope=CT_Marker, documentation=u'Column)'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'colOff'), _nsgroup.ST_Coordinate, scope=CT_Marker, documentation=u'Column Offset'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'row'), ST_RowID, scope=CT_Marker, documentation=u'Row'))
CT_Marker._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'col')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'colOff')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'row')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rowOff')), min_occurs=1, max_occurs=1)
    )
CT_Marker._ContentModel = pyxb.binding.content.ParticleModel(CT_Marker._GroupModel, min_occurs=1, max_occurs=1)



CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_GroupShape, documentation=u'Group Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvGrpSpPr'), CT_GroupShapeNonVisual, scope=CT_GroupShape, documentation=u'Non-Visual Properties for a Group Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_GroupShape, documentation=u'Connection Shape'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicalObjectFrame, scope=CT_GroupShape))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_GroupShape, documentation=u'Picture'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSpPr'), _nsgroup.CT_GroupShapeProperties, scope=CT_GroupShape, documentation=u'Group Shape Properties'))

CT_GroupShape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_GroupShape, documentation=u'Shape'))
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



CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txBody'), _nsgroup.CT_TextBody, scope=CT_Shape, documentation=u'Shape Text Body'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr'), CT_ShapeNonVisual, scope=CT_Shape, documentation=u'Non-Visual Properties for a Shape'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Shape, documentation=u'Shape Properties'))

CT_Shape._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Shape))
CT_Shape._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Shape._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txBody')), min_occurs=0L, max_occurs=1L)
    )
CT_Shape._ContentModel = pyxb.binding.content.ParticleModel(CT_Shape._GroupModel, min_occurs=1, max_occurs=1)



CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Picture, documentation=u'Shape Style'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), CT_PictureNonVisual, scope=CT_Picture, documentation=u'Non-Visual Properties for a Picture'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), _nsgroup.CT_BlipFillProperties, scope=CT_Picture, documentation=u'Picture Fill'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Picture))
CT_Picture._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blipFill')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L)
    )
CT_Picture._ContentModel = pyxb.binding.content.ParticleModel(CT_Picture._GroupModel, min_occurs=1, max_occurs=1)



CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), _nsgroup.CT_ShapeStyle, scope=CT_Connector))

CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr'), CT_ConnectorNonVisual, scope=CT_Connector, documentation=u'Non-Visual Properties for a Connection Shape'))

CT_Connector._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Connector, documentation=u'Connector Shape Properties'))
CT_Connector._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvCxnSpPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Connector._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L)
    )
CT_Connector._ContentModel = pyxb.binding.content.ParticleModel(CT_Connector._GroupModel, min_occurs=1, max_occurs=1)



CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_OneCellAnchor, documentation=u'Group Shape'))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), CT_Marker, scope=CT_OneCellAnchor))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), CT_Rel, scope=CT_OneCellAnchor, documentation=u'Content Part'))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicalObjectFrame, scope=CT_OneCellAnchor, documentation=u'Graphic Frame'))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_OneCellAnchor, documentation=u'Connection Shape'))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clientData'), CT_AnchorClientData, scope=CT_OneCellAnchor))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_OneCellAnchor))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_OneCellAnchor, documentation=u'Shape'))

CT_OneCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ext'), _nsgroup.CT_PositiveSize2D, scope=CT_OneCellAnchor))
CT_OneCellAnchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contentPart')), min_occurs=1, max_occurs=1)
    )
CT_OneCellAnchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_OneCellAnchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ext')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_OneCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clientData')), min_occurs=1L, max_occurs=1L)
    )
CT_OneCellAnchor._ContentModel = pyxb.binding.content.ParticleModel(CT_OneCellAnchor._GroupModel, min_occurs=1, max_occurs=1)



CT_GraphicalObjectFrameNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), _nsgroup.CT_NonVisualGraphicFrameProperties, scope=CT_GraphicalObjectFrameNonVisual, documentation=u'Non-Visual Graphic Frame Drawing Properties'))

CT_GraphicalObjectFrameNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_GraphicalObjectFrameNonVisual, documentation=u'Connection Non-Visual Properties'))
CT_GraphicalObjectFrameNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrameNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrameNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr')), min_occurs=1L, max_occurs=1L)
    )
CT_GraphicalObjectFrameNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrameNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_GroupShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr'), _nsgroup.CT_NonVisualGroupDrawingShapeProps, scope=CT_GroupShapeNonVisual, documentation=u'Non-Visual Group Shape Drawing Properties'))

CT_GroupShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_GroupShapeNonVisual, documentation=u'Connection Non-Visual Properties'))
CT_GroupShapeNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGrpSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_GroupShapeNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_GroupShapeNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'absoluteAnchor'), CT_AbsoluteAnchor, scope=CT_Drawing, documentation=u'Absolute Anchor Shape Size'))

CT_Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'oneCellAnchor'), CT_OneCellAnchor, scope=CT_Drawing, documentation=u'One Cell Anchor Shape Size'))

CT_Drawing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'twoCellAnchor'), CT_TwoCellAnchor, scope=CT_Drawing, documentation=u'Two Cell Anchor Shape Size'))
CT_Drawing._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_Drawing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'twoCellAnchor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Drawing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'oneCellAnchor')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Drawing._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'absoluteAnchor')), min_occurs=1, max_occurs=1)
    )
CT_Drawing._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Drawing._GroupModel_, min_occurs=0L, max_occurs=None)
    )
CT_Drawing._ContentModel = pyxb.binding.content.ParticleModel(CT_Drawing._GroupModel, min_occurs=1, max_occurs=1)



CT_GraphicalObjectFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), _nsgroup.CT_GraphicalObject, scope=CT_GraphicalObjectFrame, documentation=u'Graphic Object'))

CT_GraphicalObjectFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr'), CT_GraphicalObjectFrameNonVisual, scope=CT_GraphicalObjectFrame, documentation=u'Non-Visual Properties for a Graphic Frame'))

CT_GraphicalObjectFrame._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xfrm'), _nsgroup.CT_Transform2D, scope=CT_GraphicalObjectFrame, documentation=u'2D Transform for Graphic Frames'))
CT_GraphicalObjectFrame._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvGraphicFramePr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrame._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xfrm')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrame._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic')), min_occurs=1L, max_occurs=1L)
    )
CT_GraphicalObjectFrame._ContentModel = pyxb.binding.content.ParticleModel(CT_GraphicalObjectFrame._GroupModel, min_occurs=1, max_occurs=1)



CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'from'), CT_Marker, scope=CT_TwoCellAnchor, documentation=u'Starting Anchor Point'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'to'), CT_Marker, scope=CT_TwoCellAnchor, documentation=u'Ending Anchor Point'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicalObjectFrame, scope=CT_TwoCellAnchor, documentation=u'Graphic Frame'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_TwoCellAnchor, documentation=u'Connection Shape'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clientData'), CT_AnchorClientData, scope=CT_TwoCellAnchor, documentation=u'Client Data'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_TwoCellAnchor))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_TwoCellAnchor, documentation=u'Group Shape'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), CT_Rel, scope=CT_TwoCellAnchor, documentation=u'Content Part'))

CT_TwoCellAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_TwoCellAnchor, documentation=u'Shape'))
CT_TwoCellAnchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contentPart')), min_occurs=1, max_occurs=1)
    )
CT_TwoCellAnchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_TwoCellAnchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'from')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'to')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clientData')), min_occurs=1L, max_occurs=1L)
    )
CT_TwoCellAnchor._ContentModel = pyxb.binding.content.ParticleModel(CT_TwoCellAnchor._GroupModel, min_occurs=1, max_occurs=1)



CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), _nsgroup.CT_NonVisualPictureProperties, scope=CT_PictureNonVisual, documentation=u'Non-Visual Picture Drawing Properties'))

CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_PictureNonVisual))
CT_PictureNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr')), min_occurs=1L, max_occurs=1L)
    )
CT_PictureNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_PictureNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_ShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr'), _nsgroup.CT_NonVisualDrawingShapeProps, scope=CT_ShapeNonVisual, documentation=u'Connection Non-Visual Shape Properties'))

CT_ShapeNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_ShapeNonVisual, documentation=u'Non-Visual Drawing Properties'))
CT_ShapeNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_ShapeNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_ShapeNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pos'), _nsgroup.CT_Point2D, scope=CT_AbsoluteAnchor, documentation=u'Position'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame'), CT_GraphicalObjectFrame, scope=CT_AbsoluteAnchor, documentation=u'Graphic Frame'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cxnSp'), CT_Connector, scope=CT_AbsoluteAnchor, documentation=u'Connection Shape'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clientData'), CT_AnchorClientData, scope=CT_AbsoluteAnchor))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ext'), _nsgroup.CT_PositiveSize2D, scope=CT_AbsoluteAnchor, documentation=u'Shape Extent'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'contentPart'), CT_Rel, scope=CT_AbsoluteAnchor, documentation=u'Content Part'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, scope=CT_AbsoluteAnchor))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sp'), CT_Shape, scope=CT_AbsoluteAnchor, documentation=u'Shape'))

CT_AbsoluteAnchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grpSp'), CT_GroupShape, scope=CT_AbsoluteAnchor, documentation=u'Group Shape'))
CT_AbsoluteAnchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grpSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'graphicFrame')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cxnSp')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pic')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'contentPart')), min_occurs=1, max_occurs=1)
    )
CT_AbsoluteAnchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_AbsoluteAnchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ext')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clientData')), min_occurs=1L, max_occurs=1L)
    )
CT_AbsoluteAnchor._ContentModel = pyxb.binding.content.ParticleModel(CT_AbsoluteAnchor._GroupModel, min_occurs=1, max_occurs=1)



CT_ConnectorNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr'), _nsgroup.CT_NonVisualConnectorProperties, scope=CT_ConnectorNonVisual, documentation=u'Non-Visual Connector Shape Drawing Properties'))

CT_ConnectorNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_ConnectorNonVisual, documentation=u'Connection Non-Visual Properties'))
CT_ConnectorNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvCxnSpPr')), min_occurs=1L, max_occurs=1L)
    )
CT_ConnectorNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_ConnectorNonVisual._GroupModel, min_occurs=1, max_occurs=1)
