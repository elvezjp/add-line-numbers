# add-line-numbers

テキストファイルに行番号を付与するPythonツールです。

## 概要

AIによるコード解析やコードレビュー時に、行番号で特定の箇所を参照しやすくするためのツールです。

- テキストファイル（ソースコード、設定ファイル、ドキュメント等）に行番号を付与
- ディレクトリ構造を保持した変換処理
- 変換結果の説明ドキュメント（README.md）を自動生成

## インストール

```bash
git clone https://github.com/elvezjp/add-line-numbers.git
cd add-line-numbers
```

Python 3.8以上が必要です。外部依存ライブラリはありません。

## 使い方

```bash
# デフォルト: inputs/ → outputs/
python add_line_numbers.py

# カスタムディレクトリ指定
python add_line_numbers.py <入力ディレクトリ> <出力ディレクトリ>
```

### 例

```bash
# my_project/ 内のファイルを numbered_output/ に出力
python add_line_numbers.py my_project numbered_output
```

### 出力例

```
処理中: 64 個のファイル
入力: inputs
出力: outputs
------------------------------------------------------------
✓ src/main.py
✓ config/settings.json
✓ docs/README.md
------------------------------------------------------------
完了: 64 個のファイルを処理しました
✓ README.md を生成しました: outputs/README.md
```

## 行番号の形式

各行の先頭に4桁右揃えの行番号を付与します。

**変換前:**
```python
def hello():
    print("Hello, World!")

if __name__ == "__main__":
    hello()
```

**変換後:**
```
   1: def hello():
   2:     print("Hello, World!")
   3:
   4: if __name__ == "__main__":
   5:     hello()
```

## 対応ファイル

- **対象**: UTF-8エンコーディングのテキストファイル全般（.py, .java, .js, .json, .xml, .md, .txt 等）
- **非対応**: バイナリファイル、UTF-8以外のエンコーディング（自動スキップ）

## ファイル構成

```
add-line-numbers/
├── add_line_numbers.py   # メインスクリプト
├── test.py               # ユニットテスト
├── spec.md               # 詳細仕様書
├── LICENSE               # MITライセンス
└── README.md             # このファイル
```

## テスト

```bash
# pytestが必要です
pip install pytest

# テスト実行
pytest test.py -v
```

## License

MIT License - 詳細は [LICENSE](LICENSE) を参照してください。
