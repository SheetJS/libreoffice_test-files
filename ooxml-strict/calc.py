# Copyright 2010, Thorsten Behrens, Novell Inc.
# Modified by Muthu Subramanian
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

import sys, os, StringIO

import pyxb.binding.saxer

import opc
import dml.dml, pml.pml, props.props, sml.sml, wml.wml

def outputxml (package, xml, outDir, iteration, inFileName, inFileExt):
    currOutFile = outDir+"/"+inFileName+str(iteration)+inFileExt
    package.copyWithReplace(currOutFile, xml)

if len(sys.argv) < 4:
    print "Usage: calc.py <worklist.py> <input_file> <output_dir>"
    sys.exit(1)
else:
    exec "import "+sys.argv[1]+" as worklist"
    inFile = sys.argv[2]
    (inFileName,inFileExt) = os.path.splitext(os.path.basename(inFile))
    outDir = sys.argv[3]

    package = opc.OPCPackage(inFile)
    iteration=1

    for index in range (0, len(worklist.worklist)):
        for (fragment, mimetype, schema, reltype) in package.files(worklist.mimetypes):
            if fragment != "xl/worksheets/sheet1.xml" and \
               fragment != "xl/workbook.xml" and \
               fragment != "xl/comments1.xml":
                continue
            saxer = pyxb.binding.saxer.make_parser(location_base=fragment)
            handler = saxer.getContentHandler()
            saxer.parse(StringIO.StringIO(package.read(fragment)))
            sax_instance = handler.rootObject()

            for contentIter in sax_instance.iterateBinding(worklist.worklist[index](mimetype)):
                # iterate content n times
                for i in range(worklist.iterations(mimetype)):
                    contentIter()
                    if index == len(worklist.worklist)-1:
                        outputxml(package, {fragment: sax_instance.toxml().encode('utf-8')}, outDir, iteration, inFileName, inFileExt)
                        iteration += 1
                    else:
                        saxer2 = pyxb.binding.saxer.make_parser(location_base=fragment)
                        handler2 = saxer2.getContentHandler()
                        saxer2.parse(StringIO.StringIO(sax_instance.toxml().encode('utf-8')))
                        for j in range(index+1, len(worklist.worklist)):
                            sax_instance2 = handler2.rootObject()
                            for contentIter2 in sax_instance2.iterateBinding(worklist.worklist[j](mimetype)):
                                for i2 in range(worklist.iterations(mimetype)):
                                    contentIter2()
                                    outputxml(package, {fragment: sax_instance2.toxml().encode('utf-8')}, outDir, iteration, inFileName, inFileExt)
                                    iteration += 1
                            saxer2.parse(StringIO.StringIO(sax_instance2.toxml().encode('utf-8')))
