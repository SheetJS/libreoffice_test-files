# Copyright 2010, Radek Doulik, Novell Inc.
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

tests = [
    {
        "mimetypes"  : [ "application/vnd.openxmlformats-officedocument.presentationml.slide+xml" ],
        "input"      : "textbox_color.pptx",
        "iterations" : 2,
        "patterns"   : [re.compile(".*CT_SchemeColor.*"), re.compile(".*lumMod.*"), re.compile(".*val.*")]
    }
]
