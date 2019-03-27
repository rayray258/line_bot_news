#!/usr/bin/env python
# -*- coding: utf-8 -*-
from liff_api import *
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

    elif sys.argv[1] == 'init' and len(sys.argv) == 3:
        liff_init(sys.argv[2])
    elif sys.argv[1] == 'list':
        liffs = liff_list()
        pp.pprint(liffs)
    elif sys.argv[1] == 'add' and len(sys.argv) == 4:
        liff_added = liff_add(sys.argv[2], sys.argv[3])
        pp.pprint(liff_added)
    elif sys.argv[1] == 'delete' and len(sys.argv) == 3:
        liff_delete(sys.argv[2])
    elif sys.argv[1] == 'update' and len(sys.argv) == 3:
        liff_update(sys.argv[2])