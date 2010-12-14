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
    lambda i: [re.compile('.*CT_PrintOptions'), re.compile('.*gridLines.*')],
    lambda i: [re.compile('.*CT_PrintOptions'), re.compile('.*gridLinesSet.*')],
    lambda i: [re.compile('.*CT_PrintOptions'), re.compile('.*headings.*')],
    lambda i: [re.compile('.*CT_PrintOptions'), re.compile('.*horizontalCentered.*')],
    lambda i: [re.compile('.*CT_PrintOptions'), re.compile('.*verticalCentered.*')],
              ]
