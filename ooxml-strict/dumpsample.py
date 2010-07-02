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

import sys, os, StringIO

import pyxb.binding.saxer

import opc
import dml.dml, pml.pml, pml._msocompat, props.props, sml.sml, wml.wml

if len(sys.argv) < 3:
    print "Usage: dumpsample.py <worklist.py> <input_file> <output_dir>"
    sys.exit(1)
else:    
    exec "import "+sys.argv[1]+" as worklist"
    inFile = sys.argv[2]
    (inFileName,inFileExt) = os.path.splitext(os.path.basename(inFile))
    outDir = sys.argv[3]
    
    package = opc.OPCPackage(inFile)
    iteration=1
    
    for (fragment, mimetype, schema, reltype) in package.files(worklist.mimetypes):
        saxer = pyxb.binding.saxer.make_parser(location_base=fragment)
        handler = saxer.getContentHandler()
        saxer.parse(StringIO.StringIO(package.read(fragment)))
        sax_instance = handler.rootObject()

        for contentIter in sax_instance.iterateBinding(worklist.worklist(mimetype)):
            # iterate content n times
            for i in range(worklist.iterations(mimetype)):
                contentIter()
                currOutFile = outDir+"/"+inFileName+str(iteration)+inFileExt
                package.copyWithReplace(currOutFile,{fragment: sax_instance.toxml().encode('utf-8')})
                iteration += 1
                print "Written "+currOutFile
