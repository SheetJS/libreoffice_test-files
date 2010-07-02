import re

# use default list of xml mimetypes in opc
mimetypes = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"]

# always iterate twice over a matched element
iterations = lambda i: 1

# always use the same regexp regardless of mimetype
worklist = lambda i: [re.compile('.*CT_CalcPr'), re.compile('.*refMode.*')]
