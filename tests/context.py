# -*- coding: utf-8 -*-

import sys
import os

"""
以下でユーザーがテストを実行した際に`wiki_to_matrix`に
パスが通っていることを保証しています。
"""
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import wiki_to_matrix
