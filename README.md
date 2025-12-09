# add-line-numbers

ファイルまたはディレクトリを指定し、行番号を追加するツールです。

## 概要

テキストファイルに行番号を付与し、AI解析やコードレビュー時に行を特定しやすくするためのツールです。

- テキストファイル（ソースコード、設定ファイル、ドキュメント等）に行番号を付与
- ディレクトリ構造を保持した変換処理
- 変換結果の説明ドキュメント（README.md）を自動生成

## インストール

```bash
git clone https://github.com/your-username/add-line-numbers.git
cd add-line-numbers
```

Python 3.8以上が必要です。外部依存ライブラリはありません。

## 使い方

```bash
# デフォルト: src/ → analysis-input/
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
入力: src
出力: analysis-input
------------------------------------------------------------
✓ main/java/com/example/App.java
✓ config/settings.json
✓ docs/README.md
------------------------------------------------------------
完了: 64 個のファイルを処理しました
✓ README.md を生成しました: analysis-input/README.md
```

## 行番号の形式

各行の先頭に4桁右揃えの行番号を付与します。

**変換前:**
```
package com.example;

import java.util.List;

public class Example {
    public void method() {
        System.out.println("Hello");
    }
}
```

**変換後:**
```
   1: package com.example;
   2:
   3: import java.util.List;
   4:
   5: public class Example {
   6:     public void method() {
   7:         System.out.println("Hello");
   8:     }
   9: }
```

## 対応ファイル

- **対象**: UTF-8エンコーディングのテキストファイル全般（.py, .java, .js, .json, .xml, .md, .txt 等）
- **非対応**: バイナリファイル、UTF-8以外のエンコーディング（自動スキップ）

## License

MIT License - 詳細は [LICENSE](LICENSE) を参照してください。
