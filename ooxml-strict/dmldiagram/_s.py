# ./_s.py
# PyXB bindings for NamespaceModule
# NSM:61bf325a639b4b55f004401a9008f7f874c77855
# Generated 2010-07-02 14:32:14.161204 by PyXB version 1.1.2
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
import pyxb.binding.datatypes

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/officeDocument/2006/sharedTypes', create_if_missing=True)
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
class ST_Percentage (pyxb.binding.datatypes.string):

    """Percentage Value with Sign"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Percentage')
    _Documentation = u'Percentage Value with Sign'
ST_Percentage._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_Percentage._CF_pattern.addPattern(pattern=u'-?[0-9]+(\\.[0-9]+)?%')
ST_Percentage._InitializeFacetMap(ST_Percentage._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_Percentage', ST_Percentage)

# Atomic SimpleTypeDefinition
class ST_PositiveFixedPercentage (ST_Percentage):

    """Positive Fixed Percentage Value with Sign"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PositiveFixedPercentage')
    _Documentation = u'Positive Fixed Percentage Value with Sign'
ST_PositiveFixedPercentage._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_PositiveFixedPercentage._CF_pattern.addPattern(pattern=u'((100)|([0-9][0-9]?))(\\.[0-9][0-9]?)?%')
ST_PositiveFixedPercentage._InitializeFacetMap(ST_PositiveFixedPercentage._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_PositiveFixedPercentage', ST_PositiveFixedPercentage)

# Atomic SimpleTypeDefinition
class ST_UniversalMeasure (pyxb.binding.datatypes.string):

    """Universal Measurement"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_UniversalMeasure')
    _Documentation = u'Universal Measurement'
ST_UniversalMeasure._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_UniversalMeasure._CF_pattern.addPattern(pattern=u'-?[0-9]+(\\.[0-9]+)?(mm|cm|in|pt|pc|pi)')
ST_UniversalMeasure._InitializeFacetMap(ST_UniversalMeasure._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_UniversalMeasure', ST_UniversalMeasure)

# Atomic SimpleTypeDefinition
class ST_UnsignedDecimalNumber (pyxb.binding.datatypes.unsignedLong):

    """Unsigned Decimal Number Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_UnsignedDecimalNumber')
    _Documentation = u'Unsigned Decimal Number Value'
ST_UnsignedDecimalNumber._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_UnsignedDecimalNumber', ST_UnsignedDecimalNumber)

# Atomic SimpleTypeDefinition
class ST_PositiveUniversalMeasure (ST_UniversalMeasure):

    """Positive Universal Measurement"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PositiveUniversalMeasure')
    _Documentation = u'Positive Universal Measurement'
ST_PositiveUniversalMeasure._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_PositiveUniversalMeasure._CF_pattern.addPattern(pattern=u'[0-9]+(\\.[0-9]+)?(mm|cm|in|pt|pc|pi)')
ST_PositiveUniversalMeasure._InitializeFacetMap(ST_PositiveUniversalMeasure._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_PositiveUniversalMeasure', ST_PositiveUniversalMeasure)

# Union SimpleTypeDefinition
# superclasses pyxb.binding.datatypes.anySimpleType
class ST_TwipsMeasure (pyxb.binding.basis.STD_union):

    """Measurement in Twentieths of a Point"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TwipsMeasure')
    _Documentation = u'Measurement in Twentieths of a Point'

    _MemberTypes = ( ST_UnsignedDecimalNumber, ST_PositiveUniversalMeasure, )
ST_TwipsMeasure._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_TwipsMeasure._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TwipsMeasure)
ST_TwipsMeasure._InitializeFacetMap(ST_TwipsMeasure._CF_pattern,
   ST_TwipsMeasure._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TwipsMeasure', ST_TwipsMeasure)

# Atomic SimpleTypeDefinition
class ST_Xstring (pyxb.binding.datatypes.string):

    """Escaped String"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Xstring')
    _Documentation = u'Escaped String'
ST_Xstring._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_Xstring', ST_Xstring)

# Atomic SimpleTypeDefinition
class ST_OnOff (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """On/Off Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_OnOff')
    _Documentation = u'On/Off Value'
ST_OnOff._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_OnOff, enum_prefix=None)
ST_OnOff.on = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'on')
ST_OnOff.off = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'off')
ST_OnOff.n0 = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'0')
ST_OnOff.n1 = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'1')
ST_OnOff.true = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'true')
ST_OnOff.false = ST_OnOff._CF_enumeration.addEnumeration(unicode_value=u'false')
ST_OnOff._InitializeFacetMap(ST_OnOff._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_OnOff', ST_OnOff)

# Atomic SimpleTypeDefinition
class ST_PositivePercentage (ST_Percentage):

    """Positive Percentage Value with Sign"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PositivePercentage')
    _Documentation = u'Positive Percentage Value with Sign'
ST_PositivePercentage._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_PositivePercentage._CF_pattern.addPattern(pattern=u'[0-9]+(\\.[0-9]+)?%')
ST_PositivePercentage._InitializeFacetMap(ST_PositivePercentage._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_PositivePercentage', ST_PositivePercentage)

# Atomic SimpleTypeDefinition
class ST_YAlign (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Vertical Alignment Location"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_YAlign')
    _Documentation = u'Vertical Alignment Location'
ST_YAlign._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_YAlign, enum_prefix=None)
ST_YAlign.inline = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'inline')
ST_YAlign.top = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'top')
ST_YAlign.center = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'center')
ST_YAlign.bottom = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'bottom')
ST_YAlign.inside = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'inside')
ST_YAlign.outside = ST_YAlign._CF_enumeration.addEnumeration(unicode_value=u'outside')
ST_YAlign._InitializeFacetMap(ST_YAlign._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_YAlign', ST_YAlign)

# Atomic SimpleTypeDefinition
class ST_HexColorRGB (pyxb.binding.datatypes.hexBinary):

    """Hexadecimal Color Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_HexColorRGB')
    _Documentation = u'Hexadecimal Color Value'
ST_HexColorRGB._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
ST_HexColorRGB._InitializeFacetMap(ST_HexColorRGB._CF_length)
Namespace.addCategoryObject('typeBinding', u'ST_HexColorRGB', ST_HexColorRGB)

# Atomic SimpleTypeDefinition
class ST_String (pyxb.binding.datatypes.string):

    """String"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_String')
    _Documentation = u'String'
ST_String._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_String', ST_String)

# Atomic SimpleTypeDefinition
class ST_TrueFalse (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Boolean Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TrueFalse')
    _Documentation = u'Boolean Value'
ST_TrueFalse._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TrueFalse, enum_prefix=None)
ST_TrueFalse.t = ST_TrueFalse._CF_enumeration.addEnumeration(unicode_value=u't')
ST_TrueFalse.f = ST_TrueFalse._CF_enumeration.addEnumeration(unicode_value=u'f')
ST_TrueFalse.true = ST_TrueFalse._CF_enumeration.addEnumeration(unicode_value=u'true')
ST_TrueFalse.false = ST_TrueFalse._CF_enumeration.addEnumeration(unicode_value=u'false')
ST_TrueFalse._InitializeFacetMap(ST_TrueFalse._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TrueFalse', ST_TrueFalse)

# Atomic SimpleTypeDefinition
class ST_Guid (pyxb.binding.datatypes.token):

    """128-Bit GUID"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Guid')
    _Documentation = u'128-Bit GUID'
ST_Guid._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_Guid._CF_pattern.addPattern(pattern=u'\\{[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}\\}')
ST_Guid._InitializeFacetMap(ST_Guid._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_Guid', ST_Guid)

# Atomic SimpleTypeDefinition
class ST_Lang (pyxb.binding.datatypes.string):

    """Language Reference"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Lang')
    _Documentation = u'Language Reference'
ST_Lang._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_Lang', ST_Lang)

# Atomic SimpleTypeDefinition
class ST_Panose (pyxb.binding.datatypes.hexBinary):

    """Panose-1 Number"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Panose')
    _Documentation = u'Panose-1 Number'
ST_Panose._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
ST_Panose._InitializeFacetMap(ST_Panose._CF_length)
Namespace.addCategoryObject('typeBinding', u'ST_Panose', ST_Panose)

# Atomic SimpleTypeDefinition
class ST_FixedPercentage (ST_Percentage):

    """Fixed Percentage Value with Sign"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_FixedPercentage')
    _Documentation = u'Fixed Percentage Value with Sign'
ST_FixedPercentage._CF_pattern = pyxb.binding.facets.CF_pattern()
ST_FixedPercentage._CF_pattern.addPattern(pattern=u'-?((100)|([0-9][0-9]?))(\\.[0-9][0-9]?)?%')
ST_FixedPercentage._InitializeFacetMap(ST_FixedPercentage._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'ST_FixedPercentage', ST_FixedPercentage)

# Atomic SimpleTypeDefinition
class ST_AlgType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Cryptographic Algorithm Types"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AlgType')
    _Documentation = u'Cryptographic Algorithm Types'
ST_AlgType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_AlgType, enum_prefix=None)
ST_AlgType.typeAny = ST_AlgType._CF_enumeration.addEnumeration(unicode_value=u'typeAny')
ST_AlgType.custom = ST_AlgType._CF_enumeration.addEnumeration(unicode_value=u'custom')
ST_AlgType._InitializeFacetMap(ST_AlgType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_AlgType', ST_AlgType)

# Atomic SimpleTypeDefinition
class ST_AlgClass (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Cryptographic Algorithm Classes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AlgClass')
    _Documentation = u'Cryptographic Algorithm Classes'
ST_AlgClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_AlgClass, enum_prefix=None)
ST_AlgClass.hash = ST_AlgClass._CF_enumeration.addEnumeration(unicode_value=u'hash')
ST_AlgClass.custom = ST_AlgClass._CF_enumeration.addEnumeration(unicode_value=u'custom')
ST_AlgClass._InitializeFacetMap(ST_AlgClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_AlgClass', ST_AlgClass)

# Atomic SimpleTypeDefinition
class ST_TrueFalseBlank (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Boolean Value with Blank [False] State"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TrueFalseBlank')
    _Documentation = u'Boolean Value with Blank [False] State'
ST_TrueFalseBlank._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TrueFalseBlank, enum_prefix=None)
ST_TrueFalseBlank.t = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u't')
ST_TrueFalseBlank.f = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'f')
ST_TrueFalseBlank.true = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'true')
ST_TrueFalseBlank.false = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'false')
ST_TrueFalseBlank.emptyString = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'')
ST_TrueFalseBlank.True = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'True')
ST_TrueFalseBlank.False = ST_TrueFalseBlank._CF_enumeration.addEnumeration(unicode_value=u'False')
ST_TrueFalseBlank._InitializeFacetMap(ST_TrueFalseBlank._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TrueFalseBlank', ST_TrueFalseBlank)

# Atomic SimpleTypeDefinition
class ST_XAlign (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Horizontal Alignment Location"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_XAlign')
    _Documentation = u'Horizontal Alignment Location'
ST_XAlign._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_XAlign, enum_prefix=None)
ST_XAlign.left = ST_XAlign._CF_enumeration.addEnumeration(unicode_value=u'left')
ST_XAlign.center = ST_XAlign._CF_enumeration.addEnumeration(unicode_value=u'center')
ST_XAlign.right = ST_XAlign._CF_enumeration.addEnumeration(unicode_value=u'right')
ST_XAlign.inside = ST_XAlign._CF_enumeration.addEnumeration(unicode_value=u'inside')
ST_XAlign.outside = ST_XAlign._CF_enumeration.addEnumeration(unicode_value=u'outside')
ST_XAlign._InitializeFacetMap(ST_XAlign._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_XAlign', ST_XAlign)

# Atomic SimpleTypeDefinition
class ST_ConformanceClass (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Document Conformance Class Value"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ConformanceClass')
    _Documentation = u'Document Conformance Class Value'
ST_ConformanceClass._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_ConformanceClass, enum_prefix=None)
ST_ConformanceClass.strict = ST_ConformanceClass._CF_enumeration.addEnumeration(unicode_value=u'strict')
ST_ConformanceClass.transitional = ST_ConformanceClass._CF_enumeration.addEnumeration(unicode_value=u'transitional')
ST_ConformanceClass._InitializeFacetMap(ST_ConformanceClass._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_ConformanceClass', ST_ConformanceClass)

# Atomic SimpleTypeDefinition
class ST_ColorType (pyxb.binding.datatypes.string):

    """Color Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ColorType')
    _Documentation = u'Color Type'
ST_ColorType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'ST_ColorType', ST_ColorType)

# Atomic SimpleTypeDefinition
class ST_VerticalAlignRun (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Vertical Positioning Location"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_VerticalAlignRun')
    _Documentation = u'Vertical Positioning Location'
ST_VerticalAlignRun._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_VerticalAlignRun, enum_prefix=None)
ST_VerticalAlignRun.baseline = ST_VerticalAlignRun._CF_enumeration.addEnumeration(unicode_value=u'baseline')
ST_VerticalAlignRun.superscript = ST_VerticalAlignRun._CF_enumeration.addEnumeration(unicode_value=u'superscript')
ST_VerticalAlignRun.subscript = ST_VerticalAlignRun._CF_enumeration.addEnumeration(unicode_value=u'subscript')
ST_VerticalAlignRun._InitializeFacetMap(ST_VerticalAlignRun._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_VerticalAlignRun', ST_VerticalAlignRun)

# Atomic SimpleTypeDefinition
class ST_CryptProv (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Cryptographic Provider Types"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_CryptProv')
    _Documentation = u'Cryptographic Provider Types'
ST_CryptProv._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_CryptProv, enum_prefix=None)
ST_CryptProv.rsaAES = ST_CryptProv._CF_enumeration.addEnumeration(unicode_value=u'rsaAES')
ST_CryptProv.rsaFull = ST_CryptProv._CF_enumeration.addEnumeration(unicode_value=u'rsaFull')
ST_CryptProv.custom = ST_CryptProv._CF_enumeration.addEnumeration(unicode_value=u'custom')
ST_CryptProv._InitializeFacetMap(ST_CryptProv._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_CryptProv', ST_CryptProv)

# Atomic SimpleTypeDefinition
class ST_CalendarType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Calendar Types"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_CalendarType')
    _Documentation = u'Calendar Types'
ST_CalendarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_CalendarType, enum_prefix=None)
ST_CalendarType.gregorian = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorian')
ST_CalendarType.gregorianUs = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorianUs')
ST_CalendarType.gregorianMeFrench = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorianMeFrench')
ST_CalendarType.gregorianArabic = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorianArabic')
ST_CalendarType.hijri = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'hijri')
ST_CalendarType.hebrew = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'hebrew')
ST_CalendarType.taiwan = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'taiwan')
ST_CalendarType.japan = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'japan')
ST_CalendarType.thai = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'thai')
ST_CalendarType.korea = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'korea')
ST_CalendarType.saka = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'saka')
ST_CalendarType.gregorianXlitEnglish = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorianXlitEnglish')
ST_CalendarType.gregorianXlitFrench = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'gregorianXlitFrench')
ST_CalendarType.none = ST_CalendarType._CF_enumeration.addEnumeration(unicode_value=u'none')
ST_CalendarType._InitializeFacetMap(ST_CalendarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_CalendarType', ST_CalendarType)
