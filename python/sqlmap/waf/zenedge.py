#!/data/data/com.termux/files/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import HTTP_HEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Zenedge Web Application Firewall (Zenedge)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(get=vector)
        retval = code >= 400 and re.search(r"\AZENEDGE", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
        retval |= all(_ in (page or "") for _ in ("Your request has been blocked", "Incident ID", "/__zenedge/assets/"))
        if retval:
            break

    return retval
