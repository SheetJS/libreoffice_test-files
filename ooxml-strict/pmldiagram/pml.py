# ./pml.py
# PyXB bindings for NamespaceModule
# NSM:bfb0a44add30508ee7aaa5c69b773abf89be5d2d
# Generated 2010-07-02 14:32:20.413893 by PyXB version 1.1.2
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
import _nsgroup

Namespace = pyxb.namespace.NamespaceForURI(u'http://schemas.openxmlformats.org/presentationml/2006/main', create_if_missing=True)
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

from _nsgroup import sldMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}sldMaster
from _nsgroup import notes # {http://schemas.openxmlformats.org/presentationml/2006/main}notes
from _nsgroup import cmAuthorLst # {http://schemas.openxmlformats.org/presentationml/2006/main}cmAuthorLst
from _nsgroup import viewPr # {http://schemas.openxmlformats.org/presentationml/2006/main}viewPr
from _nsgroup import presentation # {http://schemas.openxmlformats.org/presentationml/2006/main}presentation
from _nsgroup import oleObj # {http://schemas.openxmlformats.org/presentationml/2006/main}oleObj
from _nsgroup import notesMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}notesMaster
from _nsgroup import tagLst # {http://schemas.openxmlformats.org/presentationml/2006/main}tagLst
from _nsgroup import sldLayout # {http://schemas.openxmlformats.org/presentationml/2006/main}sldLayout
from _nsgroup import sld # {http://schemas.openxmlformats.org/presentationml/2006/main}sld
from _nsgroup import cmLst # {http://schemas.openxmlformats.org/presentationml/2006/main}cmLst
from _nsgroup import handoutMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}handoutMaster
from _nsgroup import presentationPr # {http://schemas.openxmlformats.org/presentationml/2006/main}presentationPr
from _nsgroup import sldSyncPr # {http://schemas.openxmlformats.org/presentationml/2006/main}sldSyncPr
from _nsgroup import CT_TLTimeConditionList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeConditionList
from _nsgroup import CT_SlideMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideMaster
from _nsgroup import CT_HandoutMasterIdList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_HandoutMasterIdList
from _nsgroup import CT_ExtensionList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ExtensionList
from _nsgroup import CT_CustomerDataList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CustomerDataList
from _nsgroup import CT_EmbeddedFontDataId # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_EmbeddedFontDataId
from _nsgroup import CT_TLPoint # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLPoint
from _nsgroup import CT_HandoutMasterIdListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_HandoutMasterIdListEntry
from _nsgroup import CT_Background # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Background
from _nsgroup import CT_CommonSlideData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommonSlideData
from _nsgroup import CT_GraphicalObjectFrameNonVisual # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_GraphicalObjectFrameNonVisual
from _nsgroup import CT_TLAnimVariant # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimVariant
from _nsgroup import CT_TLSetBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLSetBehavior
from _nsgroup import CT_TransitionSoundAction # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TransitionSoundAction
from _nsgroup import CT_TLAnimVariantStringVal # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimVariantStringVal
from _nsgroup import CT_ModifyVerifier # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ModifyVerifier
from _nsgroup import CT_ShowInfoKiosk # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ShowInfoKiosk
from _nsgroup import CT_SlideMasterTextStyles # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideMasterTextStyles
from _nsgroup import ST_Index # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_Index
from _nsgroup import CT_IndexRange # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_IndexRange
from _nsgroup import CT_TLShapeTargetElement # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLShapeTargetElement
from _nsgroup import CT_TLGraphicalObjectBuild # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLGraphicalObjectBuild
from _nsgroup import CT_Control # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Control
from _nsgroup import CT_TLAnimVariantFloatVal # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimVariantFloatVal
from _nsgroup import ST_SplitterBarState # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SplitterBarState
from _nsgroup import CT_NormalViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NormalViewProperties
from _nsgroup import CT_TimeNodeList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TimeNodeList
from _nsgroup import CT_Picture # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Picture
from _nsgroup import ST_TLAnimateBehaviorCalcMode # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateBehaviorCalcMode
from _nsgroup import ST_TLAnimateBehaviorValueType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateBehaviorValueType
from _nsgroup import CT_TLAnimateBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateBehavior
from _nsgroup import ST_TLTriggerRuntimeNode # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTriggerRuntimeNode
from _nsgroup import CT_TLTriggerRuntimeNode # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTriggerRuntimeNode
from _nsgroup import CT_ExtensionListModify # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ExtensionListModify
from _nsgroup import CT_Empty # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Empty
from _nsgroup import CT_SlideRelationshipListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideRelationshipListEntry
from _nsgroup import CT_OutlineViewSlideList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OutlineViewSlideList
from _nsgroup import ST_TransitionInOutDirectionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TransitionInOutDirectionType
from _nsgroup import CT_InOutTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_InOutTransition
from _nsgroup import CT_Extension # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Extension
from _nsgroup import CT_ControlList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ControlList
from _nsgroup import CT_NotesSlide # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesSlide
from _nsgroup import ST_TLTimeIndefinite # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeIndefinite
from _nsgroup import ST_TLTime # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTime
from _nsgroup import CT_TLIterateIntervalTime # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLIterateIntervalTime
from _nsgroup import CT_HtmlPublishProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_HtmlPublishProperties
from _nsgroup import CT_NormalViewPortion # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NormalViewPortion
from _nsgroup import CT_ApplicationNonVisualDrawingProps # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ApplicationNonVisualDrawingProps
from _nsgroup import CT_TLByRgbColorTransform # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLByRgbColorTransform
from _nsgroup import CT_CommentAuthorList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommentAuthorList
from _nsgroup import CT_ShowInfoBrowse # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ShowInfoBrowse
from _nsgroup import CT_SlideTiming # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideTiming
from _nsgroup import CT_NotesTextViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesTextViewProperties
from _nsgroup import CT_NotesMasterIdListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesMasterIdListEntry
from _nsgroup import CT_StringTag # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_StringTag
from _nsgroup import ST_TLAnimateMotionBehaviorOrigin # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateMotionBehaviorOrigin
from _nsgroup import ST_TLAnimateMotionPathEditMode # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateMotionPathEditMode
from _nsgroup import CT_TLAnimateMotionBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateMotionBehavior
from _nsgroup import ST_Direction_ as ST_Direction # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_Direction
from _nsgroup import CT_Guide # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Guide
from _nsgroup import CT_OleObjectLink # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OleObjectLink
from _nsgroup import ST_TLTriggerEvent # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTriggerEvent
from _nsgroup import CT_TLTimeCondition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeCondition
from _nsgroup import CT_TLCommonMediaNodeData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLCommonMediaNodeData
from _nsgroup import ST_PrintColorMode # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PrintColorMode
from _nsgroup import ST_PrintWhat # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PrintWhat
from _nsgroup import CT_PrintProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_PrintProperties
from _nsgroup import ST_TransitionSideDirectionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TransitionSideDirectionType
from _nsgroup import ST_TransitionCornerDirectionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TransitionCornerDirectionType
from _nsgroup import ST_TransitionEightDirectionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TransitionEightDirectionType
from _nsgroup import CT_EightDirectionTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_EightDirectionTransition
from _nsgroup import ST_ViewType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_ViewType
from _nsgroup import CT_ViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ViewProperties
from _nsgroup import CT_Shape_ as CT_Shape # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Shape
from _nsgroup import CT_Comment # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Comment
from _nsgroup import ST_Name # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_Name
from _nsgroup import CT_CustomShow # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CustomShow
from _nsgroup import ST_TLTimeNodeMasterRelation # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeMasterRelation
from _nsgroup import ST_TLTimeNodeType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeType
from _nsgroup import ST_TLTimeNodeID # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeID
from _nsgroup import ST_TLTimeNodePresetClassType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodePresetClassType
from _nsgroup import ST_TLTimeNodeSyncType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeSyncType
from _nsgroup import ST_TLTimeNodeRestartType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeRestartType
from _nsgroup import ST_TLTimeNodeFillType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeNodeFillType
from _nsgroup import CT_TLCommonTimeNodeData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLCommonTimeNodeData
from _nsgroup import CT_GroupShape # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_GroupShape
from _nsgroup import CT_NotesMasterIdList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesMasterIdList
from _nsgroup import ST_TLCommandType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLCommandType
from _nsgroup import CT_TLCommandBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLCommandBehavior
from _nsgroup import CT_HeaderFooter # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_HeaderFooter
from _nsgroup import CT_TLTriggerTimeNodeID # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTriggerTimeNodeID
from _nsgroup import CT_TLAnimVariantIntegerVal # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimVariantIntegerVal
from _nsgroup import CT_OptionalBlackTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OptionalBlackTransition
from _nsgroup import CT_TLTimeTargetElement # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeTargetElement
from _nsgroup import CT_ShowProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ShowProperties
from _nsgroup import CT_SplitTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SplitTransition
from _nsgroup import CT_OrientationTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OrientationTransition
from _nsgroup import CT_ShapeNonVisual # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ShapeNonVisual
from _nsgroup import ST_TLOleChartBuildType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLOleChartBuildType
from _nsgroup import CT_TLOleBuildChart # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLOleBuildChart
from _nsgroup import ST_SlideMasterId # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideMasterId
from _nsgroup import CT_SlideMasterIdListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideMasterIdListEntry
from _nsgroup import ST_OleObjectFollowColorScheme # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_OleObjectFollowColorScheme
from _nsgroup import CT_OleObjectEmbed # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OleObjectEmbed
from _nsgroup import CT_Connector # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Connector
from _nsgroup import ST_SlideSizeCoordinate # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideSizeCoordinate
from _nsgroup import ST_SlideSizeType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideSizeType
from _nsgroup import CT_SlideSize # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideSize
from _nsgroup import ST_SlideId # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideId
from _nsgroup import CT_SlideIdListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideIdListEntry
from _nsgroup import CT_TLTimeNodeExclusive # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeNodeExclusive
from _nsgroup import CT_GroupShapeNonVisual # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_GroupShapeNonVisual
from _nsgroup import CT_TransitionStartSoundAction # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TransitionStartSoundAction
from _nsgroup import CT_CommonViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommonViewProperties
from _nsgroup import ST_SlideLayoutId # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideLayoutId
from _nsgroup import CT_SlideLayoutIdListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideLayoutIdListEntry
from _nsgroup import ST_BookmarkIdSeed # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_BookmarkIdSeed
from _nsgroup import CT_Presentation # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Presentation
from _nsgroup import CT_SideDirectionTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SideDirectionTransition
from _nsgroup import CT_CustomShowId # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CustomShowId
from _nsgroup import ST_TLTimeAnimateValueTime # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLTimeAnimateValueTime
from _nsgroup import CT_TLTimeAnimateValue # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeAnimateValue
from _nsgroup import CT_TLMediaNodeVideo # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLMediaNodeVideo
from _nsgroup import CT_GuideList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_GuideList
from _nsgroup import ST_WebScreenSize # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_WebScreenSize
from _nsgroup import ST_WebColorType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_WebColorType
from _nsgroup import ST_WebEncoding # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_WebEncoding
from _nsgroup import CT_WebProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_WebProperties
from _nsgroup import CT_TLBehaviorAttributeNameList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLBehaviorAttributeNameList
from _nsgroup import ST_PhotoAlbumLayout # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PhotoAlbumLayout
from _nsgroup import ST_PhotoAlbumFrameShape # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PhotoAlbumFrameShape
from _nsgroup import CT_PhotoAlbum # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_PhotoAlbum
from _nsgroup import CT_WheelTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_WheelTransition
from _nsgroup import CT_OleObject # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OleObject
from _nsgroup import CT_CommonSlideViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommonSlideViewProperties
from _nsgroup import CT_TLTimeNodeParallel # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeNodeParallel
from _nsgroup import ST_TLAnimateEffectTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateEffectTransition
from _nsgroup import CT_TLAnimateEffectBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateEffectBehavior
from _nsgroup import CT_TLTemplate # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTemplate
from _nsgroup import CT_CustomShowList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CustomShowList
from _nsgroup import CT_EmbeddedFontListEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_EmbeddedFontListEntry
from _nsgroup import CT_TLTextTargetElement # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTextTargetElement
from _nsgroup import CT_NotesMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesMaster
from _nsgroup import CT_TagList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TagList
from _nsgroup import ST_IterateType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_IterateType
from _nsgroup import CT_TLIterateData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLIterateData
from _nsgroup import ST_SlideLayoutType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_SlideLayoutType
from _nsgroup import CT_SlideLayout # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideLayout
from _nsgroup import CT_Slide # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Slide
from _nsgroup import CT_NotesViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_NotesViewProperties
from _nsgroup import CT_TLByHslColorTransform # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLByHslColorTransform
from _nsgroup import CT_TLTemplateList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTemplateList
from _nsgroup import ST_TLBehaviorAccumulateType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLBehaviorAccumulateType
from _nsgroup import ST_TLBehaviorTransformType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLBehaviorTransformType
from _nsgroup import ST_TLBehaviorOverrideType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLBehaviorOverrideType
from _nsgroup import ST_TLBehaviorAdditiveType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLBehaviorAdditiveType
from _nsgroup import CT_TLCommonBehaviorData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLCommonBehaviorData
from _nsgroup import CT_ConnectorNonVisual # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_ConnectorNonVisual
from _nsgroup import CT_TLAnimateScaleBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateScaleBehavior
from _nsgroup import CT_TLAnimVariantBooleanVal # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimVariantBooleanVal
from _nsgroup import CT_Kinsoku # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Kinsoku
from _nsgroup import CT_OutlineViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OutlineViewProperties
from _nsgroup import ST_PlaceholderSize # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PlaceholderSize
from _nsgroup import ST_PlaceholderType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_PlaceholderType
from _nsgroup import CT_Placeholder # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Placeholder
from _nsgroup import ST_TLDiagramBuildType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLDiagramBuildType
from _nsgroup import CT_TLBuildDiagram # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLBuildDiagram
from _nsgroup import ST_TransitionSpeed # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TransitionSpeed
from _nsgroup import CT_SlideTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideTransition
from _nsgroup import CT_OutlineViewSlideEntry # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_OutlineViewSlideEntry
from _nsgroup import CT_GraphicalObjectFrame # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_GraphicalObjectFrame
from _nsgroup import CT_SlideIdList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideIdList
from _nsgroup import CT_CustomerData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CustomerData
from _nsgroup import ST_TLNextActionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLNextActionType
from _nsgroup import ST_TLPreviousActionType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLPreviousActionType
from _nsgroup import CT_TLTimeNodeSequence # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeNodeSequence
from _nsgroup import CT_SlideLayoutIdList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideLayoutIdList
from _nsgroup import CT_BackgroundProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_BackgroundProperties
from _nsgroup import CT_SlideRelationshipList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideRelationshipList
from _nsgroup import CT_TLByAnimateColorTransform # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLByAnimateColorTransform
from _nsgroup import CT_TLMediaNodeAudio # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLMediaNodeAudio
from _nsgroup import CT_CommentList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommentList
from _nsgroup import CT_TagsData # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TagsData
from _nsgroup import CT_HandoutMaster # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_HandoutMaster
from _nsgroup import CT_TLAnimateRotationBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateRotationBehavior
from _nsgroup import CT_TLTimeAnimateValueList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLTimeAnimateValueList
from _nsgroup import CT_TLSubShapeId # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLSubShapeId
from _nsgroup import CT_SlideViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideViewProperties
from _nsgroup import CT_Rel # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_Rel
from _nsgroup import CT_SmartTags # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SmartTags
from _nsgroup import ST_TLAnimateColorSpace # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateColorSpace
from _nsgroup import ST_TLAnimateColorDirection # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLAnimateColorDirection
from _nsgroup import CT_TLAnimateColorBehavior # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLAnimateColorBehavior
from _nsgroup import ST_TLChartSubelementType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLChartSubelementType
from _nsgroup import CT_TLOleChartTargetElement # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLOleChartTargetElement
from _nsgroup import CT_TLIterateIntervalPercentage # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLIterateIntervalPercentage
from _nsgroup import CT_CornerDirectionTransition # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CornerDirectionTransition
from _nsgroup import CT_SlideMasterIdList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideMasterIdList
from _nsgroup import CT_PictureNonVisual # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_PictureNonVisual
from _nsgroup import CT_EmbeddedFontList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_EmbeddedFontList
from _nsgroup import CT_CommentAuthor # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_CommentAuthor
from _nsgroup import CT_SlideSorterViewProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideSorterViewProperties
from _nsgroup import CT_BuildList # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_BuildList
from _nsgroup import CT_PresentationProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_PresentationProperties
from _nsgroup import CT_SlideSyncProperties # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_SlideSyncProperties
from _nsgroup import ST_TLParaBuildType # {http://schemas.openxmlformats.org/presentationml/2006/main}ST_TLParaBuildType
from _nsgroup import CT_TLBuildParagraph # {http://schemas.openxmlformats.org/presentationml/2006/main}CT_TLBuildParagraph
