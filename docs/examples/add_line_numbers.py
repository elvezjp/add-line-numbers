   1: #!/usr/bin/env python3
   2: """
   3: テキストファイルに行番号を付けるシンプルなスクリプト
   4: 
   5: 使い方:
   6:     python add_line_numbers.py                    # inputs/ → outputs/ (デフォルト)
   7:     python add_line_numbers.py input_dir output_dir  # カスタムディレクトリ指定
   8: """
   9: 
  10: import os
  11: import sys
  12: from datetime import datetime
  13: from pathlib import Path
  14: 
  15: 
  16: def add_line_numbers_to_content(content: str) -> tuple[str, int]:
  17:     """
  18:     文字列に行番号を付与して返す
  19: 
  20:     Args:
  21:         content: 行番号を付与する元のテキスト
  22: 
  23:     Returns:
  24:         tuple: (行番号付きテキスト, 行数)
  25:     """
  26:     lines = content.splitlines()
  27:     line_count = len(lines)
  28: 
  29:     numbered_lines = []
  30:     for i, line in enumerate(lines, 1):
  31:         numbered_lines.append(f"{i:4d}: {line}")
  32: 
  33:     return "\n".join(numbered_lines), line_count
  34: 
  35: 
  36: def add_line_numbers_to_file(input_path: Path, output_path: Path) -> None:
  37:     """
  38:     テキストファイルに行番号を付けて出力する
  39: 
  40:     Args:
  41:         input_path: 入力ファイルのパス
  42:         output_path: 出力ファイルのパス
  43:     """
  44:     # 出力ディレクトリが存在しない場合は作成
  45:     output_path.parent.mkdir(parents=True, exist_ok=True)
  46: 
  47:     # ファイルを読み込んで行番号を付ける
  48:     with open(input_path, 'r', encoding='utf-8') as f:
  49:         lines = f.readlines()
  50: 
  51:     with open(output_path, 'w', encoding='utf-8') as f:
  52:         for i, line in enumerate(lines, 1):
  53:             f.write(f"{i:4d}: {line}")
  54: 
  55: 
  56: def generate_directory_tree(directory: Path, prefix: str = "", max_depth: int = 5, current_depth: int = 0) -> str:
  57:     """
  58:     ディレクトリ構造をツリー形式の文字列として生成する
  59: 
  60:     Args:
  61:         directory: 対象ディレクトリのパス
  62:         prefix: ツリー表示用のプレフィックス
  63:         max_depth: 最大探索深度
  64:         current_depth: 現在の深度
  65: 
  66:     Returns:
  67:         ツリー形式の文字列
  68:     """
  69:     if current_depth >= max_depth:
  70:         return ""
  71: 
  72:     tree_lines = []
  73: 
  74:     try:
  75:         # ディレクトリとファイルを取得してソート
  76:         entries = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name))
  77: 
  78:         for i, entry in enumerate(entries):
  79:             is_last = i == len(entries) - 1
  80: 
  81:             # ツリー記号を決定
  82:             if is_last:
  83:                 current_prefix = "└── "
  84:                 next_prefix = "    "
  85:             else:
  86:                 current_prefix = "├── "
  87:                 next_prefix = "│   "
  88: 
  89:             # エントリ名を追加
  90:             if entry.is_dir():
  91:                 tree_lines.append(f"{prefix}{current_prefix}{entry.name}/")
  92:                 # 再帰的にサブディレクトリを処理
  93:                 subtree = generate_directory_tree(entry, prefix + next_prefix, max_depth, current_depth + 1)
  94:                 if subtree:
  95:                     tree_lines.append(subtree)
  96:             else:
  97:                 # すべてのファイルを表示
  98:                 tree_lines.append(f"{prefix}{current_prefix}{entry.name}")
  99:     except PermissionError:
 100:         pass
 101: 
 102:     return "\n".join(tree_lines)
 103: 
 104: 
 105: def generate_readme(output_dir: Path, input_dir: Path) -> None:
 106:     """
 107:     行番号付きファイルディレクトリ用のREADME.mdを生成する
 108: 
 109:     Args:
 110:         output_dir: 出力ディレクトリのパス
 111:         input_dir: 入力ディレクトリのパス（生成元の参照用）
 112:     """
 113:     readme_path = output_dir / "README.md"
 114: 
 115:     # 入力ディレクトリの相対パスを取得（説明用）
 116:     try:
 117:         input_relative = Path(input_dir).resolve().relative_to(Path.cwd())
 118:     except ValueError:
 119:         input_relative = Path(input_dir)
 120: 
 121:     # 出力ディレクトリの相対パスを取得（ディレクトリ構造表示用）
 122:     try:
 123:         output_relative = Path(output_dir).resolve().relative_to(Path.cwd())
 124:         output_dirname = output_relative.name
 125:     except ValueError:
 126:         output_dirname = Path(output_dir).name
 127: 
 128:     # ディレクトリ構造を生成
 129:     directory_tree = generate_directory_tree(output_dir)
 130: 
 131:     # 現在時刻を取得
 132:     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 133: 
 134:     readme_content = f"""# 行番号付きファイルディレクトリ
 135: 
 136: ## 概要
 137: 
 138: このディレクトリには、**行番号が付与されたテキストファイル**が含まれています。
 139: 
 140: ## 行番号の形式
 141: 
 142: 各ファイル内の各行は、以下の形式で行番号が付与されています：
 143: 
 144: ```
 145:    1: package com.example;
 146:    2:
 147:    3: import java.util.List;
 148:    4: public class Example {{
 149:    5:     public void method() {{
 150:    6:         // コード
 151:    7:     }}
 152:    8: }}
 153: ```
 154: 
 155: ### 行番号フォーマットの特徴
 156: 
 157: - **形式**: `行番号: `（行番号の後にコロンとスペース）
 158: - **パディング**: 行番号は右揃えで表示され、最大桁数に合わせてスペースでパディングされます
 159: - **例**:
 160:   - 1桁の行番号: `   1: `
 161:   - 2桁の行番号: `  10: `
 162:   - 3桁の行番号: ` 100: `
 163:   - 4桁の行番号: `1000: `
 164: 
 165: ## AIへの重要な指示
 166: 
 167: ### 1. 行番号の認識
 168: 
 169: このディレクトリ内のファイルを処理する際は、**各行の先頭にある行番号を認識し、内容の一部として扱ってください**。
 170: 
 171: ### 2. 行番号参照時の形式
 172: 
 173: ファイル内の特定の行を参照する際は、**ファイル内に表示されている行番号をそのまま使用してください**。
 174: 
 175: **正しい参照例:**
 176: - 「12行目の内容を確認してください」
 177: - 「45行目から50行目までの処理を修正してください」
 178: - 「`12: import java.util.List;` の行を...」
 179: 
 180: **誤った参照例:**
 181: - 「実際のファイルの12行目」（行番号を無視した参照）
 182: 
 183: ### 3. ファイル解析時の注意点
 184: 
 185: - 行番号は**ファイル内容の一部**として扱ってください
 186: - 行番号を削除したり、無視したりしないでください
 187: - 構造解析や構文解析を行う際も、行番号を含めた状態で処理してください
 188: 
 189: ### 4. ファイル編集時の注意点
 190: 
 191: このディレクトリ内のファイルを編集する場合は：
 192: - 行番号の形式を維持してください（`行番号: `の形式）
 193: - 行番号の連続性を保ってください
 194: - 行を追加・削除する場合は、行番号を適切に再計算してください
 195: 
 196: ## ディレクトリ構造
 197: 
 198: このディレクトリは、元のファイルのディレクトリ構造を保持しています。
 199: 
 200: ```
 201: {output_dirname}/
 202: {directory_tree}
 203: ```
 204: 
 205: ## 生成元との関係
 206: 
 207: このディレクトリ内のファイルは、元のファイル（`{input_relative}`ディレクトリ）に行番号を付与して生成されたものです。
 208: 
 209: - **元のファイル**: 行番号なしの通常のファイル
 210: - **このディレクトリ**: 行番号が付与されたファイル
 211: 
 212: ## 使用例
 213: 
 214: ### ファイル参照の例
 215: 
 216: ```
 217:   12: import java.util.List;
 218:   13:
 219:   14: public class Example {{
 220:   15:     public void method() {{
 221:   16:         List<String> list = new ArrayList<>();
 222:   17:     }}
 223:   18: }}
 224: ```
 225: 
 226: 上記のファイルを参照する際は：
 227: - 「16行目の`List<String> list = new ArrayList<>();`を...」と表現してください
 228: - 実際のファイル内では「`  16: List<String> list = new ArrayList<>();`」と表示されています
 229: 
 230: ## まとめ
 231: 
 232: - 行番号はファイル内容の一部として扱う
 233: - 行番号参照時は、ファイル内に表示されている行番号を使用する
 234: - ファイル編集時も行番号の形式を維持する
 235: - 行番号を無視したり削除したりしない
 236: 
 237: ---
 238: 
 239: **注意**: このディレクトリ内のファイルは自動生成されたものです。元のファイルを変更する場合は、元のディレクトリ（`{input_relative}`など）で編集し、再度行番号を付与してください。
 240: 
 241: **生成日時**: {current_time} - このREADME.mdは `add_line_numbers.py` スクリプトによって自動生成されました。
 242: """
 243: 
 244:     readme_path.write_text(readme_content, encoding='utf-8')
 245:     print(f"✓ README.md を生成しました: {readme_path}")
 246: 
 247: 
 248: def process_directory(input_dir: str, output_dir: str) -> None:
 249:     """
 250:     ディレクトリ内の全テキストファイルを処理する
 251: 
 252:     Args:
 253:         input_dir: 入力ディレクトリ
 254:         output_dir: 出力ディレクトリ
 255:     """
 256:     input_path = Path(input_dir)
 257:     output_path = Path(output_dir)
 258: 
 259:     if not input_path.exists():
 260:         print(f"エラー: 入力ディレクトリが見つかりません: {input_dir}")
 261:         sys.exit(1)
 262: 
 263:     # 全ファイルを再帰的に探す（ディレクトリは除外）
 264:     all_files = [f for f in input_path.glob("**/*") if f.is_file()]
 265: 
 266:     if not all_files:
 267:         print(f"警告: {input_dir} 内にファイルが見つかりませんでした")
 268:         return
 269: 
 270:     print(f"処理中: {len(all_files)} 個のファイル")
 271:     print(f"入力: {input_dir}")
 272:     print(f"出力: {output_dir}")
 273:     print("-" * 60)
 274: 
 275:     processed_count = 0
 276:     skipped_count = 0
 277: 
 278:     # 各ファイルを処理
 279:     for file in all_files:
 280:         # 相対パスを取得してディレクトリ構造を保持
 281:         relative_path = file.relative_to(input_path)
 282:         output_file = output_path / relative_path
 283: 
 284:         try:
 285:             add_line_numbers_to_file(file, output_file)
 286:             print(f"✓ {relative_path}")
 287:             processed_count += 1
 288:         except UnicodeDecodeError:
 289:             print(f"✗ {relative_path}: UTF-8として読み込めないためスキップ")
 290:             skipped_count += 1
 291:         except Exception as e:
 292:             print(f"✗ {relative_path}: {e}")
 293:             skipped_count += 1
 294: 
 295:     print("-" * 60)
 296:     print(f"完了: {processed_count} 個のファイルを処理しました")
 297:     if skipped_count > 0:
 298:         print(f"スキップ: {skipped_count} 個のファイル")
 299: 
 300:     # README.mdを生成
 301:     try:
 302:         generate_readme(output_path, input_path)
 303:     except Exception as e:
 304:         print(f"警告: README.mdの生成に失敗しました: {e}")
 305: 
 306: 
 307: def main():
 308:     """メイン関数"""
 309:     # コマンドライン引数の処理
 310:     if len(sys.argv) == 1:
 311:         # デフォルト: inputs/ → outputs/
 312:         input_dir = "inputs"
 313:         output_dir = "outputs"
 314:     elif len(sys.argv) == 3:
 315:         # カスタムディレクトリ指定
 316:         input_dir = sys.argv[1]
 317:         output_dir = sys.argv[2]
 318:     else:
 319:         print(__doc__)
 320:         print("\nエラー: 引数の数が正しくありません")
 321:         print("使い方:")
 322:         print("  python add_line_numbers.py")
 323:         print("  python add_line_numbers.py <入力ディレクトリ> <出力ディレクトリ>")
 324:         sys.exit(1)
 325: 
 326:     process_directory(input_dir, output_dir)
 327: 
 328: 
 329: if __name__ == "__main__":
 330:     main()
