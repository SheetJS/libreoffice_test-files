# ./_pmlpicture.py
# PyXB bindings for NamespaceModule
# NSM:09e236dedb7ee667912db7b2d44f5ab054dd995c
# Generated 2010-07-02 14:32:20.414952 by PyXB version 1.1.2
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d927ef8c-85d5-11df-b55a-0026b9799156')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.microsoft.com/office/powerpoint/2010/main', create_if_missing=True)
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


# Complex type CT_RandomId with content type EMPTY
class CT_RandomId (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RandomId')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_microsoft_comofficepowerpoint2010main_CT_RandomId_val', pyxb.binding.datatypes.unsignedInt, required=True)
    
    val = property(__val.value, __val.set, None, None)


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_RandomId', CT_RandomId)


creationId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'creationId'), CT_RandomId)
Namespace.addCategoryObject('elementBinding', creationId.name().localName(), creationId)
