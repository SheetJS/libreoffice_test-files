# ./_pmlcompat.py
# PyXB bindings for NamespaceModule
# NSM:5b75918d653159618fffd6d486a4e307fb5c542b
# Generated 2010-07-02 14:32:20.415101 by PyXB version 1.1.2
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
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/compatibility', create_if_missing=True)
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


# Complex type CT_Compat with content type EMPTY
class CT_Compat (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Compat')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute spid uses Python identifier spid
    __spid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'spid'), 'spid', '__httpschemas_openxmlformats_orgdrawingml2006compatibility_CT_Compat_spid', _nsgroup.ST_ShapeID, required=True)
    
    spid = property(__spid.value, __spid.set, None, u'Shape ID')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __spid.name() : __spid
    }
Namespace.addCategoryObject('typeBinding', u'CT_Compat', CT_Compat)


legacyDrawing = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legacyDrawing'), CT_Compat, documentation=u'Legacy Drawing Object')
Namespace.addCategoryObject('elementBinding', legacyDrawing.name().localName(), legacyDrawing)
