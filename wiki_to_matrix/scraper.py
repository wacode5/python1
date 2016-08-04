#!usr/bin/env python
# -*- coding: utf-8 -*-

"""wikiからのhtmlの取得と整形を行う関数群
"""
from bs4 import BeautifulSoup
import requests
import re
import logging
logger = logging.getLogger(__name__)
from wiki_to_matrix.utils import wiki_pattern, html_information


def crowl(url, path, lang="en"):
    """特定のurlからhtmlを取得する

    Args:
        url (str): 取得したいhtmlのurl
        path (str): htmlを一時的に保存するディレクトリ
        lang (str): どの言語のwikipediaページをダウンロードするか
    Returns:
        html_information (namedtuple):
            str: htmlのbody contents
            list (str): html中に含まれるwikipidiaページへのurlのリスト
    """
    _download_html(url, path)
    body = _extract_body(path)
    pass


# 関数名を`_`(アンダーバー)から始めるとプライベートであることを明示できる。
def _extract_body(html):
    """htmlから興味のある内容のみを抽出する
    body以外の情報は解析に用いるには冗長なため、ここで削る

    Args:
        html (str): htmlファイルへのパス
    Returns:
        str: body contents
    """
    bsObj = BeautifulSoup(html, "lxml")
    body_content = bsObj.find('div', {"id": "bodyContent"})
    return body_content.get_text().replace(' ', '').replace("\n", '').replace("　", '')


def _download_html(url, path_to_save):
    """htmlを特定ディレクトリに保存する。


    Args:
        url (str): 取得したいurl
        path_to_save (str): 保存先ディレクトリ
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
