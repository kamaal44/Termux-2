#!/data/data/com.termux/files/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

from lib.core.datatype import AttribDict

_defaults = {
    "csvDel": ',',
    "timeSec": 5,
    "googlePage": 1,
    "verbose": 1,
    "delay": 0,
    "timeout": 30,
    "retries": 3,
    "saFreq": 0,
    "threads": 1,
    "level": 1,
    "risk": 1,
    "dumpFormat": "CSV",
    "tablePrefix": "sqlmap",
    "technique": "BEUSTQ",
    "torType": "SOCKS5",
}

defaults = AttribDict(_defaults)
