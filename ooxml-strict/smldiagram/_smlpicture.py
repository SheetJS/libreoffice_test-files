# ./_smlpicture.py
# PyXB bindings for NamespaceModule
# NSM:e87e5132fb5d3870b01207fbd5255e29c6c66759
# Generated 2010-07-02 14:32:40.123393 by PyXB version 1.1.2
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

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/picture', create_if_missing=True)
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


# Complex type CT_PictureNonVisual with content type ELEMENT_ONLY
class CT_PictureNonVisual (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureNonVisual')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/picture}cNvPicPr uses Python identifier cNvPicPr
    __cNvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), 'cNvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006picture_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006picturecNvPicPr', False)

    
    cNvPicPr = property(__cNvPicPr.value, __cNvPicPr.set, None, u'Non-Visual Picture Drawing Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/picture}cNvPr uses Python identifier cNvPr
    __cNvPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), 'cNvPr', '__httpschemas_openxmlformats_orgdrawingml2006picture_CT_PictureNonVisual_httpschemas_openxmlformats_orgdrawingml2006picturecNvPr', False)

    
    cNvPr = property(__cNvPr.value, __cNvPr.set, None, u'Non-Visual Drawing Properties')


    _ElementMap = {
        __cNvPicPr.name() : __cNvPicPr,
        __cNvPr.name() : __cNvPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureNonVisual', CT_PictureNonVisual)


# Complex type CT_Picture with content type ELEMENT_ONLY
class CT_Picture (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Picture')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/picture}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006picture_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006picturespPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/picture}nvPicPr uses Python identifier nvPicPr
    __nvPicPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), 'nvPicPr', '__httpschemas_openxmlformats_orgdrawingml2006picture_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006picturenvPicPr', False)

    
    nvPicPr = property(__nvPicPr.value, __nvPicPr.set, None, u'Non-Visual Picture Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/picture}blipFill uses Python identifier blipFill
    __blipFill = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), 'blipFill', '__httpschemas_openxmlformats_orgdrawingml2006picture_CT_Picture_httpschemas_openxmlformats_orgdrawingml2006pictureblipFill', False)

    
    blipFill = property(__blipFill.value, __blipFill.set, None, u'Picture Fill')


    _ElementMap = {
        __spPr.name() : __spPr,
        __nvPicPr.name() : __nvPicPr,
        __blipFill.name() : __blipFill
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Picture', CT_Picture)


pic = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pic'), CT_Picture, documentation=u'Picture')
Namespace.addCategoryObject('elementBinding', pic.name().localName(), pic)



CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr'), _nsgroup.CT_NonVisualPictureProperties, scope=CT_PictureNonVisual, documentation=u'Non-Visual Picture Drawing Properties'))

CT_PictureNonVisual._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cNvPr'), _nsgroup.CT_NonVisualDrawingProps, scope=CT_PictureNonVisual, documentation=u'Non-Visual Drawing Properties'))
CT_PictureNonVisual._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureNonVisual._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cNvPicPr')), min_occurs=1L, max_occurs=1L)
    )
CT_PictureNonVisual._ContentModel = pyxb.binding.content.ParticleModel(CT_PictureNonVisual._GroupModel, min_occurs=1, max_occurs=1)



CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Picture, documentation=u'Shape Properties'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr'), CT_PictureNonVisual, scope=CT_Picture, documentation=u'Non-Visual Picture Properties'))

CT_Picture._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'blipFill'), _nsgroup.CT_BlipFillProperties, scope=CT_Picture, documentation=u'Picture Fill'))
CT_Picture._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'nvPicPr')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'blipFill')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Picture._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=1L, max_occurs=1L)
    )
CT_Picture._ContentModel = pyxb.binding.content.ParticleModel(CT_Picture._GroupModel, min_occurs=1L, max_occurs=1L)
