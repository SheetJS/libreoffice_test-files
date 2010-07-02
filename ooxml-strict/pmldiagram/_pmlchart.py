# ./_pmlchart.py
# PyXB bindings for NamespaceModule
# NSM:6081d3567b633d0102a6082d6958cc7332114c3b
# Generated 2010-07-02 14:32:20.414811 by PyXB version 1.1.2
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
import _s
import _nsgroup
import _r
import _cdr

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/chart', create_if_missing=True)
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
class ST_Shape (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Shape"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Shape')
    _Documentation = u'Shape'
ST_Shape._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_Shape, enum_prefix=None)
ST_Shape.cone = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'cone')
ST_Shape.coneToMax = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'coneToMax')
ST_Shape.box = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'box')
ST_Shape.cylinder = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'cylinder')
ST_Shape.pyramid = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'pyramid')
ST_Shape.pyramidToMax = ST_Shape._CF_enumeration.addEnumeration(unicode_value=u'pyramidToMax')
ST_Shape._InitializeFacetMap(ST_Shape._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_Shape', ST_Shape)

# Atomic SimpleTypeDefinition
class ST_Crosses (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Crosses"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Crosses')
    _Documentation = u'Crosses'
ST_Crosses._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_Crosses, enum_prefix=None)
ST_Crosses.autoZero = ST_Crosses._CF_enumeration.addEnumeration(unicode_value=u'autoZero')
ST_Crosses.max = ST_Crosses._CF_enumeration.addEnumeration(unicode_value=u'max')
ST_Crosses.min = ST_Crosses._CF_enumeration.addEnumeration(unicode_value=u'min')
ST_Crosses._InitializeFacetMap(ST_Crosses._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_Crosses', ST_Crosses)

# Atomic SimpleTypeDefinition
class ST_BarDir (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Bar Direction"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_BarDir')
    _Documentation = u'Bar Direction'
ST_BarDir._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_BarDir, enum_prefix=None)
ST_BarDir.bar = ST_BarDir._CF_enumeration.addEnumeration(unicode_value=u'bar')
ST_BarDir.col = ST_BarDir._CF_enumeration.addEnumeration(unicode_value=u'col')
ST_BarDir._InitializeFacetMap(ST_BarDir._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_BarDir', ST_BarDir)

# Atomic SimpleTypeDefinition
class ST_AxisUnit (pyxb.binding.datatypes.double):

    """Axis Unit"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AxisUnit')
    _Documentation = u'Axis Unit'
ST_AxisUnit._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'0'))
ST_AxisUnit._InitializeFacetMap(ST_AxisUnit._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', u'ST_AxisUnit', ST_AxisUnit)

# Atomic SimpleTypeDefinition
class ST_PictureFormat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Picture Format"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PictureFormat')
    _Documentation = u'Picture Format'
ST_PictureFormat._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_PictureFormat, enum_prefix=None)
ST_PictureFormat.stretch = ST_PictureFormat._CF_enumeration.addEnumeration(unicode_value=u'stretch')
ST_PictureFormat.stack = ST_PictureFormat._CF_enumeration.addEnumeration(unicode_value=u'stack')
ST_PictureFormat.stackScale = ST_PictureFormat._CF_enumeration.addEnumeration(unicode_value=u'stackScale')
ST_PictureFormat._InitializeFacetMap(ST_PictureFormat._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_PictureFormat', ST_PictureFormat)

# Atomic SimpleTypeDefinition
class ST_Grouping (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Grouping"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Grouping')
    _Documentation = u'Grouping'
ST_Grouping._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_Grouping, enum_prefix=None)
ST_Grouping.percentStacked = ST_Grouping._CF_enumeration.addEnumeration(unicode_value=u'percentStacked')
ST_Grouping.standard = ST_Grouping._CF_enumeration.addEnumeration(unicode_value=u'standard')
ST_Grouping.stacked = ST_Grouping._CF_enumeration.addEnumeration(unicode_value=u'stacked')
ST_Grouping._InitializeFacetMap(ST_Grouping._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_Grouping', ST_Grouping)

# Atomic SimpleTypeDefinition
class ST_HPercent (pyxb.binding.datatypes.unsignedShort):

    """Height Percent"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_HPercent')
    _Documentation = u'Height Percent'
ST_HPercent._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_HPercent, value=pyxb.binding.datatypes.unsignedShort(500L))
ST_HPercent._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_HPercent, value=pyxb.binding.datatypes.unsignedShort(5L))
ST_HPercent._InitializeFacetMap(ST_HPercent._CF_maxInclusive,
   ST_HPercent._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_HPercent', ST_HPercent)

# Atomic SimpleTypeDefinition
class ST_ErrBarType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Error Bar Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ErrBarType')
    _Documentation = u'Error Bar Type'
ST_ErrBarType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_ErrBarType, enum_prefix=None)
ST_ErrBarType.both = ST_ErrBarType._CF_enumeration.addEnumeration(unicode_value=u'both')
ST_ErrBarType.minus = ST_ErrBarType._CF_enumeration.addEnumeration(unicode_value=u'minus')
ST_ErrBarType.plus = ST_ErrBarType._CF_enumeration.addEnumeration(unicode_value=u'plus')
ST_ErrBarType._InitializeFacetMap(ST_ErrBarType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_ErrBarType', ST_ErrBarType)

# Atomic SimpleTypeDefinition
class ST_TickLblPos (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tick Label Position"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TickLblPos')
    _Documentation = u'Tick Label Position'
ST_TickLblPos._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TickLblPos, enum_prefix=None)
ST_TickLblPos.high = ST_TickLblPos._CF_enumeration.addEnumeration(unicode_value=u'high')
ST_TickLblPos.low = ST_TickLblPos._CF_enumeration.addEnumeration(unicode_value=u'low')
ST_TickLblPos.nextTo = ST_TickLblPos._CF_enumeration.addEnumeration(unicode_value=u'nextTo')
ST_TickLblPos.none = ST_TickLblPos._CF_enumeration.addEnumeration(unicode_value=u'none')
ST_TickLblPos._InitializeFacetMap(ST_TickLblPos._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TickLblPos', ST_TickLblPos)

# Atomic SimpleTypeDefinition
class ST_DLblPos (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Data Label Position"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_DLblPos')
    _Documentation = u'Data Label Position'
ST_DLblPos._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_DLblPos, enum_prefix=None)
ST_DLblPos.bestFit = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'bestFit')
ST_DLblPos.b = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'b')
ST_DLblPos.ctr = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'ctr')
ST_DLblPos.inBase = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'inBase')
ST_DLblPos.inEnd = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'inEnd')
ST_DLblPos.l = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'l')
ST_DLblPos.outEnd = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'outEnd')
ST_DLblPos.r = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u'r')
ST_DLblPos.t = ST_DLblPos._CF_enumeration.addEnumeration(unicode_value=u't')
ST_DLblPos._InitializeFacetMap(ST_DLblPos._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_DLblPos', ST_DLblPos)

# Atomic SimpleTypeDefinition
class ST_LayoutMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Layout Mode"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LayoutMode')
    _Documentation = u'Layout Mode'
ST_LayoutMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_LayoutMode, enum_prefix=None)
ST_LayoutMode.edge = ST_LayoutMode._CF_enumeration.addEnumeration(unicode_value=u'edge')
ST_LayoutMode.factor = ST_LayoutMode._CF_enumeration.addEnumeration(unicode_value=u'factor')
ST_LayoutMode._InitializeFacetMap(ST_LayoutMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_LayoutMode', ST_LayoutMode)

# Atomic SimpleTypeDefinition
class ST_TrendlineType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Trendline Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TrendlineType')
    _Documentation = u'Trendline Type'
ST_TrendlineType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TrendlineType, enum_prefix=None)
ST_TrendlineType.exp = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'exp')
ST_TrendlineType.linear = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'linear')
ST_TrendlineType.log = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'log')
ST_TrendlineType.movingAvg = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'movingAvg')
ST_TrendlineType.poly = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'poly')
ST_TrendlineType.power = ST_TrendlineType._CF_enumeration.addEnumeration(unicode_value=u'power')
ST_TrendlineType._InitializeFacetMap(ST_TrendlineType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TrendlineType', ST_TrendlineType)

# Atomic SimpleTypeDefinition
class ST_LogBase (pyxb.binding.datatypes.double):

    """Logarithmic Base"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LogBase')
    _Documentation = u'Logarithmic Base'
ST_LogBase._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_LogBase, value=pyxb.binding.datatypes.double(1000.0))
ST_LogBase._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_LogBase, value=pyxb.binding.datatypes.double(2.0))
ST_LogBase._InitializeFacetMap(ST_LogBase._CF_maxInclusive,
   ST_LogBase._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_LogBase', ST_LogBase)

# Atomic SimpleTypeDefinition
class ST_BarGrouping (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Bar Grouping"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_BarGrouping')
    _Documentation = u'Bar Grouping'
ST_BarGrouping._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_BarGrouping, enum_prefix=None)
ST_BarGrouping.percentStacked = ST_BarGrouping._CF_enumeration.addEnumeration(unicode_value=u'percentStacked')
ST_BarGrouping.clustered = ST_BarGrouping._CF_enumeration.addEnumeration(unicode_value=u'clustered')
ST_BarGrouping.standard = ST_BarGrouping._CF_enumeration.addEnumeration(unicode_value=u'standard')
ST_BarGrouping.stacked = ST_BarGrouping._CF_enumeration.addEnumeration(unicode_value=u'stacked')
ST_BarGrouping._InitializeFacetMap(ST_BarGrouping._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_BarGrouping', ST_BarGrouping)

# Atomic SimpleTypeDefinition
class ST_FirstSliceAng (pyxb.binding.datatypes.unsignedShort):

    """First Slice Angle"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_FirstSliceAng')
    _Documentation = u'First Slice Angle'
ST_FirstSliceAng._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_FirstSliceAng, value=pyxb.binding.datatypes.unsignedShort(360L))
ST_FirstSliceAng._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_FirstSliceAng, value=pyxb.binding.datatypes.unsignedShort(0L))
ST_FirstSliceAng._InitializeFacetMap(ST_FirstSliceAng._CF_maxInclusive,
   ST_FirstSliceAng._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_FirstSliceAng', ST_FirstSliceAng)

# Atomic SimpleTypeDefinition
class ST_GapAmount (pyxb.binding.datatypes.unsignedShort):

    """Gap Amount"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_GapAmount')
    _Documentation = u'Gap Amount'
ST_GapAmount._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_GapAmount, value=pyxb.binding.datatypes.unsignedShort(500L))
ST_GapAmount._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_GapAmount, value=pyxb.binding.datatypes.unsignedShort(0L))
ST_GapAmount._InitializeFacetMap(ST_GapAmount._CF_maxInclusive,
   ST_GapAmount._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_GapAmount', ST_GapAmount)

# Atomic SimpleTypeDefinition
class ST_RadarStyle (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Radar Style"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RadarStyle')
    _Documentation = u'Radar Style'
ST_RadarStyle._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_RadarStyle, enum_prefix=None)
ST_RadarStyle.standard = ST_RadarStyle._CF_enumeration.addEnumeration(unicode_value=u'standard')
ST_RadarStyle.marker = ST_RadarStyle._CF_enumeration.addEnumeration(unicode_value=u'marker')
ST_RadarStyle.filled = ST_RadarStyle._CF_enumeration.addEnumeration(unicode_value=u'filled')
ST_RadarStyle._InitializeFacetMap(ST_RadarStyle._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_RadarStyle', ST_RadarStyle)

# Atomic SimpleTypeDefinition
class ST_SecondPieSize (pyxb.binding.datatypes.unsignedShort):

    """Second Pie Size"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_SecondPieSize')
    _Documentation = u'Second Pie Size'
ST_SecondPieSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_SecondPieSize, value=pyxb.binding.datatypes.unsignedShort(200L))
ST_SecondPieSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_SecondPieSize, value=pyxb.binding.datatypes.unsignedShort(5L))
ST_SecondPieSize._InitializeFacetMap(ST_SecondPieSize._CF_maxInclusive,
   ST_SecondPieSize._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_SecondPieSize', ST_SecondPieSize)

# Atomic SimpleTypeDefinition
class ST_Skip (pyxb.binding.datatypes.unsignedShort):

    """Skip"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Skip')
    _Documentation = u'Skip'
ST_Skip._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Skip, value=pyxb.binding.datatypes.unsignedShort(1L))
ST_Skip._InitializeFacetMap(ST_Skip._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Skip', ST_Skip)

# Atomic SimpleTypeDefinition
class ST_TickMark (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tick Mark"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TickMark')
    _Documentation = u'Tick Mark'
ST_TickMark._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TickMark, enum_prefix=None)
ST_TickMark.cross = ST_TickMark._CF_enumeration.addEnumeration(unicode_value=u'cross')
ST_TickMark.in_ = ST_TickMark._CF_enumeration.addEnumeration(unicode_value=u'in')
ST_TickMark.none = ST_TickMark._CF_enumeration.addEnumeration(unicode_value=u'none')
ST_TickMark.out = ST_TickMark._CF_enumeration.addEnumeration(unicode_value=u'out')
ST_TickMark._InitializeFacetMap(ST_TickMark._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TickMark', ST_TickMark)

# Atomic SimpleTypeDefinition
class ST_BuiltInUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Built-In Unit"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_BuiltInUnit')
    _Documentation = u'Built-In Unit'
ST_BuiltInUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_BuiltInUnit, enum_prefix=None)
ST_BuiltInUnit.hundreds = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'hundreds')
ST_BuiltInUnit.thousands = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'thousands')
ST_BuiltInUnit.tenThousands = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'tenThousands')
ST_BuiltInUnit.hundredThousands = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'hundredThousands')
ST_BuiltInUnit.millions = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'millions')
ST_BuiltInUnit.tenMillions = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'tenMillions')
ST_BuiltInUnit.hundredMillions = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'hundredMillions')
ST_BuiltInUnit.billions = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'billions')
ST_BuiltInUnit.trillions = ST_BuiltInUnit._CF_enumeration.addEnumeration(unicode_value=u'trillions')
ST_BuiltInUnit._InitializeFacetMap(ST_BuiltInUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_BuiltInUnit', ST_BuiltInUnit)

# Atomic SimpleTypeDefinition
class ST_TimeUnit (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Time Unit"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_TimeUnit')
    _Documentation = u'Time Unit'
ST_TimeUnit._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_TimeUnit, enum_prefix=None)
ST_TimeUnit.days = ST_TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'days')
ST_TimeUnit.months = ST_TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'months')
ST_TimeUnit.years = ST_TimeUnit._CF_enumeration.addEnumeration(unicode_value=u'years')
ST_TimeUnit._InitializeFacetMap(ST_TimeUnit._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_TimeUnit', ST_TimeUnit)

# Atomic SimpleTypeDefinition
class ST_AxPos (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Axis Position"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_AxPos')
    _Documentation = u'Axis Position'
ST_AxPos._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_AxPos, enum_prefix=None)
ST_AxPos.b = ST_AxPos._CF_enumeration.addEnumeration(unicode_value=u'b')
ST_AxPos.l = ST_AxPos._CF_enumeration.addEnumeration(unicode_value=u'l')
ST_AxPos.r = ST_AxPos._CF_enumeration.addEnumeration(unicode_value=u'r')
ST_AxPos.t = ST_AxPos._CF_enumeration.addEnumeration(unicode_value=u't')
ST_AxPos._InitializeFacetMap(ST_AxPos._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_AxPos', ST_AxPos)

# Atomic SimpleTypeDefinition
class ST_BubbleScale (pyxb.binding.datatypes.unsignedInt):

    """Bubble Scale"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_BubbleScale')
    _Documentation = u'Bubble Scale'
ST_BubbleScale._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_BubbleScale, value=pyxb.binding.datatypes.unsignedInt(300L))
ST_BubbleScale._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_BubbleScale, value=pyxb.binding.datatypes.unsignedInt(0L))
ST_BubbleScale._InitializeFacetMap(ST_BubbleScale._CF_maxInclusive,
   ST_BubbleScale._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_BubbleScale', ST_BubbleScale)

# Atomic SimpleTypeDefinition
class ST_ScatterStyle (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Scatter Style"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ScatterStyle')
    _Documentation = u'Scatter Style'
ST_ScatterStyle._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_ScatterStyle, enum_prefix=None)
ST_ScatterStyle.none = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'none')
ST_ScatterStyle.line = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'line')
ST_ScatterStyle.lineMarker = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'lineMarker')
ST_ScatterStyle.marker = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'marker')
ST_ScatterStyle.smooth = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'smooth')
ST_ScatterStyle.smoothMarker = ST_ScatterStyle._CF_enumeration.addEnumeration(unicode_value=u'smoothMarker')
ST_ScatterStyle._InitializeFacetMap(ST_ScatterStyle._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_ScatterStyle', ST_ScatterStyle)

# Atomic SimpleTypeDefinition
class ST_RotX (pyxb.binding.datatypes.byte):

    """X Rotation"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RotX')
    _Documentation = u'X Rotation'
ST_RotX._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_RotX, value=pyxb.binding.datatypes.byte(90))
ST_RotX._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_RotX, value=pyxb.binding.datatypes.byte(-90))
ST_RotX._InitializeFacetMap(ST_RotX._CF_maxInclusive,
   ST_RotX._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_RotX', ST_RotX)

# Atomic SimpleTypeDefinition
class ST_OfPieType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Pie of Pie or Bar of Pie Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_OfPieType')
    _Documentation = u'Pie of Pie or Bar of Pie Type'
ST_OfPieType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_OfPieType, enum_prefix=None)
ST_OfPieType.pie = ST_OfPieType._CF_enumeration.addEnumeration(unicode_value=u'pie')
ST_OfPieType.bar = ST_OfPieType._CF_enumeration.addEnumeration(unicode_value=u'bar')
ST_OfPieType._InitializeFacetMap(ST_OfPieType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_OfPieType', ST_OfPieType)

# Atomic SimpleTypeDefinition
class ST_ErrDir (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Error Bar Direction"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ErrDir')
    _Documentation = u'Error Bar Direction'
ST_ErrDir._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_ErrDir, enum_prefix=None)
ST_ErrDir.x = ST_ErrDir._CF_enumeration.addEnumeration(unicode_value=u'x')
ST_ErrDir.y = ST_ErrDir._CF_enumeration.addEnumeration(unicode_value=u'y')
ST_ErrDir._InitializeFacetMap(ST_ErrDir._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_ErrDir', ST_ErrDir)

# Atomic SimpleTypeDefinition
class ST_MarkerSize (pyxb.binding.datatypes.unsignedByte):

    """Marker Size"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_MarkerSize')
    _Documentation = u'Marker Size'
ST_MarkerSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_MarkerSize, value=pyxb.binding.datatypes.unsignedByte(72L))
ST_MarkerSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_MarkerSize, value=pyxb.binding.datatypes.unsignedByte(2L))
ST_MarkerSize._InitializeFacetMap(ST_MarkerSize._CF_maxInclusive,
   ST_MarkerSize._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_MarkerSize', ST_MarkerSize)

# Atomic SimpleTypeDefinition
class ST_LblOffset (pyxb.binding.datatypes.unsignedShort):

    """Label Offset"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LblOffset')
    _Documentation = u'Label Offset'
ST_LblOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_LblOffset, value=pyxb.binding.datatypes.unsignedShort(1000L))
ST_LblOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_LblOffset, value=pyxb.binding.datatypes.unsignedShort(0L))
ST_LblOffset._InitializeFacetMap(ST_LblOffset._CF_maxInclusive,
   ST_LblOffset._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_LblOffset', ST_LblOffset)

# Atomic SimpleTypeDefinition
class ST_LegendPos (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Legend Position"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LegendPos')
    _Documentation = u'Legend Position'
ST_LegendPos._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_LegendPos, enum_prefix=None)
ST_LegendPos.b = ST_LegendPos._CF_enumeration.addEnumeration(unicode_value=u'b')
ST_LegendPos.tr = ST_LegendPos._CF_enumeration.addEnumeration(unicode_value=u'tr')
ST_LegendPos.l = ST_LegendPos._CF_enumeration.addEnumeration(unicode_value=u'l')
ST_LegendPos.r = ST_LegendPos._CF_enumeration.addEnumeration(unicode_value=u'r')
ST_LegendPos.t = ST_LegendPos._CF_enumeration.addEnumeration(unicode_value=u't')
ST_LegendPos._InitializeFacetMap(ST_LegendPos._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_LegendPos', ST_LegendPos)

# Atomic SimpleTypeDefinition
class ST_PageSetupOrientation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Printed Page Orientation"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PageSetupOrientation')
    _Documentation = u'Printed Page Orientation'
ST_PageSetupOrientation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_PageSetupOrientation, enum_prefix=None)
ST_PageSetupOrientation.default = ST_PageSetupOrientation._CF_enumeration.addEnumeration(unicode_value=u'default')
ST_PageSetupOrientation.portrait = ST_PageSetupOrientation._CF_enumeration.addEnumeration(unicode_value=u'portrait')
ST_PageSetupOrientation.landscape = ST_PageSetupOrientation._CF_enumeration.addEnumeration(unicode_value=u'landscape')
ST_PageSetupOrientation._InitializeFacetMap(ST_PageSetupOrientation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_PageSetupOrientation', ST_PageSetupOrientation)

# Atomic SimpleTypeDefinition
class ST_Period (pyxb.binding.datatypes.unsignedByte):

    """Period"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Period')
    _Documentation = u'Period'
ST_Period._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_Period, value=pyxb.binding.datatypes.unsignedByte(255L))
ST_Period._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Period, value=pyxb.binding.datatypes.unsignedByte(2L))
ST_Period._InitializeFacetMap(ST_Period._CF_maxInclusive,
   ST_Period._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Period', ST_Period)

# Atomic SimpleTypeDefinition
class ST_HoleSize (pyxb.binding.datatypes.unsignedByte):

    """Hole Size"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_HoleSize')
    _Documentation = u'Hole Size'
ST_HoleSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_HoleSize, value=pyxb.binding.datatypes.unsignedByte(90L))
ST_HoleSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_HoleSize, value=pyxb.binding.datatypes.unsignedByte(10L))
ST_HoleSize._InitializeFacetMap(ST_HoleSize._CF_maxInclusive,
   ST_HoleSize._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_HoleSize', ST_HoleSize)

# Atomic SimpleTypeDefinition
class ST_DispBlanksAs (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Display Blanks As"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_DispBlanksAs')
    _Documentation = u'Display Blanks As'
ST_DispBlanksAs._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_DispBlanksAs, enum_prefix=None)
ST_DispBlanksAs.span = ST_DispBlanksAs._CF_enumeration.addEnumeration(unicode_value=u'span')
ST_DispBlanksAs.gap = ST_DispBlanksAs._CF_enumeration.addEnumeration(unicode_value=u'gap')
ST_DispBlanksAs.zero = ST_DispBlanksAs._CF_enumeration.addEnumeration(unicode_value=u'zero')
ST_DispBlanksAs._InitializeFacetMap(ST_DispBlanksAs._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_DispBlanksAs', ST_DispBlanksAs)

# Atomic SimpleTypeDefinition
class ST_SplitType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Split Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_SplitType')
    _Documentation = u'Split Type'
ST_SplitType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_SplitType, enum_prefix=None)
ST_SplitType.auto = ST_SplitType._CF_enumeration.addEnumeration(unicode_value=u'auto')
ST_SplitType.cust = ST_SplitType._CF_enumeration.addEnumeration(unicode_value=u'cust')
ST_SplitType.percent = ST_SplitType._CF_enumeration.addEnumeration(unicode_value=u'percent')
ST_SplitType.pos = ST_SplitType._CF_enumeration.addEnumeration(unicode_value=u'pos')
ST_SplitType.val = ST_SplitType._CF_enumeration.addEnumeration(unicode_value=u'val')
ST_SplitType._InitializeFacetMap(ST_SplitType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_SplitType', ST_SplitType)

# Atomic SimpleTypeDefinition
class ST_SizeRepresents (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Size Represents"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_SizeRepresents')
    _Documentation = u'Size Represents'
ST_SizeRepresents._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_SizeRepresents, enum_prefix=None)
ST_SizeRepresents.area = ST_SizeRepresents._CF_enumeration.addEnumeration(unicode_value=u'area')
ST_SizeRepresents.w = ST_SizeRepresents._CF_enumeration.addEnumeration(unicode_value=u'w')
ST_SizeRepresents._InitializeFacetMap(ST_SizeRepresents._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_SizeRepresents', ST_SizeRepresents)

# Atomic SimpleTypeDefinition
class ST_MarkerStyle (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Marker Style"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_MarkerStyle')
    _Documentation = u'Marker Style'
ST_MarkerStyle._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_MarkerStyle, enum_prefix=None)
ST_MarkerStyle.circle = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'circle')
ST_MarkerStyle.dash = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'dash')
ST_MarkerStyle.diamond = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'diamond')
ST_MarkerStyle.dot = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'dot')
ST_MarkerStyle.none = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'none')
ST_MarkerStyle.picture = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'picture')
ST_MarkerStyle.plus = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'plus')
ST_MarkerStyle.square = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'square')
ST_MarkerStyle.star = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'star')
ST_MarkerStyle.triangle = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'triangle')
ST_MarkerStyle.x = ST_MarkerStyle._CF_enumeration.addEnumeration(unicode_value=u'x')
ST_MarkerStyle._InitializeFacetMap(ST_MarkerStyle._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_MarkerStyle', ST_MarkerStyle)

# Atomic SimpleTypeDefinition
class ST_LblAlgn (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Label Alignment"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LblAlgn')
    _Documentation = u'Label Alignment'
ST_LblAlgn._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_LblAlgn, enum_prefix=None)
ST_LblAlgn.ctr = ST_LblAlgn._CF_enumeration.addEnumeration(unicode_value=u'ctr')
ST_LblAlgn.l = ST_LblAlgn._CF_enumeration.addEnumeration(unicode_value=u'l')
ST_LblAlgn.r = ST_LblAlgn._CF_enumeration.addEnumeration(unicode_value=u'r')
ST_LblAlgn._InitializeFacetMap(ST_LblAlgn._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_LblAlgn', ST_LblAlgn)

# Atomic SimpleTypeDefinition
class ST_LayoutTarget (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Layout Target"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_LayoutTarget')
    _Documentation = u'Layout Target'
ST_LayoutTarget._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_LayoutTarget, enum_prefix=None)
ST_LayoutTarget.inner = ST_LayoutTarget._CF_enumeration.addEnumeration(unicode_value=u'inner')
ST_LayoutTarget.outer = ST_LayoutTarget._CF_enumeration.addEnumeration(unicode_value=u'outer')
ST_LayoutTarget._InitializeFacetMap(ST_LayoutTarget._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_LayoutTarget', ST_LayoutTarget)

# Atomic SimpleTypeDefinition
class ST_DepthPercent (pyxb.binding.datatypes.unsignedShort):

    """Depth Percent"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_DepthPercent')
    _Documentation = u'Depth Percent'
ST_DepthPercent._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_DepthPercent, value=pyxb.binding.datatypes.unsignedShort(2000L))
ST_DepthPercent._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_DepthPercent, value=pyxb.binding.datatypes.unsignedShort(20L))
ST_DepthPercent._InitializeFacetMap(ST_DepthPercent._CF_maxInclusive,
   ST_DepthPercent._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_DepthPercent', ST_DepthPercent)

# Atomic SimpleTypeDefinition
class ST_Style (pyxb.binding.datatypes.unsignedByte):

    """Style"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Style')
    _Documentation = u'Style'
ST_Style._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_Style, value=pyxb.binding.datatypes.unsignedByte(48L))
ST_Style._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Style, value=pyxb.binding.datatypes.unsignedByte(1L))
ST_Style._InitializeFacetMap(ST_Style._CF_maxInclusive,
   ST_Style._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Style', ST_Style)

# Atomic SimpleTypeDefinition
class ST_RotY (pyxb.binding.datatypes.unsignedShort):

    """Y Rotation"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_RotY')
    _Documentation = u'Y Rotation'
ST_RotY._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_RotY, value=pyxb.binding.datatypes.unsignedShort(360L))
ST_RotY._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_RotY, value=pyxb.binding.datatypes.unsignedShort(0L))
ST_RotY._InitializeFacetMap(ST_RotY._CF_maxInclusive,
   ST_RotY._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_RotY', ST_RotY)

# Atomic SimpleTypeDefinition
class ST_ErrValType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Error Value Type"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_ErrValType')
    _Documentation = u'Error Value Type'
ST_ErrValType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_ErrValType, enum_prefix=None)
ST_ErrValType.cust = ST_ErrValType._CF_enumeration.addEnumeration(unicode_value=u'cust')
ST_ErrValType.fixedVal = ST_ErrValType._CF_enumeration.addEnumeration(unicode_value=u'fixedVal')
ST_ErrValType.percentage = ST_ErrValType._CF_enumeration.addEnumeration(unicode_value=u'percentage')
ST_ErrValType.stdDev = ST_ErrValType._CF_enumeration.addEnumeration(unicode_value=u'stdDev')
ST_ErrValType.stdErr = ST_ErrValType._CF_enumeration.addEnumeration(unicode_value=u'stdErr')
ST_ErrValType._InitializeFacetMap(ST_ErrValType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_ErrValType', ST_ErrValType)

# Atomic SimpleTypeDefinition
class ST_Order (pyxb.binding.datatypes.unsignedByte):

    """Order"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Order')
    _Documentation = u'Order'
ST_Order._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_Order, value=pyxb.binding.datatypes.unsignedByte(6L))
ST_Order._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Order, value=pyxb.binding.datatypes.unsignedByte(2L))
ST_Order._InitializeFacetMap(ST_Order._CF_maxInclusive,
   ST_Order._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Order', ST_Order)

# Atomic SimpleTypeDefinition
class ST_Orientation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Orientation"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Orientation')
    _Documentation = u'Orientation'
ST_Orientation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_Orientation, enum_prefix=None)
ST_Orientation.maxMin = ST_Orientation._CF_enumeration.addEnumeration(unicode_value=u'maxMin')
ST_Orientation.minMax = ST_Orientation._CF_enumeration.addEnumeration(unicode_value=u'minMax')
ST_Orientation._InitializeFacetMap(ST_Orientation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_Orientation', ST_Orientation)

# Atomic SimpleTypeDefinition
class ST_PictureStackUnit (pyxb.binding.datatypes.double):

    """Picture Stack Unit"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_PictureStackUnit')
    _Documentation = u'Picture Stack Unit'
ST_PictureStackUnit._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.double, value=pyxb.binding.datatypes.anySimpleType(u'0'))
ST_PictureStackUnit._InitializeFacetMap(ST_PictureStackUnit._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', u'ST_PictureStackUnit', ST_PictureStackUnit)

# Atomic SimpleTypeDefinition
class ST_Overlap (pyxb.binding.datatypes.byte):

    """Overlap"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Overlap')
    _Documentation = u'Overlap'
ST_Overlap._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_Overlap, value=pyxb.binding.datatypes.byte(100))
ST_Overlap._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Overlap, value=pyxb.binding.datatypes.byte(-100))
ST_Overlap._InitializeFacetMap(ST_Overlap._CF_maxInclusive,
   ST_Overlap._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Overlap', ST_Overlap)

# Atomic SimpleTypeDefinition
class ST_CrossBetween (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Cross Between"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_CrossBetween')
    _Documentation = u'Cross Between'
ST_CrossBetween._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=ST_CrossBetween, enum_prefix=None)
ST_CrossBetween.between = ST_CrossBetween._CF_enumeration.addEnumeration(unicode_value=u'between')
ST_CrossBetween.midCat = ST_CrossBetween._CF_enumeration.addEnumeration(unicode_value=u'midCat')
ST_CrossBetween._InitializeFacetMap(ST_CrossBetween._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'ST_CrossBetween', ST_CrossBetween)

# Atomic SimpleTypeDefinition
class ST_Perspective (pyxb.binding.datatypes.unsignedByte):

    """Perspective"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ST_Perspective')
    _Documentation = u'Perspective'
ST_Perspective._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=ST_Perspective, value=pyxb.binding.datatypes.unsignedByte(240L))
ST_Perspective._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=ST_Perspective, value=pyxb.binding.datatypes.unsignedByte(0L))
ST_Perspective._InitializeFacetMap(ST_Perspective._CF_maxInclusive,
   ST_Perspective._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', u'ST_Perspective', ST_Perspective)

# Complex type CT_StrRef with content type ELEMENT_ONLY
class CT_StrRef (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_StrRef')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrRef_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}f uses Python identifier f
    __f = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'f'), 'f', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrRef_httpschemas_openxmlformats_orgdrawingml2006chartf', False)

    
    f = property(__f.value, __f.set, None, u'Formula')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}strCache uses Python identifier strCache
    __strCache = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'strCache'), 'strCache', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrRef_httpschemas_openxmlformats_orgdrawingml2006chartstrCache', False)

    
    strCache = property(__strCache.value, __strCache.set, None, u'String Cache')


    _ElementMap = {
        __extLst.name() : __extLst,
        __f.name() : __f,
        __strCache.name() : __strCache
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_StrRef', CT_StrRef)


# Complex type CT_Boolean with content type EMPTY
class CT_Boolean (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Boolean')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Boolean_val', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    val = property(__val.value, __val.set, None, u'Boolean Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Boolean', CT_Boolean)


# Complex type CT_UnsignedInt with content type EMPTY
class CT_UnsignedInt (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_UnsignedInt')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UnsignedInt_val', pyxb.binding.datatypes.unsignedInt, required=True)
    
    val = property(__val.value, __val.set, None, u'Integer Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_UnsignedInt', CT_UnsignedInt)


# Complex type CT_PieChart with content type ELEMENT_ONLY
class CT_PieChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PieChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Pie Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}firstSliceAng uses Python identifier firstSliceAng
    __firstSliceAng = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng'), 'firstSliceAng', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieChart_httpschemas_openxmlformats_orgdrawingml2006chartfirstSliceAng', False)

    
    firstSliceAng = property(__firstSliceAng.value, __firstSliceAng.set, None, u'First Slice Angle')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)


    _ElementMap = {
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __ser.name() : __ser,
        __firstSliceAng.name() : __firstSliceAng,
        __varyColors.name() : __varyColors
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PieChart', CT_PieChart)


# Complex type CT_SerTx with content type ELEMENT_ONLY
class CT_SerTx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SerTx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}strRef uses Python identifier strRef
    __strRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'strRef'), 'strRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerTx_httpschemas_openxmlformats_orgdrawingml2006chartstrRef', False)

    
    strRef = property(__strRef.value, __strRef.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}v uses Python identifier v
    __v = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'v'), 'v', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerTx_httpschemas_openxmlformats_orgdrawingml2006chartv', False)

    
    v = property(__v.value, __v.set, None, None)


    _ElementMap = {
        __strRef.name() : __strRef,
        __v.name() : __v
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_SerTx', CT_SerTx)


# Complex type CT_ChartLines with content type ELEMENT_ONLY
class CT_ChartLines (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ChartLines')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartLines_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)


    _ElementMap = {
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ChartLines', CT_ChartLines)


# Complex type CT_Shape with content type EMPTY
class CT_Shape (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Shape')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Shape_val', ST_Shape, unicode_default=u'box')
    
    val = property(__val.value, __val.set, None, u'Shape Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Shape', CT_Shape)


# Complex type CT_AxDataSource with content type ELEMENT_ONLY
class CT_AxDataSource (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AxDataSource')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}multiLvlStrRef uses Python identifier multiLvlStrRef
    __multiLvlStrRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrRef'), 'multiLvlStrRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxDataSource_httpschemas_openxmlformats_orgdrawingml2006chartmultiLvlStrRef', False)

    
    multiLvlStrRef = property(__multiLvlStrRef.value, __multiLvlStrRef.set, None, u'Multi Level String Reference')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numRef uses Python identifier numRef
    __numRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numRef'), 'numRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxDataSource_httpschemas_openxmlformats_orgdrawingml2006chartnumRef', False)

    
    numRef = property(__numRef.value, __numRef.set, None, u'Number Reference')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}strLit uses Python identifier strLit
    __strLit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'strLit'), 'strLit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxDataSource_httpschemas_openxmlformats_orgdrawingml2006chartstrLit', False)

    
    strLit = property(__strLit.value, __strLit.set, None, u'String Literal')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}strRef uses Python identifier strRef
    __strRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'strRef'), 'strRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxDataSource_httpschemas_openxmlformats_orgdrawingml2006chartstrRef', False)

    
    strRef = property(__strRef.value, __strRef.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numLit uses Python identifier numLit
    __numLit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numLit'), 'numLit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxDataSource_httpschemas_openxmlformats_orgdrawingml2006chartnumLit', False)

    
    numLit = property(__numLit.value, __numLit.set, None, u'Number Literal')


    _ElementMap = {
        __multiLvlStrRef.name() : __multiLvlStrRef,
        __numRef.name() : __numRef,
        __strLit.name() : __strLit,
        __strRef.name() : __strRef,
        __numLit.name() : __numLit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_AxDataSource', CT_AxDataSource)


# Complex type CT_DPt with content type ELEMENT_ONLY
class CT_DPt (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DPt')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}invertIfNegative uses Python identifier invertIfNegative
    __invertIfNegative = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), 'invertIfNegative', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartinvertIfNegative', False)

    
    invertIfNegative = property(__invertIfNegative.value, __invertIfNegative.set, None, u'Invert if Negative')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubble3D uses Python identifier bubble3D
    __bubble3D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), 'bubble3D', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartbubble3D', False)

    
    bubble3D = property(__bubble3D.value, __bubble3D.set, None, u'3D Bubble')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}explosion uses Python identifier explosion
    __explosion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'explosion'), 'explosion', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartexplosion', False)

    
    explosion = property(__explosion.value, __explosion.set, None, u'Explosion')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureOptions uses Python identifier pictureOptions
    __pictureOptions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), 'pictureOptions', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DPt_httpschemas_openxmlformats_orgdrawingml2006chartpictureOptions', False)

    
    pictureOptions = property(__pictureOptions.value, __pictureOptions.set, None, None)


    _ElementMap = {
        __invertIfNegative.name() : __invertIfNegative,
        __idx.name() : __idx,
        __marker.name() : __marker,
        __bubble3D.name() : __bubble3D,
        __extLst.name() : __extLst,
        __explosion.name() : __explosion,
        __spPr.name() : __spPr,
        __pictureOptions.name() : __pictureOptions
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DPt', CT_DPt)


# Complex type CT_NumData with content type ELEMENT_ONLY
class CT_NumData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_NumData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumData_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}formatCode uses Python identifier formatCode
    __formatCode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'formatCode'), 'formatCode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumData_httpschemas_openxmlformats_orgdrawingml2006chartformatCode', False)

    
    formatCode = property(__formatCode.value, __formatCode.set, None, u'Format Code')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pt uses Python identifier pt
    __pt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pt'), 'pt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumData_httpschemas_openxmlformats_orgdrawingml2006chartpt', True)

    
    pt = property(__pt.value, __pt.set, None, u'Numeric Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ptCount uses Python identifier ptCount
    __ptCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), 'ptCount', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumData_httpschemas_openxmlformats_orgdrawingml2006chartptCount', False)

    
    ptCount = property(__ptCount.value, __ptCount.set, None, u'Point Count')


    _ElementMap = {
        __extLst.name() : __extLst,
        __formatCode.name() : __formatCode,
        __pt.name() : __pt,
        __ptCount.name() : __ptCount
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_NumData', CT_NumData)


# Complex type CT_DLbls with content type ELEMENT_ONLY
class CT_DLbls (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DLbls')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbl uses Python identifier dLbl
    __dLbl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbl'), 'dLbl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartdLbl', True)

    
    dLbl = property(__dLbl.value, __dLbl.set, None, u'Data Label')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showCatName uses Python identifier showCatName
    __showCatName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showCatName'), 'showCatName', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowCatName', False)

    
    showCatName = property(__showCatName.value, __showCatName.set, None, u'Show Category Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showSerName uses Python identifier showSerName
    __showSerName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showSerName'), 'showSerName', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowSerName', False)

    
    showSerName = property(__showSerName.value, __showSerName.set, None, u'Show Series Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLblPos uses Python identifier dLblPos
    __dLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLblPos'), 'dLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartdLblPos', False)

    
    dLblPos = property(__dLblPos.value, __dLblPos.set, None, u'Data Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showPercent uses Python identifier showPercent
    __showPercent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showPercent'), 'showPercent', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowPercent', False)

    
    showPercent = property(__showPercent.value, __showPercent.set, None, u'Show Percent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}leaderLines uses Python identifier leaderLines
    __leaderLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'leaderLines'), 'leaderLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartleaderLines', False)

    
    leaderLines = property(__leaderLines.value, __leaderLines.set, None, u'Leader Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showLeaderLines uses Python identifier showLeaderLines
    __showLeaderLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showLeaderLines'), 'showLeaderLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowLeaderLines', False)

    
    showLeaderLines = property(__showLeaderLines.value, __showLeaderLines.set, None, u'Show Leader Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showBubbleSize uses Python identifier showBubbleSize
    __showBubbleSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize'), 'showBubbleSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowBubbleSize', False)

    
    showBubbleSize = property(__showBubbleSize.value, __showBubbleSize.set, None, u'Show Bubble Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showLegendKey uses Python identifier showLegendKey
    __showLegendKey = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey'), 'showLegendKey', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowLegendKey', False)

    
    showLegendKey = property(__showLegendKey.value, __showLegendKey.set, None, u'Show Legend Key')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}separator uses Python identifier separator
    __separator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'separator'), 'separator', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartseparator', False)

    
    separator = property(__separator.value, __separator.set, None, u'Separator')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showVal uses Python identifier showVal
    __showVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showVal'), 'showVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartshowVal', False)

    
    showVal = property(__showVal.value, __showVal.set, None, u'Show Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbls_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')


    _ElementMap = {
        __dLbl.name() : __dLbl,
        __showCatName.name() : __showCatName,
        __spPr.name() : __spPr,
        __delete.name() : __delete,
        __showSerName.name() : __showSerName,
        __dLblPos.name() : __dLblPos,
        __txPr.name() : __txPr,
        __showPercent.name() : __showPercent,
        __leaderLines.name() : __leaderLines,
        __extLst.name() : __extLst,
        __showLeaderLines.name() : __showLeaderLines,
        __showBubbleSize.name() : __showBubbleSize,
        __showLegendKey.name() : __showLegendKey,
        __separator.name() : __separator,
        __showVal.name() : __showVal,
        __numFmt.name() : __numFmt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DLbls', CT_DLbls)


# Complex type CT_Crosses with content type EMPTY
class CT_Crosses (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Crosses')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Crosses_val', ST_Crosses, required=True)
    
    val = property(__val.value, __val.set, None, u'Crosses Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Crosses', CT_Crosses)


# Complex type CT_BarDir with content type EMPTY
class CT_BarDir (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BarDir')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarDir_val', ST_BarDir, unicode_default=u'col')
    
    val = property(__val.value, __val.set, None, u'Bar Direction Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_BarDir', CT_BarDir)


# Complex type CT_NumFmt with content type EMPTY
class CT_NumFmt (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_NumFmt')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute sourceLinked uses Python identifier sourceLinked
    __sourceLinked = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sourceLinked'), 'sourceLinked', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumFmt_sourceLinked', pyxb.binding.datatypes.boolean)
    
    sourceLinked = property(__sourceLinked.value, __sourceLinked.set, None, u'Linked to Source')

    
    # Attribute formatCode uses Python identifier formatCode
    __formatCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatCode'), 'formatCode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumFmt_formatCode', _s.ST_Xstring, required=True)
    
    formatCode = property(__formatCode.value, __formatCode.set, None, u'Number Format Code')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __sourceLinked.name() : __sourceLinked,
        __formatCode.name() : __formatCode
    }
Namespace.addCategoryObject('typeBinding', u'CT_NumFmt', CT_NumFmt)


# Complex type CT_LineSer with content type ELEMENT_ONLY
class CT_LineSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LineSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendline uses Python identifier trendline
    __trendline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendline'), 'trendline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006charttrendline', True)

    
    trendline = property(__trendline.value, __trendline.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}smooth uses Python identifier smooth
    __smooth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'smooth'), 'smooth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006chartsmooth', False)

    
    smooth = property(__smooth.value, __smooth.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBars uses Python identifier errBars
    __errBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBars'), 'errBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineSer_httpschemas_openxmlformats_orgdrawingml2006charterrBars', False)

    
    errBars = property(__errBars.value, __errBars.set, None, u'Error Bars')


    _ElementMap = {
        __order.name() : __order,
        __idx.name() : __idx,
        __marker.name() : __marker,
        __val.name() : __val,
        __tx.name() : __tx,
        __cat.name() : __cat,
        __extLst.name() : __extLst,
        __spPr.name() : __spPr,
        __dLbls.name() : __dLbls,
        __trendline.name() : __trendline,
        __dPt.name() : __dPt,
        __smooth.name() : __smooth,
        __errBars.name() : __errBars
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_LineSer', CT_LineSer)


# Complex type CT_ExtensionList with content type ELEMENT_ONLY
class CT_ExtensionList (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ExtensionList')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ext uses Python identifier ext
    __ext = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ext'), 'ext', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ExtensionList_httpschemas_openxmlformats_orgdrawingml2006chartext', True)

    
    ext = property(__ext.value, __ext.set, None, u'Extension')


    _ElementMap = {
        __ext.name() : __ext
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ExtensionList', CT_ExtensionList)


# Complex type CT_AxisUnit with content type EMPTY
class CT_AxisUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AxisUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxisUnit_val', ST_AxisUnit, required=True)
    
    val = property(__val.value, __val.set, None, u'Major Unit Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_AxisUnit', CT_AxisUnit)


# Complex type CT_Marker with content type ELEMENT_ONLY
class CT_Marker (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Marker')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}symbol uses Python identifier symbol
    __symbol = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'symbol'), 'symbol', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartsymbol', False)

    
    symbol = property(__symbol.value, __symbol.set, None, u'Symbol')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}size uses Python identifier size
    __size = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'size'), 'size', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartsize', False)

    
    size = property(__size.value, __size.set, None, u'Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Marker_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)


    _ElementMap = {
        __extLst.name() : __extLst,
        __symbol.name() : __symbol,
        __size.name() : __size,
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Marker', CT_Marker)


# Complex type CT_Title with content type ELEMENT_ONLY
class CT_Title (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Title')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Chart Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}overlay uses Python identifier overlay
    __overlay = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'overlay'), 'overlay', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Title_httpschemas_openxmlformats_orgdrawingml2006chartoverlay', False)

    
    overlay = property(__overlay.value, __overlay.set, None, u'Overlay')


    _ElementMap = {
        __spPr.name() : __spPr,
        __txPr.name() : __txPr,
        __extLst.name() : __extLst,
        __tx.name() : __tx,
        __layout.name() : __layout,
        __overlay.name() : __overlay
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Title', CT_Title)


# Complex type CT_PictureFormat with content type EMPTY
class CT_PictureFormat (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureFormat')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureFormat_val', ST_PictureFormat, required=True)
    
    val = property(__val.value, __val.set, None, u'Picture Format Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureFormat', CT_PictureFormat)


# Complex type CT_ErrBars with content type ELEMENT_ONLY
class CT_ErrBars (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ErrBars')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minus uses Python identifier minus
    __minus = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minus'), 'minus', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartminus', False)

    
    minus = property(__minus.value, __minus.set, None, u'Minus')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errDir uses Python identifier errDir
    __errDir = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errDir'), 'errDir', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006charterrDir', False)

    
    errDir = property(__errDir.value, __errDir.set, None, u'Error Bar Direction')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, u'Error Bar Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBarType uses Python identifier errBarType
    __errBarType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBarType'), 'errBarType', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006charterrBarType', False)

    
    errBarType = property(__errBarType.value, __errBarType.set, None, u'Error Bar Type')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}plus uses Python identifier plus
    __plus = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'plus'), 'plus', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartplus', False)

    
    plus = property(__plus.value, __plus.set, None, u'Plus')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errValType uses Python identifier errValType
    __errValType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errValType'), 'errValType', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006charterrValType', False)

    
    errValType = property(__errValType.value, __errValType.set, None, u'Error Bar Value Type')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}noEndCap uses Python identifier noEndCap
    __noEndCap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'noEndCap'), 'noEndCap', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBars_httpschemas_openxmlformats_orgdrawingml2006chartnoEndCap', False)

    
    noEndCap = property(__noEndCap.value, __noEndCap.set, None, u'No End Cap')


    _ElementMap = {
        __minus.name() : __minus,
        __errDir.name() : __errDir,
        __val.name() : __val,
        __errBarType.name() : __errBarType,
        __plus.name() : __plus,
        __spPr.name() : __spPr,
        __errValType.name() : __errValType,
        __extLst.name() : __extLst,
        __noEndCap.name() : __noEndCap
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ErrBars', CT_ErrBars)


# Complex type CT_Extension with content type ELEMENT_ONLY
class CT_Extension (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Extension')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute uri uses Python identifier uri
    __uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'uri'), 'uri', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Extension_uri', pyxb.binding.datatypes.token)
    
    uri = property(__uri.value, __uri.set, None, u'Uniform Resource Identifier')

    _HasWildcardElement = True

    _ElementMap = {
        
    }
    _AttributeMap = {
        __uri.name() : __uri
    }
Namespace.addCategoryObject('typeBinding', u'CT_Extension', CT_Extension)


# Complex type CT_DateAx with content type ELEMENT_ONLY
class CT_DateAx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DateAx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorTimeUnit uses Python identifier minorTimeUnit
    __minorTimeUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorTimeUnit'), 'minorTimeUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartminorTimeUnit', False)

    
    minorTimeUnit = property(__minorTimeUnit.value, __minorTimeUnit.set, None, u'Minor Time Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartaxId', False)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scaling uses Python identifier scaling
    __scaling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scaling'), 'scaling', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartscaling', False)

    
    scaling = property(__scaling.value, __scaling.set, None, u'Scaling')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorGridlines uses Python identifier majorGridlines
    __majorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), 'majorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorGridlines', False)

    
    majorGridlines = property(__majorGridlines.value, __majorGridlines.set, None, u'Major Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorGridlines uses Python identifier minorGridlines
    __minorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), 'minorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartminorGridlines', False)

    
    minorGridlines = property(__minorGridlines.value, __minorGridlines.set, None, u'Minor Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006charttitle', False)

    
    title = property(__title.value, __title.set, None, u'Title')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorTickMark uses Python identifier majorTickMark
    __majorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), 'majorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorTickMark', False)

    
    majorTickMark = property(__majorTickMark.value, __majorTickMark.set, None, u'Major Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorTickMark uses Python identifier minorTickMark
    __minorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), 'minorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartminorTickMark', False)

    
    minorTickMark = property(__minorTickMark.value, __minorTickMark.set, None, u'Minor Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblPos uses Python identifier tickLblPos
    __tickLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), 'tickLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblPos', False)

    
    tickLblPos = property(__tickLblPos.value, __tickLblPos.set, None, u'Tick Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axPos uses Python identifier axPos
    __axPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axPos'), 'axPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartaxPos', False)

    
    axPos = property(__axPos.value, __axPos.set, None, u'Axis Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossAx uses Python identifier crossAx
    __crossAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), 'crossAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossAx', False)

    
    crossAx = property(__crossAx.value, __crossAx.set, None, u'Crossing Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}auto uses Python identifier auto
    __auto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'auto'), 'auto', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartauto', False)

    
    auto = property(__auto.value, __auto.set, None, u'Automatic Category Axis')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}baseTimeUnit uses Python identifier baseTimeUnit
    __baseTimeUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'baseTimeUnit'), 'baseTimeUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartbaseTimeUnit', False)

    
    baseTimeUnit = property(__baseTimeUnit.value, __baseTimeUnit.set, None, u'Base Time Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lblOffset uses Python identifier lblOffset
    __lblOffset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lblOffset'), 'lblOffset', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartlblOffset', False)

    
    lblOffset = property(__lblOffset.value, __lblOffset.set, None, u'Label Offset')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crosses'), 'crosses', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartcrosses', False)

    
    crosses = property(__crosses.value, __crosses.set, None, u'Crosses')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossesAt uses Python identifier crossesAt
    __crossesAt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), 'crossesAt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossesAt', False)

    
    crossesAt = property(__crossesAt.value, __crossesAt.set, None, u'Crossing Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorUnit uses Python identifier majorUnit
    __majorUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorUnit'), 'majorUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorUnit', False)

    
    majorUnit = property(__majorUnit.value, __majorUnit.set, None, u'Major Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorTimeUnit uses Python identifier majorTimeUnit
    __majorTimeUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorTimeUnit'), 'majorTimeUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorTimeUnit', False)

    
    majorTimeUnit = property(__majorTimeUnit.value, __majorTimeUnit.set, None, u'Major Time Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorUnit uses Python identifier minorUnit
    __minorUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorUnit'), 'minorUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DateAx_httpschemas_openxmlformats_orgdrawingml2006chartminorUnit', False)

    
    minorUnit = property(__minorUnit.value, __minorUnit.set, None, u'Minor Unit')


    _ElementMap = {
        __minorTimeUnit.name() : __minorTimeUnit,
        __axId.name() : __axId,
        __extLst.name() : __extLst,
        __scaling.name() : __scaling,
        __delete.name() : __delete,
        __majorGridlines.name() : __majorGridlines,
        __minorGridlines.name() : __minorGridlines,
        __title.name() : __title,
        __numFmt.name() : __numFmt,
        __majorTickMark.name() : __majorTickMark,
        __minorTickMark.name() : __minorTickMark,
        __tickLblPos.name() : __tickLblPos,
        __axPos.name() : __axPos,
        __txPr.name() : __txPr,
        __crossAx.name() : __crossAx,
        __auto.name() : __auto,
        __baseTimeUnit.name() : __baseTimeUnit,
        __lblOffset.name() : __lblOffset,
        __crosses.name() : __crosses,
        __crossesAt.name() : __crossesAt,
        __majorUnit.name() : __majorUnit,
        __spPr.name() : __spPr,
        __majorTimeUnit.name() : __majorTimeUnit,
        __minorUnit.name() : __minorUnit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DateAx', CT_DateAx)


# Complex type CT_Grouping with content type EMPTY
class CT_Grouping (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Grouping')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Grouping_val', ST_Grouping, unicode_default=u'standard')
    
    val = property(__val.value, __val.set, None, u'Grouping Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Grouping', CT_Grouping)


# Complex type CT_HeaderFooter with content type ELEMENT_ONLY
class CT_HeaderFooter (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_HeaderFooter')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}oddHeader uses Python identifier oddHeader
    __oddHeader = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'oddHeader'), 'oddHeader', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartoddHeader', False)

    
    oddHeader = property(__oddHeader.value, __oddHeader.set, None, u'Odd Header')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}evenHeader uses Python identifier evenHeader
    __evenHeader = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'evenHeader'), 'evenHeader', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartevenHeader', False)

    
    evenHeader = property(__evenHeader.value, __evenHeader.set, None, u'Even Header')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}oddFooter uses Python identifier oddFooter
    __oddFooter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'oddFooter'), 'oddFooter', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartoddFooter', False)

    
    oddFooter = property(__oddFooter.value, __oddFooter.set, None, u'Odd Footer')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}evenFooter uses Python identifier evenFooter
    __evenFooter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'evenFooter'), 'evenFooter', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartevenFooter', False)

    
    evenFooter = property(__evenFooter.value, __evenFooter.set, None, u'Even Footer')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}firstHeader uses Python identifier firstHeader
    __firstHeader = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstHeader'), 'firstHeader', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartfirstHeader', False)

    
    firstHeader = property(__firstHeader.value, __firstHeader.set, None, u'First Header')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}firstFooter uses Python identifier firstFooter
    __firstFooter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstFooter'), 'firstFooter', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_httpschemas_openxmlformats_orgdrawingml2006chartfirstFooter', False)

    
    firstFooter = property(__firstFooter.value, __firstFooter.set, None, u'First Footer')

    
    # Attribute differentFirst uses Python identifier differentFirst
    __differentFirst = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'differentFirst'), 'differentFirst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_differentFirst', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    differentFirst = property(__differentFirst.value, __differentFirst.set, None, u'Different First')

    
    # Attribute differentOddEven uses Python identifier differentOddEven
    __differentOddEven = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'differentOddEven'), 'differentOddEven', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_differentOddEven', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    differentOddEven = property(__differentOddEven.value, __differentOddEven.set, None, u'Different Odd Even')

    
    # Attribute alignWithMargins uses Python identifier alignWithMargins
    __alignWithMargins = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'alignWithMargins'), 'alignWithMargins', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HeaderFooter_alignWithMargins', pyxb.binding.datatypes.boolean, unicode_default=u'true')
    
    alignWithMargins = property(__alignWithMargins.value, __alignWithMargins.set, None, u'Align With Margins')


    _ElementMap = {
        __oddHeader.name() : __oddHeader,
        __evenHeader.name() : __evenHeader,
        __oddFooter.name() : __oddFooter,
        __evenFooter.name() : __evenFooter,
        __firstHeader.name() : __firstHeader,
        __firstFooter.name() : __firstFooter
    }
    _AttributeMap = {
        __differentFirst.name() : __differentFirst,
        __differentOddEven.name() : __differentOddEven,
        __alignWithMargins.name() : __alignWithMargins
    }
Namespace.addCategoryObject('typeBinding', u'CT_HeaderFooter', CT_HeaderFooter)


# Complex type CT_UpDownBars with content type ELEMENT_ONLY
class CT_UpDownBars (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_UpDownBars')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UpDownBars_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapWidth uses Python identifier gapWidth
    __gapWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), 'gapWidth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UpDownBars_httpschemas_openxmlformats_orgdrawingml2006chartgapWidth', False)

    
    gapWidth = property(__gapWidth.value, __gapWidth.set, None, u'Gap Width')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}upBars uses Python identifier upBars
    __upBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'upBars'), 'upBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UpDownBars_httpschemas_openxmlformats_orgdrawingml2006chartupBars', False)

    
    upBars = property(__upBars.value, __upBars.set, None, u'Up Bars')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}downBars uses Python identifier downBars
    __downBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'downBars'), 'downBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UpDownBars_httpschemas_openxmlformats_orgdrawingml2006chartdownBars', False)

    
    downBars = property(__downBars.value, __downBars.set, None, u'Down Bars')


    _ElementMap = {
        __extLst.name() : __extLst,
        __gapWidth.name() : __gapWidth,
        __upBars.name() : __upBars,
        __downBars.name() : __downBars
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_UpDownBars', CT_UpDownBars)


# Complex type CT_ValAx with content type ELEMENT_ONLY
class CT_ValAx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ValAx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dispUnits uses Python identifier dispUnits
    __dispUnits = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dispUnits'), 'dispUnits', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartdispUnits', False)

    
    dispUnits = property(__dispUnits.value, __dispUnits.set, None, u'Display Units')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossAx uses Python identifier crossAx
    __crossAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), 'crossAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossAx', False)

    
    crossAx = property(__crossAx.value, __crossAx.set, None, u'Crossing Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorTickMark uses Python identifier majorTickMark
    __majorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), 'majorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorTickMark', False)

    
    majorTickMark = property(__majorTickMark.value, __majorTickMark.set, None, u'Major Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scaling uses Python identifier scaling
    __scaling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scaling'), 'scaling', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartscaling', False)

    
    scaling = property(__scaling.value, __scaling.set, None, u'Scaling')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorTickMark uses Python identifier minorTickMark
    __minorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), 'minorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartminorTickMark', False)

    
    minorTickMark = property(__minorTickMark.value, __minorTickMark.set, None, u'Minor Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossesAt uses Python identifier crossesAt
    __crossesAt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), 'crossesAt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossesAt', False)

    
    crossesAt = property(__crossesAt.value, __crossesAt.set, None, u'Crossing Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorGridlines uses Python identifier majorGridlines
    __majorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), 'majorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorGridlines', False)

    
    majorGridlines = property(__majorGridlines.value, __majorGridlines.set, None, u'Major Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axPos uses Python identifier axPos
    __axPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axPos'), 'axPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartaxPos', False)

    
    axPos = property(__axPos.value, __axPos.set, None, u'Axis Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crosses'), 'crosses', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartcrosses', False)

    
    crosses = property(__crosses.value, __crosses.set, None, u'Crosses')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblPos uses Python identifier tickLblPos
    __tickLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), 'tickLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblPos', False)

    
    tickLblPos = property(__tickLblPos.value, __tickLblPos.set, None, u'Tick Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorGridlines uses Python identifier minorGridlines
    __minorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), 'minorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartminorGridlines', False)

    
    minorGridlines = property(__minorGridlines.value, __minorGridlines.set, None, u'Minor Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorUnit uses Python identifier majorUnit
    __majorUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorUnit'), 'majorUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorUnit', False)

    
    majorUnit = property(__majorUnit.value, __majorUnit.set, None, u'Major Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossBetween uses Python identifier crossBetween
    __crossBetween = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossBetween'), 'crossBetween', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossBetween', False)

    
    crossBetween = property(__crossBetween.value, __crossBetween.set, None, u'Cross Between')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartaxId', False)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006charttitle', False)

    
    title = property(__title.value, __title.set, None, u'Title')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorUnit uses Python identifier minorUnit
    __minorUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorUnit'), 'minorUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006chartminorUnit', False)

    
    minorUnit = property(__minorUnit.value, __minorUnit.set, None, u'Minor Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ValAx_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)


    _ElementMap = {
        __numFmt.name() : __numFmt,
        __dispUnits.name() : __dispUnits,
        __delete.name() : __delete,
        __crossAx.name() : __crossAx,
        __majorTickMark.name() : __majorTickMark,
        __scaling.name() : __scaling,
        __extLst.name() : __extLst,
        __minorTickMark.name() : __minorTickMark,
        __crossesAt.name() : __crossesAt,
        __majorGridlines.name() : __majorGridlines,
        __axPos.name() : __axPos,
        __crosses.name() : __crosses,
        __tickLblPos.name() : __tickLblPos,
        __minorGridlines.name() : __minorGridlines,
        __majorUnit.name() : __majorUnit,
        __crossBetween.name() : __crossBetween,
        __spPr.name() : __spPr,
        __axId.name() : __axId,
        __title.name() : __title,
        __minorUnit.name() : __minorUnit,
        __txPr.name() : __txPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ValAx', CT_ValAx)


# Complex type CT_HPercent with content type EMPTY
class CT_HPercent (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_HPercent')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HPercent_val', ST_HPercent, unicode_default=u'100')
    
    val = property(__val.value, __val.set, None, u'Height Percent Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_HPercent', CT_HPercent)


# Complex type CT_Double with content type EMPTY
class CT_Double (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Double')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Double_val', pyxb.binding.datatypes.double, required=True)
    
    val = property(__val.value, __val.set, None, u'Floating Point Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Double', CT_Double)


# Complex type CT_ErrBarType with content type EMPTY
class CT_ErrBarType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ErrBarType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrBarType_val', ST_ErrBarType, unicode_default=u'both')
    
    val = property(__val.value, __val.set, None, u'Error Bar Type Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_ErrBarType', CT_ErrBarType)


# Complex type CT_TickLblPos with content type EMPTY
class CT_TickLblPos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TickLblPos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TickLblPos_val', ST_TickLblPos, unicode_default=u'nextTo')
    
    val = property(__val.value, __val.set, None, u'Tick Label Position Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_TickLblPos', CT_TickLblPos)


# Complex type CT_DLblPos with content type EMPTY
class CT_DLblPos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DLblPos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLblPos_val', ST_DLblPos, required=True)
    
    val = property(__val.value, __val.set, None, u'Data Label Position Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_DLblPos', CT_DLblPos)


# Complex type CT_PrintSettings with content type ELEMENT_ONLY
class CT_PrintSettings (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PrintSettings')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}legacyDrawingHF uses Python identifier legacyDrawingHF
    __legacyDrawingHF = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legacyDrawingHF'), 'legacyDrawingHF', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PrintSettings_httpschemas_openxmlformats_orgdrawingml2006chartlegacyDrawingHF', False)

    
    legacyDrawingHF = property(__legacyDrawingHF.value, __legacyDrawingHF.set, None, u'Legacy Drawing for Headers and Footers')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}headerFooter uses Python identifier headerFooter
    __headerFooter = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'headerFooter'), 'headerFooter', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PrintSettings_httpschemas_openxmlformats_orgdrawingml2006chartheaderFooter', False)

    
    headerFooter = property(__headerFooter.value, __headerFooter.set, None, u'Header and Footer')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pageMargins uses Python identifier pageMargins
    __pageMargins = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pageMargins'), 'pageMargins', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PrintSettings_httpschemas_openxmlformats_orgdrawingml2006chartpageMargins', False)

    
    pageMargins = property(__pageMargins.value, __pageMargins.set, None, u'Page Margins')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pageSetup uses Python identifier pageSetup
    __pageSetup = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pageSetup'), 'pageSetup', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PrintSettings_httpschemas_openxmlformats_orgdrawingml2006chartpageSetup', False)

    
    pageSetup = property(__pageSetup.value, __pageSetup.set, None, u'Page Setup')


    _ElementMap = {
        __legacyDrawingHF.name() : __legacyDrawingHF,
        __headerFooter.name() : __headerFooter,
        __pageMargins.name() : __pageMargins,
        __pageSetup.name() : __pageSetup
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PrintSettings', CT_PrintSettings)


# Complex type CT_Tx with content type ELEMENT_ONLY
class CT_Tx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Tx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}strRef uses Python identifier strRef
    __strRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'strRef'), 'strRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Tx_httpschemas_openxmlformats_orgdrawingml2006chartstrRef', False)

    
    strRef = property(__strRef.value, __strRef.set, None, u'String Reference')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}rich uses Python identifier rich
    __rich = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rich'), 'rich', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Tx_httpschemas_openxmlformats_orgdrawingml2006chartrich', False)

    
    rich = property(__rich.value, __rich.set, None, u'Rich Text')


    _ElementMap = {
        __strRef.name() : __strRef,
        __rich.name() : __rich
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Tx', CT_Tx)


# Complex type CT_LayoutMode with content type EMPTY
class CT_LayoutMode (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LayoutMode')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LayoutMode_val', ST_LayoutMode, unicode_default=u'factor')
    
    val = property(__val.value, __val.set, None, u'Layout Mode Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LayoutMode', CT_LayoutMode)


# Complex type CT_NumDataSource with content type ELEMENT_ONLY
class CT_NumDataSource (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_NumDataSource')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numRef uses Python identifier numRef
    __numRef = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numRef'), 'numRef', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumDataSource_httpschemas_openxmlformats_orgdrawingml2006chartnumRef', False)

    
    numRef = property(__numRef.value, __numRef.set, None, u'Number Reference')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numLit uses Python identifier numLit
    __numLit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numLit'), 'numLit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumDataSource_httpschemas_openxmlformats_orgdrawingml2006chartnumLit', False)

    
    numLit = property(__numLit.value, __numLit.set, None, u'Number Literal')


    _ElementMap = {
        __numRef.name() : __numRef,
        __numLit.name() : __numLit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_NumDataSource', CT_NumDataSource)


# Complex type CT_TrendlineType with content type EMPTY
class CT_TrendlineType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TrendlineType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineType_val', ST_TrendlineType, unicode_default=u'linear')
    
    val = property(__val.value, __val.set, None, u'Trendline Type Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_TrendlineType', CT_TrendlineType)


# Complex type CT_SurfaceSer with content type ELEMENT_ONLY
class CT_SurfaceSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SurfaceSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')


    _ElementMap = {
        __idx.name() : __idx,
        __cat.name() : __cat,
        __val.name() : __val,
        __spPr.name() : __spPr,
        __extLst.name() : __extLst,
        __order.name() : __order,
        __tx.name() : __tx
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_SurfaceSer', CT_SurfaceSer)


# Complex type CT_LogBase with content type EMPTY
class CT_LogBase (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LogBase')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LogBase_val', ST_LogBase, required=True)
    
    val = property(__val.value, __val.set, None, u'Logarithmic Base Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LogBase', CT_LogBase)


# Complex type CT_BarChart with content type ELEMENT_ONLY
class CT_BarChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BarChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Bar Grouping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}barDir uses Python identifier barDir
    __barDir = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'barDir'), 'barDir', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartbarDir', False)

    
    barDir = property(__barDir.value, __barDir.set, None, u'Bar Direction')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}overlap uses Python identifier overlap
    __overlap = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'overlap'), 'overlap', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartoverlap', False)

    
    overlap = property(__overlap.value, __overlap.set, None, u'Overlap')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}serLines uses Python identifier serLines
    __serLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'serLines'), 'serLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartserLines', True)

    
    serLines = property(__serLines.value, __serLines.set, None, u'Series Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapWidth uses Python identifier gapWidth
    __gapWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), 'gapWidth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartgapWidth', False)

    
    gapWidth = property(__gapWidth.value, __gapWidth.set, None, u'Gap Width')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Bar Chart Series')


    _ElementMap = {
        __grouping.name() : __grouping,
        __barDir.name() : __barDir,
        __overlap.name() : __overlap,
        __axId.name() : __axId,
        __serLines.name() : __serLines,
        __gapWidth.name() : __gapWidth,
        __varyColors.name() : __varyColors,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __ser.name() : __ser
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BarChart', CT_BarChart)


# Complex type CT_BarGrouping with content type EMPTY
class CT_BarGrouping (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BarGrouping')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarGrouping_val', ST_BarGrouping, unicode_default=u'clustered')
    
    val = property(__val.value, __val.set, None, u'Bar Grouping Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_BarGrouping', CT_BarGrouping)


# Complex type CT_PivotSource with content type ELEMENT_ONLY
class CT_PivotSource (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PivotSource')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotSource_httpschemas_openxmlformats_orgdrawingml2006chartextLst', True)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotSource_httpschemas_openxmlformats_orgdrawingml2006chartname', False)

    
    name = property(__name.value, __name.set, None, u'Pivot Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}fmtId uses Python identifier fmtId
    __fmtId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'fmtId'), 'fmtId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotSource_httpschemas_openxmlformats_orgdrawingml2006chartfmtId', False)

    
    fmtId = property(__fmtId.value, __fmtId.set, None, u'Format ID')


    _ElementMap = {
        __extLst.name() : __extLst,
        __name.name() : __name,
        __fmtId.name() : __fmtId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PivotSource', CT_PivotSource)


# Complex type CT_FirstSliceAng with content type EMPTY
class CT_FirstSliceAng (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_FirstSliceAng')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_FirstSliceAng_val', ST_FirstSliceAng, unicode_default=u'0')
    
    val = property(__val.value, __val.set, None, u'First Slice Angle Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_FirstSliceAng', CT_FirstSliceAng)


# Complex type CT_GapAmount with content type EMPTY
class CT_GapAmount (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_GapAmount')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_GapAmount_val', ST_GapAmount, unicode_default=u'150')
    
    val = property(__val.value, __val.set, None, u'Gap Size Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_GapAmount', CT_GapAmount)


# Complex type CT_RadarStyle with content type EMPTY
class CT_RadarStyle (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RadarStyle')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarStyle_val', ST_RadarStyle, unicode_default=u'standard')
    
    val = property(__val.value, __val.set, None, u'Radar Style Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_RadarStyle', CT_RadarStyle)


# Complex type CT_SecondPieSize with content type EMPTY
class CT_SecondPieSize (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SecondPieSize')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SecondPieSize_val', ST_SecondPieSize, unicode_default=u'75')
    
    val = property(__val.value, __val.set, None, u'Second Pie Size Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_SecondPieSize', CT_SecondPieSize)


# Complex type CT_Skip with content type EMPTY
class CT_Skip (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Skip')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Skip_val', ST_Skip, required=True)
    
    val = property(__val.value, __val.set, None, u'Tick Skip Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Skip', CT_Skip)


# Complex type CT_TickMark with content type EMPTY
class CT_TickMark (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TickMark')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TickMark_val', ST_TickMark, unicode_default=u'cross')
    
    val = property(__val.value, __val.set, None, u'Tick Mark Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_TickMark', CT_TickMark)


# Complex type CT_MultiLvlStrData with content type ELEMENT_ONLY
class CT_MultiLvlStrData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_MultiLvlStrData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrData_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ptCount uses Python identifier ptCount
    __ptCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), 'ptCount', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrData_httpschemas_openxmlformats_orgdrawingml2006chartptCount', False)

    
    ptCount = property(__ptCount.value, __ptCount.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lvl uses Python identifier lvl
    __lvl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lvl'), 'lvl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrData_httpschemas_openxmlformats_orgdrawingml2006chartlvl', True)

    
    lvl = property(__lvl.value, __lvl.set, None, u'Level')


    _ElementMap = {
        __extLst.name() : __extLst,
        __ptCount.name() : __ptCount,
        __lvl.name() : __lvl
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_MultiLvlStrData', CT_MultiLvlStrData)


# Complex type CT_Layout with content type ELEMENT_ONLY
class CT_Layout (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Layout')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Layout_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}manualLayout uses Python identifier manualLayout
    __manualLayout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'manualLayout'), 'manualLayout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Layout_httpschemas_openxmlformats_orgdrawingml2006chartmanualLayout', False)

    
    manualLayout = property(__manualLayout.value, __manualLayout.set, None, u'Manual Layout')


    _ElementMap = {
        __extLst.name() : __extLst,
        __manualLayout.name() : __manualLayout
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Layout', CT_Layout)


# Complex type CT_BandFmt with content type ELEMENT_ONLY
class CT_BandFmt (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BandFmt')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BandFmt_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BandFmt_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, None)


    _ElementMap = {
        __spPr.name() : __spPr,
        __idx.name() : __idx
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BandFmt', CT_BandFmt)


# Complex type CT_AreaSer with content type ELEMENT_ONLY
class CT_AreaSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AreaSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendline uses Python identifier trendline
    __trendline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendline'), 'trendline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006charttrendline', True)

    
    trendline = property(__trendline.value, __trendline.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureOptions uses Python identifier pictureOptions
    __pictureOptions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), 'pictureOptions', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartpictureOptions', False)

    
    pictureOptions = property(__pictureOptions.value, __pictureOptions.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, u'Values')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBars uses Python identifier errBars
    __errBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBars'), 'errBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006charterrBars', True)

    
    errBars = property(__errBars.value, __errBars.set, None, u'Error Bars')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')


    _ElementMap = {
        __spPr.name() : __spPr,
        __dPt.name() : __dPt,
        __trendline.name() : __trendline,
        __pictureOptions.name() : __pictureOptions,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __idx.name() : __idx,
        __val.name() : __val,
        __order.name() : __order,
        __errBars.name() : __errBars,
        __tx.name() : __tx,
        __cat.name() : __cat
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_AreaSer', CT_AreaSer)


# Complex type CT_BuiltInUnit with content type EMPTY
class CT_BuiltInUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BuiltInUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BuiltInUnit_val', ST_BuiltInUnit, unicode_default=u'thousands')
    
    val = property(__val.value, __val.set, None, u'Built In Unit Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_BuiltInUnit', CT_BuiltInUnit)


# Complex type CT_Trendline with content type ELEMENT_ONLY
class CT_Trendline (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Trendline')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendlineType uses Python identifier trendlineType
    __trendlineType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendlineType'), 'trendlineType', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006charttrendlineType', False)

    
    trendlineType = property(__trendlineType.value, __trendlineType.set, None, u'Trendline Type')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Polynomial Trendline Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dispEq uses Python identifier dispEq
    __dispEq = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dispEq'), 'dispEq', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartdispEq', False)

    
    dispEq = property(__dispEq.value, __dispEq.set, None, u'Display Equation')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}period uses Python identifier period
    __period = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'period'), 'period', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartperiod', False)

    
    period = property(__period.value, __period.set, None, u'Period')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dispRSqr uses Python identifier dispRSqr
    __dispRSqr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dispRSqr'), 'dispRSqr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartdispRSqr', False)

    
    dispRSqr = property(__dispRSqr.value, __dispRSqr.set, None, u'Display R Squared Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}forward uses Python identifier forward
    __forward = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'forward'), 'forward', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartforward', False)

    
    forward = property(__forward.value, __forward.set, None, u'Forward')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}name uses Python identifier name
    __name = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'name'), 'name', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartname', False)

    
    name = property(__name.value, __name.set, None, u'Trendline Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendlineLbl uses Python identifier trendlineLbl
    __trendlineLbl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendlineLbl'), 'trendlineLbl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006charttrendlineLbl', False)

    
    trendlineLbl = property(__trendlineLbl.value, __trendlineLbl.set, None, u'Trendline Label')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}backward uses Python identifier backward
    __backward = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backward'), 'backward', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartbackward', False)

    
    backward = property(__backward.value, __backward.set, None, u'Backward')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}intercept uses Python identifier intercept
    __intercept = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'intercept'), 'intercept', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Trendline_httpschemas_openxmlformats_orgdrawingml2006chartintercept', False)

    
    intercept = property(__intercept.value, __intercept.set, None, u'Intercept')


    _ElementMap = {
        __trendlineType.name() : __trendlineType,
        __order.name() : __order,
        __dispEq.name() : __dispEq,
        __period.name() : __period,
        __dispRSqr.name() : __dispRSqr,
        __forward.name() : __forward,
        __name.name() : __name,
        __extLst.name() : __extLst,
        __trendlineLbl.name() : __trendlineLbl,
        __backward.name() : __backward,
        __spPr.name() : __spPr,
        __intercept.name() : __intercept
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Trendline', CT_Trendline)


# Complex type CT_PlotArea with content type ELEMENT_ONLY
class CT_PlotArea (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PlotArea')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scatterChart uses Python identifier scatterChart
    __scatterChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scatterChart'), 'scatterChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartscatterChart', True)

    
    scatterChart = property(__scatterChart.value, __scatterChart.set, None, u'Scatter Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pieChart uses Python identifier pieChart
    __pieChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pieChart'), 'pieChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartpieChart', True)

    
    pieChart = property(__pieChart.value, __pieChart.set, None, u'Pie Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dateAx uses Python identifier dateAx
    __dateAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dateAx'), 'dateAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartdateAx', True)

    
    dateAx = property(__dateAx.value, __dateAx.set, None, u'Date Axis')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bar3DChart uses Python identifier bar3DChart
    __bar3DChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bar3DChart'), 'bar3DChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartbar3DChart', True)

    
    bar3DChart = property(__bar3DChart.value, __bar3DChart.set, None, u'3D Bar Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}doughnutChart uses Python identifier doughnutChart
    __doughnutChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'doughnutChart'), 'doughnutChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartdoughnutChart', True)

    
    doughnutChart = property(__doughnutChart.value, __doughnutChart.set, None, u'Doughnut Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}barChart uses Python identifier barChart
    __barChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'barChart'), 'barChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartbarChart', True)

    
    barChart = property(__barChart.value, __barChart.set, None, u'Bar Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ofPieChart uses Python identifier ofPieChart
    __ofPieChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ofPieChart'), 'ofPieChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartofPieChart', True)

    
    ofPieChart = property(__ofPieChart.value, __ofPieChart.set, None, u'Pie of Pie or Bar of Pie Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}surfaceChart uses Python identifier surfaceChart
    __surfaceChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surfaceChart'), 'surfaceChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartsurfaceChart', True)

    
    surfaceChart = property(__surfaceChart.value, __surfaceChart.set, None, u'Surface Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}surface3DChart uses Python identifier surface3DChart
    __surface3DChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'surface3DChart'), 'surface3DChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartsurface3DChart', True)

    
    surface3DChart = property(__surface3DChart.value, __surface3DChart.set, None, u'3D Surface Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubbleChart uses Python identifier bubbleChart
    __bubbleChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubbleChart'), 'bubbleChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartbubbleChart', True)

    
    bubbleChart = property(__bubbleChart.value, __bubbleChart.set, None, u'Bubble Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}catAx uses Python identifier catAx
    __catAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'catAx'), 'catAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartcatAx', True)

    
    catAx = property(__catAx.value, __catAx.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pie3DChart uses Python identifier pie3DChart
    __pie3DChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pie3DChart'), 'pie3DChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartpie3DChart', True)

    
    pie3DChart = property(__pie3DChart.value, __pie3DChart.set, None, u'3D Pie Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}serAx uses Python identifier serAx
    __serAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'serAx'), 'serAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartserAx', True)

    
    serAx = property(__serAx.value, __serAx.set, None, u'Series Axis')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dTable uses Python identifier dTable
    __dTable = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dTable'), 'dTable', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartdTable', False)

    
    dTable = property(__dTable.value, __dTable.set, None, u'Data Table')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}areaChart uses Python identifier areaChart
    __areaChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'areaChart'), 'areaChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartareaChart', True)

    
    areaChart = property(__areaChart.value, __areaChart.set, None, u'Area Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}valAx uses Python identifier valAx
    __valAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'valAx'), 'valAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartvalAx', True)

    
    valAx = property(__valAx.value, __valAx.set, None, u'Value Axis')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}area3DChart uses Python identifier area3DChart
    __area3DChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'area3DChart'), 'area3DChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartarea3DChart', True)

    
    area3DChart = property(__area3DChart.value, __area3DChart.set, None, u'3D Area Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lineChart uses Python identifier lineChart
    __lineChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lineChart'), 'lineChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartlineChart', True)

    
    lineChart = property(__lineChart.value, __lineChart.set, None, u'Line Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}line3DChart uses Python identifier line3DChart
    __line3DChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'line3DChart'), 'line3DChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartline3DChart', True)

    
    line3DChart = property(__line3DChart.value, __line3DChart.set, None, u'3D Line Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}stockChart uses Python identifier stockChart
    __stockChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'stockChart'), 'stockChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartstockChart', True)

    
    stockChart = property(__stockChart.value, __stockChart.set, None, u'Stock Charts')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}radarChart uses Python identifier radarChart
    __radarChart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'radarChart'), 'radarChart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PlotArea_httpschemas_openxmlformats_orgdrawingml2006chartradarChart', True)

    
    radarChart = property(__radarChart.value, __radarChart.set, None, u'Radar Charts')


    _ElementMap = {
        __scatterChart.name() : __scatterChart,
        __pieChart.name() : __pieChart,
        __dateAx.name() : __dateAx,
        __bar3DChart.name() : __bar3DChart,
        __doughnutChart.name() : __doughnutChart,
        __barChart.name() : __barChart,
        __ofPieChart.name() : __ofPieChart,
        __surfaceChart.name() : __surfaceChart,
        __surface3DChart.name() : __surface3DChart,
        __bubbleChart.name() : __bubbleChart,
        __catAx.name() : __catAx,
        __pie3DChart.name() : __pie3DChart,
        __layout.name() : __layout,
        __serAx.name() : __serAx,
        __dTable.name() : __dTable,
        __areaChart.name() : __areaChart,
        __valAx.name() : __valAx,
        __spPr.name() : __spPr,
        __area3DChart.name() : __area3DChart,
        __extLst.name() : __extLst,
        __lineChart.name() : __lineChart,
        __line3DChart.name() : __line3DChart,
        __stockChart.name() : __stockChart,
        __radarChart.name() : __radarChart
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PlotArea', CT_PlotArea)


# Complex type CT_BubbleSer with content type ELEMENT_ONLY
class CT_BubbleSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BubbleSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}yVal uses Python identifier yVal
    __yVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'yVal'), 'yVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartyVal', False)

    
    yVal = property(__yVal.value, __yVal.set, None, u'Y Values')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}invertIfNegative uses Python identifier invertIfNegative
    __invertIfNegative = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), 'invertIfNegative', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartinvertIfNegative', False)

    
    invertIfNegative = property(__invertIfNegative.value, __invertIfNegative.set, None, u'Invert if Negative')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubbleSize uses Python identifier bubbleSize
    __bubbleSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubbleSize'), 'bubbleSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartbubbleSize', False)

    
    bubbleSize = property(__bubbleSize.value, __bubbleSize.set, None, u'Bubble Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}xVal uses Python identifier xVal
    __xVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'xVal'), 'xVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartxVal', False)

    
    xVal = property(__xVal.value, __xVal.set, None, u'X Values')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubble3D uses Python identifier bubble3D
    __bubble3D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), 'bubble3D', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartbubble3D', False)

    
    bubble3D = property(__bubble3D.value, __bubble3D.set, None, u'3D Bubble')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendline uses Python identifier trendline
    __trendline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendline'), 'trendline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006charttrendline', True)

    
    trendline = property(__trendline.value, __trendline.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBars uses Python identifier errBars
    __errBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBars'), 'errBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleSer_httpschemas_openxmlformats_orgdrawingml2006charterrBars', True)

    
    errBars = property(__errBars.value, __errBars.set, None, u'Error Bars')


    _ElementMap = {
        __yVal.name() : __yVal,
        __invertIfNegative.name() : __invertIfNegative,
        __idx.name() : __idx,
        __dPt.name() : __dPt,
        __bubbleSize.name() : __bubbleSize,
        __order.name() : __order,
        __xVal.name() : __xVal,
        __bubble3D.name() : __bubble3D,
        __dLbls.name() : __dLbls,
        __tx.name() : __tx,
        __trendline.name() : __trendline,
        __extLst.name() : __extLst,
        __spPr.name() : __spPr,
        __errBars.name() : __errBars
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BubbleSer', CT_BubbleSer)


# Complex type CT_PictureOptions with content type ELEMENT_ONLY
class CT_PictureOptions (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureOptions')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureStackUnit uses Python identifier pictureStackUnit
    __pictureStackUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureStackUnit'), 'pictureStackUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureOptions_httpschemas_openxmlformats_orgdrawingml2006chartpictureStackUnit', False)

    
    pictureStackUnit = property(__pictureStackUnit.value, __pictureStackUnit.set, None, u'Picture Stack Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}applyToFront uses Python identifier applyToFront
    __applyToFront = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'applyToFront'), 'applyToFront', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureOptions_httpschemas_openxmlformats_orgdrawingml2006chartapplyToFront', False)

    
    applyToFront = property(__applyToFront.value, __applyToFront.set, None, u'Apply To Front')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}applyToEnd uses Python identifier applyToEnd
    __applyToEnd = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'applyToEnd'), 'applyToEnd', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureOptions_httpschemas_openxmlformats_orgdrawingml2006chartapplyToEnd', False)

    
    applyToEnd = property(__applyToEnd.value, __applyToEnd.set, None, u'Apply to End')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}applyToSides uses Python identifier applyToSides
    __applyToSides = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'applyToSides'), 'applyToSides', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureOptions_httpschemas_openxmlformats_orgdrawingml2006chartapplyToSides', False)

    
    applyToSides = property(__applyToSides.value, __applyToSides.set, None, u'Apply To Sides')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureFormat uses Python identifier pictureFormat
    __pictureFormat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureFormat'), 'pictureFormat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureOptions_httpschemas_openxmlformats_orgdrawingml2006chartpictureFormat', False)

    
    pictureFormat = property(__pictureFormat.value, __pictureFormat.set, None, u'Picture Format')


    _ElementMap = {
        __pictureStackUnit.name() : __pictureStackUnit,
        __applyToFront.name() : __applyToFront,
        __applyToEnd.name() : __applyToEnd,
        __applyToSides.name() : __applyToSides,
        __pictureFormat.name() : __pictureFormat
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureOptions', CT_PictureOptions)


# Complex type CT_DispUnitsLbl with content type ELEMENT_ONLY
class CT_DispUnitsLbl (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DispUnitsLbl')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnitsLbl_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnitsLbl_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnitsLbl_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnitsLbl_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)


    _ElementMap = {
        __txPr.name() : __txPr,
        __layout.name() : __layout,
        __tx.name() : __tx,
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DispUnitsLbl', CT_DispUnitsLbl)


# Complex type CT_Line3DChart with content type ELEMENT_ONLY
class CT_Line3DChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Line3DChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dropLines uses Python identifier dropLines
    __dropLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), 'dropLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdropLines', False)

    
    dropLines = property(__dropLines.value, __dropLines.set, None, u'Drop Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Grouping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapDepth uses Python identifier gapDepth
    __gapDepth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), 'gapDepth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Line3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgapDepth', False)

    
    gapDepth = property(__gapDepth.value, __gapDepth.set, None, u'Gap Depth')


    _ElementMap = {
        __axId.name() : __axId,
        __dLbls.name() : __dLbls,
        __dropLines.name() : __dropLines,
        __extLst.name() : __extLst,
        __ser.name() : __ser,
        __varyColors.name() : __varyColors,
        __grouping.name() : __grouping,
        __gapDepth.name() : __gapDepth
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Line3DChart', CT_Line3DChart)


# Complex type CT_RelId with content type EMPTY
class CT_RelId (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RelId')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://schemas.openxmlformats.org/officeDocument/2006/relationships}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/officeDocument/2006/relationships'), u'id'), 'id', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RelId_httpschemas_openxmlformats_orgofficeDocument2006relationshipsid', _r.ST_RelationshipId, required=True)
    
    id = property(__id.value, __id.set, None, u'Relationship ID')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'CT_RelId', CT_RelId)


# Complex type CT_TimeUnit with content type EMPTY
class CT_TimeUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TimeUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TimeUnit_val', ST_TimeUnit, unicode_default=u'days')
    
    val = property(__val.value, __val.set, None, u'Time Unit Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_TimeUnit', CT_TimeUnit)


# Complex type CT_UpDownBar with content type ELEMENT_ONLY
class CT_UpDownBar (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_UpDownBar')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_UpDownBar_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)


    _ElementMap = {
        __spPr.name() : __spPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_UpDownBar', CT_UpDownBar)


# Complex type CT_AxPos with content type EMPTY
class CT_AxPos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AxPos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AxPos_val', ST_AxPos, required=True)
    
    val = property(__val.value, __val.set, None, u'Axis Position Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_AxPos', CT_AxPos)


# Complex type CT_SurfaceChart with content type ELEMENT_ONLY
class CT_SurfaceChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SurfaceChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bandFmts uses Python identifier bandFmts
    __bandFmts = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bandFmts'), 'bandFmts', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceChart_httpschemas_openxmlformats_orgdrawingml2006chartbandFmts', False)

    
    bandFmts = property(__bandFmts.value, __bandFmts.set, None, u'Band Formats')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Surface Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}wireframe uses Python identifier wireframe
    __wireframe = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wireframe'), 'wireframe', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceChart_httpschemas_openxmlformats_orgdrawingml2006chartwireframe', False)

    
    wireframe = property(__wireframe.value, __wireframe.set, None, u'Wireframe')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SurfaceChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')


    _ElementMap = {
        __extLst.name() : __extLst,
        __bandFmts.name() : __bandFmts,
        __ser.name() : __ser,
        __wireframe.name() : __wireframe,
        __axId.name() : __axId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_SurfaceChart', CT_SurfaceChart)


# Complex type CT_Lvl with content type ELEMENT_ONLY
class CT_Lvl (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Lvl')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pt uses Python identifier pt
    __pt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pt'), 'pt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Lvl_httpschemas_openxmlformats_orgdrawingml2006chartpt', True)

    
    pt = property(__pt.value, __pt.set, None, u'String Point')


    _ElementMap = {
        __pt.name() : __pt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Lvl', CT_Lvl)


# Complex type CT_BubbleScale with content type EMPTY
class CT_BubbleScale (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BubbleScale')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleScale_val', ST_BubbleScale, unicode_default=u'100')
    
    val = property(__val.value, __val.set, None, u'Bubble Scale Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_BubbleScale', CT_BubbleScale)


# Complex type CT_RadarSer with content type ELEMENT_ONLY
class CT_RadarSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RadarSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')


    _ElementMap = {
        __marker.name() : __marker,
        __dLbls.name() : __dLbls,
        __cat.name() : __cat,
        __idx.name() : __idx,
        __val.name() : __val,
        __order.name() : __order,
        __extLst.name() : __extLst,
        __tx.name() : __tx,
        __spPr.name() : __spPr,
        __dPt.name() : __dPt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_RadarSer', CT_RadarSer)


# Complex type CT_ScatterChart with content type ELEMENT_ONLY
class CT_ScatterChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ScatterChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scatterStyle uses Python identifier scatterStyle
    __scatterStyle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scatterStyle'), 'scatterStyle', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartscatterStyle', False)

    
    scatterStyle = property(__scatterStyle.value, __scatterStyle.set, None, u'Scatter Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, u'Vary Colors by Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Scatter Chart Series')


    _ElementMap = {
        __axId.name() : __axId,
        __scatterStyle.name() : __scatterStyle,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __varyColors.name() : __varyColors,
        __ser.name() : __ser
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ScatterChart', CT_ScatterChart)


# Complex type CT_ScatterStyle with content type EMPTY
class CT_ScatterStyle (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ScatterStyle')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterStyle_val', ST_ScatterStyle, unicode_default=u'marker')
    
    val = property(__val.value, __val.set, None, u'Scatter Style Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_ScatterStyle', CT_ScatterStyle)


# Complex type CT_PieSer with content type ELEMENT_ONLY
class CT_PieSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PieSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}explosion uses Python identifier explosion
    __explosion = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'explosion'), 'explosion', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006chartexplosion', False)

    
    explosion = property(__explosion.value, __explosion.set, None, u'Explosion')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PieSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')


    _ElementMap = {
        __spPr.name() : __spPr,
        __idx.name() : __idx,
        __dLbls.name() : __dLbls,
        __cat.name() : __cat,
        __dPt.name() : __dPt,
        __val.name() : __val,
        __order.name() : __order,
        __extLst.name() : __extLst,
        __explosion.name() : __explosion,
        __tx.name() : __tx
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PieSer', CT_PieSer)


# Complex type CT_StrData with content type ELEMENT_ONLY
class CT_StrData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_StrData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrData_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ptCount uses Python identifier ptCount
    __ptCount = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), 'ptCount', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrData_httpschemas_openxmlformats_orgdrawingml2006chartptCount', False)

    
    ptCount = property(__ptCount.value, __ptCount.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pt uses Python identifier pt
    __pt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pt'), 'pt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrData_httpschemas_openxmlformats_orgdrawingml2006chartpt', True)

    
    pt = property(__pt.value, __pt.set, None, None)


    _ElementMap = {
        __extLst.name() : __extLst,
        __ptCount.name() : __ptCount,
        __pt.name() : __pt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_StrData', CT_StrData)


# Complex type CT_RotX with content type EMPTY
class CT_RotX (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RotX')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RotX_val', ST_RotX, unicode_default=u'0')
    
    val = property(__val.value, __val.set, None, u'X Rotation Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_RotX', CT_RotX)


# Complex type CT_DLbl with content type ELEMENT_ONLY
class CT_DLbl (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DLbl')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showCatName uses Python identifier showCatName
    __showCatName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showCatName'), 'showCatName', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowCatName', False)

    
    showCatName = property(__showCatName.value, __showCatName.set, None, u'Show Category Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showSerName uses Python identifier showSerName
    __showSerName = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showSerName'), 'showSerName', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowSerName', False)

    
    showSerName = property(__showSerName.value, __showSerName.set, None, u'Show Series Name')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showPercent uses Python identifier showPercent
    __showPercent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showPercent'), 'showPercent', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowPercent', False)

    
    showPercent = property(__showPercent.value, __showPercent.set, None, u'Show Percent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showBubbleSize uses Python identifier showBubbleSize
    __showBubbleSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize'), 'showBubbleSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowBubbleSize', False)

    
    showBubbleSize = property(__showBubbleSize.value, __showBubbleSize.set, None, u'Show Bubble Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showLegendKey uses Python identifier showLegendKey
    __showLegendKey = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey'), 'showLegendKey', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowLegendKey', False)

    
    showLegendKey = property(__showLegendKey.value, __showLegendKey.set, None, u'Show Legend Key')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLblPos uses Python identifier dLblPos
    __dLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLblPos'), 'dLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartdLblPos', False)

    
    dLblPos = property(__dLblPos.value, __dLblPos.set, None, u'Data Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}separator uses Python identifier separator
    __separator = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'separator'), 'separator', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartseparator', False)

    
    separator = property(__separator.value, __separator.set, None, u'Separator')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showVal uses Python identifier showVal
    __showVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showVal'), 'showVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartshowVal', False)

    
    showVal = property(__showVal.value, __showVal.set, None, u'Show Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DLbl_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')


    _ElementMap = {
        __delete.name() : __delete,
        __idx.name() : __idx,
        __showCatName.name() : __showCatName,
        __spPr.name() : __spPr,
        __showSerName.name() : __showSerName,
        __txPr.name() : __txPr,
        __layout.name() : __layout,
        __showPercent.name() : __showPercent,
        __extLst.name() : __extLst,
        __tx.name() : __tx,
        __showBubbleSize.name() : __showBubbleSize,
        __showLegendKey.name() : __showLegendKey,
        __dLblPos.name() : __dLblPos,
        __separator.name() : __separator,
        __showVal.name() : __showVal,
        __numFmt.name() : __numFmt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DLbl', CT_DLbl)


# Complex type CT_OfPieType with content type EMPTY
class CT_OfPieType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_OfPieType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieType_val', ST_OfPieType, unicode_default=u'pie')
    
    val = property(__val.value, __val.set, None, u'Pie of Pie or Bar of Pie Type Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_OfPieType', CT_OfPieType)


# Complex type CT_ErrDir with content type EMPTY
class CT_ErrDir (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ErrDir')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrDir_val', ST_ErrDir, required=True)
    
    val = property(__val.value, __val.set, None, u'Error Bar Direction Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_ErrDir', CT_ErrDir)


# Complex type CT_ExternalData with content type ELEMENT_ONLY
class CT_ExternalData (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ExternalData')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}autoUpdate uses Python identifier autoUpdate
    __autoUpdate = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'autoUpdate'), 'autoUpdate', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ExternalData_httpschemas_openxmlformats_orgdrawingml2006chartautoUpdate', False)

    
    autoUpdate = property(__autoUpdate.value, __autoUpdate.set, None, u'Update Automatically')

    
    # Attribute {http://schemas.openxmlformats.org/officeDocument/2006/relationships}id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/officeDocument/2006/relationships'), u'id'), 'id', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ExternalData_httpschemas_openxmlformats_orgofficeDocument2006relationshipsid', _r.ST_RelationshipId, required=True)
    
    id = property(__id.value, __id.set, None, u'Relationship ID')


    _ElementMap = {
        __autoUpdate.name() : __autoUpdate
    }
    _AttributeMap = {
        __id.name() : __id
    }
Namespace.addCategoryObject('typeBinding', u'CT_ExternalData', CT_ExternalData)


# Complex type CT_DoughnutChart with content type ELEMENT_ONLY
class CT_DoughnutChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DoughnutChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}holeSize uses Python identifier holeSize
    __holeSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'holeSize'), 'holeSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartholeSize', False)

    
    holeSize = property(__holeSize.value, __holeSize.set, None, u'Hole Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}firstSliceAng uses Python identifier firstSliceAng
    __firstSliceAng = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng'), 'firstSliceAng', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartfirstSliceAng', False)

    
    firstSliceAng = property(__firstSliceAng.value, __firstSliceAng.set, None, u'First Slice Angle')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DoughnutChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Pie Chart Series')


    _ElementMap = {
        __holeSize.name() : __holeSize,
        __dLbls.name() : __dLbls,
        __firstSliceAng.name() : __firstSliceAng,
        __extLst.name() : __extLst,
        __varyColors.name() : __varyColors,
        __ser.name() : __ser
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DoughnutChart', CT_DoughnutChart)


# Complex type CT_Scaling with content type ELEMENT_ONLY
class CT_Scaling (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Scaling')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Scaling_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}logBase uses Python identifier logBase
    __logBase = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'logBase'), 'logBase', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Scaling_httpschemas_openxmlformats_orgdrawingml2006chartlogBase', False)

    
    logBase = property(__logBase.value, __logBase.set, None, u'Logarithmic Base')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}max uses Python identifier max
    __max = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'max'), 'max', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Scaling_httpschemas_openxmlformats_orgdrawingml2006chartmax', False)

    
    max = property(__max.value, __max.set, None, u'Maximum')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}min uses Python identifier min
    __min = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'min'), 'min', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Scaling_httpschemas_openxmlformats_orgdrawingml2006chartmin', False)

    
    min = property(__min.value, __min.set, None, u'Minimum')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'orientation'), 'orientation', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Scaling_httpschemas_openxmlformats_orgdrawingml2006chartorientation', False)

    
    orientation = property(__orientation.value, __orientation.set, None, u'Axis Orientation')


    _ElementMap = {
        __extLst.name() : __extLst,
        __logBase.name() : __logBase,
        __max.name() : __max,
        __min.name() : __min,
        __orientation.name() : __orientation
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Scaling', CT_Scaling)


# Complex type CT_PivotFmts with content type ELEMENT_ONLY
class CT_PivotFmts (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PivotFmts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pivotFmt uses Python identifier pivotFmt
    __pivotFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pivotFmt'), 'pivotFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmts_httpschemas_openxmlformats_orgdrawingml2006chartpivotFmt', True)

    
    pivotFmt = property(__pivotFmt.value, __pivotFmt.set, None, u'Pivot Format')


    _ElementMap = {
        __pivotFmt.name() : __pivotFmt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PivotFmts', CT_PivotFmts)


# Complex type CT_MarkerSize with content type EMPTY
class CT_MarkerSize (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_MarkerSize')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MarkerSize_val', ST_MarkerSize, unicode_default=u'5')
    
    val = property(__val.value, __val.set, None, u'Marker Size Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_MarkerSize', CT_MarkerSize)


# Complex type CT_CustSplit with content type ELEMENT_ONLY
class CT_CustSplit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_CustSplit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}secondPiePt uses Python identifier secondPiePt
    __secondPiePt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'secondPiePt'), 'secondPiePt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CustSplit_httpschemas_openxmlformats_orgdrawingml2006chartsecondPiePt', True)

    
    secondPiePt = property(__secondPiePt.value, __secondPiePt.set, None, u'Second Pie Point')


    _ElementMap = {
        __secondPiePt.name() : __secondPiePt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_CustSplit', CT_CustSplit)


# Complex type CT_LblOffset with content type EMPTY
class CT_LblOffset (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LblOffset')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LblOffset_val', ST_LblOffset, unicode_default=u'100')
    
    val = property(__val.value, __val.set, None, u'Label Offset Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LblOffset', CT_LblOffset)


# Complex type CT_LegendPos with content type EMPTY
class CT_LegendPos (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LegendPos')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LegendPos_val', ST_LegendPos, unicode_default=u'r')
    
    val = property(__val.value, __val.set, None, u'Legend Position Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LegendPos', CT_LegendPos)


# Complex type CT_DispUnits with content type ELEMENT_ONLY
class CT_DispUnits (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DispUnits')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnits_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}custUnit uses Python identifier custUnit
    __custUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'custUnit'), 'custUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnits_httpschemas_openxmlformats_orgdrawingml2006chartcustUnit', False)

    
    custUnit = property(__custUnit.value, __custUnit.set, None, u'Custom Display Unit')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dispUnitsLbl uses Python identifier dispUnitsLbl
    __dispUnitsLbl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dispUnitsLbl'), 'dispUnitsLbl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnits_httpschemas_openxmlformats_orgdrawingml2006chartdispUnitsLbl', False)

    
    dispUnitsLbl = property(__dispUnitsLbl.value, __dispUnitsLbl.set, None, u'Display Units Label')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}builtInUnit uses Python identifier builtInUnit
    __builtInUnit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'builtInUnit'), 'builtInUnit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispUnits_httpschemas_openxmlformats_orgdrawingml2006chartbuiltInUnit', False)

    
    builtInUnit = property(__builtInUnit.value, __builtInUnit.set, None, u'Built in Display Unit Value')


    _ElementMap = {
        __extLst.name() : __extLst,
        __custUnit.name() : __custUnit,
        __dispUnitsLbl.name() : __dispUnitsLbl,
        __builtInUnit.name() : __builtInUnit
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DispUnits', CT_DispUnits)


# Complex type CT_ManualLayout with content type ELEMENT_ONLY
class CT_ManualLayout (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ManualLayout')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layoutTarget uses Python identifier layoutTarget
    __layoutTarget = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layoutTarget'), 'layoutTarget', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartlayoutTarget', False)

    
    layoutTarget = property(__layoutTarget.value, __layoutTarget.set, None, u'Layout Target')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}w uses Python identifier w
    __w = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'w'), 'w', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartw', False)

    
    w = property(__w.value, __w.set, None, u'Width')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}h uses Python identifier h
    __h = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'h'), 'h', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006charth', False)

    
    h = property(__h.value, __h.set, None, u'Height')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}y uses Python identifier y
    __y = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'y'), 'y', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006charty', False)

    
    y = property(__y.value, __y.set, None, u'Top')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}wMode uses Python identifier wMode
    __wMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wMode'), 'wMode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartwMode', False)

    
    wMode = property(__wMode.value, __wMode.set, None, u'Width Mode')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}yMode uses Python identifier yMode
    __yMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'yMode'), 'yMode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartyMode', False)

    
    yMode = property(__yMode.value, __yMode.set, None, u'Top Mode')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}hMode uses Python identifier hMode
    __hMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hMode'), 'hMode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006charthMode', False)

    
    hMode = property(__hMode.value, __hMode.set, None, u'Height Mode')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}x uses Python identifier x
    __x = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'x'), 'x', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartx', False)

    
    x = property(__x.value, __x.set, None, u'Left')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}xMode uses Python identifier xMode
    __xMode = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'xMode'), 'xMode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ManualLayout_httpschemas_openxmlformats_orgdrawingml2006chartxMode', False)

    
    xMode = property(__xMode.value, __xMode.set, None, u'Left Mode')


    _ElementMap = {
        __layoutTarget.name() : __layoutTarget,
        __extLst.name() : __extLst,
        __w.name() : __w,
        __h.name() : __h,
        __y.name() : __y,
        __wMode.name() : __wMode,
        __yMode.name() : __yMode,
        __hMode.name() : __hMode,
        __x.name() : __x,
        __xMode.name() : __xMode
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ManualLayout', CT_ManualLayout)


# Complex type CT_Area3DChart with content type ELEMENT_ONLY
class CT_Area3DChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Area3DChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Grouping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Area Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapDepth uses Python identifier gapDepth
    __gapDepth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), 'gapDepth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgapDepth', False)

    
    gapDepth = property(__gapDepth.value, __gapDepth.set, None, u'Gap Depth')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dropLines uses Python identifier dropLines
    __dropLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), 'dropLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdropLines', False)

    
    dropLines = property(__dropLines.value, __dropLines.set, None, u'Drop Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Area3DChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')


    _ElementMap = {
        __varyColors.name() : __varyColors,
        __grouping.name() : __grouping,
        __ser.name() : __ser,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __gapDepth.name() : __gapDepth,
        __dropLines.name() : __dropLines,
        __axId.name() : __axId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Area3DChart', CT_Area3DChart)


# Complex type CT_LineChart with content type ELEMENT_ONLY
class CT_LineChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LineChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dropLines uses Python identifier dropLines
    __dropLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), 'dropLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartdropLines', False)

    
    dropLines = property(__dropLines.value, __dropLines.set, None, u'Drop Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}smooth uses Python identifier smooth
    __smooth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'smooth'), 'smooth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartsmooth', False)

    
    smooth = property(__smooth.value, __smooth.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Grouping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}hiLowLines uses Python identifier hiLowLines
    __hiLowLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines'), 'hiLowLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006charthiLowLines', False)

    
    hiLowLines = property(__hiLowLines.value, __hiLowLines.set, None, u'High Low Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Show Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}upDownBars uses Python identifier upDownBars
    __upDownBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'upDownBars'), 'upDownBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartupDownBars', False)

    
    upDownBars = property(__upDownBars.value, __upDownBars.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LineChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, None)


    _ElementMap = {
        __axId.name() : __axId,
        __dLbls.name() : __dLbls,
        __dropLines.name() : __dropLines,
        __extLst.name() : __extLst,
        __smooth.name() : __smooth,
        __grouping.name() : __grouping,
        __hiLowLines.name() : __hiLowLines,
        __marker.name() : __marker,
        __varyColors.name() : __varyColors,
        __upDownBars.name() : __upDownBars,
        __ser.name() : __ser
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_LineChart', CT_LineChart)


# Complex type CT_PageSetup with content type EMPTY
class CT_PageSetup (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PageSetup')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute paperSize uses Python identifier paperSize
    __paperSize = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'paperSize'), 'paperSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_paperSize', pyxb.binding.datatypes.unsignedInt, unicode_default=u'1')
    
    paperSize = property(__paperSize.value, __paperSize.set, None, u'Page Size')

    
    # Attribute paperHeight uses Python identifier paperHeight
    __paperHeight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'paperHeight'), 'paperHeight', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_paperHeight', _s.ST_PositiveUniversalMeasure)
    
    paperHeight = property(__paperHeight.value, __paperHeight.set, None, u'Paper Height')

    
    # Attribute draft uses Python identifier draft
    __draft = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'draft'), 'draft', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_draft', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    draft = property(__draft.value, __draft.set, None, u'Draft')

    
    # Attribute useFirstPageNumber uses Python identifier useFirstPageNumber
    __useFirstPageNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'useFirstPageNumber'), 'useFirstPageNumber', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_useFirstPageNumber', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    useFirstPageNumber = property(__useFirstPageNumber.value, __useFirstPageNumber.set, None, u'Use First Page Number')

    
    # Attribute paperWidth uses Python identifier paperWidth
    __paperWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'paperWidth'), 'paperWidth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_paperWidth', _s.ST_PositiveUniversalMeasure)
    
    paperWidth = property(__paperWidth.value, __paperWidth.set, None, u'Paper Width')

    
    # Attribute horizontalDpi uses Python identifier horizontalDpi
    __horizontalDpi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'horizontalDpi'), 'horizontalDpi', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_horizontalDpi', pyxb.binding.datatypes.int, unicode_default=u'600')
    
    horizontalDpi = property(__horizontalDpi.value, __horizontalDpi.set, None, u'Horizontal DPI')

    
    # Attribute firstPageNumber uses Python identifier firstPageNumber
    __firstPageNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'firstPageNumber'), 'firstPageNumber', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_firstPageNumber', pyxb.binding.datatypes.unsignedInt, unicode_default=u'1')
    
    firstPageNumber = property(__firstPageNumber.value, __firstPageNumber.set, None, u'First Page Number')

    
    # Attribute verticalDpi uses Python identifier verticalDpi
    __verticalDpi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'verticalDpi'), 'verticalDpi', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_verticalDpi', pyxb.binding.datatypes.int, unicode_default=u'600')
    
    verticalDpi = property(__verticalDpi.value, __verticalDpi.set, None, u'Vertical DPI')

    
    # Attribute orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'orientation'), 'orientation', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_orientation', ST_PageSetupOrientation, unicode_default=u'default')
    
    orientation = property(__orientation.value, __orientation.set, None, u'Orientation')

    
    # Attribute copies uses Python identifier copies
    __copies = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'copies'), 'copies', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_copies', pyxb.binding.datatypes.unsignedInt, unicode_default=u'1')
    
    copies = property(__copies.value, __copies.set, None, u'Copies')

    
    # Attribute blackAndWhite uses Python identifier blackAndWhite
    __blackAndWhite = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'blackAndWhite'), 'blackAndWhite', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageSetup_blackAndWhite', pyxb.binding.datatypes.boolean, unicode_default=u'false')
    
    blackAndWhite = property(__blackAndWhite.value, __blackAndWhite.set, None, u'Black and White')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __paperSize.name() : __paperSize,
        __paperHeight.name() : __paperHeight,
        __draft.name() : __draft,
        __useFirstPageNumber.name() : __useFirstPageNumber,
        __paperWidth.name() : __paperWidth,
        __horizontalDpi.name() : __horizontalDpi,
        __firstPageNumber.name() : __firstPageNumber,
        __verticalDpi.name() : __verticalDpi,
        __orientation.name() : __orientation,
        __copies.name() : __copies,
        __blackAndWhite.name() : __blackAndWhite
    }
Namespace.addCategoryObject('typeBinding', u'CT_PageSetup', CT_PageSetup)


# Complex type CT_MultiLvlStrRef with content type ELEMENT_ONLY
class CT_MultiLvlStrRef (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_MultiLvlStrRef')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrRef_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}f uses Python identifier f
    __f = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'f'), 'f', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrRef_httpschemas_openxmlformats_orgdrawingml2006chartf', False)

    
    f = property(__f.value, __f.set, None, u'Formula')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}multiLvlStrCache uses Python identifier multiLvlStrCache
    __multiLvlStrCache = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrCache'), 'multiLvlStrCache', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MultiLvlStrRef_httpschemas_openxmlformats_orgdrawingml2006chartmultiLvlStrCache', False)

    
    multiLvlStrCache = property(__multiLvlStrCache.value, __multiLvlStrCache.set, None, u'Multi Level String Cache')


    _ElementMap = {
        __extLst.name() : __extLst,
        __f.name() : __f,
        __multiLvlStrCache.name() : __multiLvlStrCache
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_MultiLvlStrRef', CT_MultiLvlStrRef)


# Complex type CT_CatAx with content type ELEMENT_ONLY
class CT_CatAx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_CatAx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartaxId', False)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scaling uses Python identifier scaling
    __scaling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scaling'), 'scaling', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartscaling', False)

    
    scaling = property(__scaling.value, __scaling.set, None, u'Scaling')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorGridlines uses Python identifier minorGridlines
    __minorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), 'minorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartminorGridlines', False)

    
    minorGridlines = property(__minorGridlines.value, __minorGridlines.set, None, u'Minor Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorGridlines uses Python identifier majorGridlines
    __majorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), 'majorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorGridlines', False)

    
    majorGridlines = property(__majorGridlines.value, __majorGridlines.set, None, u'Major Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006charttitle', False)

    
    title = property(__title.value, __title.set, None, u'Title')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lblOffset uses Python identifier lblOffset
    __lblOffset = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lblOffset'), 'lblOffset', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartlblOffset', False)

    
    lblOffset = property(__lblOffset.value, __lblOffset.set, None, u'Label Offset')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorTickMark uses Python identifier majorTickMark
    __majorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), 'majorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorTickMark', False)

    
    majorTickMark = property(__majorTickMark.value, __majorTickMark.set, None, u'Major Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorTickMark uses Python identifier minorTickMark
    __minorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), 'minorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartminorTickMark', False)

    
    minorTickMark = property(__minorTickMark.value, __minorTickMark.set, None, u'Minor Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblSkip uses Python identifier tickLblSkip
    __tickLblSkip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip'), 'tickLblSkip', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblSkip', False)

    
    tickLblSkip = property(__tickLblSkip.value, __tickLblSkip.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickMarkSkip uses Python identifier tickMarkSkip
    __tickMarkSkip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip'), 'tickMarkSkip', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006charttickMarkSkip', False)

    
    tickMarkSkip = property(__tickMarkSkip.value, __tickMarkSkip.set, None, u'Tick Mark Skip')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}noMultiLvlLbl uses Python identifier noMultiLvlLbl
    __noMultiLvlLbl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'noMultiLvlLbl'), 'noMultiLvlLbl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartnoMultiLvlLbl', False)

    
    noMultiLvlLbl = property(__noMultiLvlLbl.value, __noMultiLvlLbl.set, None, u'No Multi-level Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblPos uses Python identifier tickLblPos
    __tickLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), 'tickLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblPos', False)

    
    tickLblPos = property(__tickLblPos.value, __tickLblPos.set, None, u'Tick Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossAx uses Python identifier crossAx
    __crossAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), 'crossAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossAx', False)

    
    crossAx = property(__crossAx.value, __crossAx.set, None, u'Crossing Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axPos uses Python identifier axPos
    __axPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axPos'), 'axPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartaxPos', False)

    
    axPos = property(__axPos.value, __axPos.set, None, u'Axis Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crosses'), 'crosses', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartcrosses', False)

    
    crosses = property(__crosses.value, __crosses.set, None, u'Crosses')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lblAlgn uses Python identifier lblAlgn
    __lblAlgn = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lblAlgn'), 'lblAlgn', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartlblAlgn', False)

    
    lblAlgn = property(__lblAlgn.value, __lblAlgn.set, None, u'Label Alignment')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossesAt uses Python identifier crossesAt
    __crossesAt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), 'crossesAt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossesAt', False)

    
    crossesAt = property(__crossesAt.value, __crossesAt.set, None, u'Crossing Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}auto uses Python identifier auto
    __auto = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'auto'), 'auto', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CatAx_httpschemas_openxmlformats_orgdrawingml2006chartauto', False)

    
    auto = property(__auto.value, __auto.set, None, u'Automatic Category Axis')


    _ElementMap = {
        __axId.name() : __axId,
        __extLst.name() : __extLst,
        __scaling.name() : __scaling,
        __minorGridlines.name() : __minorGridlines,
        __delete.name() : __delete,
        __majorGridlines.name() : __majorGridlines,
        __title.name() : __title,
        __lblOffset.name() : __lblOffset,
        __numFmt.name() : __numFmt,
        __majorTickMark.name() : __majorTickMark,
        __minorTickMark.name() : __minorTickMark,
        __tickLblSkip.name() : __tickLblSkip,
        __tickMarkSkip.name() : __tickMarkSkip,
        __spPr.name() : __spPr,
        __noMultiLvlLbl.name() : __noMultiLvlLbl,
        __txPr.name() : __txPr,
        __tickLblPos.name() : __tickLblPos,
        __crossAx.name() : __crossAx,
        __axPos.name() : __axPos,
        __crosses.name() : __crosses,
        __lblAlgn.name() : __lblAlgn,
        __crossesAt.name() : __crossesAt,
        __auto.name() : __auto
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_CatAx', CT_CatAx)


# Complex type CT_Period with content type EMPTY
class CT_Period (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Period')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Period_val', ST_Period, unicode_default=u'2')
    
    val = property(__val.value, __val.set, None, u'Period Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Period', CT_Period)


# Complex type CT_OfPieChart with content type ELEMENT_ONLY
class CT_OfPieChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_OfPieChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}splitPos uses Python identifier splitPos
    __splitPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'splitPos'), 'splitPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartsplitPos', False)

    
    splitPos = property(__splitPos.value, __splitPos.set, None, u'Split Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Pie Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapWidth uses Python identifier gapWidth
    __gapWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), 'gapWidth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartgapWidth', False)

    
    gapWidth = property(__gapWidth.value, __gapWidth.set, None, u'Gap Width')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ofPieType uses Python identifier ofPieType
    __ofPieType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ofPieType'), 'ofPieType', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartofPieType', False)

    
    ofPieType = property(__ofPieType.value, __ofPieType.set, None, u'Pie of Pie or Bar of Pie Type')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}secondPieSize uses Python identifier secondPieSize
    __secondPieSize = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'secondPieSize'), 'secondPieSize', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartsecondPieSize', False)

    
    secondPieSize = property(__secondPieSize.value, __secondPieSize.set, None, u'Second Pie Size')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}custSplit uses Python identifier custSplit
    __custSplit = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'custSplit'), 'custSplit', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartcustSplit', False)

    
    custSplit = property(__custSplit.value, __custSplit.set, None, u'Custom Split')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}serLines uses Python identifier serLines
    __serLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'serLines'), 'serLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartserLines', True)

    
    serLines = property(__serLines.value, __serLines.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}splitType uses Python identifier splitType
    __splitType = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'splitType'), 'splitType', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_OfPieChart_httpschemas_openxmlformats_orgdrawingml2006chartsplitType', False)

    
    splitType = property(__splitType.value, __splitType.set, None, u'Split Type')


    _ElementMap = {
        __splitPos.name() : __splitPos,
        __ser.name() : __ser,
        __gapWidth.name() : __gapWidth,
        __varyColors.name() : __varyColors,
        __ofPieType.name() : __ofPieType,
        __secondPieSize.name() : __secondPieSize,
        __custSplit.name() : __custSplit,
        __serLines.name() : __serLines,
        __dLbls.name() : __dLbls,
        __extLst.name() : __extLst,
        __splitType.name() : __splitType
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_OfPieChart', CT_OfPieChart)


# Complex type CT_HoleSize with content type EMPTY
class CT_HoleSize (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_HoleSize')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_HoleSize_val', ST_HoleSize, unicode_default=u'10')
    
    val = property(__val.value, __val.set, None, u'Hole Size Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_HoleSize', CT_HoleSize)


# Complex type CT_BarSer with content type ELEMENT_ONLY
class CT_BarSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BarSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}invertIfNegative uses Python identifier invertIfNegative
    __invertIfNegative = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), 'invertIfNegative', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartinvertIfNegative', False)

    
    invertIfNegative = property(__invertIfNegative.value, __invertIfNegative.set, None, u'Invert if Negative')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}cat uses Python identifier cat
    __cat = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'cat'), 'cat', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartcat', False)

    
    cat = property(__cat.value, __cat.set, None, u'Category Axis Data')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}val uses Python identifier val
    __val = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartval', False)

    
    val = property(__val.value, __val.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBars uses Python identifier errBars
    __errBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBars'), 'errBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006charterrBars', False)

    
    errBars = property(__errBars.value, __errBars.set, None, u'Error Bars')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendline uses Python identifier trendline
    __trendline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendline'), 'trendline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006charttrendline', True)

    
    trendline = property(__trendline.value, __trendline.set, None, u'Trendlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shape'), 'shape', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartshape', False)

    
    shape = property(__shape.value, __shape.set, None, u'Shape')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureOptions uses Python identifier pictureOptions
    __pictureOptions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), 'pictureOptions', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BarSer_httpschemas_openxmlformats_orgdrawingml2006chartpictureOptions', False)

    
    pictureOptions = property(__pictureOptions.value, __pictureOptions.set, None, None)


    _ElementMap = {
        __invertIfNegative.name() : __invertIfNegative,
        __idx.name() : __idx,
        __cat.name() : __cat,
        __order.name() : __order,
        __val.name() : __val,
        __dPt.name() : __dPt,
        __errBars.name() : __errBars,
        __dLbls.name() : __dLbls,
        __spPr.name() : __spPr,
        __tx.name() : __tx,
        __extLst.name() : __extLst,
        __trendline.name() : __trendline,
        __shape.name() : __shape,
        __pictureOptions.name() : __pictureOptions
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BarSer', CT_BarSer)


# Complex type CT_Surface with content type ELEMENT_ONLY
class CT_Surface (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Surface')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'thickness'), 'thickness', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface_httpschemas_openxmlformats_orgdrawingml2006chartthickness', False)

    
    thickness = property(__thickness.value, __thickness.set, None, u'Thickness')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pictureOptions uses Python identifier pictureOptions
    __pictureOptions = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), 'pictureOptions', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface_httpschemas_openxmlformats_orgdrawingml2006chartpictureOptions', False)

    
    pictureOptions = property(__pictureOptions.value, __pictureOptions.set, None, u'Picture Options')


    _ElementMap = {
        __extLst.name() : __extLst,
        __thickness.name() : __thickness,
        __spPr.name() : __spPr,
        __pictureOptions.name() : __pictureOptions
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Surface', CT_Surface)


# Complex type CT_StrVal with content type ELEMENT_ONLY
class CT_StrVal (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_StrVal')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}v uses Python identifier v
    __v = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'v'), 'v', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrVal_httpschemas_openxmlformats_orgdrawingml2006chartv', False)

    
    v = property(__v.value, __v.set, None, u'Text Value')

    
    # Attribute idx uses Python identifier idx
    __idx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StrVal_idx', pyxb.binding.datatypes.unsignedInt, required=True)
    
    idx = property(__idx.value, __idx.set, None, u'Index')


    _ElementMap = {
        __v.name() : __v
    }
    _AttributeMap = {
        __idx.name() : __idx
    }
Namespace.addCategoryObject('typeBinding', u'CT_StrVal', CT_StrVal)


# Complex type CT_DispBlanksAs with content type EMPTY
class CT_DispBlanksAs (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DispBlanksAs')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DispBlanksAs_val', ST_DispBlanksAs, unicode_default=u'zero')
    
    val = property(__val.value, __val.set, None, u'Display Blanks As Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_DispBlanksAs', CT_DispBlanksAs)


# Complex type CT_Pie3DChart with content type ELEMENT_ONLY
class CT_Pie3DChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Pie3DChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Pie3DChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Pie3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Pie3DChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Pie3DChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Pie Chart Series')


    _ElementMap = {
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __varyColors.name() : __varyColors,
        __ser.name() : __ser
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Pie3DChart', CT_Pie3DChart)


# Complex type CT_RadarChart with content type ELEMENT_ONLY
class CT_RadarChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RadarChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}radarStyle uses Python identifier radarStyle
    __radarStyle = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'radarStyle'), 'radarStyle', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartradarStyle', False)

    
    radarStyle = property(__radarStyle.value, __radarStyle.set, None, u'Radar Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Radar Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RadarChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')


    _ElementMap = {
        __extLst.name() : __extLst,
        __radarStyle.name() : __radarStyle,
        __varyColors.name() : __varyColors,
        __ser.name() : __ser,
        __dLbls.name() : __dLbls,
        __axId.name() : __axId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_RadarChart', CT_RadarChart)


# Complex type CT_DTable with content type ELEMENT_ONLY
class CT_DTable (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DTable')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showVertBorder uses Python identifier showVertBorder
    __showVertBorder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showVertBorder'), 'showVertBorder', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartshowVertBorder', False)

    
    showVertBorder = property(__showVertBorder.value, __showVertBorder.set, None, u'Show Vertical Border')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showOutline uses Python identifier showOutline
    __showOutline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showOutline'), 'showOutline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartshowOutline', False)

    
    showOutline = property(__showOutline.value, __showOutline.set, None, u'Show Outline Border')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showKeys uses Python identifier showKeys
    __showKeys = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showKeys'), 'showKeys', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartshowKeys', False)

    
    showKeys = property(__showKeys.value, __showKeys.set, None, u'Show Legend Keys')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, u'Text Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showHorzBorder uses Python identifier showHorzBorder
    __showHorzBorder = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showHorzBorder'), 'showHorzBorder', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DTable_httpschemas_openxmlformats_orgdrawingml2006chartshowHorzBorder', False)

    
    showHorzBorder = property(__showHorzBorder.value, __showHorzBorder.set, None, u'Show Horizontal Border')


    _ElementMap = {
        __showVertBorder.name() : __showVertBorder,
        __extLst.name() : __extLst,
        __showOutline.name() : __showOutline,
        __showKeys.name() : __showKeys,
        __spPr.name() : __spPr,
        __txPr.name() : __txPr,
        __showHorzBorder.name() : __showHorzBorder
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_DTable', CT_DTable)


# Complex type CT_NumRef with content type ELEMENT_ONLY
class CT_NumRef (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_NumRef')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumRef_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}f uses Python identifier f
    __f = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'f'), 'f', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumRef_httpschemas_openxmlformats_orgdrawingml2006chartf', False)

    
    f = property(__f.value, __f.set, None, u'Formula')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numCache uses Python identifier numCache
    __numCache = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numCache'), 'numCache', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumRef_httpschemas_openxmlformats_orgdrawingml2006chartnumCache', False)

    
    numCache = property(__numCache.value, __numCache.set, None, u'Number Cache')


    _ElementMap = {
        __extLst.name() : __extLst,
        __f.name() : __f,
        __numCache.name() : __numCache
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_NumRef', CT_NumRef)


# Complex type CT_BubbleChart with content type ELEMENT_ONLY
class CT_BubbleChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BubbleChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showNegBubbles uses Python identifier showNegBubbles
    __showNegBubbles = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showNegBubbles'), 'showNegBubbles', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartshowNegBubbles', False)

    
    showNegBubbles = property(__showNegBubbles.value, __showNegBubbles.set, None, u'Show Negative Bubbles')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}sizeRepresents uses Python identifier sizeRepresents
    __sizeRepresents = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sizeRepresents'), 'sizeRepresents', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartsizeRepresents', False)

    
    sizeRepresents = property(__sizeRepresents.value, __sizeRepresents.set, None, u'Size Represents')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Bubble Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubble3D uses Python identifier bubble3D
    __bubble3D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), 'bubble3D', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartbubble3D', False)

    
    bubble3D = property(__bubble3D.value, __bubble3D.set, None, u'3D Bubble')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bubbleScale uses Python identifier bubbleScale
    __bubbleScale = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bubbleScale'), 'bubbleScale', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BubbleChart_httpschemas_openxmlformats_orgdrawingml2006chartbubbleScale', False)

    
    bubbleScale = property(__bubbleScale.value, __bubbleScale.set, None, u'Bubble Scale')


    _ElementMap = {
        __showNegBubbles.name() : __showNegBubbles,
        __sizeRepresents.name() : __sizeRepresents,
        __ser.name() : __ser,
        __axId.name() : __axId,
        __dLbls.name() : __dLbls,
        __varyColors.name() : __varyColors,
        __extLst.name() : __extLst,
        __bubble3D.name() : __bubble3D,
        __bubbleScale.name() : __bubbleScale
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BubbleChart', CT_BubbleChart)


# Complex type CT_SplitType with content type EMPTY
class CT_SplitType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SplitType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SplitType_val', ST_SplitType, unicode_default=u'auto')
    
    val = property(__val.value, __val.set, None, u'Split Type Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_SplitType', CT_SplitType)


# Complex type CT_BandFmts with content type ELEMENT_ONLY
class CT_BandFmts (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_BandFmts')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bandFmt uses Python identifier bandFmt
    __bandFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bandFmt'), 'bandFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_BandFmts_httpschemas_openxmlformats_orgdrawingml2006chartbandFmt', True)

    
    bandFmt = property(__bandFmt.value, __bandFmt.set, None, u'Band Format')


    _ElementMap = {
        __bandFmt.name() : __bandFmt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_BandFmts', CT_BandFmts)


# Complex type CT_SizeRepresents with content type EMPTY
class CT_SizeRepresents (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SizeRepresents')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SizeRepresents_val', ST_SizeRepresents, unicode_default=u'area')
    
    val = property(__val.value, __val.set, None, u'Size Represents Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_SizeRepresents', CT_SizeRepresents)


# Complex type CT_NumVal with content type ELEMENT_ONLY
class CT_NumVal (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_NumVal')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}v uses Python identifier v
    __v = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'v'), 'v', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumVal_httpschemas_openxmlformats_orgdrawingml2006chartv', False)

    
    v = property(__v.value, __v.set, None, u'Numeric Value')

    
    # Attribute formatCode uses Python identifier formatCode
    __formatCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'formatCode'), 'formatCode', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumVal_formatCode', _s.ST_Xstring)
    
    formatCode = property(__formatCode.value, __formatCode.set, None, u'Number Format')

    
    # Attribute idx uses Python identifier idx
    __idx = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_NumVal_idx', pyxb.binding.datatypes.unsignedInt, required=True)
    
    idx = property(__idx.value, __idx.set, None, u'Index')


    _ElementMap = {
        __v.name() : __v
    }
    _AttributeMap = {
        __formatCode.name() : __formatCode,
        __idx.name() : __idx
    }
Namespace.addCategoryObject('typeBinding', u'CT_NumVal', CT_NumVal)


# Complex type CT_ScatterSer with content type ELEMENT_ONLY
class CT_ScatterSer (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ScatterSer')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}yVal uses Python identifier yVal
    __yVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'yVal'), 'yVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartyVal', False)

    
    yVal = property(__yVal.value, __yVal.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dPt uses Python identifier dPt
    __dPt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dPt'), 'dPt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartdPt', True)

    
    dPt = property(__dPt.value, __dPt.set, None, u'Data Point')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}smooth uses Python identifier smooth
    __smooth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'smooth'), 'smooth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartsmooth', False)

    
    smooth = property(__smooth.value, __smooth.set, None, u'Smoothing')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}order uses Python identifier order
    __order = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'order'), 'order', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartorder', False)

    
    order = property(__order.value, __order.set, None, u'Order')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}trendline uses Python identifier trendline
    __trendline = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'trendline'), 'trendline', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006charttrendline', True)

    
    trendline = property(__trendline.value, __trendline.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, u'Series Text')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}errBars uses Python identifier errBars
    __errBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'errBars'), 'errBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006charterrBars', True)

    
    errBars = property(__errBars.value, __errBars.set, None, u'Error Bars')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}xVal uses Python identifier xVal
    __xVal = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'xVal'), 'xVal', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ScatterSer_httpschemas_openxmlformats_orgdrawingml2006chartxVal', False)

    
    xVal = property(__xVal.value, __xVal.set, None, None)


    _ElementMap = {
        __yVal.name() : __yVal,
        __dPt.name() : __dPt,
        __smooth.name() : __smooth,
        __idx.name() : __idx,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls,
        __order.name() : __order,
        __marker.name() : __marker,
        __trendline.name() : __trendline,
        __tx.name() : __tx,
        __errBars.name() : __errBars,
        __spPr.name() : __spPr,
        __xVal.name() : __xVal
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ScatterSer', CT_ScatterSer)


# Complex type CT_MarkerStyle with content type EMPTY
class CT_MarkerStyle (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_MarkerStyle')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_MarkerStyle_val', ST_MarkerStyle, required=True)
    
    val = property(__val.value, __val.set, None, u'Marker Style Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_MarkerStyle', CT_MarkerStyle)


# Complex type CT_LblAlgn with content type EMPTY
class CT_LblAlgn (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LblAlgn')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LblAlgn_val', ST_LblAlgn, required=True)
    
    val = property(__val.value, __val.set, None, u'Label Alignment Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LblAlgn', CT_LblAlgn)


# Complex type CT_LayoutTarget with content type EMPTY
class CT_LayoutTarget (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LayoutTarget')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LayoutTarget_val', ST_LayoutTarget, unicode_default=u'outer')
    
    val = property(__val.value, __val.set, None, u'Layout Target Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_LayoutTarget', CT_LayoutTarget)


# Complex type CT_DepthPercent with content type EMPTY
class CT_DepthPercent (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_DepthPercent')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_DepthPercent_val', ST_DepthPercent, unicode_default=u'100')
    
    val = property(__val.value, __val.set, None, u'Depth Percent Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_DepthPercent', CT_DepthPercent)


# Complex type CT_Style with content type EMPTY
class CT_Style (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Style')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Style_val', ST_Style, required=True)
    
    val = property(__val.value, __val.set, None, u'Style Type')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Style', CT_Style)


# Complex type CT_TrendlineLbl with content type ELEMENT_ONLY
class CT_TrendlineLbl (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TrendlineLbl')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tx uses Python identifier tx
    __tx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tx'), 'tx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006charttx', False)

    
    tx = property(__tx.value, __tx.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TrendlineLbl_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')


    _ElementMap = {
        __spPr.name() : __spPr,
        __txPr.name() : __txPr,
        __extLst.name() : __extLst,
        __layout.name() : __layout,
        __tx.name() : __tx,
        __numFmt.name() : __numFmt
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_TrendlineLbl', CT_TrendlineLbl)


# Complex type CT_AreaChart with content type ELEMENT_ONLY
class CT_AreaChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_AreaChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Area Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dropLines uses Python identifier dropLines
    __dropLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), 'dropLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartdropLines', False)

    
    dropLines = property(__dropLines.value, __dropLines.set, None, u'Drop Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Grouping')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_AreaChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)


    _ElementMap = {
        __ser.name() : __ser,
        __axId.name() : __axId,
        __extLst.name() : __extLst,
        __dropLines.name() : __dropLines,
        __dLbls.name() : __dLbls,
        __grouping.name() : __grouping,
        __varyColors.name() : __varyColors
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_AreaChart', CT_AreaChart)


# Complex type CT_PageMargins with content type EMPTY
class CT_PageMargins (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PageMargins')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute header uses Python identifier header
    __header = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'header'), 'header', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_header', pyxb.binding.datatypes.double, required=True)
    
    header = property(__header.value, __header.set, None, u'Header')

    
    # Attribute footer uses Python identifier footer
    __footer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'footer'), 'footer', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_footer', pyxb.binding.datatypes.double, required=True)
    
    footer = property(__footer.value, __footer.set, None, u'Footer')

    
    # Attribute l uses Python identifier l
    __l = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'l'), 'l', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_l', pyxb.binding.datatypes.double, required=True)
    
    l = property(__l.value, __l.set, None, u'Left')

    
    # Attribute r uses Python identifier r
    __r = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'r'), 'r', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_r', pyxb.binding.datatypes.double, required=True)
    
    r = property(__r.value, __r.set, None, u'Right')

    
    # Attribute b uses Python identifier b
    __b = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'b'), 'b', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_b', pyxb.binding.datatypes.double, required=True)
    
    b = property(__b.value, __b.set, None, u'Bottom')

    
    # Attribute t uses Python identifier t
    __t = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't'), 't', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PageMargins_t', pyxb.binding.datatypes.double, required=True)
    
    t = property(__t.value, __t.set, None, u'Top')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __header.name() : __header,
        __footer.name() : __footer,
        __l.name() : __l,
        __r.name() : __r,
        __b.name() : __b,
        __t.name() : __t
    }
Namespace.addCategoryObject('typeBinding', u'CT_PageMargins', CT_PageMargins)


# Complex type CT_RotY with content type EMPTY
class CT_RotY (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_RotY')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_RotY_val', ST_RotY, unicode_default=u'0')
    
    val = property(__val.value, __val.set, None, u'Y Rotation Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_RotY', CT_RotY)


# Complex type CT_ErrValType with content type EMPTY
class CT_ErrValType (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ErrValType')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ErrValType_val', ST_ErrValType, unicode_default=u'fixedVal')
    
    val = property(__val.value, __val.set, None, u'Error Bar Type Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_ErrValType', CT_ErrValType)


# Complex type CT_Order with content type EMPTY
class CT_Order (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Order')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Order_val', ST_Order, unicode_default=u'2')
    
    val = property(__val.value, __val.set, None, u'Order Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Order', CT_Order)


# Complex type CT_Chart with content type ELEMENT_ONLY
class CT_Chart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Chart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}view3D uses Python identifier view3D
    __view3D = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'view3D'), 'view3D', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartview3D', False)

    
    view3D = property(__view3D.value, __view3D.set, None, u'View In 3D')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}showDLblsOverMax uses Python identifier showDLblsOverMax
    __showDLblsOverMax = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'showDLblsOverMax'), 'showDLblsOverMax', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartshowDLblsOverMax', False)

    
    showDLblsOverMax = property(__showDLblsOverMax.value, __showDLblsOverMax.set, None, u'Show Data Labels over Maximum')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}plotVisOnly uses Python identifier plotVisOnly
    __plotVisOnly = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'plotVisOnly'), 'plotVisOnly', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartplotVisOnly', False)

    
    plotVisOnly = property(__plotVisOnly.value, __plotVisOnly.set, None, u'Plot Visible Only')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}floor uses Python identifier floor
    __floor = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'floor'), 'floor', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartfloor', False)

    
    floor = property(__floor.value, __floor.set, None, u'Floor')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dispBlanksAs uses Python identifier dispBlanksAs
    __dispBlanksAs = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dispBlanksAs'), 'dispBlanksAs', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartdispBlanksAs', False)

    
    dispBlanksAs = property(__dispBlanksAs.value, __dispBlanksAs.set, None, u'Display Blanks As')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}sideWall uses Python identifier sideWall
    __sideWall = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'sideWall'), 'sideWall', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartsideWall', False)

    
    sideWall = property(__sideWall.value, __sideWall.set, None, u'Side Wall')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}legend uses Python identifier legend
    __legend = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legend'), 'legend', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartlegend', False)

    
    legend = property(__legend.value, __legend.set, None, u'Legend')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006charttitle', False)

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}backWall uses Python identifier backWall
    __backWall = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'backWall'), 'backWall', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartbackWall', False)

    
    backWall = property(__backWall.value, __backWall.set, None, u'Back Wall')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}autoTitleDeleted uses Python identifier autoTitleDeleted
    __autoTitleDeleted = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'autoTitleDeleted'), 'autoTitleDeleted', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartautoTitleDeleted', False)

    
    autoTitleDeleted = property(__autoTitleDeleted.value, __autoTitleDeleted.set, None, u'Auto Title Is Deleted')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}plotArea uses Python identifier plotArea
    __plotArea = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'plotArea'), 'plotArea', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartplotArea', False)

    
    plotArea = property(__plotArea.value, __plotArea.set, None, u'Plot Area')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pivotFmts uses Python identifier pivotFmts
    __pivotFmts = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pivotFmts'), 'pivotFmts', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Chart_httpschemas_openxmlformats_orgdrawingml2006chartpivotFmts', False)

    
    pivotFmts = property(__pivotFmts.value, __pivotFmts.set, None, u'Pivot Formats')


    _ElementMap = {
        __view3D.name() : __view3D,
        __showDLblsOverMax.name() : __showDLblsOverMax,
        __plotVisOnly.name() : __plotVisOnly,
        __floor.name() : __floor,
        __dispBlanksAs.name() : __dispBlanksAs,
        __sideWall.name() : __sideWall,
        __legend.name() : __legend,
        __title.name() : __title,
        __backWall.name() : __backWall,
        __autoTitleDeleted.name() : __autoTitleDeleted,
        __extLst.name() : __extLst,
        __plotArea.name() : __plotArea,
        __pivotFmts.name() : __pivotFmts
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Chart', CT_Chart)


# Complex type CT_Orientation with content type EMPTY
class CT_Orientation (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Orientation')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Orientation_val', ST_Orientation, unicode_default=u'minMax')
    
    val = property(__val.value, __val.set, None, u'Orientation Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Orientation', CT_Orientation)


# Complex type CT_Bar3DChart with content type ELEMENT_ONLY
class CT_Bar3DChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Bar3DChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}varyColors uses Python identifier varyColors
    __varyColors = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), 'varyColors', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartvaryColors', False)

    
    varyColors = property(__varyColors.value, __varyColors.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapDepth uses Python identifier gapDepth
    __gapDepth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), 'gapDepth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgapDepth', False)

    
    gapDepth = property(__gapDepth.value, __gapDepth.set, None, u'Gap Depth')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}shape uses Python identifier shape
    __shape = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'shape'), 'shape', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartshape', False)

    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Bar Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}gapWidth uses Python identifier gapWidth
    __gapWidth = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), 'gapWidth', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgapWidth', False)

    
    gapWidth = property(__gapWidth.value, __gapWidth.set, None, u'Gap Width')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}barDir uses Python identifier barDir
    __barDir = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'barDir'), 'barDir', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartbarDir', False)

    
    barDir = property(__barDir.value, __barDir.set, None, u'Bar Direction')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}grouping uses Python identifier grouping
    __grouping = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'grouping'), 'grouping', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Bar3DChart_httpschemas_openxmlformats_orgdrawingml2006chartgrouping', False)

    
    grouping = property(__grouping.value, __grouping.set, None, u'Bar Grouping')


    _ElementMap = {
        __varyColors.name() : __varyColors,
        __gapDepth.name() : __gapDepth,
        __shape.name() : __shape,
        __ser.name() : __ser,
        __axId.name() : __axId,
        __gapWidth.name() : __gapWidth,
        __dLbls.name() : __dLbls,
        __extLst.name() : __extLst,
        __barDir.name() : __barDir,
        __grouping.name() : __grouping
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Bar3DChart', CT_Bar3DChart)


# Complex type CT_Protection with content type ELEMENT_ONLY
class CT_Protection (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Protection')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}userInterface uses Python identifier userInterface
    __userInterface = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'userInterface'), 'userInterface', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Protection_httpschemas_openxmlformats_orgdrawingml2006chartuserInterface', False)

    
    userInterface = property(__userInterface.value, __userInterface.set, None, u'User Interface')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}chartObject uses Python identifier chartObject
    __chartObject = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'chartObject'), 'chartObject', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Protection_httpschemas_openxmlformats_orgdrawingml2006chartchartObject', False)

    
    chartObject = property(__chartObject.value, __chartObject.set, None, u'Chart Object')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}selection uses Python identifier selection
    __selection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'selection'), 'selection', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Protection_httpschemas_openxmlformats_orgdrawingml2006chartselection', False)

    
    selection = property(__selection.value, __selection.set, None, u'Selection')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}formatting uses Python identifier formatting
    __formatting = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'formatting'), 'formatting', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Protection_httpschemas_openxmlformats_orgdrawingml2006chartformatting', False)

    
    formatting = property(__formatting.value, __formatting.set, None, u'Formatting')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}data uses Python identifier data
    __data = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'data'), 'data', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Protection_httpschemas_openxmlformats_orgdrawingml2006chartdata', False)

    
    data = property(__data.value, __data.set, None, u'Data Cannot Be Changed')


    _ElementMap = {
        __userInterface.name() : __userInterface,
        __chartObject.name() : __chartObject,
        __selection.name() : __selection,
        __formatting.name() : __formatting,
        __data.name() : __data
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Protection', CT_Protection)


# Complex type CT_PictureStackUnit with content type EMPTY
class CT_PictureStackUnit (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PictureStackUnit')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PictureStackUnit_val', ST_PictureStackUnit, required=True)
    
    val = property(__val.value, __val.set, None, u'Picture Stack Unit')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_PictureStackUnit', CT_PictureStackUnit)


# Complex type CT_Overlap with content type EMPTY
class CT_Overlap (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Overlap')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Overlap_val', ST_Overlap, unicode_default=u'0')
    
    val = property(__val.value, __val.set, None, u'Overlap Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Overlap', CT_Overlap)


# Complex type CT_Legend with content type ELEMENT_ONLY
class CT_Legend (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Legend')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}overlay uses Python identifier overlay
    __overlay = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'overlay'), 'overlay', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartoverlay', False)

    
    overlay = property(__overlay.value, __overlay.set, None, u'Overlay')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}layout uses Python identifier layout
    __layout = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'layout'), 'layout', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartlayout', False)

    
    layout = property(__layout.value, __layout.set, None, u'Layout')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}legendPos uses Python identifier legendPos
    __legendPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legendPos'), 'legendPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartlegendPos', False)

    
    legendPos = property(__legendPos.value, __legendPos.set, None, u'Legend Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}legendEntry uses Python identifier legendEntry
    __legendEntry = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'legendEntry'), 'legendEntry', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Legend_httpschemas_openxmlformats_orgdrawingml2006chartlegendEntry', True)

    
    legendEntry = property(__legendEntry.value, __legendEntry.set, None, u'Legend Entry')


    _ElementMap = {
        __overlay.name() : __overlay,
        __layout.name() : __layout,
        __spPr.name() : __spPr,
        __txPr.name() : __txPr,
        __legendPos.name() : __legendPos,
        __extLst.name() : __extLst,
        __legendEntry.name() : __legendEntry
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Legend', CT_Legend)


# Complex type CT_CrossBetween with content type EMPTY
class CT_CrossBetween (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_CrossBetween')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_CrossBetween_val', ST_CrossBetween, required=True)
    
    val = property(__val.value, __val.set, None, u'Cross Between Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_CrossBetween', CT_CrossBetween)


# Complex type CT_StockChart with content type ELEMENT_ONLY
class CT_StockChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_StockChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dropLines uses Python identifier dropLines
    __dropLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), 'dropLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartdropLines', False)

    
    dropLines = property(__dropLines.value, __dropLines.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}hiLowLines uses Python identifier hiLowLines
    __hiLowLines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines'), 'hiLowLines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006charthiLowLines', False)

    
    hiLowLines = property(__hiLowLines.value, __hiLowLines.set, None, u'High Low Lines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}upDownBars uses Python identifier upDownBars
    __upDownBars = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'upDownBars'), 'upDownBars', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartupDownBars', False)

    
    upDownBars = property(__upDownBars.value, __upDownBars.set, None, u'Up/Down Bars')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Line Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbls uses Python identifier dLbls
    __dLbls = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), 'dLbls', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_StockChart_httpschemas_openxmlformats_orgdrawingml2006chartdLbls', False)

    
    dLbls = property(__dLbls.value, __dLbls.set, None, u'Data Labels')


    _ElementMap = {
        __dropLines.name() : __dropLines,
        __hiLowLines.name() : __hiLowLines,
        __upDownBars.name() : __upDownBars,
        __axId.name() : __axId,
        __ser.name() : __ser,
        __extLst.name() : __extLst,
        __dLbls.name() : __dLbls
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_StockChart', CT_StockChart)


# Complex type CT_Perspective with content type EMPTY
class CT_Perspective (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Perspective')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Perspective_val', ST_Perspective, unicode_default=u'30')
    
    val = property(__val.value, __val.set, None, u'Perspective Value')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_Perspective', CT_Perspective)


# Complex type CT_SerAx with content type ELEMENT_ONLY
class CT_SerAx (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_SerAx')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}title uses Python identifier title
    __title = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006charttitle', False)

    
    title = property(__title.value, __title.set, None, u'Title')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}scaling uses Python identifier scaling
    __scaling = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'scaling'), 'scaling', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartscaling', False)

    
    scaling = property(__scaling.value, __scaling.set, None, u'Scaling')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorTickMark uses Python identifier majorTickMark
    __majorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), 'majorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorTickMark', False)

    
    majorTickMark = property(__majorTickMark.value, __majorTickMark.set, None, u'Major Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axPos uses Python identifier axPos
    __axPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axPos'), 'axPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartaxPos', False)

    
    axPos = property(__axPos.value, __axPos.set, None, u'Axis Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}numFmt uses Python identifier numFmt
    __numFmt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), 'numFmt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartnumFmt', False)

    
    numFmt = property(__numFmt.value, __numFmt.set, None, u'Number Format')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorTickMark uses Python identifier minorTickMark
    __minorTickMark = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), 'minorTickMark', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartminorTickMark', False)

    
    minorTickMark = property(__minorTickMark.value, __minorTickMark.set, None, u'Minor Tick Mark')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}majorGridlines uses Python identifier majorGridlines
    __majorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), 'majorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartmajorGridlines', False)

    
    majorGridlines = property(__majorGridlines.value, __majorGridlines.set, None, u'Major Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblPos uses Python identifier tickLblPos
    __tickLblPos = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), 'tickLblPos', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblPos', False)

    
    tickLblPos = property(__tickLblPos.value, __tickLblPos.set, None, u'Tick Label Position')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossAx uses Python identifier crossAx
    __crossAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), 'crossAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossAx', False)

    
    crossAx = property(__crossAx.value, __crossAx.set, None, u'Crossing Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}minorGridlines uses Python identifier minorGridlines
    __minorGridlines = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), 'minorGridlines', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartminorGridlines', False)

    
    minorGridlines = property(__minorGridlines.value, __minorGridlines.set, None, u'Minor Gridlines')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crossesAt uses Python identifier crossesAt
    __crossesAt = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), 'crossesAt', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartcrossesAt', False)

    
    crossesAt = property(__crossesAt.value, __crossesAt.set, None, u'Crossing Value')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartaxId', False)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}crosses uses Python identifier crosses
    __crosses = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'crosses'), 'crosses', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006chartcrosses', False)

    
    crosses = property(__crosses.value, __crosses.set, None, u'Crosses')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickMarkSkip uses Python identifier tickMarkSkip
    __tickMarkSkip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip'), 'tickMarkSkip', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006charttickMarkSkip', False)

    
    tickMarkSkip = property(__tickMarkSkip.value, __tickMarkSkip.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}tickLblSkip uses Python identifier tickLblSkip
    __tickLblSkip = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip'), 'tickLblSkip', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_SerAx_httpschemas_openxmlformats_orgdrawingml2006charttickLblSkip', False)

    
    tickLblSkip = property(__tickLblSkip.value, __tickLblSkip.set, None, u'Tick Label Skip')


    _ElementMap = {
        __title.name() : __title,
        __extLst.name() : __extLst,
        __scaling.name() : __scaling,
        __txPr.name() : __txPr,
        __spPr.name() : __spPr,
        __delete.name() : __delete,
        __majorTickMark.name() : __majorTickMark,
        __axPos.name() : __axPos,
        __numFmt.name() : __numFmt,
        __minorTickMark.name() : __minorTickMark,
        __majorGridlines.name() : __majorGridlines,
        __tickLblPos.name() : __tickLblPos,
        __crossAx.name() : __crossAx,
        __minorGridlines.name() : __minorGridlines,
        __crossesAt.name() : __crossesAt,
        __axId.name() : __axId,
        __crosses.name() : __crosses,
        __tickMarkSkip.name() : __tickMarkSkip,
        __tickLblSkip.name() : __tickLblSkip
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_SerAx', CT_SerAx)


# Complex type CT_Surface3DChart with content type ELEMENT_ONLY
class CT_Surface3DChart (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_Surface3DChart')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface3DChart_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}bandFmts uses Python identifier bandFmts
    __bandFmts = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'bandFmts'), 'bandFmts', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface3DChart_httpschemas_openxmlformats_orgdrawingml2006chartbandFmts', False)

    
    bandFmts = property(__bandFmts.value, __bandFmts.set, None, u'Band Formats')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}axId uses Python identifier axId
    __axId = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'axId'), 'axId', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface3DChart_httpschemas_openxmlformats_orgdrawingml2006chartaxId', True)

    
    axId = property(__axId.value, __axId.set, None, u'Axis ID')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}ser uses Python identifier ser
    __ser = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'ser'), 'ser', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface3DChart_httpschemas_openxmlformats_orgdrawingml2006chartser', True)

    
    ser = property(__ser.value, __ser.set, None, u'Surface Chart Series')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}wireframe uses Python identifier wireframe
    __wireframe = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'wireframe'), 'wireframe', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_Surface3DChart_httpschemas_openxmlformats_orgdrawingml2006chartwireframe', False)

    
    wireframe = property(__wireframe.value, __wireframe.set, None, u'Wireframe')


    _ElementMap = {
        __extLst.name() : __extLst,
        __bandFmts.name() : __bandFmts,
        __axId.name() : __axId,
        __ser.name() : __ser,
        __wireframe.name() : __wireframe
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_Surface3DChart', CT_Surface3DChart)


# Complex type CT_LegendEntry with content type ELEMENT_ONLY
class CT_LegendEntry (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_LegendEntry')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LegendEntry_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LegendEntry_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'delete'), 'delete', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LegendEntry_httpschemas_openxmlformats_orgdrawingml2006chartdelete', False)

    
    delete = property(__delete.value, __delete.set, None, u'Delete')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_LegendEntry_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)


    _ElementMap = {
        __extLst.name() : __extLst,
        __idx.name() : __idx,
        __delete.name() : __delete,
        __txPr.name() : __txPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_LegendEntry', CT_LegendEntry)


# Complex type CT_View3D with content type ELEMENT_ONLY
class CT_View3D (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_View3D')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}rAngAx uses Python identifier rAngAx
    __rAngAx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rAngAx'), 'rAngAx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartrAngAx', False)

    
    rAngAx = property(__rAngAx.value, __rAngAx.set, None, u'Right Angle Axes')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}depthPercent uses Python identifier depthPercent
    __depthPercent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'depthPercent'), 'depthPercent', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartdepthPercent', False)

    
    depthPercent = property(__depthPercent.value, __depthPercent.set, None, u'Depth Percent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}rotX uses Python identifier rotX
    __rotX = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rotX'), 'rotX', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartrotX', False)

    
    rotX = property(__rotX.value, __rotX.set, None, u'X Rotation')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}hPercent uses Python identifier hPercent
    __hPercent = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'hPercent'), 'hPercent', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006charthPercent', False)

    
    hPercent = property(__hPercent.value, __hPercent.set, None, u'Height Percent')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}rotY uses Python identifier rotY
    __rotY = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'rotY'), 'rotY', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartrotY', False)

    
    rotY = property(__rotY.value, __rotY.set, None, u'Y Rotation')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}perspective uses Python identifier perspective
    __perspective = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'perspective'), 'perspective', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_View3D_httpschemas_openxmlformats_orgdrawingml2006chartperspective', False)

    
    perspective = property(__perspective.value, __perspective.set, None, u'Perspective')


    _ElementMap = {
        __rAngAx.name() : __rAngAx,
        __depthPercent.name() : __depthPercent,
        __rotX.name() : __rotX,
        __extLst.name() : __extLst,
        __hPercent.name() : __hPercent,
        __rotY.name() : __rotY,
        __perspective.name() : __perspective
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_View3D', CT_View3D)


# Complex type CT_PivotFmt with content type ELEMENT_ONLY
class CT_PivotFmt (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_PivotFmt')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}dLbl uses Python identifier dLbl
    __dLbl = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'dLbl'), 'dLbl', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006chartdLbl', False)

    
    dLbl = property(__dLbl.value, __dLbl.set, None, u'Data Label')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}marker uses Python identifier marker
    __marker = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'marker'), 'marker', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006chartmarker', False)

    
    marker = property(__marker.value, __marker.set, None, u'Marker')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}idx uses Python identifier idx
    __idx = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'idx'), 'idx', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006chartidx', False)

    
    idx = property(__idx.value, __idx.set, None, u'Index')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, None)

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_PivotFmt_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)


    _ElementMap = {
        __dLbl.name() : __dLbl,
        __extLst.name() : __extLst,
        __marker.name() : __marker,
        __idx.name() : __idx,
        __spPr.name() : __spPr,
        __txPr.name() : __txPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_PivotFmt', CT_PivotFmt)


# Complex type CT_TextLanguageID with content type EMPTY
class CT_TextLanguageID (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_TextLanguageID')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute val uses Python identifier val
    __val = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'val'), 'val', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_TextLanguageID_val', _s.ST_Lang, required=True)
    
    val = property(__val.value, __val.set, None, u'Language Code')


    _ElementMap = {
        
    }
    _AttributeMap = {
        __val.name() : __val
    }
Namespace.addCategoryObject('typeBinding', u'CT_TextLanguageID', CT_TextLanguageID)


# Complex type CT_ChartSpace with content type ELEMENT_ONLY
class CT_ChartSpace (pyxb.binding.basis.complexTypeDefinition):
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'CT_ChartSpace')
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}clrMapOvr uses Python identifier clrMapOvr
    __clrMapOvr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'clrMapOvr'), 'clrMapOvr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartclrMapOvr', False)

    
    clrMapOvr = property(__clrMapOvr.value, __clrMapOvr.set, None, u'Color Map Override')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}pivotSource uses Python identifier pivotSource
    __pivotSource = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'pivotSource'), 'pivotSource', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartpivotSource', False)

    
    pivotSource = property(__pivotSource.value, __pivotSource.set, None, u'Pivot Source')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}userShapes uses Python identifier userShapes
    __userShapes = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'userShapes'), 'userShapes', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartuserShapes', False)

    
    userShapes = property(__userShapes.value, __userShapes.set, None, u'Reference to Chart Drawing Part')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}date1904 uses Python identifier date1904
    __date1904 = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'date1904'), 'date1904', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartdate1904', False)

    
    date1904 = property(__date1904.value, __date1904.set, None, u'1904 Date System')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}protection uses Python identifier protection
    __protection = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'protection'), 'protection', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartprotection', False)

    
    protection = property(__protection.value, __protection.set, None, u'Protection')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}lang uses Python identifier lang
    __lang = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'lang'), 'lang', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartlang', False)

    
    lang = property(__lang.value, __lang.set, None, u'Editing Language')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}externalData uses Python identifier externalData
    __externalData = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'externalData'), 'externalData', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartexternalData', False)

    
    externalData = property(__externalData.value, __externalData.set, None, u'External Data Relationship')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}chart uses Python identifier chart
    __chart = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'chart'), 'chart', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartchart', False)

    
    chart = property(__chart.value, __chart.set, None, u'Chart')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}roundedCorners uses Python identifier roundedCorners
    __roundedCorners = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'roundedCorners'), 'roundedCorners', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartroundedCorners', False)

    
    roundedCorners = property(__roundedCorners.value, __roundedCorners.set, None, u'Rounded Corners')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}spPr uses Python identifier spPr
    __spPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'spPr'), 'spPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartspPr', False)

    
    spPr = property(__spPr.value, __spPr.set, None, u'Shape Properties')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}style uses Python identifier style
    __style = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'style'), 'style', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartstyle', False)

    
    style = property(__style.value, __style.set, None, u'Style')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}printSettings uses Python identifier printSettings
    __printSettings = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'printSettings'), 'printSettings', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartprintSettings', False)

    
    printSettings = property(__printSettings.value, __printSettings.set, None, u'Print Settings')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}extLst uses Python identifier extLst
    __extLst = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'extLst'), 'extLst', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006chartextLst', False)

    
    extLst = property(__extLst.value, __extLst.set, None, u'Chart Extensibility')

    
    # Element {http://schemas.openxmlformats.org/drawingml/2006/chart}txPr uses Python identifier txPr
    __txPr = pyxb.binding.content.ElementUse(pyxb.namespace.ExpandedName(Namespace, u'txPr'), 'txPr', '__httpschemas_openxmlformats_orgdrawingml2006chart_CT_ChartSpace_httpschemas_openxmlformats_orgdrawingml2006charttxPr', False)

    
    txPr = property(__txPr.value, __txPr.set, None, None)


    _ElementMap = {
        __clrMapOvr.name() : __clrMapOvr,
        __pivotSource.name() : __pivotSource,
        __userShapes.name() : __userShapes,
        __date1904.name() : __date1904,
        __protection.name() : __protection,
        __lang.name() : __lang,
        __externalData.name() : __externalData,
        __chart.name() : __chart,
        __roundedCorners.name() : __roundedCorners,
        __spPr.name() : __spPr,
        __style.name() : __style,
        __printSettings.name() : __printSettings,
        __extLst.name() : __extLst,
        __txPr.name() : __txPr
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'CT_ChartSpace', CT_ChartSpace)


userShapes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'userShapes'), _cdr.CT_Drawing, documentation=u'User Shapes')
Namespace.addCategoryObject('elementBinding', userShapes.name().localName(), userShapes)

chart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chart'), CT_RelId, documentation=u'Reference to Chart Part')
Namespace.addCategoryObject('elementBinding', chart.name().localName(), chart)

chartSpace = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chartSpace'), CT_ChartSpace, documentation=u'Chart Space')
Namespace.addCategoryObject('elementBinding', chartSpace.name().localName(), chartSpace)



CT_StrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_StrRef))

CT_StrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'f'), pyxb.binding.datatypes.string, scope=CT_StrRef, documentation=u'Formula'))

CT_StrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strCache'), CT_StrData, scope=CT_StrRef, documentation=u'String Cache'))
CT_StrRef._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_StrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'f')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strCache')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_StrRef._ContentModel = pyxb.binding.content.ParticleModel(CT_StrRef._GroupModel, min_occurs=1, max_occurs=1)



CT_PieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_PieChart, documentation=u'Chart Extensibility'))

CT_PieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_PieChart, documentation=u'Data Labels'))

CT_PieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_PieSer, scope=CT_PieChart, documentation=u'Pie Chart Series'))

CT_PieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng'), CT_FirstSliceAng, scope=CT_PieChart, documentation=u'First Slice Angle'))

CT_PieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_PieChart))
CT_PieChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_PieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_PieChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PieChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_PieChart._ContentModel = pyxb.binding.content.ParticleModel(CT_PieChart._GroupModel, min_occurs=1, max_occurs=1)



CT_SerTx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strRef'), CT_StrRef, scope=CT_SerTx))

CT_SerTx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'v'), _s.ST_Xstring, scope=CT_SerTx))
CT_SerTx._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_SerTx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerTx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'v')), min_occurs=1L, max_occurs=1L)
    )
CT_SerTx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SerTx._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_SerTx._ContentModel = pyxb.binding.content.ParticleModel(CT_SerTx._GroupModel, min_occurs=1, max_occurs=1)



CT_ChartLines._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_ChartLines))
CT_ChartLines._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ChartLines._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_ChartLines._ContentModel = pyxb.binding.content.ParticleModel(CT_ChartLines._GroupModel, min_occurs=1, max_occurs=1)



CT_AxDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrRef'), CT_MultiLvlStrRef, scope=CT_AxDataSource, documentation=u'Multi Level String Reference'))

CT_AxDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numRef'), CT_NumRef, scope=CT_AxDataSource, documentation=u'Number Reference'))

CT_AxDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strLit'), CT_StrData, scope=CT_AxDataSource, documentation=u'String Literal'))

CT_AxDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strRef'), CT_StrRef, scope=CT_AxDataSource))

CT_AxDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numLit'), CT_NumData, scope=CT_AxDataSource, documentation=u'Number Literal'))
CT_AxDataSource._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_AxDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AxDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AxDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numLit')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AxDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AxDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strLit')), min_occurs=1L, max_occurs=1L)
    )
CT_AxDataSource._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AxDataSource._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_AxDataSource._ContentModel = pyxb.binding.content.ParticleModel(CT_AxDataSource._GroupModel, min_occurs=1, max_occurs=1)



CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), CT_Boolean, scope=CT_DPt, documentation=u'Invert if Negative'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_DPt, documentation=u'Index'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Marker, scope=CT_DPt, documentation=u'Marker'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), CT_Boolean, scope=CT_DPt, documentation=u'3D Bubble'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DPt, documentation=u'Chart Extensibility'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'explosion'), CT_UnsignedInt, scope=CT_DPt, documentation=u'Explosion'))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DPt))

CT_DPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), CT_PictureOptions, scope=CT_DPt))
CT_DPt._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubble3D')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'explosion')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DPt._ContentModel = pyxb.binding.content.ParticleModel(CT_DPt._GroupModel, min_occurs=1, max_occurs=1)



CT_NumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_NumData))

CT_NumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatCode'), _s.ST_Xstring, scope=CT_NumData, documentation=u'Format Code'))

CT_NumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pt'), CT_NumVal, scope=CT_NumData, documentation=u'Numeric Point'))

CT_NumData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), CT_UnsignedInt, scope=CT_NumData, documentation=u'Point Count'))
CT_NumData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_NumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'formatCode')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_NumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ptCount')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_NumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_NumData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_NumData._ContentModel = pyxb.binding.content.ParticleModel(CT_NumData._GroupModel, min_occurs=1, max_occurs=1)



CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbl'), CT_DLbl, scope=CT_DLbls, documentation=u'Data Label'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showCatName'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Category Name'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DLbls))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_DLbls, documentation=u'Delete'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showSerName'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Series Name'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLblPos'), CT_DLblPos, scope=CT_DLbls, documentation=u'Data Label Position'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_DLbls))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showPercent'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Percent'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'leaderLines'), CT_ChartLines, scope=CT_DLbls, documentation=u'Leader Lines'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DLbls, documentation=u'Chart Extensibility'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showLeaderLines'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Leader Lines'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Bubble Size'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Legend Key'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'separator'), pyxb.binding.datatypes.string, scope=CT_DLbls, documentation=u'Separator'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showVal'), CT_Boolean, scope=CT_DLbls, documentation=u'Show Value'))

CT_DLbls._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_DLbls, documentation=u'Number Format'))
CT_DLbls._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showCatName')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showSerName')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showPercent')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'separator')), min_occurs=0L, max_occurs=1L)
    )
CT_DLbls._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbls._GroupModel_3, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showLeaderLines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'leaderLines')), min_occurs=0L, max_occurs=1L)
    )
CT_DLbls._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbls._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_DLbls._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbl')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_DLbls._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_DLbls._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DLbls._ContentModel = pyxb.binding.content.ParticleModel(CT_DLbls._GroupModel, min_occurs=1, max_occurs=1)



CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_LineSer, documentation=u'Order'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_LineSer, documentation=u'Index'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Marker, scope=CT_LineSer, documentation=u'Marker'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_LineSer))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_LineSer, documentation=u'Series Text'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_LineSer, documentation=u'Category Axis Data'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_LineSer, documentation=u'Chart Extensibility'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_LineSer))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_LineSer, documentation=u'Data Labels'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendline'), CT_Trendline, scope=CT_LineSer))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_LineSer, documentation=u'Data Point'))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'smooth'), CT_Boolean, scope=CT_LineSer))

CT_LineSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBars'), CT_ErrBars, scope=CT_LineSer, documentation=u'Error Bars'))
CT_LineSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_LineSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LineSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendline')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'smooth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_LineSer._ContentModel = pyxb.binding.content.ParticleModel(CT_LineSer._GroupModel, min_occurs=1, max_occurs=1)



CT_ExtensionList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ext'), CT_Extension, scope=CT_ExtensionList, documentation=u'Extension'))
CT_ExtensionList._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ExtensionList._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ext')), min_occurs=0L, max_occurs=None)
    )
CT_ExtensionList._ContentModel = pyxb.binding.content.ParticleModel(CT_ExtensionList._GroupModel, min_occurs=1, max_occurs=1)



CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Marker, documentation=u'Chart Extensibility'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'symbol'), CT_MarkerStyle, scope=CT_Marker, documentation=u'Symbol'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'size'), CT_MarkerSize, scope=CT_Marker, documentation=u'Size'))

CT_Marker._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Marker))
CT_Marker._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'symbol')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'size')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Marker._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Marker._ContentModel = pyxb.binding.content.ParticleModel(CT_Marker._GroupModel, min_occurs=1, max_occurs=1)



CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Title))

CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_Title))

CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Title, documentation=u'Chart Extensibility'))

CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_Tx, scope=CT_Title, documentation=u'Chart Text'))

CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_Title, documentation=u'Layout'))

CT_Title._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overlay'), CT_Boolean, scope=CT_Title, documentation=u'Overlay'))
CT_Title._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overlay')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Title._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Title._ContentModel = pyxb.binding.content.ParticleModel(CT_Title._GroupModel, min_occurs=1, max_occurs=1)



CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minus'), CT_NumDataSource, scope=CT_ErrBars, documentation=u'Minus'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errDir'), CT_ErrDir, scope=CT_ErrBars, documentation=u'Error Bar Direction'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_Double, scope=CT_ErrBars, documentation=u'Error Bar Value'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBarType'), CT_ErrBarType, scope=CT_ErrBars, documentation=u'Error Bar Type'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'plus'), CT_NumDataSource, scope=CT_ErrBars, documentation=u'Plus'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_ErrBars))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errValType'), CT_ErrValType, scope=CT_ErrBars, documentation=u'Error Bar Value Type'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ErrBars, documentation=u'Chart Extensibility'))

CT_ErrBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'noEndCap'), CT_Boolean, scope=CT_ErrBars, documentation=u'No End Cap'))
CT_ErrBars._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errDir')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBarType')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errValType')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'noEndCap')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'plus')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minus')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ErrBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ErrBars._ContentModel = pyxb.binding.content.ParticleModel(CT_ErrBars._GroupModel, min_occurs=1, max_occurs=1)


CT_Extension._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), min_occurs=1, max_occurs=1)
    )
CT_Extension._ContentModel = pyxb.binding.content.ParticleModel(CT_Extension._GroupModel, min_occurs=1, max_occurs=1)



CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorTimeUnit'), CT_TimeUnit, scope=CT_DateAx, documentation=u'Minor Time Unit'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_DateAx, documentation=u'Axis ID'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DateAx, documentation=u'Chart Extensibility'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scaling'), CT_Scaling, scope=CT_DateAx, documentation=u'Scaling'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_DateAx, documentation=u'Delete'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), CT_ChartLines, scope=CT_DateAx, documentation=u'Major Gridlines'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), CT_ChartLines, scope=CT_DateAx, documentation=u'Minor Gridlines'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), CT_Title, scope=CT_DateAx, documentation=u'Title'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_DateAx, documentation=u'Number Format'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), CT_TickMark, scope=CT_DateAx, documentation=u'Major Tick Mark'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), CT_TickMark, scope=CT_DateAx, documentation=u'Minor Tick Mark'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), CT_TickLblPos, scope=CT_DateAx, documentation=u'Tick Label Position'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axPos'), CT_AxPos, scope=CT_DateAx, documentation=u'Axis Position'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_DateAx))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), CT_UnsignedInt, scope=CT_DateAx, documentation=u'Crossing Axis ID'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'auto'), CT_Boolean, scope=CT_DateAx, documentation=u'Automatic Category Axis'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'baseTimeUnit'), CT_TimeUnit, scope=CT_DateAx, documentation=u'Base Time Unit'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lblOffset'), CT_LblOffset, scope=CT_DateAx, documentation=u'Label Offset'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crosses'), CT_Crosses, scope=CT_DateAx, documentation=u'Crosses'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), CT_Double, scope=CT_DateAx, documentation=u'Crossing Value'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorUnit'), CT_AxisUnit, scope=CT_DateAx, documentation=u'Major Unit'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DateAx))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorTimeUnit'), CT_TimeUnit, scope=CT_DateAx, documentation=u'Major Time Unit'))

CT_DateAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorUnit'), CT_AxisUnit, scope=CT_DateAx, documentation=u'Minor Unit'))
CT_DateAx._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crosses')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossesAt')), min_occurs=1L, max_occurs=1L)
    )
CT_DateAx._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scaling')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axPos')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._GroupModel_2, min_occurs=0L, max_occurs=1L)
    )
CT_DateAx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DateAx._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'auto')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lblOffset')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'baseTimeUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorTimeUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorTimeUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DateAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DateAx._ContentModel = pyxb.binding.content.ParticleModel(CT_DateAx._GroupModel, min_occurs=1, max_occurs=1)



CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'oddHeader'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'Odd Header'))

CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'evenHeader'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'Even Header'))

CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'oddFooter'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'Odd Footer'))

CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'evenFooter'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'Even Footer'))

CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstHeader'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'First Header'))

CT_HeaderFooter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstFooter'), _s.ST_Xstring, scope=CT_HeaderFooter, documentation=u'First Footer'))
CT_HeaderFooter._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'oddHeader')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'oddFooter')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'evenHeader')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'evenFooter')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstHeader')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_HeaderFooter._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstFooter')), min_occurs=0L, max_occurs=1L)
    )
CT_HeaderFooter._ContentModel = pyxb.binding.content.ParticleModel(CT_HeaderFooter._GroupModel, min_occurs=1, max_occurs=1)



CT_UpDownBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_UpDownBars, documentation=u'Chart Extensibility'))

CT_UpDownBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), CT_GapAmount, scope=CT_UpDownBars, documentation=u'Gap Width'))

CT_UpDownBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'upBars'), CT_UpDownBar, scope=CT_UpDownBars, documentation=u'Up Bars'))

CT_UpDownBars._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'downBars'), CT_UpDownBar, scope=CT_UpDownBars, documentation=u'Down Bars'))
CT_UpDownBars._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_UpDownBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapWidth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_UpDownBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'upBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_UpDownBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'downBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_UpDownBars._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_UpDownBars._ContentModel = pyxb.binding.content.ParticleModel(CT_UpDownBars._GroupModel, min_occurs=1, max_occurs=1)



CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_ValAx, documentation=u'Number Format'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispUnits'), CT_DispUnits, scope=CT_ValAx, documentation=u'Display Units'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_ValAx, documentation=u'Delete'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), CT_UnsignedInt, scope=CT_ValAx, documentation=u'Crossing Axis ID'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), CT_TickMark, scope=CT_ValAx, documentation=u'Major Tick Mark'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scaling'), CT_Scaling, scope=CT_ValAx, documentation=u'Scaling'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ValAx, documentation=u'Chart Extensibility'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), CT_TickMark, scope=CT_ValAx, documentation=u'Minor Tick Mark'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), CT_Double, scope=CT_ValAx, documentation=u'Crossing Value'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), CT_ChartLines, scope=CT_ValAx, documentation=u'Major Gridlines'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axPos'), CT_AxPos, scope=CT_ValAx, documentation=u'Axis Position'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crosses'), CT_Crosses, scope=CT_ValAx, documentation=u'Crosses'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), CT_TickLblPos, scope=CT_ValAx, documentation=u'Tick Label Position'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), CT_ChartLines, scope=CT_ValAx, documentation=u'Minor Gridlines'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorUnit'), CT_AxisUnit, scope=CT_ValAx, documentation=u'Major Unit'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossBetween'), CT_CrossBetween, scope=CT_ValAx, documentation=u'Cross Between'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_ValAx))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_ValAx, documentation=u'Axis ID'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), CT_Title, scope=CT_ValAx, documentation=u'Title'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorUnit'), CT_AxisUnit, scope=CT_ValAx, documentation=u'Minor Unit'))

CT_ValAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_ValAx))
CT_ValAx._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crosses')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossesAt')), min_occurs=1L, max_occurs=1L)
    )
CT_ValAx._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scaling')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axPos')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._GroupModel_2, min_occurs=0L, max_occurs=1L)
    )
CT_ValAx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ValAx._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossBetween')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorUnit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispUnits')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ValAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ValAx._ContentModel = pyxb.binding.content.ParticleModel(CT_ValAx._GroupModel, min_occurs=1, max_occurs=1)



CT_PrintSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legacyDrawingHF'), CT_RelId, scope=CT_PrintSettings, documentation=u'Legacy Drawing for Headers and Footers'))

CT_PrintSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'headerFooter'), CT_HeaderFooter, scope=CT_PrintSettings, documentation=u'Header and Footer'))

CT_PrintSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pageMargins'), CT_PageMargins, scope=CT_PrintSettings, documentation=u'Page Margins'))

CT_PrintSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pageSetup'), CT_PageSetup, scope=CT_PrintSettings, documentation=u'Page Setup'))
CT_PrintSettings._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PrintSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'headerFooter')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PrintSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pageMargins')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PrintSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pageSetup')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PrintSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legacyDrawingHF')), min_occurs=0L, max_occurs=1L)
    )
CT_PrintSettings._ContentModel = pyxb.binding.content.ParticleModel(CT_PrintSettings._GroupModel, min_occurs=1, max_occurs=1)



CT_Tx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'strRef'), CT_StrRef, scope=CT_Tx, documentation=u'String Reference'))

CT_Tx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rich'), _nsgroup.CT_TextBody, scope=CT_Tx, documentation=u'Rich Text'))
CT_Tx._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_Tx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'strRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Tx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rich')), min_occurs=1L, max_occurs=1L)
    )
CT_Tx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Tx._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_Tx._ContentModel = pyxb.binding.content.ParticleModel(CT_Tx._GroupModel, min_occurs=1, max_occurs=1)



CT_NumDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numRef'), CT_NumRef, scope=CT_NumDataSource, documentation=u'Number Reference'))

CT_NumDataSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numLit'), CT_NumData, scope=CT_NumDataSource, documentation=u'Number Literal'))
CT_NumDataSource._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_NumDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numRef')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_NumDataSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numLit')), min_occurs=1L, max_occurs=1L)
    )
CT_NumDataSource._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_NumDataSource._GroupModel_, min_occurs=1L, max_occurs=1L)
    )
CT_NumDataSource._ContentModel = pyxb.binding.content.ParticleModel(CT_NumDataSource._GroupModel, min_occurs=1, max_occurs=1)



CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_SurfaceSer, documentation=u'Index'))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_SurfaceSer, documentation=u'Category Axis Data'))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_SurfaceSer))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_SurfaceSer))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_SurfaceSer, documentation=u'Chart Extensibility'))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_SurfaceSer, documentation=u'Order'))

CT_SurfaceSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_SurfaceSer, documentation=u'Series Text'))
CT_SurfaceSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_SurfaceSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_SurfaceSer._ContentModel = pyxb.binding.content.ParticleModel(CT_SurfaceSer._GroupModel, min_occurs=1, max_occurs=1)



CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_BarGrouping, scope=CT_BarChart, documentation=u'Bar Grouping'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'barDir'), CT_BarDir, scope=CT_BarChart, documentation=u'Bar Direction'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overlap'), CT_Overlap, scope=CT_BarChart, documentation=u'Overlap'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_BarChart, documentation=u'Axis ID'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serLines'), CT_ChartLines, scope=CT_BarChart, documentation=u'Series Lines'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), CT_GapAmount, scope=CT_BarChart, documentation=u'Gap Width'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_BarChart))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_BarChart, documentation=u'Chart Extensibility'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_BarChart, documentation=u'Data Labels'))

CT_BarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_BarSer, scope=CT_BarChart, documentation=u'Bar Chart Series'))
CT_BarChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'barDir')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_BarChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BarChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapWidth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overlap')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serLines')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_BarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_BarChart._ContentModel = pyxb.binding.content.ParticleModel(CT_BarChart._GroupModel, min_occurs=1, max_occurs=1)



CT_PivotSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_PivotSource, documentation=u'Chart Extensibility'))

CT_PivotSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), _s.ST_Xstring, scope=CT_PivotSource, documentation=u'Pivot Name'))

CT_PivotSource._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fmtId'), CT_UnsignedInt, scope=CT_PivotSource, documentation=u'Format ID'))
CT_PivotSource._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PivotSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fmtId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotSource._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=None)
    )
CT_PivotSource._ContentModel = pyxb.binding.content.ParticleModel(CT_PivotSource._GroupModel, min_occurs=1, max_occurs=1)



CT_MultiLvlStrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_MultiLvlStrData))

CT_MultiLvlStrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), CT_UnsignedInt, scope=CT_MultiLvlStrData))

CT_MultiLvlStrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lvl'), CT_Lvl, scope=CT_MultiLvlStrData, documentation=u'Level'))
CT_MultiLvlStrData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ptCount')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lvl')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_MultiLvlStrData._ContentModel = pyxb.binding.content.ParticleModel(CT_MultiLvlStrData._GroupModel, min_occurs=1, max_occurs=1)



CT_Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Layout, documentation=u'Chart Extensibility'))

CT_Layout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'manualLayout'), CT_ManualLayout, scope=CT_Layout, documentation=u'Manual Layout'))
CT_Layout._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'manualLayout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Layout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Layout._ContentModel = pyxb.binding.content.ParticleModel(CT_Layout._GroupModel, min_occurs=1, max_occurs=1)



CT_BandFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_BandFmt))

CT_BandFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_BandFmt))
CT_BandFmt._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BandFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BandFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_BandFmt._ContentModel = pyxb.binding.content.ParticleModel(CT_BandFmt._GroupModel, min_occurs=1, max_occurs=1)



CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_AreaSer))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_AreaSer, documentation=u'Data Point'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendline'), CT_Trendline, scope=CT_AreaSer))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), CT_PictureOptions, scope=CT_AreaSer))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_AreaSer, documentation=u'Chart Extensibility'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_AreaSer, documentation=u'Data Labels'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_AreaSer, documentation=u'Index'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_AreaSer, documentation=u'Values'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_AreaSer, documentation=u'Order'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBars'), CT_ErrBars, scope=CT_AreaSer, documentation=u'Error Bars'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_AreaSer, documentation=u'Series Text'))

CT_AreaSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_AreaSer, documentation=u'Category Axis Data'))
CT_AreaSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_AreaSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AreaSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendline')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBars')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_AreaSer._ContentModel = pyxb.binding.content.ParticleModel(CT_AreaSer._GroupModel, min_occurs=1, max_occurs=1)



CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendlineType'), CT_TrendlineType, scope=CT_Trendline, documentation=u'Trendline Type'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_Order, scope=CT_Trendline, documentation=u'Polynomial Trendline Order'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispEq'), CT_Boolean, scope=CT_Trendline, documentation=u'Display Equation'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'period'), CT_Period, scope=CT_Trendline, documentation=u'Period'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispRSqr'), CT_Boolean, scope=CT_Trendline, documentation=u'Display R Squared Value'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'forward'), CT_Double, scope=CT_Trendline, documentation=u'Forward'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'name'), pyxb.binding.datatypes.string, scope=CT_Trendline, documentation=u'Trendline Name'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Trendline, documentation=u'Chart Extensibility'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendlineLbl'), CT_TrendlineLbl, scope=CT_Trendline, documentation=u'Trendline Label'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backward'), CT_Double, scope=CT_Trendline, documentation=u'Backward'))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Trendline))

CT_Trendline._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'intercept'), CT_Double, scope=CT_Trendline, documentation=u'Intercept'))
CT_Trendline._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'name')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendlineType')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'period')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'forward')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backward')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'intercept')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispRSqr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispEq')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendlineLbl')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Trendline._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Trendline._ContentModel = pyxb.binding.content.ParticleModel(CT_Trendline._GroupModel, min_occurs=1, max_occurs=1)



CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scatterChart'), CT_ScatterChart, scope=CT_PlotArea, documentation=u'Scatter Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pieChart'), CT_PieChart, scope=CT_PlotArea, documentation=u'Pie Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dateAx'), CT_DateAx, scope=CT_PlotArea, documentation=u'Date Axis'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bar3DChart'), CT_Bar3DChart, scope=CT_PlotArea, documentation=u'3D Bar Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'doughnutChart'), CT_DoughnutChart, scope=CT_PlotArea, documentation=u'Doughnut Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'barChart'), CT_BarChart, scope=CT_PlotArea, documentation=u'Bar Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ofPieChart'), CT_OfPieChart, scope=CT_PlotArea, documentation=u'Pie of Pie or Bar of Pie Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surfaceChart'), CT_SurfaceChart, scope=CT_PlotArea, documentation=u'Surface Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'surface3DChart'), CT_Surface3DChart, scope=CT_PlotArea, documentation=u'3D Surface Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubbleChart'), CT_BubbleChart, scope=CT_PlotArea, documentation=u'Bubble Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'catAx'), CT_CatAx, scope=CT_PlotArea, documentation=u'Category Axis Data'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pie3DChart'), CT_Pie3DChart, scope=CT_PlotArea, documentation=u'3D Pie Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_PlotArea, documentation=u'Layout'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serAx'), CT_SerAx, scope=CT_PlotArea, documentation=u'Series Axis'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dTable'), CT_DTable, scope=CT_PlotArea, documentation=u'Data Table'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'areaChart'), CT_AreaChart, scope=CT_PlotArea, documentation=u'Area Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'valAx'), CT_ValAx, scope=CT_PlotArea, documentation=u'Value Axis'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_PlotArea))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'area3DChart'), CT_Area3DChart, scope=CT_PlotArea, documentation=u'3D Area Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_PlotArea, documentation=u'Chart Extensibility'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lineChart'), CT_LineChart, scope=CT_PlotArea, documentation=u'Line Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'line3DChart'), CT_Line3DChart, scope=CT_PlotArea, documentation=u'3D Line Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'stockChart'), CT_StockChart, scope=CT_PlotArea, documentation=u'Stock Charts'))

CT_PlotArea._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'radarChart'), CT_RadarChart, scope=CT_PlotArea, documentation=u'Radar Charts'))
CT_PlotArea._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'areaChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'area3DChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lineChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'line3DChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'stockChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'radarChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scatterChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pieChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pie3DChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'doughnutChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'barChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bar3DChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ofPieChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surfaceChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'surface3DChart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubbleChart')), min_occurs=1L, max_occurs=1L)
    )
CT_PlotArea._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'valAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'catAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dateAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serAx')), min_occurs=1L, max_occurs=1L)
    )
CT_PlotArea._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._GroupModel_, min_occurs=1L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_PlotArea._GroupModel_2, min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dTable')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PlotArea._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_PlotArea._ContentModel = pyxb.binding.content.ParticleModel(CT_PlotArea._GroupModel, min_occurs=1, max_occurs=1)



CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yVal'), CT_NumDataSource, scope=CT_BubbleSer, documentation=u'Y Values'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), CT_Boolean, scope=CT_BubbleSer, documentation=u'Invert if Negative'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_BubbleSer, documentation=u'Index'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_BubbleSer, documentation=u'Data Point'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubbleSize'), CT_NumDataSource, scope=CT_BubbleSer, documentation=u'Bubble Size'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_BubbleSer, documentation=u'Order'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xVal'), CT_AxDataSource, scope=CT_BubbleSer, documentation=u'X Values'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), CT_Boolean, scope=CT_BubbleSer, documentation=u'3D Bubble'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_BubbleSer, documentation=u'Data Labels'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_BubbleSer, documentation=u'Series Text'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendline'), CT_Trendline, scope=CT_BubbleSer))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_BubbleSer, documentation=u'Chart Extensibility'))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_BubbleSer))

CT_BubbleSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBars'), CT_ErrBars, scope=CT_BubbleSer, documentation=u'Error Bars'))
CT_BubbleSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_BubbleSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BubbleSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendline')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBars')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubbleSize')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubble3D')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_BubbleSer._ContentModel = pyxb.binding.content.ParticleModel(CT_BubbleSer._GroupModel, min_occurs=1, max_occurs=1)



CT_PictureOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureStackUnit'), CT_PictureStackUnit, scope=CT_PictureOptions, documentation=u'Picture Stack Unit'))

CT_PictureOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'applyToFront'), CT_Boolean, scope=CT_PictureOptions, documentation=u'Apply To Front'))

CT_PictureOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'applyToEnd'), CT_Boolean, scope=CT_PictureOptions, documentation=u'Apply to End'))

CT_PictureOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'applyToSides'), CT_Boolean, scope=CT_PictureOptions, documentation=u'Apply To Sides'))

CT_PictureOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureFormat'), CT_PictureFormat, scope=CT_PictureOptions, documentation=u'Picture Format'))
CT_PictureOptions._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PictureOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'applyToFront')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'applyToSides')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'applyToEnd')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureFormat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PictureOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureStackUnit')), min_occurs=0L, max_occurs=1L)
    )
CT_PictureOptions._ContentModel = pyxb.binding.content.ParticleModel(CT_PictureOptions._GroupModel, min_occurs=1, max_occurs=1)



CT_DispUnitsLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_DispUnitsLbl))

CT_DispUnitsLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_DispUnitsLbl, documentation=u'Layout'))

CT_DispUnitsLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_Tx, scope=CT_DispUnitsLbl))

CT_DispUnitsLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DispUnitsLbl))
CT_DispUnitsLbl._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DispUnitsLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DispUnitsLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DispUnitsLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DispUnitsLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L)
    )
CT_DispUnitsLbl._ContentModel = pyxb.binding.content.ParticleModel(CT_DispUnitsLbl._GroupModel, min_occurs=1, max_occurs=1)



CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_Line3DChart, documentation=u'Axis ID'))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_Line3DChart, documentation=u'Data Labels'))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), CT_ChartLines, scope=CT_Line3DChart, documentation=u'Drop Lines'))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Line3DChart, documentation=u'Chart Extensibility'))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_LineSer, scope=CT_Line3DChart))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_Line3DChart))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_Grouping, scope=CT_Line3DChart, documentation=u'Grouping'))

CT_Line3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), CT_GapAmount, scope=CT_Line3DChart, documentation=u'Gap Depth'))
CT_Line3DChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dropLines')), min_occurs=0L, max_occurs=1L)
    )
CT_Line3DChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Line3DChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapDepth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=3L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CT_Line3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Line3DChart._ContentModel = pyxb.binding.content.ParticleModel(CT_Line3DChart._GroupModel, min_occurs=1, max_occurs=1)



CT_UpDownBar._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_UpDownBar))
CT_UpDownBar._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_UpDownBar._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_UpDownBar._ContentModel = pyxb.binding.content.ParticleModel(CT_UpDownBar._GroupModel, min_occurs=1, max_occurs=1)



CT_SurfaceChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_SurfaceChart, documentation=u'Chart Extensibility'))

CT_SurfaceChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bandFmts'), CT_BandFmts, scope=CT_SurfaceChart, documentation=u'Band Formats'))

CT_SurfaceChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_SurfaceSer, scope=CT_SurfaceChart, documentation=u'Surface Chart Series'))

CT_SurfaceChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wireframe'), CT_Boolean, scope=CT_SurfaceChart, documentation=u'Wireframe'))

CT_SurfaceChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_SurfaceChart, documentation=u'Axis ID'))
CT_SurfaceChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wireframe')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bandFmts')), min_occurs=0L, max_occurs=1L)
    )
CT_SurfaceChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CT_SurfaceChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_SurfaceChart._ContentModel = pyxb.binding.content.ParticleModel(CT_SurfaceChart._GroupModel, min_occurs=1, max_occurs=1)



CT_Lvl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pt'), CT_StrVal, scope=CT_Lvl, documentation=u'String Point'))
CT_Lvl._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Lvl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pt')), min_occurs=0L, max_occurs=None)
    )
CT_Lvl._ContentModel = pyxb.binding.content.ParticleModel(CT_Lvl._GroupModel, min_occurs=1, max_occurs=1)



CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Marker, scope=CT_RadarSer, documentation=u'Marker'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_RadarSer, documentation=u'Data Labels'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_RadarSer, documentation=u'Category Axis Data'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_RadarSer, documentation=u'Index'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_RadarSer))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_RadarSer, documentation=u'Order'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_RadarSer, documentation=u'Chart Extensibility'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_RadarSer, documentation=u'Series Text'))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_RadarSer))

CT_RadarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_RadarSer, documentation=u'Data Point'))
CT_RadarSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_RadarSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_RadarSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_RadarSer._ContentModel = pyxb.binding.content.ParticleModel(CT_RadarSer._GroupModel, min_occurs=1, max_occurs=1)



CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_ScatterChart, documentation=u'Axis ID'))

CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scatterStyle'), CT_ScatterStyle, scope=CT_ScatterChart, documentation=u'Scatter Style'))

CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ScatterChart, documentation=u'Chart Extensibility'))

CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_ScatterChart, documentation=u'Data Labels'))

CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_ScatterChart, documentation=u'Vary Colors by Point'))

CT_ScatterChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_ScatterSer, scope=CT_ScatterChart, documentation=u'Scatter Chart Series'))
CT_ScatterChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scatterStyle')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_ScatterChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ScatterChart._ContentModel = pyxb.binding.content.ParticleModel(CT_ScatterChart._GroupModel, min_occurs=1, max_occurs=1)



CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_PieSer))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_PieSer, documentation=u'Index'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_PieSer, documentation=u'Data Labels'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_PieSer, documentation=u'Category Axis Data'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_PieSer, documentation=u'Data Point'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_PieSer))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_PieSer, documentation=u'Order'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_PieSer, documentation=u'Chart Extensibility'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'explosion'), CT_UnsignedInt, scope=CT_PieSer, documentation=u'Explosion'))

CT_PieSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_PieSer, documentation=u'Series Text'))
CT_PieSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_PieSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PieSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'explosion')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PieSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_PieSer._ContentModel = pyxb.binding.content.ParticleModel(CT_PieSer._GroupModel, min_occurs=1, max_occurs=1)



CT_StrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_StrData))

CT_StrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ptCount'), CT_UnsignedInt, scope=CT_StrData))

CT_StrData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pt'), CT_StrVal, scope=CT_StrData))
CT_StrData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_StrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ptCount')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_StrData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_StrData._ContentModel = pyxb.binding.content.ParticleModel(CT_StrData._GroupModel, min_occurs=1, max_occurs=1)



CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_DLbl, documentation=u'Delete'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_DLbl, documentation=u'Index'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showCatName'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Category Name'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DLbl))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showSerName'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Series Name'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_DLbl))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_DLbl, documentation=u'Layout'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showPercent'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Percent'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DLbl, documentation=u'Chart Extensibility'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_Tx, scope=CT_DLbl))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Bubble Size'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Legend Key'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLblPos'), CT_DLblPos, scope=CT_DLbl, documentation=u'Data Label Position'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'separator'), pyxb.binding.datatypes.string, scope=CT_DLbl, documentation=u'Separator'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showVal'), CT_Boolean, scope=CT_DLbl, documentation=u'Show Value'))

CT_DLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_DLbl, documentation=u'Number Format'))
CT_DLbl._GroupModel_3 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showLegendKey')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showCatName')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showSerName')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showPercent')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showBubbleSize')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'separator')), min_occurs=0L, max_occurs=1L)
    )
CT_DLbl._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._GroupModel_3, min_occurs=1L, max_occurs=1L)
    )
CT_DLbl._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_DLbl._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DLbl._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_DLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DLbl._ContentModel = pyxb.binding.content.ParticleModel(CT_DLbl._GroupModel, min_occurs=1, max_occurs=1)



CT_ExternalData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'autoUpdate'), CT_Boolean, scope=CT_ExternalData, documentation=u'Update Automatically'))
CT_ExternalData._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ExternalData._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'autoUpdate')), min_occurs=0L, max_occurs=1L)
    )
CT_ExternalData._ContentModel = pyxb.binding.content.ParticleModel(CT_ExternalData._GroupModel, min_occurs=1, max_occurs=1)



CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'holeSize'), CT_HoleSize, scope=CT_DoughnutChart, documentation=u'Hole Size'))

CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_DoughnutChart, documentation=u'Data Labels'))

CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng'), CT_FirstSliceAng, scope=CT_DoughnutChart, documentation=u'First Slice Angle'))

CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DoughnutChart, documentation=u'Chart Extensibility'))

CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_DoughnutChart))

CT_DoughnutChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_PieSer, scope=CT_DoughnutChart, documentation=u'Pie Chart Series'))
CT_DoughnutChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_DoughnutChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstSliceAng')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'holeSize')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DoughnutChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DoughnutChart._ContentModel = pyxb.binding.content.ParticleModel(CT_DoughnutChart._GroupModel, min_occurs=1, max_occurs=1)



CT_Scaling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Scaling, documentation=u'Chart Extensibility'))

CT_Scaling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'logBase'), CT_LogBase, scope=CT_Scaling, documentation=u'Logarithmic Base'))

CT_Scaling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'max'), CT_Double, scope=CT_Scaling, documentation=u'Maximum'))

CT_Scaling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'min'), CT_Double, scope=CT_Scaling, documentation=u'Minimum'))

CT_Scaling._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orientation'), CT_Orientation, scope=CT_Scaling, documentation=u'Axis Orientation'))
CT_Scaling._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Scaling._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'logBase')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Scaling._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orientation')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Scaling._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'max')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Scaling._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'min')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Scaling._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Scaling._ContentModel = pyxb.binding.content.ParticleModel(CT_Scaling._GroupModel, min_occurs=1, max_occurs=1)



CT_PivotFmts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pivotFmt'), CT_PivotFmt, scope=CT_PivotFmts, documentation=u'Pivot Format'))
CT_PivotFmts._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PivotFmts._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pivotFmt')), min_occurs=0L, max_occurs=None)
    )
CT_PivotFmts._ContentModel = pyxb.binding.content.ParticleModel(CT_PivotFmts._GroupModel, min_occurs=1, max_occurs=1)



CT_CustSplit._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secondPiePt'), CT_UnsignedInt, scope=CT_CustSplit, documentation=u'Second Pie Point'))
CT_CustSplit._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_CustSplit._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secondPiePt')), min_occurs=0L, max_occurs=None)
    )
CT_CustSplit._ContentModel = pyxb.binding.content.ParticleModel(CT_CustSplit._GroupModel, min_occurs=1, max_occurs=1)



CT_DispUnits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DispUnits, documentation=u'Chart Extensibility'))

CT_DispUnits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'custUnit'), CT_Double, scope=CT_DispUnits, documentation=u'Custom Display Unit'))

CT_DispUnits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispUnitsLbl'), CT_DispUnitsLbl, scope=CT_DispUnits, documentation=u'Display Units Label'))

CT_DispUnits._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'builtInUnit'), CT_BuiltInUnit, scope=CT_DispUnits, documentation=u'Built in Display Unit Value'))
CT_DispUnits._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_DispUnits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'custUnit')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DispUnits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'builtInUnit')), min_occurs=1L, max_occurs=1L)
    )
CT_DispUnits._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DispUnits._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_DispUnits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispUnitsLbl')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DispUnits._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DispUnits._ContentModel = pyxb.binding.content.ParticleModel(CT_DispUnits._GroupModel, min_occurs=1, max_occurs=1)



CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layoutTarget'), CT_LayoutTarget, scope=CT_ManualLayout, documentation=u'Layout Target'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ManualLayout, documentation=u'Chart Extensibility'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'w'), CT_Double, scope=CT_ManualLayout, documentation=u'Width'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'h'), CT_Double, scope=CT_ManualLayout, documentation=u'Height'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'y'), CT_Double, scope=CT_ManualLayout, documentation=u'Top'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wMode'), CT_LayoutMode, scope=CT_ManualLayout, documentation=u'Width Mode'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yMode'), CT_LayoutMode, scope=CT_ManualLayout, documentation=u'Top Mode'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hMode'), CT_LayoutMode, scope=CT_ManualLayout, documentation=u'Height Mode'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'x'), CT_Double, scope=CT_ManualLayout, documentation=u'Left'))

CT_ManualLayout._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xMode'), CT_LayoutMode, scope=CT_ManualLayout, documentation=u'Left Mode'))
CT_ManualLayout._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layoutTarget')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xMode')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yMode')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wMode')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hMode')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'x')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'y')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'w')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'h')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ManualLayout._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ManualLayout._ContentModel = pyxb.binding.content.ParticleModel(CT_ManualLayout._GroupModel, min_occurs=1, max_occurs=1)



CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_Area3DChart))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_Grouping, scope=CT_Area3DChart, documentation=u'Grouping'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_AreaSer, scope=CT_Area3DChart, documentation=u'Area Chart Series'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Area3DChart, documentation=u'Chart Extensibility'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_Area3DChart, documentation=u'Data Labels'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), CT_GapAmount, scope=CT_Area3DChart, documentation=u'Gap Depth'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), CT_ChartLines, scope=CT_Area3DChart, documentation=u'Drop Lines'))

CT_Area3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_Area3DChart, documentation=u'Axis ID'))
CT_Area3DChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dropLines')), min_occurs=0L, max_occurs=1L)
    )
CT_Area3DChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Area3DChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapDepth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CT_Area3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Area3DChart._ContentModel = pyxb.binding.content.ParticleModel(CT_Area3DChart._GroupModel, min_occurs=1, max_occurs=1)



CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_LineChart, documentation=u'Axis ID'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_LineChart, documentation=u'Data Labels'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), CT_ChartLines, scope=CT_LineChart, documentation=u'Drop Lines'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_LineChart, documentation=u'Chart Extensibility'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'smooth'), CT_Boolean, scope=CT_LineChart))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_Grouping, scope=CT_LineChart, documentation=u'Grouping'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines'), CT_ChartLines, scope=CT_LineChart, documentation=u'High Low Lines'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Boolean, scope=CT_LineChart, documentation=u'Show Marker'))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_LineChart))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'upDownBars'), CT_UpDownBars, scope=CT_LineChart))

CT_LineChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_LineSer, scope=CT_LineChart))
CT_LineChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dropLines')), min_occurs=0L, max_occurs=1L)
    )
CT_LineChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LineChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'upDownBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'smooth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_LineChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_LineChart._ContentModel = pyxb.binding.content.ParticleModel(CT_LineChart._GroupModel, min_occurs=1, max_occurs=1)



CT_MultiLvlStrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_MultiLvlStrRef))

CT_MultiLvlStrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'f'), pyxb.binding.datatypes.string, scope=CT_MultiLvlStrRef, documentation=u'Formula'))

CT_MultiLvlStrRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrCache'), CT_MultiLvlStrData, scope=CT_MultiLvlStrRef, documentation=u'Multi Level String Cache'))
CT_MultiLvlStrRef._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'f')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'multiLvlStrCache')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_MultiLvlStrRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_MultiLvlStrRef._ContentModel = pyxb.binding.content.ParticleModel(CT_MultiLvlStrRef._GroupModel, min_occurs=1, max_occurs=1)



CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_CatAx, documentation=u'Axis ID'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_CatAx, documentation=u'Chart Extensibility'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scaling'), CT_Scaling, scope=CT_CatAx, documentation=u'Scaling'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), CT_ChartLines, scope=CT_CatAx, documentation=u'Minor Gridlines'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_CatAx, documentation=u'Delete'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), CT_ChartLines, scope=CT_CatAx, documentation=u'Major Gridlines'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), CT_Title, scope=CT_CatAx, documentation=u'Title'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lblOffset'), CT_LblOffset, scope=CT_CatAx, documentation=u'Label Offset'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_CatAx, documentation=u'Number Format'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), CT_TickMark, scope=CT_CatAx, documentation=u'Major Tick Mark'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), CT_TickMark, scope=CT_CatAx, documentation=u'Minor Tick Mark'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip'), CT_Skip, scope=CT_CatAx))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip'), CT_Skip, scope=CT_CatAx, documentation=u'Tick Mark Skip'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_CatAx))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'noMultiLvlLbl'), CT_Boolean, scope=CT_CatAx, documentation=u'No Multi-level Labels'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_CatAx))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), CT_TickLblPos, scope=CT_CatAx, documentation=u'Tick Label Position'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), CT_UnsignedInt, scope=CT_CatAx, documentation=u'Crossing Axis ID'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axPos'), CT_AxPos, scope=CT_CatAx, documentation=u'Axis Position'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crosses'), CT_Crosses, scope=CT_CatAx, documentation=u'Crosses'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lblAlgn'), CT_LblAlgn, scope=CT_CatAx, documentation=u'Label Alignment'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), CT_Double, scope=CT_CatAx, documentation=u'Crossing Value'))

CT_CatAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'auto'), CT_Boolean, scope=CT_CatAx, documentation=u'Automatic Category Axis'))
CT_CatAx._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crosses')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossesAt')), min_occurs=1L, max_occurs=1L)
    )
CT_CatAx._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scaling')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axPos')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._GroupModel_2, min_occurs=0L, max_occurs=1L)
    )
CT_CatAx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_CatAx._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'auto')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lblAlgn')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lblOffset')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'noMultiLvlLbl')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_CatAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_CatAx._ContentModel = pyxb.binding.content.ParticleModel(CT_CatAx._GroupModel, min_occurs=1, max_occurs=1)



CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'splitPos'), CT_Double, scope=CT_OfPieChart, documentation=u'Split Position'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_PieSer, scope=CT_OfPieChart, documentation=u'Pie Chart Series'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), CT_GapAmount, scope=CT_OfPieChart, documentation=u'Gap Width'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_OfPieChart))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ofPieType'), CT_OfPieType, scope=CT_OfPieChart, documentation=u'Pie of Pie or Bar of Pie Type'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'secondPieSize'), CT_SecondPieSize, scope=CT_OfPieChart, documentation=u'Second Pie Size'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'custSplit'), CT_CustSplit, scope=CT_OfPieChart, documentation=u'Custom Split'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'serLines'), CT_ChartLines, scope=CT_OfPieChart))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_OfPieChart, documentation=u'Data Labels'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_OfPieChart, documentation=u'Chart Extensibility'))

CT_OfPieChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'splitType'), CT_SplitType, scope=CT_OfPieChart, documentation=u'Split Type'))
CT_OfPieChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_OfPieChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ofPieType')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapWidth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'splitType')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'splitPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'custSplit')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'secondPieSize')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'serLines')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_OfPieChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_OfPieChart._ContentModel = pyxb.binding.content.ParticleModel(CT_OfPieChart._GroupModel, min_occurs=1, max_occurs=1)



CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative'), CT_Boolean, scope=CT_BarSer, documentation=u'Invert if Negative'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_BarSer, documentation=u'Index'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cat'), CT_AxDataSource, scope=CT_BarSer, documentation=u'Category Axis Data'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_BarSer, documentation=u'Order'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'val'), CT_NumDataSource, scope=CT_BarSer))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_BarSer, documentation=u'Data Point'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBars'), CT_ErrBars, scope=CT_BarSer, documentation=u'Error Bars'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_BarSer, documentation=u'Data Labels'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_BarSer))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_BarSer, documentation=u'Series Text'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_BarSer, documentation=u'Chart Extensibility'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendline'), CT_Trendline, scope=CT_BarSer, documentation=u'Trendlines'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shape'), CT_Shape, scope=CT_BarSer, documentation=u'Shape'))

CT_BarSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), CT_PictureOptions, scope=CT_BarSer))
CT_BarSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_BarSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BarSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'invertIfNegative')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendline')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cat')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'val')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shape')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BarSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_BarSer._ContentModel = pyxb.binding.content.ParticleModel(CT_BarSer._GroupModel, min_occurs=1, max_occurs=1)



CT_Surface._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Surface, documentation=u'Chart Extensibility'))

CT_Surface._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'thickness'), CT_UnsignedInt, scope=CT_Surface, documentation=u'Thickness'))

CT_Surface._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Surface))

CT_Surface._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions'), CT_PictureOptions, scope=CT_Surface, documentation=u'Picture Options'))
CT_Surface._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Surface._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'thickness')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Surface._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Surface._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pictureOptions')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Surface._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Surface._ContentModel = pyxb.binding.content.ParticleModel(CT_Surface._GroupModel, min_occurs=1, max_occurs=1)



CT_StrVal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'v'), _s.ST_Xstring, scope=CT_StrVal, documentation=u'Text Value'))
CT_StrVal._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_StrVal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'v')), min_occurs=1L, max_occurs=1L)
    )
CT_StrVal._ContentModel = pyxb.binding.content.ParticleModel(CT_StrVal._GroupModel, min_occurs=1, max_occurs=1)



CT_Pie3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Pie3DChart, documentation=u'Chart Extensibility'))

CT_Pie3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_Pie3DChart, documentation=u'Data Labels'))

CT_Pie3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_Pie3DChart))

CT_Pie3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_PieSer, scope=CT_Pie3DChart, documentation=u'Pie Chart Series'))
CT_Pie3DChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Pie3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Pie3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Pie3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_Pie3DChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Pie3DChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Pie3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Pie3DChart._ContentModel = pyxb.binding.content.ParticleModel(CT_Pie3DChart._GroupModel, min_occurs=1, max_occurs=1)



CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_RadarChart, documentation=u'Chart Extensibility'))

CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'radarStyle'), CT_RadarStyle, scope=CT_RadarChart, documentation=u'Radar Style'))

CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_RadarChart))

CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_RadarSer, scope=CT_RadarChart, documentation=u'Radar Chart Series'))

CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_RadarChart, documentation=u'Data Labels'))

CT_RadarChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_RadarChart, documentation=u'Axis ID'))
CT_RadarChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'radarStyle')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_RadarChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_RadarChart._ContentModel = pyxb.binding.content.ParticleModel(CT_RadarChart._GroupModel, min_occurs=1, max_occurs=1)



CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showVertBorder'), CT_Boolean, scope=CT_DTable, documentation=u'Show Vertical Border'))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_DTable, documentation=u'Chart Extensibility'))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showOutline'), CT_Boolean, scope=CT_DTable, documentation=u'Show Outline Border'))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showKeys'), CT_Boolean, scope=CT_DTable, documentation=u'Show Legend Keys'))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_DTable))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_DTable, documentation=u'Text Properties'))

CT_DTable._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showHorzBorder'), CT_Boolean, scope=CT_DTable, documentation=u'Show Horizontal Border'))
CT_DTable._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showHorzBorder')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showVertBorder')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showOutline')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showKeys')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_DTable._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_DTable._ContentModel = pyxb.binding.content.ParticleModel(CT_DTable._GroupModel, min_occurs=1, max_occurs=1)



CT_NumRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_NumRef))

CT_NumRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'f'), pyxb.binding.datatypes.string, scope=CT_NumRef, documentation=u'Formula'))

CT_NumRef._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numCache'), CT_NumData, scope=CT_NumRef, documentation=u'Number Cache'))
CT_NumRef._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_NumRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'f')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_NumRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numCache')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_NumRef._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_NumRef._ContentModel = pyxb.binding.content.ParticleModel(CT_NumRef._GroupModel, min_occurs=1, max_occurs=1)



CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showNegBubbles'), CT_Boolean, scope=CT_BubbleChart, documentation=u'Show Negative Bubbles'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sizeRepresents'), CT_SizeRepresents, scope=CT_BubbleChart, documentation=u'Size Represents'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_BubbleSer, scope=CT_BubbleChart, documentation=u'Bubble Chart Series'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_BubbleChart, documentation=u'Axis ID'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_BubbleChart, documentation=u'Data Labels'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_BubbleChart))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_BubbleChart, documentation=u'Chart Extensibility'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubble3D'), CT_Boolean, scope=CT_BubbleChart, documentation=u'3D Bubble'))

CT_BubbleChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bubbleScale'), CT_BubbleScale, scope=CT_BubbleChart, documentation=u'Bubble Scale'))
CT_BubbleChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubble3D')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bubbleScale')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showNegBubbles')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sizeRepresents')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_BubbleChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_BubbleChart._ContentModel = pyxb.binding.content.ParticleModel(CT_BubbleChart._GroupModel, min_occurs=1, max_occurs=1)



CT_BandFmts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bandFmt'), CT_BandFmt, scope=CT_BandFmts, documentation=u'Band Format'))
CT_BandFmts._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_BandFmts._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bandFmt')), min_occurs=0L, max_occurs=None)
    )
CT_BandFmts._ContentModel = pyxb.binding.content.ParticleModel(CT_BandFmts._GroupModel, min_occurs=1, max_occurs=1)



CT_NumVal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'v'), _s.ST_Xstring, scope=CT_NumVal, documentation=u'Numeric Value'))
CT_NumVal._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_NumVal._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'v')), min_occurs=1L, max_occurs=1L)
    )
CT_NumVal._ContentModel = pyxb.binding.content.ParticleModel(CT_NumVal._GroupModel, min_occurs=1, max_occurs=1)



CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yVal'), CT_NumDataSource, scope=CT_ScatterSer))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dPt'), CT_DPt, scope=CT_ScatterSer, documentation=u'Data Point'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'smooth'), CT_Boolean, scope=CT_ScatterSer, documentation=u'Smoothing'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_ScatterSer, documentation=u'Index'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ScatterSer, documentation=u'Chart Extensibility'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_ScatterSer, documentation=u'Data Labels'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'order'), CT_UnsignedInt, scope=CT_ScatterSer, documentation=u'Order'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Marker, scope=CT_ScatterSer, documentation=u'Marker'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'trendline'), CT_Trendline, scope=CT_ScatterSer))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_SerTx, scope=CT_ScatterSer, documentation=u'Series Text'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'errBars'), CT_ErrBars, scope=CT_ScatterSer, documentation=u'Error Bars'))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_ScatterSer))

CT_ScatterSer._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'xVal'), CT_AxDataSource, scope=CT_ScatterSer))
CT_ScatterSer._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'order')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L)
    )
CT_ScatterSer._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ScatterSer._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dPt')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'trendline')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'errBars')), min_occurs=0L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'xVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yVal')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'smooth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ScatterSer._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ScatterSer._ContentModel = pyxb.binding.content.ParticleModel(CT_ScatterSer._GroupModel, min_occurs=1, max_occurs=1)



CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_TrendlineLbl))

CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_TrendlineLbl))

CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_TrendlineLbl, documentation=u'Chart Extensibility'))

CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_TrendlineLbl, documentation=u'Layout'))

CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tx'), CT_Tx, scope=CT_TrendlineLbl))

CT_TrendlineLbl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_TrendlineLbl, documentation=u'Number Format'))
CT_TrendlineLbl._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_TrendlineLbl._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_TrendlineLbl._ContentModel = pyxb.binding.content.ParticleModel(CT_TrendlineLbl._GroupModel, min_occurs=1, max_occurs=1)



CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_AreaSer, scope=CT_AreaChart, documentation=u'Area Chart Series'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_AreaChart, documentation=u'Axis ID'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_AreaChart, documentation=u'Chart Extensibility'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), CT_ChartLines, scope=CT_AreaChart, documentation=u'Drop Lines'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_AreaChart, documentation=u'Data Labels'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_Grouping, scope=CT_AreaChart, documentation=u'Grouping'))

CT_AreaChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_AreaChart))
CT_AreaChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dropLines')), min_occurs=0L, max_occurs=1L)
    )
CT_AreaChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_AreaChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_AreaChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_AreaChart._ContentModel = pyxb.binding.content.ParticleModel(CT_AreaChart._GroupModel, min_occurs=1, max_occurs=1)



CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'view3D'), CT_View3D, scope=CT_Chart, documentation=u'View In 3D'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'showDLblsOverMax'), CT_Boolean, scope=CT_Chart, documentation=u'Show Data Labels over Maximum'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'plotVisOnly'), CT_Boolean, scope=CT_Chart, documentation=u'Plot Visible Only'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'floor'), CT_Surface, scope=CT_Chart, documentation=u'Floor'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dispBlanksAs'), CT_DispBlanksAs, scope=CT_Chart, documentation=u'Display Blanks As'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sideWall'), CT_Surface, scope=CT_Chart, documentation=u'Side Wall'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legend'), CT_Legend, scope=CT_Chart, documentation=u'Legend'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), CT_Title, scope=CT_Chart))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'backWall'), CT_Surface, scope=CT_Chart, documentation=u'Back Wall'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'autoTitleDeleted'), CT_Boolean, scope=CT_Chart, documentation=u'Auto Title Is Deleted'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Chart, documentation=u'Chart Extensibility'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'plotArea'), CT_PlotArea, scope=CT_Chart, documentation=u'Plot Area'))

CT_Chart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pivotFmts'), CT_PivotFmts, scope=CT_Chart, documentation=u'Pivot Formats'))
CT_Chart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'autoTitleDeleted')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pivotFmts')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'view3D')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'floor')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sideWall')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'backWall')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'plotArea')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legend')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'plotVisOnly')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dispBlanksAs')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'showDLblsOverMax')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Chart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Chart._ContentModel = pyxb.binding.content.ParticleModel(CT_Chart._GroupModel, min_occurs=1, max_occurs=1)



CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'varyColors'), CT_Boolean, scope=CT_Bar3DChart))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapDepth'), CT_GapAmount, scope=CT_Bar3DChart, documentation=u'Gap Depth'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'shape'), CT_Shape, scope=CT_Bar3DChart))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_BarSer, scope=CT_Bar3DChart, documentation=u'Bar Chart Series'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_Bar3DChart, documentation=u'Axis ID'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'gapWidth'), CT_GapAmount, scope=CT_Bar3DChart, documentation=u'Gap Width'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_Bar3DChart, documentation=u'Data Labels'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Bar3DChart, documentation=u'Chart Extensibility'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'barDir'), CT_BarDir, scope=CT_Bar3DChart, documentation=u'Bar Direction'))

CT_Bar3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'grouping'), CT_BarGrouping, scope=CT_Bar3DChart, documentation=u'Bar Grouping'))
CT_Bar3DChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'barDir')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'grouping')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'varyColors')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L)
    )
CT_Bar3DChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapWidth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'gapDepth')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'shape')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CT_Bar3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Bar3DChart._ContentModel = pyxb.binding.content.ParticleModel(CT_Bar3DChart._GroupModel, min_occurs=1, max_occurs=1)



CT_Protection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'userInterface'), CT_Boolean, scope=CT_Protection, documentation=u'User Interface'))

CT_Protection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chartObject'), CT_Boolean, scope=CT_Protection, documentation=u'Chart Object'))

CT_Protection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'selection'), CT_Boolean, scope=CT_Protection, documentation=u'Selection'))

CT_Protection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'formatting'), CT_Boolean, scope=CT_Protection, documentation=u'Formatting'))

CT_Protection._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'data'), CT_Boolean, scope=CT_Protection, documentation=u'Data Cannot Be Changed'))
CT_Protection._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Protection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chartObject')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Protection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'data')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Protection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'formatting')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Protection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'selection')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Protection._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'userInterface')), min_occurs=0L, max_occurs=1L)
    )
CT_Protection._ContentModel = pyxb.binding.content.ParticleModel(CT_Protection._GroupModel, min_occurs=1, max_occurs=1)



CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'overlay'), CT_Boolean, scope=CT_Legend, documentation=u'Overlay'))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'layout'), CT_Layout, scope=CT_Legend, documentation=u'Layout'))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_Legend))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_Legend))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legendPos'), CT_LegendPos, scope=CT_Legend, documentation=u'Legend Position'))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Legend, documentation=u'Chart Extensibility'))

CT_Legend._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'legendEntry'), CT_LegendEntry, scope=CT_Legend, documentation=u'Legend Entry'))
CT_Legend._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legendPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'legendEntry')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'layout')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'overlay')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Legend._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Legend._ContentModel = pyxb.binding.content.ParticleModel(CT_Legend._GroupModel, min_occurs=1, max_occurs=1)



CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dropLines'), CT_ChartLines, scope=CT_StockChart))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines'), CT_ChartLines, scope=CT_StockChart, documentation=u'High Low Lines'))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'upDownBars'), CT_UpDownBars, scope=CT_StockChart, documentation=u'Up/Down Bars'))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_StockChart, documentation=u'Axis ID'))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_LineSer, scope=CT_StockChart, documentation=u'Line Chart Series'))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_StockChart, documentation=u'Chart Extensibility'))

CT_StockChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbls'), CT_DLbls, scope=CT_StockChart, documentation=u'Data Labels'))
CT_StockChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=3L, max_occurs=4L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbls')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dropLines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hiLowLines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'upDownBars')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=2L, max_occurs=2L),
    pyxb.binding.content.ParticleModel(CT_StockChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_StockChart._ContentModel = pyxb.binding.content.ParticleModel(CT_StockChart._GroupModel, min_occurs=1, max_occurs=1)



CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), CT_Title, scope=CT_SerAx, documentation=u'Title'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_SerAx, documentation=u'Chart Extensibility'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'scaling'), CT_Scaling, scope=CT_SerAx, documentation=u'Scaling'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_SerAx))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_SerAx))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_SerAx, documentation=u'Delete'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark'), CT_TickMark, scope=CT_SerAx, documentation=u'Major Tick Mark'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axPos'), CT_AxPos, scope=CT_SerAx, documentation=u'Axis Position'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'numFmt'), CT_NumFmt, scope=CT_SerAx, documentation=u'Number Format'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark'), CT_TickMark, scope=CT_SerAx, documentation=u'Minor Tick Mark'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines'), CT_ChartLines, scope=CT_SerAx, documentation=u'Major Gridlines'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos'), CT_TickLblPos, scope=CT_SerAx, documentation=u'Tick Label Position'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossAx'), CT_UnsignedInt, scope=CT_SerAx, documentation=u'Crossing Axis ID'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines'), CT_ChartLines, scope=CT_SerAx, documentation=u'Minor Gridlines'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crossesAt'), CT_Double, scope=CT_SerAx, documentation=u'Crossing Value'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_SerAx, documentation=u'Axis ID'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'crosses'), CT_Crosses, scope=CT_SerAx, documentation=u'Crosses'))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip'), CT_Skip, scope=CT_SerAx))

CT_SerAx._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip'), CT_Skip, scope=CT_SerAx, documentation=u'Tick Label Skip'))
CT_SerAx._GroupModel_2 = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crosses')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossesAt')), min_occurs=1L, max_occurs=1L)
    )
CT_SerAx._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'scaling')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axPos')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorGridlines')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'numFmt')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'majorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'minorTickMark')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblPos')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'crossAx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._GroupModel_2, min_occurs=0L, max_occurs=1L)
    )
CT_SerAx._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_SerAx._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickLblSkip')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'tickMarkSkip')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_SerAx._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_SerAx._ContentModel = pyxb.binding.content.ParticleModel(CT_SerAx._GroupModel, min_occurs=1, max_occurs=1)



CT_Surface3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_Surface3DChart, documentation=u'Chart Extensibility'))

CT_Surface3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'bandFmts'), CT_BandFmts, scope=CT_Surface3DChart, documentation=u'Band Formats'))

CT_Surface3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'axId'), CT_UnsignedInt, scope=CT_Surface3DChart, documentation=u'Axis ID'))

CT_Surface3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ser'), CT_SurfaceSer, scope=CT_Surface3DChart, documentation=u'Surface Chart Series'))

CT_Surface3DChart._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'wireframe'), CT_Boolean, scope=CT_Surface3DChart, documentation=u'Wireframe'))
CT_Surface3DChart._GroupModel_ = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'wireframe')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ser')), min_occurs=0L, max_occurs=None),
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'bandFmts')), min_occurs=0L, max_occurs=1L)
    )
CT_Surface3DChart._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._GroupModel_, min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'axId')), min_occurs=3L, max_occurs=3L),
    pyxb.binding.content.ParticleModel(CT_Surface3DChart._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_Surface3DChart._ContentModel = pyxb.binding.content.ParticleModel(CT_Surface3DChart._GroupModel, min_occurs=1, max_occurs=1)



CT_LegendEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_LegendEntry, documentation=u'Chart Extensibility'))

CT_LegendEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_LegendEntry, documentation=u'Index'))

CT_LegendEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'delete'), CT_Boolean, scope=CT_LegendEntry, documentation=u'Delete'))

CT_LegendEntry._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_LegendEntry))
CT_LegendEntry._GroupModel_2 = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LegendEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L)
    )
CT_LegendEntry._GroupModel_ = pyxb.binding.content.GroupChoice(
    pyxb.binding.content.ParticleModel(CT_LegendEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'delete')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LegendEntry._GroupModel_2, min_occurs=1L, max_occurs=1L)
    )
CT_LegendEntry._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_LegendEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_LegendEntry._GroupModel_, min_occurs=1, max_occurs=1),
    pyxb.binding.content.ParticleModel(CT_LegendEntry._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_LegendEntry._ContentModel = pyxb.binding.content.ParticleModel(CT_LegendEntry._GroupModel, min_occurs=1, max_occurs=1)



CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rAngAx'), CT_Boolean, scope=CT_View3D, documentation=u'Right Angle Axes'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'depthPercent'), CT_DepthPercent, scope=CT_View3D, documentation=u'Depth Percent'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rotX'), CT_RotX, scope=CT_View3D, documentation=u'X Rotation'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_View3D, documentation=u'Chart Extensibility'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'hPercent'), CT_HPercent, scope=CT_View3D, documentation=u'Height Percent'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'rotY'), CT_RotY, scope=CT_View3D, documentation=u'Y Rotation'))

CT_View3D._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'perspective'), CT_Perspective, scope=CT_View3D, documentation=u'Perspective'))
CT_View3D._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rotX')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'hPercent')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rotY')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'depthPercent')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'rAngAx')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'perspective')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_View3D._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_View3D._ContentModel = pyxb.binding.content.ParticleModel(CT_View3D._GroupModel, min_occurs=1, max_occurs=1)



CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dLbl'), CT_DLbl, scope=CT_PivotFmt, documentation=u'Data Label'))

CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_PivotFmt, documentation=u'Chart Extensibility'))

CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'marker'), CT_Marker, scope=CT_PivotFmt, documentation=u'Marker'))

CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'idx'), CT_UnsignedInt, scope=CT_PivotFmt, documentation=u'Index'))

CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_PivotFmt))

CT_PivotFmt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_PivotFmt))
CT_PivotFmt._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'idx')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'marker')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dLbl')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_PivotFmt._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_PivotFmt._ContentModel = pyxb.binding.content.ParticleModel(CT_PivotFmt._GroupModel, min_occurs=1, max_occurs=1)



CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'clrMapOvr'), _nsgroup.CT_ColorMapping, scope=CT_ChartSpace, documentation=u'Color Map Override'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'pivotSource'), CT_PivotSource, scope=CT_ChartSpace, documentation=u'Pivot Source'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'userShapes'), CT_RelId, scope=CT_ChartSpace, documentation=u'Reference to Chart Drawing Part'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'date1904'), CT_Boolean, scope=CT_ChartSpace, documentation=u'1904 Date System'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'protection'), CT_Protection, scope=CT_ChartSpace, documentation=u'Protection'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lang'), CT_TextLanguageID, scope=CT_ChartSpace, documentation=u'Editing Language'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'externalData'), CT_ExternalData, scope=CT_ChartSpace, documentation=u'External Data Relationship'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chart'), CT_Chart, scope=CT_ChartSpace, documentation=u'Chart'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'roundedCorners'), CT_Boolean, scope=CT_ChartSpace, documentation=u'Rounded Corners'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'spPr'), _nsgroup.CT_ShapeProperties, scope=CT_ChartSpace, documentation=u'Shape Properties'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'style'), CT_Style, scope=CT_ChartSpace, documentation=u'Style'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'printSettings'), CT_PrintSettings, scope=CT_ChartSpace, documentation=u'Print Settings'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'extLst'), CT_ExtensionList, scope=CT_ChartSpace, documentation=u'Chart Extensibility'))

CT_ChartSpace._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'txPr'), _nsgroup.CT_TextBody, scope=CT_ChartSpace))
CT_ChartSpace._GroupModel = pyxb.binding.content.GroupSequence(
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'date1904')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lang')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'roundedCorners')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'style')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'clrMapOvr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'pivotSource')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'protection')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chart')), min_occurs=1L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'spPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'txPr')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'externalData')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'printSettings')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'userShapes')), min_occurs=0L, max_occurs=1L),
    pyxb.binding.content.ParticleModel(CT_ChartSpace._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'extLst')), min_occurs=0L, max_occurs=1L)
    )
CT_ChartSpace._ContentModel = pyxb.binding.content.ParticleModel(CT_ChartSpace._GroupModel, min_occurs=1, max_occurs=1)
