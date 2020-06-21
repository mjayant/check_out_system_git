#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Loading src folder
"""

import sys
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(os.path.dirname(cur_dir), 'src')

if src not in sys.path:
    sys.path.append(src)
