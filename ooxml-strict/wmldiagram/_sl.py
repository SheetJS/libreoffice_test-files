# ./_sl.py
# PyXB bindings for NamespaceModule
# NSM:d0e3914a078773ab474224ae0ae04d6eeac77a8f
# Generated 2010-07-02 14:32:29.363307 by PyXB version 1.1.2
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

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/schemaLibrary/2006/main', create_if_missing=True)
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


# Complex type CT_Schema with content type EMPTY
class CT_Schema (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Schema')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://schemas.openxmlformats.org/schemaLibrary/2006/main}schemaLanguage uses Python identifier schemaLanguage
    __schemaLanguage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'schemaLanguage'), 'schemaLanguage', '__httpschemas_openxmlformats_orgschemaLibrary2006main_CT_Schema_httpschemas_openxmlformats_orgschemaLibrary2006mainschemaLanguage', pyxb.binding.datatypes.token)
    
    schemaLanguage = property(__schemaLanguage.value, __schemaLanguage.set, None, u'Schema Language')

    
    # Attribute {http://schemas.openxmlformats.org/schemaLibrary/2006/main}uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'uri'), 'uri', '__httpschemas_openxmlformats_orgschemaLibrary2006main_CT_Schema_httpschemas_openxmlformats_orgschemaLibrary2006mainuri', pyxb.binding.datatypes.string, unicode_default=u'')
    
    uri = property(__uri.value, __uri.set, None, u'Custom XML Schema Namespace')

    
    # Attribute {http://schemas.openxmlformats.org/schemaLibrary/2006/main}schemaLocation uses Python identifier schemaLocation
    __schemaLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'schemaLocation'), 'schemaLocation', '__httpschemas_openxmlformats_orgschemaLibrary2006main_CT_Schema_httpschemas_openxmlformats_orgschemaLibrary2006mainschemaLocation', pyxb.binding.datatypes.string)
    
    schemaLocation = property(__schemaLocation.value, __schemaLocation.set, None, u'Custom XML Schema Location')

    
    # Attribute {http://schemas.openxmlformats.org/schemaLibrary/2006/main}manifestLocation uses Python identifier manifestLocation
    __manifestLocation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'manifestLocation'), 'manifestLocation', '__httpschemas_openxmlformats_orgschemaLibrary2006main_CT_Schema_httpschemas_openxmlformats_orgschemaLibrary2006mainmanifestLocation', pyxb.binding.datatypes.string)
    
    manifestLocation = property(__manifestLocation.value, __manifestLocation.set, None, u'Supplementary XML File Location')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __schemaLanguage.name() : __schemaLanguage,
        __uri.name() : __uri,
        __schemaLocation.name() : __schemaLocation,
        __manifestLocation.name() : __manifestLocation
    }
Namespace.addCategoryObject('typeBinding', u'CT_Schema', CT_Schema)


# Complex type CT_SchemaLibrary with content type ELEMENT_ONLY
class CT_SchemaLibrary (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SchemaLibrary')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/schemaLibrary/2006/main}schema uses Python identifier schema
    __schema = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'schema'), 'schema', '__httpschemas_openxmlformats_orgschemaLibrary2006main_CT_SchemaLibrary_httpschemas_openxmlformats_orgschemaLibrary2006mainschema', True)

    
    schema = property(__schema.value, __schema.set, None, u'Custom XML Schema Reference')


    _ElementMap = {
        __schema.name() : __schema
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_SchemaLibrary', CT_SchemaLibrary)


schemaLibrary = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'schemaLibrary'), CT_SchemaLibrary, documentation=u'Embedded Custom XML Schema Supplementary Data')
Namespace.addCategoryObject('elementBinding', schemaLibrary.name().localName(), schemaLibrary)



CT_SchemaLibrary._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'schema'), CT_Schema, scope=CT_SchemaLibrary, documentation=u'Custom XML Schema Reference'))
CT_SchemaLibrary._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SchemaLibrary._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'schema')), min_occurs=0L, max_occurs=None)
    )
CT_SchemaLibrary._ContentModel = pyxb.binding.content.ParticleModel(CT_SchemaLibrary._GroupModel, min_occurs=1, max_occurs=1)
