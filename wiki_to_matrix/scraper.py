#!usr/bin/env python
# -*- coding: utf-8 -*-
"""wikiからのhtmlの取得と整形を行う関数群
"""
from bs4 import BeautifulSoup
import requests
import logging
logger = logging.getLogger(__name__)
from wiki_to_matrix.utils import wiki_pattern, html_information


def crowl(url, path):
    """特定のurlからhtmlの情報を取得する

    BeautifulSoupを用いてパースし、bodyの内容だけを返す。

    Args:
        url (str): 取得したいhtmlのurl
        path (str): htmlを一時的に保存するディレクトリ
    Returns:
        html_information (namedtuple):
            str: htmlのbody contents
            list (str): html中に含まれるwikipidiaページへのurlのリスト。
                wiki内の内部リンクの場合、`wiki_pattern`から開始するので、
                これをうまく使って内部リンクのみを抽出する。
    """
    path_to_text = _download_html(url, path)



# 関数名を`_`(アンダーバー)から始めるとプライベートであることを明示できる。
def _download_html(url, path_to_save):
    """htmlを特定ディレクトリ以下に保存し、そのファイル名を返す。

    例えば
    urlが"http://thisis/example.com"
    path_to_saveが"/path/to/save"の場合
    ファイル名は"/path/to/save/example.html"になる。

    Args:
        url (str): 取得したいurl
        path_to_save (str): 保存先ディレクトリ
    Returns:
        str: 保存先ファイル名のパス
    """
    pass


# 以下のように書くことで、
# このファイルを直接スクリプトとして実行した場合にのみ実行するコマンド
# を定義することができる。
# が、モジュールの場合、テスト以外にこれを用いるのは
# アンチパターンなのでやめたほうが良い
if __name__ == '__main__':
    import doctest

    # doctestを実行する。
    # 今回は`Examples:`を記述した関数がないので空テスト
    doctest.testmod()
