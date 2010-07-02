# Copyright 2010, Thorsten Behrens, Novell Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain a
# copy of the License at:
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import sys
import os
import zipfile
import xml.sax
import xml.etree.ElementTree as ElemTree

# 3-tuples of media type, root schema uri, and relationship type uri
# (contains all xml-ish file types of ooxml)
xml_type_map = [
             ("application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml",
			  "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
			  "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/endnotes"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/fontTable"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footnotes"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/glossaryDocument"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"),

             ("application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
              "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/webSettings"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/calcChain"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/chartsheet"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/connections"),

             ("application/xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/xmlMaps"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/dialogsheet"),

             ("application/vnd.openxmlformats-officedocument.drawing+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/drawing"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/externalLink"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/sheetMetadata"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotTable"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/pivotCacheDefinition"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/queryTable"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/revisionHeaders"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/revisionLog"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/usernames"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableSingleCells"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/mains",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/table"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/volatileDependencies"),
              
             ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"),

             ("application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
              "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet"),

             ("application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/commentAuthors"),

             ("application/vnd.openxmlformats-officedocument.presentationml.comments+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"),

             ("application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/handoutMaster"),

             ("application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster"),

             ("application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide"),

             ("application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument"),

             ("application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps"),

             ("application/vnd.openxmlformats-officedocument.presentationml.slide+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide"),

             ("application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout"),

             ("application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster"),

             ("application/vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideUpdateInfo"),

             ("application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
              "http://schemas.openxmlformats.org/presentationml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps"),

             ("application/vnd.openxmlformats-officedocument.drawingml.chart+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/chart",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/chart"),

             ("application/vnd.openxmlformats-officedocument.drawingml.chartshapes+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/chart",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/chartUserShapes"),

             ("application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/diagram",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramColors"),

             ("application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/diagram",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramData"),

             ("application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/diagram",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramLayout"),

             ("application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/diagram",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/diagramQuickStyle"),

             ("application/vnd.openxmlformats-officedocument.theme+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme"),

             ("application/vnd.openxmlformats-officedocument.themeOverride+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/themeOverride"),

             ("application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
              "http://schemas.openxmlformats.org/drawingml/2006/main",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles"),

             ("application/xml",
              "http://schemas.openxmlformats.org/officeDocument/2006/additionalCharacteristics",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml"),

             ("application/xml",
              "http://schemas.openxmlformats.org/officeDocument/2006/bibliography",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXml"),

             ("application/vnd.openxmlformats-officedocument.customXmlProperties+xml",
              "http://schemas.openxmlformats.org/officeDocument/2006/customXmlDataProps",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/customXmlProps"),

             ("application/vnd.openxmlformats-package.digital-signature-xmlsignature+xml",
              "http://schemas.openxmlformats.org/package/2006/digital-signature",
              "http://schemas.openxmlformats.org/package/2006/relationships/digital-signature/signature"),

             ("application/vnd.openxmlformats-officedocument.custom-properties+xml",
              "http://schemas.openxmlformats.org/officeDocument/2006/custom-properties",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/custom-properties"),

             ("application/vnd.openxmlformats-officedocument.extended-properties+xml",
              "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties",
              "http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties")
]

def createContentTypeMap (xml):
    defaultMap={}
    overrideMap={}
    tree = ElemTree.XML(xml)
    ns=lambda s: "{http://schemas.openxmlformats.org/package/2006/content-types}"+s
    for elem in tree.findall(ns("Default")):
        defaultMap[elem.get("Extension")] = elem.get("ContentType")
    for elem in tree.findall(ns("Override")):
        overrideMap[elem.get("PartName")] = elem.get("ContentType")
    return (defaultMap, overrideMap)

ALL = 'all'
ALL_XML = 'xml'
ALL_OOXML = 'ooxml'    

class OPCPackage (zipfile.ZipFile):
    """Specialization of ZipFile for operating on OPC packages.

    Class provides high-level functionality like <<give me all xml files of a
    certain mimetype>>, and makes sure the OPC packaging constraints are
    maintained.

    Also, as long as http://bugs.python.org/issue2824 is open, the
    copyWithReplace() function comes in handy, cloning the zip file into a new
    place, and replacing a set of contained files with new content.
    """
    def __init__ (self, file, mode="r"):
        zipfile.ZipFile.__init__(self, file, mode)
        self.defaultMap, self.overrideMap = createContentTypeMap(
            self.read("[Content_Types].xml"))
        
    def _findContentType (self, path):
        """Lookup path in content type map, return mediatype"""
        extension = os.path.splitext(path)[1]
        if path in self.overrideMap:
            return self.overrideMap[path]
        elif extension in self.defaultMap:
            return self.defaultMap[extension]

    __def_schema="http://dummyschema/"
    __def_relation="http://dummyrelation/"
        
    def files (self, mimetypes=ALL):
        """Iterator subsequently returning all files from the package,
        that match the given list of mimetypes.

        Special values for mimetypes (besides a list of mimetype
        strings) are ALL, ALL_XML and ALL_OOXML (the latter only
        containing xml files as specified in IS29500).
        """

        if mimetypes == ALL_OOXML:
            mimetypes = xml_type_map
        elif mimetypes != ALL and mimetypes != ALL_XML:
            mimetypes = [(i,OPCPackage.__def_schema,OPCPackage.__def_relation) for i in mimetypes]

        # scan all contained files, yield those matching one of
        # xml_type_map's xml media types
        for fragment in self.namelist():
            mimetype = self._findContentType("/"+fragment)
            if not mimetype is None:
                if mimetypes == ALL:
                    yield (fragment, mimetype, __def_schema, __def_relation)
                elif mimetypes == ALL_XML:
                    if mimetype.endswith("+xml"):
                        yield (fragment, mimetype, __def_schema, __def_relation)
                else:        
                    for elem in mimetypes:
                        if elem[0] == mimetype:
                            yield (fragment, mimetype, elem[1], elem[2])

    def copyWithReplace (self, newPath, newContent):
        """Clone existing zip archive to newPath location, replace
        all files from list of pairs newContent with content given
        there.

        Example:
        OPCPackage.copyWithReplace(\"/tmp/blah\",{\"a/sub/dir/content.txt\": \"I am the new content\"})
        """
        target=zipfile.ZipFile(newPath,mode="w")
        for fragment in self.namelist():
            if fragment in newContent:
                target.writestr(fragment,newContent[fragment])
            else:
                target.writestr(fragment,self.read(fragment))
        target.close()
