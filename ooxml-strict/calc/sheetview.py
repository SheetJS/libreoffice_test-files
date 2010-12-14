# Copyright 2010, Muthu Subramanian, Novell Inc.
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

import re
from opc import ALL_OOXML as ALL_OOXML

# use default list of xml mimetypes in opc
mimetypes = ALL_OOXML

# always iterate once over a matched element
iterations = lambda i: 1

# always use the same regexp regardless of mimetype
worklist = [ 
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*colorId.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*defaultGridColor.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*rightToLeft.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*showFormulas.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*showGridLines.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*showOutlineSymbols.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*showRowColHeaders.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*showZeros.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*tabSelected.*')],
#    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*topLeftCell.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*view.*')],
    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*windowProtection.*')],
#    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*workbookViewId.*')],
#    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*zoomScale.*')],
#    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*zoomScaleNormal.*')],
#    lambda i: [re.compile('.*CT_SheetView'), re.compile('.*zoomScalePageLayoutView.*')],
              ]
