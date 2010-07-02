# ./_wp.py
# PyXB bindings for NamespaceModule
# NSM:e70a070947c9f7a694110d1ec51c3edad95aec59
# Generated 2010-07-02 14:32:29.364338 by PyXB version 1.1.2
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

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing', create_if_missing=True)
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
class ST_WrapDistance (pyxb.binding.datatypes.unsignedInt):

    """Distance from Text"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_WrapDistance')
    _Documentation = u'Distance from Text'
ST_WrapDistance._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_WrapDistance', ST_WrapDistance)

# Atomic SimpleTypeDefinition
class ST_AlignV (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Vertical Alignment Definition"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AlignV')
    _Documentation = u'Vertical Alignment Definition'
ST_AlignV._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_AlignV, enum_prefix=None)
ST_AlignV.top = ST_AlignV._CF_enumeration.addEnumeration(unicode_value=u'top')
ST_AlignV.bottom = ST_AlignV._CF_enumeration.addEnumeration(unicode_value=u'bottom')
ST_AlignV.center = ST_AlignV._CF_enumeration.addEnumeration(unicode_value=u'center')
ST_AlignV.inside = ST_AlignV._CF_enumeration.addEnumeration(unicode_value=u'inside')
ST_AlignV.outside = ST_AlignV._CF_enumeration.addEnumeration(unicode_value=u'outside')
ST_AlignV._InitializeFacetMap(ST_AlignV._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_AlignV', ST_AlignV)

# Atomic SimpleTypeDefinition
class ST_WrapText (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Text Wrapping Location"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_WrapText')
    _Documentation = u'Text Wrapping Location'
ST_WrapText._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_WrapText, enum_prefix=None)
ST_WrapText.bothSides = ST_WrapText._CF_enumeration.addEnumeration(unicode_value=u'bothSides')
ST_WrapText.left = ST_WrapText._CF_enumeration.addEnumeration(unicode_value=u'left')
ST_WrapText.right = ST_WrapText._CF_enumeration.addEnumeration(unicode_value=u'right')
ST_WrapText.largest = ST_WrapText._CF_enumeration.addEnumeration(unicode_value=u'largest')
ST_WrapText._InitializeFacetMap(ST_WrapText._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_WrapText', ST_WrapText)

# Atomic SimpleTypeDefinition
class ST_PositionOffset (pyxb.binding.datatypes.int):

    """Absolute Position Offset Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PositionOffset')
    _Documentation = u'Absolute Position Offset Value'
ST_PositionOffset._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_PositionOffset', ST_PositionOffset)

# Atomic SimpleTypeDefinition
class ST_RelFromH (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Horizontal Relative Positioning"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RelFromH')
    _Documentation = u'Horizontal Relative Positioning'
ST_RelFromH._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_RelFromH, enum_prefix=None)
ST_RelFromH.margin = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'margin')
ST_RelFromH.page = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'page')
ST_RelFromH.column = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'column')
ST_RelFromH.character = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'character')
ST_RelFromH.leftMargin = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'leftMargin')
ST_RelFromH.rightMargin = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'rightMargin')
ST_RelFromH.insideMargin = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'insideMargin')
ST_RelFromH.outsideMargin = ST_RelFromH._CF_enumeration.addEnumeration(unicode_value=u'outsideMargin')
ST_RelFromH._InitializeFacetMap(ST_RelFromH._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_RelFromH', ST_RelFromH)

# Atomic SimpleTypeDefinition
class ST_AlignH (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Relative Horizontal Alignment Positions"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AlignH')
    _Documentation = u'Relative Horizontal Alignment Positions'
ST_AlignH._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_AlignH, enum_prefix=None)
ST_AlignH.left = ST_AlignH._CF_enumeration.addEnumeration(unicode_value=u'left')
ST_AlignH.right = ST_AlignH._CF_enumeration.addEnumeration(unicode_value=u'right')
ST_AlignH.center = ST_AlignH._CF_enumeration.addEnumeration(unicode_value=u'center')
ST_AlignH.inside = ST_AlignH._CF_enumeration.addEnumeration(unicode_value=u'inside')
ST_AlignH.outside = ST_AlignH._CF_enumeration.addEnumeration(unicode_value=u'outside')
ST_AlignH._InitializeFacetMap(ST_AlignH._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_AlignH', ST_AlignH)

# Atomic SimpleTypeDefinition
class ST_RelFromV (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """Vertical Relative Positioning"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RelFromV')
    _Documentation = u'Vertical Relative Positioning'
ST_RelFromV._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_RelFromV, enum_prefix=None)
ST_RelFromV.margin = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'margin')
ST_RelFromV.page = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'page')
ST_RelFromV.paragraph = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'paragraph')
ST_RelFromV.line = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'line')
ST_RelFromV.topMargin = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'topMargin')
ST_RelFromV.bottomMargin = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'bottomMargin')
ST_RelFromV.insideMargin = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'insideMargin')
ST_RelFromV.outsideMargin = ST_RelFromV._CF_enumeration.addEnumeration(unicode_value=u'outsideMargin')
ST_RelFromV._InitializeFacetMap(ST_RelFromV._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_RelFromV', ST_RelFromV)

# Complex type CT_WrapNone with content type EMPTY
class CT_WrapNone (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapNone')
    # Base type is pyxb.binding.datatypes.anyType

    _ElementMap = {
        
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapNone', CT_WrapNone)


# Complex type CT_Inline with content type ELEMENT_ONLY
class CT_Inline (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Inline')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/main}graphic uses Python identifier graphic
    __graphic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), 'graphic', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_httpschemas_openxmlformats_orgdrawingml2006maingraphic', False)

    
    graphic = property(__graphic.value, __graphic.set, None, u'Graphic Object')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extent'), 'extent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingextent', False)

    
    extent = property(__extent.value, __extent.set, None, u'Drawing Object Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}cNvGraphicFramePr uses Python identifier cNvGraphicFramePr
    __cNvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), 'cNvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingcNvGraphicFramePr', False)

    
    cNvGraphicFramePr = property(__cNvGraphicFramePr.value, __cNvGraphicFramePr.set, None, u'Common DrawingML Non-Visual Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}effectExtent uses Python identifier effectExtent
    __effectExtent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), 'effectExtent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingeffectExtent', False)

    
    effectExtent = property(__effectExtent.value, __effectExtent.set, None, u'Inline Wrapping Extent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr uses Python identifier docPr
    __docPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'docPr'), 'docPr', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingdocPr', False)

    
    docPr = property(__docPr.value, __docPr.set, None, u'Drawing Object Non-Visual Properties')

    
    # Attribute distT uses Python identifier distT
    __distT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distT'), 'distT', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_distT', ST_WrapDistance)
    
    distT = property(__distT.value, __distT.set, None, u'Distance From Text on Top Edge')

    
    # Attribute distR uses Python identifier distR
    __distR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distR'), 'distR', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_distR', ST_WrapDistance)
    
    distR = property(__distR.value, __distR.set, None, u'Distance From Text on Right Edge')

    
    # Attribute distB uses Python identifier distB
    __distB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distB'), 'distB', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_distB', ST_WrapDistance)
    
    distB = property(__distB.value, __distB.set, None, u'Distance From Text on Bottom Edge')

    
    # Attribute distL uses Python identifier distL
    __distL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distL'), 'distL', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Inline_distL', ST_WrapDistance)
    
    distL = property(__distL.value, __distL.set, None, u'Distance From Text on Left Edge')


    _ElementMap = {
        __graphic.name() : __graphic,
        __extent.name() : __extent,
        __cNvGraphicFramePr.name() : __cNvGraphicFramePr,
        __effectExtent.name() : __effectExtent,
        __docPr.name() : __docPr
    }
    _AttributeMap = {
        __distT.name() : __distT,
        __distR.name() : __distR,
        __distB.name() : __distB,
        __distL.name() : __distL
    }
Namespace.addCategoryObject('typeBinding', u'CT_Inline', CT_Inline)


# Complex type CT_WrapPath with content type ELEMENT_ONLY
class CT_WrapPath (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapPath')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}lineTo uses Python identifier lineTo
    __lineTo = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lineTo'), 'lineTo', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapPath_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawinglineTo', True)

    
    lineTo = property(__lineTo.value, __lineTo.set, None, u'Wrapping Polygon Line End Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}start uses Python identifier start
    __start = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'start'), 'start', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapPath_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingstart', False)

    
    start = property(__start.value, __start.set, None, u'Wrapping Polygon Start')

    
    # Attribute edited uses Python identifier edited
    __edited = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'edited'), 'edited', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapPath_edited', pyxb.binding.datatypes.boolean)
    
    edited = property(__edited.value, __edited.set, None, u'Wrapping Points Modified')


    _ElementMap = {
        __lineTo.name() : __lineTo,
        __start.name() : __start
    }
    _AttributeMap = {
        __edited.name() : __edited
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapPath', CT_WrapPath)


# Complex type CT_WrapSquare with content type ELEMENT_ONLY
class CT_WrapSquare (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapSquare')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}effectExtent uses Python identifier effectExtent
    __effectExtent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), 'effectExtent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingeffectExtent', False)

    
    effectExtent = property(__effectExtent.value, __effectExtent.set, None, u'Object Extents Including Effects')

    
    # Attribute wrapText uses Python identifier wrapText
    __wrapText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'wrapText'), 'wrapText', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_wrapText', ST_WrapText, required=True)
    
    wrapText = property(__wrapText.value, __wrapText.set, None, u'Text Wrapping Location')

    
    # Attribute distB uses Python identifier distB
    __distB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distB'), 'distB', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_distB', ST_WrapDistance)
    
    distB = property(__distB.value, __distB.set, None, u'Distance From Text on Bottom Edge')

    
    # Attribute distR uses Python identifier distR
    __distR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distR'), 'distR', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_distR', ST_WrapDistance)
    
    distR = property(__distR.value, __distR.set, None, u'Distance From Text on Right Edge')

    
    # Attribute distL uses Python identifier distL
    __distL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distL'), 'distL', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_distL', ST_WrapDistance)
    
    distL = property(__distL.value, __distL.set, None, u'Distance From Text on Left Edge')

    
    # Attribute distT uses Python identifier distT
    __distT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distT'), 'distT', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapSquare_distT', ST_WrapDistance)
    
    distT = property(__distT.value, __distT.set, None, u'Distance From Text (Top)')


    _ElementMap = {
        __effectExtent.name() : __effectExtent
    }
    _AttributeMap = {
        __wrapText.name() : __wrapText,
        __distB.name() : __distB,
        __distR.name() : __distR,
        __distL.name() : __distL,
        __distT.name() : __distT
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapSquare', CT_WrapSquare)


# Complex type CT_WrapThrough with content type ELEMENT_ONLY
class CT_WrapThrough (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapThrough')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapPolygon uses Python identifier wrapPolygon
    __wrapPolygon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon'), 'wrapPolygon', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapThrough_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapPolygon', False)

    
    wrapPolygon = property(__wrapPolygon.value, __wrapPolygon.set, None, u'Wrapping Polygon')

    
    # Attribute wrapText uses Python identifier wrapText
    __wrapText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'wrapText'), 'wrapText', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapThrough_wrapText', ST_WrapText, required=True)
    
    wrapText = property(__wrapText.value, __wrapText.set, None, u'Text Wrapping Location')

    
    # Attribute distR uses Python identifier distR
    __distR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distR'), 'distR', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapThrough_distR', ST_WrapDistance)
    
    distR = property(__distR.value, __distR.set, None, u'Distance From Text on Right Edge')

    
    # Attribute distL uses Python identifier distL
    __distL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distL'), 'distL', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapThrough_distL', ST_WrapDistance)
    
    distL = property(__distL.value, __distL.set, None, u'Distance From Text on Left Edge')


    _ElementMap = {
        __wrapPolygon.name() : __wrapPolygon
    }
    _AttributeMap = {
        __wrapText.name() : __wrapText,
        __distR.name() : __distR,
        __distL.name() : __distL
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapThrough', CT_WrapThrough)


# Complex type CT_EffectExtent with content type EMPTY
class CT_EffectExtent (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_EffectExtent')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'r'), 'r', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_EffectExtent_r', _nsgroup.ST_Coordinate, required=True)
    
    r = property(__r.value, __r.set, None, u'Additional Extent on Right Edge')

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_EffectExtent_b', _nsgroup.ST_Coordinate, required=True)
    
    b = property(__b.value, __b.set, None, u'Additional Extent on Bottom Edge')

    
    # Attribute t uses Python identifier t
    __t = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't'), 't', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_EffectExtent_t', _nsgroup.ST_Coordinate, required=True)
    
    t = property(__t.value, __t.set, None, u'Additional Extent on Top Edge')

    
    # Attribute l uses Python identifier l
    __l = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'l'), 'l', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_EffectExtent_l', _nsgroup.ST_Coordinate, required=True)
    
    l = property(__l.value, __l.set, None, u'Additional Extent on Left Edge')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __r.name() : __r,
        __b.name() : __b,
        __t.name() : __t,
        __l.name() : __l
    }
Namespace.addCategoryObject('typeBinding', u'CT_EffectExtent', CT_EffectExtent)


# Complex type CT_Anchor with content type ELEMENT_ONLY
class CT_Anchor (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Anchor')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapSquare uses Python identifier wrapSquare
    __wrapSquare = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapSquare'), 'wrapSquare', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapSquare', False)

    
    wrapSquare = property(__wrapSquare.value, __wrapSquare.set, None, u'Square Wrapping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent uses Python identifier extent
    __extent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extent'), 'extent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingextent', False)

    
    extent = property(__extent.value, __extent.set, None, u'Inline Drawing Object Extents')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapTight uses Python identifier wrapTight
    __wrapTight = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapTight'), 'wrapTight', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapTight', False)

    
    wrapTight = property(__wrapTight.value, __wrapTight.set, None, u'Tight Wrapping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapThrough uses Python identifier wrapThrough
    __wrapThrough = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapThrough'), 'wrapThrough', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapThrough', False)

    
    wrapThrough = property(__wrapThrough.value, __wrapThrough.set, None, u'Through Wrapping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}effectExtent uses Python identifier effectExtent
    __effectExtent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), 'effectExtent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingeffectExtent', False)

    
    effectExtent = property(__effectExtent.value, __effectExtent.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}cNvGraphicFramePr uses Python identifier cNvGraphicFramePr
    __cNvGraphicFramePr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), 'cNvGraphicFramePr', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingcNvGraphicFramePr', False)

    
    cNvGraphicFramePr = property(__cNvGraphicFramePr.value, __cNvGraphicFramePr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}simplePos uses Python identifier simplePos
    __simplePos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'simplePos'), 'simplePos', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingsimplePos', False)

    
    simplePos = property(__simplePos.value, __simplePos.set, None, u'Simple Positioning Coordinates')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}docPr uses Python identifier docPr
    __docPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'docPr'), 'docPr', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingdocPr', False)

    
    docPr = property(__docPr.value, __docPr.set, None, u'Drawing Object Non-Visual Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}positionH uses Python identifier positionH
    __positionH = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'positionH'), 'positionH', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingpositionH', False)

    
    positionH = property(__positionH.value, __positionH.set, None, u'Horizontal Positioning')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapNone uses Python identifier wrapNone
    __wrapNone = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapNone'), 'wrapNone', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapNone', False)

    
    wrapNone = property(__wrapNone.value, __wrapNone.set, None, u'No Text Wrapping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/main}graphic uses Python identifier graphic
    __graphic = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), 'graphic', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006maingraphic', False)

    
    graphic = property(__graphic.value, __graphic.set, None, u'Graphic Object')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapTopAndBottom uses Python identifier wrapTopAndBottom
    __wrapTopAndBottom = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapTopAndBottom'), 'wrapTopAndBottom', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapTopAndBottom', False)

    
    wrapTopAndBottom = property(__wrapTopAndBottom.value, __wrapTopAndBottom.set, None, u'Top and Bottom Wrapping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}positionV uses Python identifier positionV
    __positionV = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'positionV'), 'positionV', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingpositionV', False)

    
    positionV = property(__positionV.value, __positionV.set, None, u'Vertical Positioning')

    
    # Attribute locked uses Python identifier locked
    __locked = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locked'), 'locked', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_locked', pyxb.binding.datatypes.boolean, required=True)
    
    locked = property(__locked.value, __locked.set, None, u'Lock Anchor')

    
    # Attribute hidden uses Python identifier hidden
    __hidden = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'hidden'), 'hidden', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_hidden', pyxb.binding.datatypes.boolean)
    
    hidden = property(__hidden.value, __hidden.set, None, u'Hidden')

    
    # Attribute simplePos uses Python identifier simplePos_
    __simplePos_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'simplePos'), 'simplePos_', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_simplePos', pyxb.binding.datatypes.boolean)
    
    simplePos_ = property(__simplePos_.value, __simplePos_.set, None, u'Page Positioning')

    
    # Attribute relativeHeight uses Python identifier relativeHeight
    __relativeHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'relativeHeight'), 'relativeHeight', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_relativeHeight', pyxb.binding.datatypes.unsignedInt, required=True)
    
    relativeHeight = property(__relativeHeight.value, __relativeHeight.set, None, u'Relative Z-Ordering Position')

    
    # Attribute distT uses Python identifier distT
    __distT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distT'), 'distT', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_distT', ST_WrapDistance)
    
    distT = property(__distT.value, __distT.set, None, u'Distance From Text on Top Edge')

    
    # Attribute allowOverlap uses Python identifier allowOverlap
    __allowOverlap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'allowOverlap'), 'allowOverlap', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_allowOverlap', pyxb.binding.datatypes.boolean, required=True)
    
    allowOverlap = property(__allowOverlap.value, __allowOverlap.set, None, u'Allow Objects to Overlap')

    
    # Attribute distB uses Python identifier distB
    __distB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distB'), 'distB', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_distB', ST_WrapDistance)
    
    distB = property(__distB.value, __distB.set, None, u'Distance From Text on Bottom Edge')

    
    # Attribute behindDoc uses Python identifier behindDoc
    __behindDoc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'behindDoc'), 'behindDoc', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_behindDoc', pyxb.binding.datatypes.boolean, required=True)
    
    behindDoc = property(__behindDoc.value, __behindDoc.set, None, u'Display Behind Document Text')

    
    # Attribute distL uses Python identifier distL
    __distL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distL'), 'distL', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_distL', ST_WrapDistance)
    
    distL = property(__distL.value, __distL.set, None, u'Distance From Text on Left Edge')

    
    # Attribute layoutInCell uses Python identifier layoutInCell
    __layoutInCell = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'layoutInCell'), 'layoutInCell', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_layoutInCell', pyxb.binding.datatypes.boolean, required=True)
    
    layoutInCell = property(__layoutInCell.value, __layoutInCell.set, None, u'Layout In Table Cell')

    
    # Attribute distR uses Python identifier distR
    __distR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distR'), 'distR', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_Anchor_distR', ST_WrapDistance)
    
    distR = property(__distR.value, __distR.set, None, u'Distance From Text on Right Edge')


    _ElementMap = {
        __wrapSquare.name() : __wrapSquare,
        __extent.name() : __extent,
        __wrapTight.name() : __wrapTight,
        __wrapThrough.name() : __wrapThrough,
        __effectExtent.name() : __effectExtent,
        __cNvGraphicFramePr.name() : __cNvGraphicFramePr,
        __simplePos.name() : __simplePos,
        __docPr.name() : __docPr,
        __positionH.name() : __positionH,
        __wrapNone.name() : __wrapNone,
        __graphic.name() : __graphic,
        __wrapTopAndBottom.name() : __wrapTopAndBottom,
        __positionV.name() : __positionV
    }
    _AttributeMap = {
        __locked.name() : __locked,
        __hidden.name() : __hidden,
        __simplePos_.name() : __simplePos_,
        __relativeHeight.name() : __relativeHeight,
        __distT.name() : __distT,
        __allowOverlap.name() : __allowOverlap,
        __distB.name() : __distB,
        __behindDoc.name() : __behindDoc,
        __distL.name() : __distL,
        __layoutInCell.name() : __layoutInCell,
        __distR.name() : __distR
    }
Namespace.addCategoryObject('typeBinding', u'CT_Anchor', CT_Anchor)


# Complex type CT_WrapTight with content type ELEMENT_ONLY
class CT_WrapTight (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapTight')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}wrapPolygon uses Python identifier wrapPolygon
    __wrapPolygon = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon'), 'wrapPolygon', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTight_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingwrapPolygon', False)

    
    wrapPolygon = property(__wrapPolygon.value, __wrapPolygon.set, None, u'Tight Wrapping Extents Polygon')

    
    # Attribute wrapText uses Python identifier wrapText
    __wrapText = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'wrapText'), 'wrapText', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTight_wrapText', ST_WrapText, required=True)
    
    wrapText = property(__wrapText.value, __wrapText.set, None, u'Text Wrapping Location')

    
    # Attribute distR uses Python identifier distR
    __distR = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distR'), 'distR', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTight_distR', ST_WrapDistance)
    
    distR = property(__distR.value, __distR.set, None, u'Distance From Text on Right Edge')

    
    # Attribute distL uses Python identifier distL
    __distL = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distL'), 'distL', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTight_distL', ST_WrapDistance)
    
    distL = property(__distL.value, __distL.set, None, u'Distance From Test on Left Edge')


    _ElementMap = {
        __wrapPolygon.name() : __wrapPolygon
    }
    _AttributeMap = {
        __wrapText.name() : __wrapText,
        __distR.name() : __distR,
        __distL.name() : __distL
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapTight', CT_WrapTight)


# Complex type CT_PosH with content type ELEMENT_ONLY
class CT_PosH (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PosH')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}align uses Python identifier align
    __align = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'align'), 'align', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosH_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingalign', False)

    
    align = property(__align.value, __align.set, None, u'Relative Horizontal Alignment')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}posOffset uses Python identifier posOffset
    __posOffset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'posOffset'), 'posOffset', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosH_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingposOffset', False)

    
    posOffset = property(__posOffset.value, __posOffset.set, None, u'Absolute Position Offset')

    
    # Attribute relativeFrom uses Python identifier relativeFrom
    __relativeFrom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'relativeFrom'), 'relativeFrom', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosH_relativeFrom', ST_RelFromH, required=True)
    
    relativeFrom = property(__relativeFrom.value, __relativeFrom.set, None, u'Horizontal Position Relative Base')


    _ElementMap = {
        __align.name() : __align,
        __posOffset.name() : __posOffset
    }
    _AttributeMap = {
        __relativeFrom.name() : __relativeFrom
    }
Namespace.addCategoryObject('typeBinding', u'CT_PosH', CT_PosH)


# Complex type CT_WrapTopBottom with content type ELEMENT_ONLY
class CT_WrapTopBottom (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_WrapTopBottom')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}effectExtent uses Python identifier effectExtent
    __effectExtent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), 'effectExtent', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTopBottom_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingeffectExtent', False)

    
    effectExtent = property(__effectExtent.value, __effectExtent.set, None, u'Wrapping Boundaries')

    
    # Attribute distT uses Python identifier distT
    __distT = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distT'), 'distT', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTopBottom_distT', ST_WrapDistance)
    
    distT = property(__distT.value, __distT.set, None, u'Distance From Text on Top Edge')

    
    # Attribute distB uses Python identifier distB
    __distB = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'distB'), 'distB', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_WrapTopBottom_distB', ST_WrapDistance)
    
    distB = property(__distB.value, __distB.set, None, u'Distance From Text on Bottom Edge')


    _ElementMap = {
        __effectExtent.name() : __effectExtent
    }
    _AttributeMap = {
        __distT.name() : __distT,
        __distB.name() : __distB
    }
Namespace.addCategoryObject('typeBinding', u'CT_WrapTopBottom', CT_WrapTopBottom)


# Complex type CT_PosV with content type ELEMENT_ONLY
class CT_PosV (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PosV')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}align uses Python identifier align
    __align = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'align'), 'align', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosV_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingalign', False)

    
    align = property(__align.value, __align.set, None, u'Relative Vertical Alignment')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}posOffset uses Python identifier posOffset
    __posOffset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'posOffset'), 'posOffset', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosV_httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawingposOffset', False)

    
    posOffset = property(__posOffset.value, __posOffset.set, None, None)

    
    # Attribute relativeFrom uses Python identifier relativeFrom
    __relativeFrom = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'relativeFrom'), 'relativeFrom', '__httpschemas_openxmlformats_orgdrawingml2006wordprocessingDrawing_CT_PosV_relativeFrom', ST_RelFromV, required=True)
    
    relativeFrom = property(__relativeFrom.value, __relativeFrom.set, None, u'Vertical Position Relative Base')


    _ElementMap = {
        __align.name() : __align,
        __posOffset.name() : __posOffset
    }
    _AttributeMap = {
        __relativeFrom.name() : __relativeFrom
    }
Namespace.addCategoryObject('typeBinding', u'CT_PosV', CT_PosV)


inline = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'inline'), CT_Inline, documentation=u'Inline DrawingML Object')
Namespace.addCategoryObject('elementBinding', inline.name().localName(), inline)

anchor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'anchor'), CT_Anchor, documentation=u'Anchor for Floating DrawingML Object')
Namespace.addCategoryObject('elementBinding', anchor.name().localName(), anchor)



CT_Inline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), _nsgroup.CT_GraphicalObject, scope=CT_Inline, documentation=u'Graphic Object'))

CT_Inline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extent'), _nsgroup.CT_PositiveSize2D, scope=CT_Inline, documentation=u'Drawing Object Size'))

CT_Inline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), _nsgroup.CT_NonVisualGraphicFrameProperties, scope=CT_Inline, documentation=u'Common DrawingML Non-Visual Properties'))

CT_Inline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), CT_EffectExtent, scope=CT_Inline, documentation=u'Inline Wrapping Extent'))

CT_Inline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'docPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_Inline, documentation=u'Drawing Object Non-Visual Properties'))
CT_Inline._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Inline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extent')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Inline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectExtent')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Inline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'docPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Inline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Inline._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic')), min_occurs=1L, max_occurs=1L)
    )
CT_Inline._ContentModel = pyxb.binding.content.ParticleModel(CT_Inline._GroupModel, min_occurs=1, max_occurs=1)



CT_WrapPath._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineTo'), _nsgroup.CT_Point2D, scope=CT_WrapPath, documentation=u'Wrapping Polygon Line End Position'))

CT_WrapPath._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'start'), _nsgroup.CT_Point2D, scope=CT_WrapPath, documentation=u'Wrapping Polygon Start'))
CT_WrapPath._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_WrapPath._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'start')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_WrapPath._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineTo')), min_occurs=2L, max_occurs=None)
    )
CT_WrapPath._ContentModel = pyxb.binding.content.ParticleModel(CT_WrapPath._GroupModel, min_occurs=1, max_occurs=1)



CT_WrapSquare._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), CT_EffectExtent, scope=CT_WrapSquare, documentation=u'Object Extents Including Effects'))
CT_WrapSquare._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_WrapSquare._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectExtent')), min_occurs=0L, max_occurs=1)
    )
CT_WrapSquare._ContentModel = pyxb.binding.content.ParticleModel(CT_WrapSquare._GroupModel, min_occurs=1, max_occurs=1)



CT_WrapThrough._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon'), CT_WrapPath, scope=CT_WrapThrough, documentation=u'Wrapping Polygon'))
CT_WrapThrough._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_WrapThrough._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon')), min_occurs=1L, max_occurs=1L)
    )
CT_WrapThrough._ContentModel = pyxb.binding.content.ParticleModel(CT_WrapThrough._GroupModel, min_occurs=1, max_occurs=1)



CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapSquare'), CT_WrapSquare, scope=CT_Anchor, documentation=u'Square Wrapping'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extent'), _nsgroup.CT_PositiveSize2D, scope=CT_Anchor, documentation=u'Inline Drawing Object Extents'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapTight'), CT_WrapTight, scope=CT_Anchor, documentation=u'Tight Wrapping'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapThrough'), CT_WrapThrough, scope=CT_Anchor, documentation=u'Through Wrapping'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), CT_EffectExtent, scope=CT_Anchor))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr'), _nsgroup.CT_NonVisualGraphicFrameProperties, scope=CT_Anchor))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'simplePos'), _nsgroup.CT_Point2D, scope=CT_Anchor, documentation=u'Simple Positioning Coordinates'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'docPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_Anchor, documentation=u'Drawing Object Non-Visual Properties'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'positionH'), CT_PosH, scope=CT_Anchor, documentation=u'Horizontal Positioning'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapNone'), CT_WrapNone, scope=CT_Anchor, documentation=u'No Text Wrapping'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic'), _nsgroup.CT_GraphicalObject, scope=CT_Anchor, documentation=u'Graphic Object'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapTopAndBottom'), CT_WrapTopBottom, scope=CT_Anchor, documentation=u'Top and Bottom Wrapping'))

CT_Anchor._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'positionV'), CT_PosV, scope=CT_Anchor, documentation=u'Vertical Positioning'))
CT_Anchor._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapNone')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapSquare')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapTight')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapThrough')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapTopAndBottom')), min_occurs=1L, max_occurs=1L)
    )
CT_Anchor._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Anchor._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_Anchor._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'simplePos')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'positionH')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'positionV')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extent')), min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectExtent')), min_occurs=0L, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'docPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvGraphicFramePr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Anchor._UseForTag(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main'), u'graphic')), min_occurs=1L, max_occurs=1L)
    )
CT_Anchor._ContentModel = pyxb.binding.content.ParticleModel(CT_Anchor._GroupModel, min_occurs=1, max_occurs=1)



CT_WrapTight._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon'), CT_WrapPath, scope=CT_WrapTight, documentation=u'Tight Wrapping Extents Polygon'))
CT_WrapTight._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_WrapTight._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wrapPolygon')), min_occurs=1L, max_occurs=1L)
    )
CT_WrapTight._ContentModel = pyxb.binding.content.ParticleModel(CT_WrapTight._GroupModel, min_occurs=1, max_occurs=1)



CT_PosH._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'align'), ST_AlignH, scope=CT_PosH, documentation=u'Relative Horizontal Alignment'))

CT_PosH._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'posOffset'), ST_PositionOffset, scope=CT_PosH, documentation=u'Absolute Position Offset'))
CT_PosH._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_PosH._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'align')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PosH._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'posOffset')), min_occurs=1L, max_occurs=1L)
    )
CT_PosH._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PosH._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_PosH._ContentModel = pyxb.binding.content.ParticleModel(CT_PosH._GroupModel, min_occurs=1, max_occurs=1)



CT_WrapTopBottom._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'effectExtent'), CT_EffectExtent, scope=CT_WrapTopBottom, documentation=u'Wrapping Boundaries'))
CT_WrapTopBottom._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_WrapTopBottom._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'effectExtent')), min_occurs=0L, max_occurs=1)
    )
CT_WrapTopBottom._ContentModel = pyxb.binding.content.ParticleModel(CT_WrapTopBottom._GroupModel, min_occurs=1, max_occurs=1)



CT_PosV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'align'), ST_AlignV, scope=CT_PosV, documentation=u'Relative Vertical Alignment'))

CT_PosV._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'posOffset'), ST_PositionOffset, scope=CT_PosV))
CT_PosV._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_PosV._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'align')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PosV._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'posOffset')), min_occurs=1L, max_occurs=1L)
    )
CT_PosV._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PosV._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_PosV._ContentModel = pyxb.binding.content.ParticleModel(CT_PosV._GroupModel, min_occurs=1, max_occurs=1)
