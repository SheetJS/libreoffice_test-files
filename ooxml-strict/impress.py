# Copyright 2010, Thorsten Behrens, Radek Doulik, Novell Inc.
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
import dml.dml, pml.pml, pml._msocompat, props.props, sml.sml, wml.wml

if len(sys.argv) < 3:
    print "Usage: impress.py <tests.py> <output_dir>"
    sys.exit(1)
else:
    exec "import "+sys.argv[1]+" as worklist"

    inFile = None;
    mimetypes = None;

    outDir = sys.argv[2]

    if len(sys.argv) > 3:
        fileMatch = re.compile('.*' + sys.argv[3] + '.*')
    else:
        fileMatch = re.compile('.*')

    for test in worklist.tests:
        if 'mimetypes' in test:
            mimetypes = test['mimetypes']

        if mimetypes == None:
            print "no mimetypes specified"
            sys.exit(1)

        if 'input' in test:
            inFile = test['input']
            iteration=1

        if inFile == None:
            print "no input file specified"
            sys.exit(1)

        if fileMatch.match(inFile) is None:
            continue

        atOnce = False;
        if 'atOnce' in test:
            atOnce = True;

        inFile = "impress/" + inFile
        (inFileName,inFileExt) = os.path.splitext(os.path.basename(inFile))
        package = opc.OPCPackage(inFile)

        for (fragment, mimetype, schema, reltype) in package.files(mimetypes):

            saxer = pyxb.binding.saxer.make_parser(location_base=fragment)
            handler = saxer.getContentHandler()
            saxer.parse(StringIO.StringIO(package.read(fragment)))
            sax_instance = handler.rootObject()

            if not atOnce:
                for contentIter in sax_instance.iterateBinding(test['patterns']):
                    # iterate content n times
                    for i in range(test['iterations']):
                        contentIter()
                        currOutFile = outDir+"/"+inFileName+str(iteration)+inFileExt
                        package.copyWithReplace(currOutFile,{fragment: sax_instance.toxml().encode('utf-8')})
                        iteration += 1
            else:
                for i in range(test['iterations']):
                    for contentIter in sax_instance.iterateBinding(test['patterns']):
                        contentIter()
                    currOutFile = outDir+"/"+inFileName+str(iteration)+inFileExt
                    package.copyWithReplace(currOutFile,{fragment: sax_instance.toxml().encode('utf-8')})
                    iteration += 1
