# 二次面接課題

二次面接課題のPythonを使って作られた提出物（コンソールアプリケーション）

## 前提条件

- [Python](https://www.python.org/downloads/) - 3.6.x (このバージョン以上)

`python --verson` で、Pythonのバージョンを確認できます。他のPCでは、Pythonが`python3`と呼ばれるので、それをチェックしてください。

`python3`なら、実行説明での`python`は、`python3`にしてください。

## 実行説明

#### インデックスファイルを作成する機能

```bash
python main.py generate_index
```

これで、インデックスファイルが作成されます。

違うデータソースを使いたいなら、`-s`か`--source`任意の引数を追加したら、できます。

```bash
python main.py generate_index -s <データソースのディレクトリ>
```

#### 検索し出力する機能

```bash
python main.py search
```

上記のコマンドを実行したら、コンソールアプリが入力に待つようになります。検索するキーワードを入力したら、コンソールで直接に住所レコードの結果が出力されます。

キーワードがなしで、enterボターンを押すと、コンソールアプリがクロースされます。

#### テスト

```bash
python tests.py -v
```

シンプルな単体テストも書いてありますので、上記のコマンドでテストが実行できます。

