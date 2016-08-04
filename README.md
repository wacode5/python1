# pythonパッケージ作成のチュートリアル

## 目標

wikipediaの特定URLからN次までのリンクを全て取得し、それぞれの文書をベクトル化したデータに直すためのパッケージを作成します。

今回はhtmlを取得し、そのbodyの内容と内部に含まれるリンクの一覧を取得するだけでOKです。

すでに雛形は作成してあるので、関数の中身を記述して動作するようにしましょう。

## ファイルの説明

* `setup.py` ... インストール、テストなどの要件を定義するファイル。どのファイルを配布物に含めたいか、より詳細に指定する場合は`MANIFEST.in`という独自DSLで記述することになるが、はじめは必要ない。
* `requirements.txt` ... 依存パッケージを定義するファイル。
* `docs/` ... `sphinx-quickstart`で生成したSphinxドキュメントのテンプレート
* `.gitignore` ... はじめは[github推奨のもの](https://github.com/github/gitignore/blob/master/Python.gitignore)を使っておく。pythonに限らず有用
* `LICENSE.txt` ... ライセンスの全文。今回は[MITライセンス](http://choosealicense.com/licenses/mit/)
* `tests/` テストを置く。
* `examples/` ... 大規模なフレームワークの場合、使用例を記述しておくと使いやすくなる。
* `wiki_to_vec/` ... ソースコードのディレクトリ。

## TIPS

* `https://github.com/kennethreitz/samplemod` にパッケージの雛形が置いてあります。
* `ipython`中で`object??`を実行すると、その中身を見ることができます。`requests`や`BeautifulSoup`の使用方法がわからない時はこれで参照しましょう。

### テスト

`tests/`以下に置くテストは、設計が定まっていない段階で書くと全て無駄になる可能性があるため、あくまで大雑把な入出力にとどめておくことをおすすめします。

TDDのためのテストは`doctest`の方が多くの点で優れています。

## 処理済みデータ

[Pokemon GoのWiki Page](https://en.wikipedia.org/wiki/Pok%C3%A9mon_Go)を起点として、2次までの範囲にあるwikipediaページの英語版を処理した結果が以下になります。以降の解析に用いてください。

* [wikiページ間のリンクの有無を表すデータ](https://s3-ap-northeast-1.amazonaws.com/wacode5/graph_en.csv.gz)
* [それぞれの文書をDoc2Vecで行列形式に変換したデータ](https://s3-ap-northeast-1.amazonaws.com/wacode5/result_vector.csv.gz)

## Advanced

余裕があったら以下にも挑戦してみましょう。

1. 起点となるURLからリンクをたどりN次までの文書全てを取得するよう拡張する。(Scrapyの使用を考えても良い)
2. 抽出したbodyのテキストを学習済みdoc2vecに入れてベクトル化したデータを取得する。
3. html間のハイパーリンクを隣接行列で表ようにする。
4. `__main__.py`を作成し、コマンドラインスクリプトとして実行することもできるようにする。
5. `async`あるいは`multiprocessing`を用いてパフォーマンスを向上する。
