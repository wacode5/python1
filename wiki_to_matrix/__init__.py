#!usr/bin/env python
# -*- coding: utf-8 -*-
"""ディレクトリをパッケージ化するためのファイル。
"""


# 以下のimport文を書いておくことで外部から関数をimportしようとした際に
# from wiki_to_matrix import crowl
# だけでインポートできるようになる
from .scraper import crowl
