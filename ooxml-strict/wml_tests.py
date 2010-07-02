# Copyright 2010, Cedric Bosdonnat, Novell Inc.
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
import re

import opc
import dml.dml, pml.pml, props.props, sml.sml, wml.wml

if len(sys.argv) < 3:
    print "Usage: wml_tests.py <worklist.py> <output_dir>"
    sys.exit(1)
else:    
    exec "import "+sys.argv[1]+" as testcases"
    
    inFile = testcases.testcases['template']
    (inFileName,inFileExt) = os.path.splitext(os.path.basename(inFile))
    
    package = opc.OPCPackage(inFile)
    
    outDir = sys.argv[2]
    
    for case in testcases.testcases['tasks']:
        
        print "\n--- Creating tests '"+case['name']+"'\n"
        
        iteration=1
        for (fragment, mimetype, schema, reltype) in package.files(testcases.testcases['mimetypes']):
            saxer = pyxb.binding.saxer.make_parser(location_base=fragment)
            handler = saxer.getContentHandler()
            print "Parsing fragment %s\n" % fragment
            saxer.parse(StringIO.StringIO(package.read(fragment)))
            sax_instance = handler.rootObject()
        
            for contentIter in sax_instance.iterateBinding(case['worklist'](mimetype)):
                # iterate content n times
                for i in range(case['iterations'](mimetype)):
                    contentIter()
                    currOutFile = outDir+"/"+inFileName+"-"+case['name']+str(iteration)+inFileExt
                    package.copyWithReplace(currOutFile,{fragment: sax_instance.toxml().encode('utf-8')})
                    iteration += 1
                    print "Written "+currOutFile
