#!usr/bin/env python
# -*- coding: utf-8 -*-
"""パッケージ内の他のモジュールで使用するオブジェクト群
"""
from collections import namedtuple
import re

html_information = namedtuple('html_information', ["body", "urls"])
wiki_pattern = re.compile("^(/wiki/)((?!:).)*$")
