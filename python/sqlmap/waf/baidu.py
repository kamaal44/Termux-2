#!/data/data/com.termux/files/usr/bin/env python

"""
Copyright (c) 2006-2018 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re

from lib.core.enums import HTTP_HEADER
from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "Yunjiasu Web Application Firewall (Baidu)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        _, headers, _ = get_page(get=vector)
        retval = re.search(r"fhl", headers.get("X-Server", ""), re.I) is not None
        retval |= re.search(r"yunjiasu-nginx", headers.get(HTTP_HEADER.SERVER, ""), re.I) is not None
        if retval:
            break

    return retval
