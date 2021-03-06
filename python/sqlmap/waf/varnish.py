#!/data/data/com.termux/files/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Varnish FireWall (OWASP)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, headers, code = get_page(get=vector)
        retval = code == 404 and re.search(r"\bXID: \d+", page or "") is not None
        retval |= code >= 400 and "Request rejected by xVarnish-WAF" in (page or "")
        if retval:
            break

    return retval
