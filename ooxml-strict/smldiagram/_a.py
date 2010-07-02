# ./_a.py
# PyXB bindings for NamespaceModule
# NSM:b1de9718f9d20df6f07682d1d4e3edc19321d557
# Generated 2010-07-02 14:32:40.122022 by PyXB version 1.1.2
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
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/drawingml/2006/main', create_if_missing=True)
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

from _nsgroup import themeManager # {http://schemas.openxmlformats.org/drawingml/2006/main}themeManager
from _nsgroup import tblStyleLst # {http://schemas.openxmlformats.org/drawingml/2006/main}tblStyleLst
from _nsgroup import theme # {http://schemas.openxmlformats.org/drawingml/2006/main}theme
from _nsgroup import graphic # {http://schemas.openxmlformats.org/drawingml/2006/main}graphic
from _nsgroup import videoFile # {http://schemas.openxmlformats.org/drawingml/2006/main}videoFile
from _nsgroup import themeOverride # {http://schemas.openxmlformats.org/drawingml/2006/main}themeOverride
from _nsgroup import blip # {http://schemas.openxmlformats.org/drawingml/2006/main}blip
from _nsgroup import tbl # {http://schemas.openxmlformats.org/drawingml/2006/main}tbl
from _nsgroup import CT_GrayscaleEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GrayscaleEffect
from _nsgroup import ST_BlackWhiteMode # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_BlackWhiteMode
from _nsgroup import CT_ShapeProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ShapeProperties
from _nsgroup import CT_NoFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NoFillProperties
from _nsgroup import CT_FillEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FillEffect
from _nsgroup import CT_ThemeableLineStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ThemeableLineStyle
from _nsgroup import ST_PercentageDecimal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PercentageDecimal
from _nsgroup import ST_Percentage # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_Percentage
from _nsgroup import CT_Percentage # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Percentage
from _nsgroup import CT_AlphaInverseEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaInverseEffect
from _nsgroup import CT_NonVisualDrawingShapeProps # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualDrawingShapeProps
from _nsgroup import CT_SRgbColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SRgbColor
from _nsgroup import ST_SystemColorVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_SystemColorVal
from _nsgroup import CT_SystemColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SystemColor
from _nsgroup import ST_CoordinateUnqualified # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_CoordinateUnqualified
from _nsgroup import ST_GeomGuideName # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_GeomGuideName
from _nsgroup import ST_AdjCoordinate # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AdjCoordinate
from _nsgroup import CT_AdjPoint2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AdjPoint2D
from _nsgroup import ST_PresetPatternVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetPatternVal
from _nsgroup import CT_PatternFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PatternFillProperties
from _nsgroup import CT_GvmlUseShapeRectangle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlUseShapeRectangle
from _nsgroup import CT_Scale2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Scale2D
from _nsgroup import CT_ColorScheme # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorScheme
from _nsgroup import CT_Scene3D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Scene3D
from _nsgroup import CT_BackgroundFormatting # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BackgroundFormatting
from _nsgroup import CT_EmptyElement # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EmptyElement
from _nsgroup import ST_PresetColorVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetColorVal
from _nsgroup import CT_PresetColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PresetColor
from _nsgroup import CT_Boolean # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Boolean
from _nsgroup import ST_TextBulletSizePercent # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextBulletSizePercent
from _nsgroup import CT_TextBulletSizePercent # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBulletSizePercent
from _nsgroup import ST_PositiveCoordinate # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositiveCoordinate
from _nsgroup import CT_SoftEdgesEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SoftEdgesEffect
from _nsgroup import CT_OfficeArtExtensionList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_OfficeArtExtensionList
from _nsgroup import ST_LightRigDirection # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LightRigDirection
from _nsgroup import ST_LightRigType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LightRigType
from _nsgroup import CT_LightRig # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LightRig
from _nsgroup import CT_InverseTransform # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_InverseTransform
from _nsgroup import CT_GvmlShape # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlShape
from _nsgroup import ST_FontCollectionIndex # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_FontCollectionIndex
from _nsgroup import CT_FontReference # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FontReference
from _nsgroup import ST_Angle # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_Angle
from _nsgroup import CT_Angle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Angle
from _nsgroup import ST_PositivePercentageDecimal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositivePercentageDecimal
from _nsgroup import ST_PositivePercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositivePercentage
from _nsgroup import CT_PositivePercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PositivePercentage
from _nsgroup import CT_BlipFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BlipFillProperties
from _nsgroup import CT_LineJoinMiterProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineJoinMiterProperties
from _nsgroup import ST_PositiveFixedAngle # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositiveFixedAngle
from _nsgroup import CT_HslColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_HslColor
from _nsgroup import ST_PositiveFixedPercentageDecimal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositiveFixedPercentageDecimal
from _nsgroup import ST_PositiveFixedPercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositiveFixedPercentage
from _nsgroup import CT_PositiveFixedPercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PositiveFixedPercentage
from _nsgroup import ST_SchemeColorVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_SchemeColorVal
from _nsgroup import CT_SchemeColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SchemeColor
from _nsgroup import CT_Path2DLineTo # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DLineTo
from _nsgroup import CT_TableStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableStyle
from _nsgroup import ST_Coordinate32Unqualified # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_Coordinate32Unqualified
from _nsgroup import ST_TextMargin # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextMargin
from _nsgroup import ST_Coordinate32 # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_Coordinate32
from _nsgroup import ST_TextFontAlignType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextFontAlignType
from _nsgroup import ST_TextIndent # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextIndent
from _nsgroup import ST_TextAlignType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextAlignType
from _nsgroup import ST_TextIndentLevelType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextIndentLevelType
from _nsgroup import CT_TextParagraphProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextParagraphProperties
from _nsgroup import CT_ClipboardStyleSheet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ClipboardStyleSheet
from _nsgroup import CT_ColorChangeEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorChangeEffect
from _nsgroup import CT_DuotoneEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_DuotoneEffect
from _nsgroup import CT_TextUnderlineLineFollowText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextUnderlineLineFollowText
from _nsgroup import CT_GraphicalObject # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GraphicalObject
from _nsgroup import CT_TableStyleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableStyleList
from _nsgroup import CT_AlphaReplaceEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaReplaceEffect
from _nsgroup import ST_TextTypeface # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextTypeface
from _nsgroup import CT_TextFont # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextFont
from _nsgroup import CT_GrayscaleTransform # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GrayscaleTransform
from _nsgroup import ST_TextCapsType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextCapsType
from _nsgroup import ST_TextPointUnqualified # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextPointUnqualified
from _nsgroup import ST_TextPoint # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextPoint
from _nsgroup import ST_TextNonNegativePoint # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextNonNegativePoint
from _nsgroup import ST_TextStrikeType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextStrikeType
from _nsgroup import ST_TextUnderlineType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextUnderlineType
from _nsgroup import ST_TextFontSize # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextFontSize
from _nsgroup import CT_TextCharacterProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextCharacterProperties
from _nsgroup import CT_OfficeStyleSheet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_OfficeStyleSheet
from _nsgroup import CT_NonVisualGroupDrawingShapeProps # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualGroupDrawingShapeProps
from _nsgroup import CT_ShapeStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ShapeStyle
from _nsgroup import ST_TextBulletStartAtNum # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextBulletStartAtNum
from _nsgroup import ST_TextAutonumberScheme # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextAutonumberScheme
from _nsgroup import CT_TextAutonumberBullet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextAutonumberBullet
from _nsgroup import CT_EffectList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectList
from _nsgroup import CT_ScRgbColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ScRgbColor
from _nsgroup import ST_EffectContainerType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_EffectContainerType
from _nsgroup import CT_EffectContainer # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectContainer
from _nsgroup import ST_PenAlignment # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PenAlignment
from _nsgroup import ST_CompoundLine # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_CompoundLine
from _nsgroup import ST_LineWidth # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LineWidth
from _nsgroup import ST_LineCap # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LineCap
from _nsgroup import CT_LineProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineProperties
from _nsgroup import ST_PathShadeType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PathShadeType
from _nsgroup import CT_PathShadeProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PathShadeProperties
from _nsgroup import ST_RectAlignment # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_RectAlignment
from _nsgroup import ST_FixedAngle # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_FixedAngle
from _nsgroup import CT_OuterShadowEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_OuterShadowEffect
from _nsgroup import ST_ColorSchemeIndex # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_ColorSchemeIndex
from _nsgroup import CT_ColorMapping # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorMapping
from _nsgroup import ST_StyleMatrixColumnIndex # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_StyleMatrixColumnIndex
from _nsgroup import CT_StyleMatrixReference # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_StyleMatrixReference
from _nsgroup import CT_Color # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Color
from _nsgroup import CT_EffectStyleItem # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectStyleItem
from _nsgroup import CT_GeomGuideList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GeomGuideList
from _nsgroup import CT_TableProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableProperties
from _nsgroup import CT_LineJoinRound # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineJoinRound
from _nsgroup import CT_ComplementTransform # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ComplementTransform
from _nsgroup import CT_ShapeLocking # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ShapeLocking
from _nsgroup import ST_TileFlipMode # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TileFlipMode
from _nsgroup import ST_Coordinate # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_Coordinate
from _nsgroup import CT_TileInfoProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TileInfoProperties
from _nsgroup import CT_FontCollection # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FontCollection
from _nsgroup import CT_AlphaFloorEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaFloorEffect
from _nsgroup import ST_ShapeType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_ShapeType
from _nsgroup import ST_FixedPercentageDecimal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_FixedPercentageDecimal
from _nsgroup import ST_FixedPercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_FixedPercentage
from _nsgroup import CT_FixedPercentage # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FixedPercentage
from _nsgroup import CT_TextBody # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBody
from _nsgroup import CT_AudioCD # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AudioCD
from _nsgroup import CT_PositiveFixedAngle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PositiveFixedAngle
from _nsgroup import CT_DefaultShapeDefinition # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_DefaultShapeDefinition
from _nsgroup import CT_GammaTransform # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GammaTransform
from _nsgroup import ST_PresetMaterialType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetMaterialType
from _nsgroup import CT_Shape3D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Shape3D
from _nsgroup import CT_BaseStyles # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BaseStyles
from _nsgroup import CT_GvmlGraphicalObjectFrame # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlGraphicalObjectFrame
from _nsgroup import ST_TextWrappingType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextWrappingType
from _nsgroup import ST_TextColumnCount # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextColumnCount
from _nsgroup import ST_TextAnchoringType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextAnchoringType
from _nsgroup import ST_PositiveCoordinate32 # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PositiveCoordinate32
from _nsgroup import ST_TextVertOverflowType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextVertOverflowType
from _nsgroup import ST_TextHorzOverflowType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextHorzOverflowType
from _nsgroup import ST_TextVerticalType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextVerticalType
from _nsgroup import CT_TextBodyProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBodyProperties
from _nsgroup import CT_EffectReference # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectReference
from _nsgroup import CT_GlowEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GlowEffect
from _nsgroup import CT_Path2DCubicBezierTo # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DCubicBezierTo
from _nsgroup import CT_GradientFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GradientFillProperties
from _nsgroup import CT_GvmlTextShape # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlTextShape
from _nsgroup import CT_InverseGammaTransform # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_InverseGammaTransform
from _nsgroup import CT_LineJoinBevel # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineJoinBevel
from _nsgroup import CT_StyleMatrix # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_StyleMatrix
from _nsgroup import ST_TextTabAlignType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextTabAlignType
from _nsgroup import CT_TextTabStop # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextTabStop
from _nsgroup import CT_TextBulletTypefaceFollowText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBulletTypefaceFollowText
from _nsgroup import CT_LineStyleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineStyleList
from _nsgroup import CT_BlurEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BlurEffect
from _nsgroup import CT_GroupShapeProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GroupShapeProperties
from _nsgroup import ST_ShapeID # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_ShapeID
from _nsgroup import CT_SphereCoords # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SphereCoords
from _nsgroup import ST_OnOffStyleType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_OnOffStyleType
from _nsgroup import CT_TableStyleTextStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableStyleTextStyle
from _nsgroup import ST_ChartBuildStep # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_ChartBuildStep
from _nsgroup import CT_AnimationChartElement # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationChartElement
from _nsgroup import CT_TextNoAutofit # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextNoAutofit
from _nsgroup import CT_TextLineBreak # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextLineBreak
from _nsgroup import CT_AlphaModulateFixedEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaModulateFixedEffect
from _nsgroup import CT_SolidColorFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SolidColorFillProperties
from _nsgroup import CT_ColorSchemeList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorSchemeList
from _nsgroup import CT_NonVisualGraphicFrameProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualGraphicFrameProperties
from _nsgroup import CT_Vector3D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Vector3D
from _nsgroup import CT_TablePartStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TablePartStyle
from _nsgroup import ST_PresetLineDashVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetLineDashVal
from _nsgroup import CT_PresetLineDashProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PresetLineDashProperties
from _nsgroup import CT_TableCell # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableCell
from _nsgroup import CT_NonVisualConnectorProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualConnectorProperties
from _nsgroup import ST_TextSpacingPoint # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextSpacingPoint
from _nsgroup import CT_TextSpacingPoint # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextSpacingPoint
from _nsgroup import CT_ColorMappingOverride # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorMappingOverride
from _nsgroup import CT_OfficeArtExtension # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_OfficeArtExtension
from _nsgroup import CT_VideoFile # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_VideoFile
from _nsgroup import CT_AudioCDTime # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AudioCDTime
from _nsgroup import CT_Transform2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Transform2D
from _nsgroup import CT_XYAdjustHandle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_XYAdjustHandle
from _nsgroup import CT_ReflectionEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ReflectionEffect
from _nsgroup import CT_TextSpacing # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextSpacing
from _nsgroup import CT_GroupFillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GroupFillProperties
from _nsgroup import ST_DrawingElementId # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_DrawingElementId
from _nsgroup import CT_NonVisualDrawingProps # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualDrawingProps
from _nsgroup import CT_AnimationGraphicalObjectBuildProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationGraphicalObjectBuildProperties
from _nsgroup import CT_TextBlipBullet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBlipBullet
from _nsgroup import CT_TableCellProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableCellProperties
from _nsgroup import CT_GvmlGroupShape # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlGroupShape
from _nsgroup import CT_FlatText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FlatText
from _nsgroup import CT_SupplementalFont # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_SupplementalFont
from _nsgroup import CT_Hyperlink # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Hyperlink
from _nsgroup import CT_GvmlPictureNonVisual # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlPictureNonVisual
from _nsgroup import CT_CustomGeometry2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_CustomGeometry2D
from _nsgroup import CT_NonVisualPictureProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_NonVisualPictureProperties
from _nsgroup import CT_TextShapeAutofit # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextShapeAutofit
from _nsgroup import CT_AdjustHandleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AdjustHandleList
from _nsgroup import CT_Path2DMoveTo # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DMoveTo
from _nsgroup import CT_RelativeOffsetEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_RelativeOffsetEffect
from _nsgroup import CT_ColorReplaceEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorReplaceEffect
from _nsgroup import CT_AlphaOutsetEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaOutsetEffect
from _nsgroup import CT_RelativeRect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_RelativeRect
from _nsgroup import ST_AdjAngle # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AdjAngle
from _nsgroup import CT_ConnectionSite # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ConnectionSite
from _nsgroup import CT_TextUnderlineFillGroupWrapper # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextUnderlineFillGroupWrapper
from _nsgroup import CT_TextNoBullet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextNoBullet
from _nsgroup import CT_Connection # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Connection
from _nsgroup import CT_TextBulletSizeFollowText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBulletSizeFollowText
from _nsgroup import CT_TextListStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextListStyle
from _nsgroup import CT_AlphaCeilingEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaCeilingEffect
from _nsgroup import CT_TextField # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextField
from _nsgroup import CT_StretchInfoProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_StretchInfoProperties
from _nsgroup import CT_BiLevelEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BiLevelEffect
from _nsgroup import CT_EffectProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectProperties
from _nsgroup import CT_PositiveSize2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PositiveSize2D
from _nsgroup import CT_Point2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Point2D
from _nsgroup import CT_GvmlPicture # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlPicture
from _nsgroup import ST_TextShapeType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextShapeType
from _nsgroup import CT_PresetTextShape # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PresetTextShape
from _nsgroup import CT_GvmlShapeNonVisual # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlShapeNonVisual
from _nsgroup import CT_TintEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TintEffect
from _nsgroup import ST_PresetShadowVal # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetShadowVal
from _nsgroup import CT_PresetShadowEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PresetShadowEffect
from _nsgroup import CT_GvmlGroupShapeNonVisual # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlGroupShapeNonVisual
from _nsgroup import CT_InnerShadowEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_InnerShadowEffect
from _nsgroup import ST_LineEndLength # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LineEndLength
from _nsgroup import ST_LineEndType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LineEndType
from _nsgroup import ST_LineEndWidth # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_LineEndWidth
from _nsgroup import CT_LineEndProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LineEndProperties
from _nsgroup import CT_Path2DList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DList
from _nsgroup import CT_Path2DQuadBezierTo # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DQuadBezierTo
from _nsgroup import CT_TransformEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TransformEffect
from _nsgroup import CT_HSLEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_HSLEffect
from _nsgroup import CT_AlphaModulateEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaModulateEffect
from _nsgroup import ST_AnimationBuildType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AnimationBuildType
from _nsgroup import ST_AnimationChartOnlyBuildType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AnimationChartOnlyBuildType
from _nsgroup import ST_AnimationChartBuildType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AnimationChartBuildType
from _nsgroup import CT_AnimationChartBuildProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationChartBuildProperties
from _nsgroup import CT_FillStyleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FillStyleList
from _nsgroup import CT_LuminanceEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LuminanceEffect
from _nsgroup import CT_QuickTimeFile # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_QuickTimeFile
from _nsgroup import CT_BackgroundFillStyleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BackgroundFillStyleList
from _nsgroup import CT_EmbeddedWAVAudioFile # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EmbeddedWAVAudioFile
from _nsgroup import CT_FontScheme # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FontScheme
from _nsgroup import ST_BevelPresetType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_BevelPresetType
from _nsgroup import CT_Bevel # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Bevel
from _nsgroup import CT_ObjectStyleDefaults # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ObjectStyleDefaults
from _nsgroup import CT_TableRow # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableRow
from _nsgroup import CT_TextBulletColorFollowText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBulletColorFollowText
from _nsgroup import CT_Point3D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Point3D
from _nsgroup import CT_GroupTransform2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GroupTransform2D
from _nsgroup import CT_AudioFile # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AudioFile
from _nsgroup import ST_PathFillMode # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PathFillMode
from _nsgroup import CT_Path2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2D
from _nsgroup import CT_AnimationElementChoice # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationElementChoice
from _nsgroup import CT_Headers # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Headers
from _nsgroup import CT_BaseStylesOverride # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BaseStylesOverride
from _nsgroup import ST_BlipCompression # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_BlipCompression
from _nsgroup import CT_Blip # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Blip
from _nsgroup import ST_GeomGuideFormula # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_GeomGuideFormula
from _nsgroup import CT_GeomGuide # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GeomGuide
from _nsgroup import CT_PresetGeometry2D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PresetGeometry2D
from _nsgroup import ST_TextFontScalePercent # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextFontScalePercent
from _nsgroup import ST_TextFontScalePercentOrPercentString # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextFontScalePercentOrPercentString
from _nsgroup import ST_TextSpacingPercent # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextSpacingPercent
from _nsgroup import ST_TextSpacingPercentOrPercentString # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_TextSpacingPercentOrPercentString
from _nsgroup import CT_TextNormalAutofit # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextNormalAutofit
from _nsgroup import CT_RegularTextRun # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_RegularTextRun
from _nsgroup import ST_DgmBuildStep # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_DgmBuildStep
from _nsgroup import CT_AnimationDgmElement # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationDgmElement
from _nsgroup import CT_FillProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FillProperties
from _nsgroup import CT_TextCharBullet # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextCharBullet
from _nsgroup import CT_Cell3D # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Cell3D
from _nsgroup import CT_TextTabStopList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextTabStopList
from _nsgroup import CT_AlphaBiLevelEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AlphaBiLevelEffect
from _nsgroup import CT_TableBackgroundStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableBackgroundStyle
from _nsgroup import CT_DashStop # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_DashStop
from _nsgroup import ST_BlendMode # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_BlendMode
from _nsgroup import CT_FillOverlayEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_FillOverlayEffect
from _nsgroup import CT_Backdrop # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Backdrop
from _nsgroup import CT_Path2DClose # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DClose
from _nsgroup import ST_AnimationDgmOnlyBuildType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AnimationDgmOnlyBuildType
from _nsgroup import ST_AnimationDgmBuildType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_AnimationDgmBuildType
from _nsgroup import CT_AnimationDgmBuildProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_AnimationDgmBuildProperties
from _nsgroup import CT_GvmlGraphicFrameNonVisual # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlGraphicFrameNonVisual
from _nsgroup import CT_TextUnderlineFillFollowText # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextUnderlineFillFollowText
from _nsgroup import CT_ColorSchemeAndMapping # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorSchemeAndMapping
from _nsgroup import CT_TableCol # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableCol
from _nsgroup import CT_PolarAdjustHandle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PolarAdjustHandle
from _nsgroup import CT_WholeE2oFormatting # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_WholeE2oFormatting
from _nsgroup import CT_GraphicalObjectFrameLocking # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GraphicalObjectFrameLocking
from _nsgroup import CT_GvmlConnector # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlConnector
from _nsgroup import CT_TextParagraph # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextParagraph
from _nsgroup import CT_Path2DArcTo # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Path2DArcTo
from _nsgroup import CT_TableCellBorderStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableCellBorderStyle
from _nsgroup import CT_ConnectionSiteList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ConnectionSiteList
from _nsgroup import CT_LinearShadeProperties # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_LinearShadeProperties
from _nsgroup import CT_GradientStop # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GradientStop
from _nsgroup import CT_GeomRect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GeomRect
from _nsgroup import CT_ColorMRU # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ColorMRU
from _nsgroup import CT_GraphicalObjectData # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GraphicalObjectData
from _nsgroup import CT_TextBulletSizePoint # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextBulletSizePoint
from _nsgroup import CT_TableGrid # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableGrid
from _nsgroup import CT_Ratio # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Ratio
from _nsgroup import CT_GroupLocking # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GroupLocking
from _nsgroup import ST_FOVAngle # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_FOVAngle
from _nsgroup import ST_PresetCameraType # {http://schemas.openxmlformats.org/drawingml/2006/main}ST_PresetCameraType
from _nsgroup import CT_Camera # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Camera
from _nsgroup import CT_BlendEffect # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_BlendEffect
from _nsgroup import CT_EffectStyleList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_EffectStyleList
from _nsgroup import CT_TableStyleCellStyle # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TableStyleCellStyle
from _nsgroup import CT_CustomColorList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_CustomColorList
from _nsgroup import CT_DashStopList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_DashStopList
from _nsgroup import CT_GradientStopList # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GradientStopList
from _nsgroup import CT_CustomColor # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_CustomColor
from _nsgroup import CT_PictureLocking # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_PictureLocking
from _nsgroup import CT_Table # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_Table
from _nsgroup import CT_ConnectorLocking # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_ConnectorLocking
from _nsgroup import CT_GvmlConnectorNonVisual # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_GvmlConnectorNonVisual
from _nsgroup import CT_TextSpacingPercent # {http://schemas.openxmlformats.org/drawingml/2006/main}CT_TextSpacingPercent
