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

import re
from opc import ALL_OOXML as ALL_OOXML

testcases = {
    'template'  : 'writer/templates/parapr.docx',
    'mimetypes' : ["application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
                   "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"],
    'tasks'     : [
        {
            'name'       : 'OnOff',
            'iterations' : lambda i: 6,
            'worklist'   : lambda i: [re.compile('.*CT_OnOff'), re.compile('.*val.*')]
        },
        {
            'name'       : 'Ind',
            'iterations' : lambda i: 2,
            'worklist'   : lambda i: [re.compile('.*CT_Ind'), re.compile('.*(end|firstLine|hanging|start).*')]
        },
        {
            'name'       : 'Jc',
            'iterations' : lambda i: 10,
            'worklist'   : lambda i: [re.compile('.*CT_Jc'), re.compile('.*val.*')]
        },
        {
            'name'       : 'Spacing',
            'iterations' : lambda i: 2,
            'worklist'   : lambda i: [re.compile('.*CT_Spacing'), re.compile('.*(after|before|line)(Lines)?')]
        },
        {
            'name'       : 'Spacing_lineRule',
            'iterations' : lambda i: 3,
            'worklist'   : lambda i: [re.compile('.*CT_Spacing'), re.compile('.*(lineRule).*')]
        },
        {
            'name'       : 'Spacing_autospacing',
            'iterations' : lambda i: 2,
            'worklist'   : lambda i: [re.compile('.*CT_Spacing'), re.compile('.*(after|before)Autospacing')]
        },
        {
            'name'       : 'Shd_colors',
            'iterations' : lambda i: 2,
            'worklist'   : lambda i: [re.compile('.*CT_Shd'), re.compile('.*(color|fill)')]
        },
        {
            'name'       : 'Tab_leader',
            'iterations' : lambda i: 6,
            'worklist'   : lambda i: [re.compile('.*CT_Tab'), re.compile('.*leader')]
        },
        {
            'name'       : 'Tab_pos',
            'iterations' : lambda i: 2,
            'worklist'   : lambda i: [re.compile('.*CT_Tab'), re.compile('.*pos')]
        },
        {
            'name'       : 'Tab_val',
            'iterations' : lambda i: 7,
            'worklist'   : lambda i: [re.compile('.*CT_Tab'), re.compile('.*val')]
        },
        {
            'name'       : 'TextAlignment',
            'iterations' : lambda i: 5,
            'worklist'   : lambda i: [re.compile('.*CT_TextAlignment'), re.compile('.*val')]
        }
    ]
}
