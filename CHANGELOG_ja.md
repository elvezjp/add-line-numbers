# 変更履歴
[English](https://github.com/elvezjp/add-line-numbers/blob/main/CHANGELOG.md) | [日本語](https://github.com/elvezjp/add-line-numbers/blob/main/CHANGELOG_ja.md)

このプロジェクトのすべての重要な変更を記録します。

フォーマットは [Keep a Changelog](https://keepachangelog.com/ja/1.0.0/) に基づき、
バージョン管理は [セマンティックバージョニング](https://semver.org/lang/ja/) に準拠しています。

## [未リリース]

## [0.1.3] - 2026-08-09

### セキュリティ
- 推移的な開発依存パッケージ `cryptography` の下限を `>= 50.0.0` に引き上げ、
  [GHSA-537c-gmf6-5ccf](https://github.com/pyca/cryptography/security/advisories/GHSA-537c-gmf6-5ccf)
  （`cryptography` の wheel `< 48.0.1` に脆弱な OpenSSL が同梱されている問題）および
  [GHSA-g6cj-pr64-35w5](https://github.com/pyca/cryptography/security/advisories/GHSA-g6cj-pr64-35w5)
  （`< 50.0.0` の PKCS#7 `EnvelopedData` 復号に Bleichenbacher オラクルが存在する問題）に対応
  - `pyproject.toml` に `[tool.uv]` の `constraint-dependencies` を追加
  - `uv.lock` を再生成（`cryptography` 48.0.0 → 50.0.0）
  - ランタイムには影響なし: `cryptography` は Linux 上で `twine`（開発依存）経由でのみ導入される

### 変更
- **PyPI 公開を手動実行のみに変更**: `publish.yml` の tag `v*` push トリガーを廃止し、
  Actions から `workflow_dispatch` で `target`（`testpypi` / `pypi`）を選んで起動する方式に変更
  - タグはリリースの記録であり、依存元リポジトリからの参照を固定する用途でも打つため、
    タグ push だけで PyPI 公開が走らないようにした
  - `publish-testpypi.yml` を `publish.yml` に統合し、旧ファイルを削除。
    TestPyPI へのリハーサルは同 workflow の `target: testpypi` 実行に相当する
  - 公開前のテスト必須化は維持: `build` ジョブが配布物のビルド前に `pytest` を実行する

## [0.1.2] - 2026-05-14

### 追加
- PyPI / TestPyPI 公開用 GitHub Actions ワークフローを追加
  - `publish.yml`: tag `v*` の push をトリガーに PyPI へ公開（Trusted Publisher / OIDC）
  - `publish-testpypi.yml`: `workflow_dispatch` 手動起動で TestPyPI へ公開

### 変更
- 最小サポート Python バージョンを 3.9 から 3.11 に引き上げ
  - 開発依存（pytest 9.x）が Python 3.10 以上を要求し、3.9 環境では脆弱な
    pytest 8.x に固定されるため、サポート対象を整理
- README.md / README_ja.md の内部リンクと画像参照を `github.com` /
  `raw.githubusercontent.com` の絶対 URL に変更
  - PyPI のプロジェクト説明ページでは相対リンクがレンダリングされないため

## [0.1.1] - 2026-03-11

### 変更
- 最小サポート Python バージョンを 3.8 から 3.9 に引き上げ
  - 組み込み型の添字型ヒント（PEP 585）を使用するため 3.9 以上が必要

## [0.1.0] - 2025-01-25

### 追加
- テキストファイルに4桁右寄せの行番号を自動付与する機能
- 入力ディレクトリの構造を保持したまま出力ディレクトリにコピーする機能
- 出力ディレクトリに自動生成READMEを作成する機能
- UTF-8テキストファイル（.py, .java, .js, .json, .xml, .md, .txtなど）のサポート
- バイナリファイル・非UTF-8ファイルの自動スキップ機能
- コマンドライン引数による入力・出力ディレクトリの指定機能
- 文字列を直接処理する `add_line_numbers_to_content()` 関数
- pytestによるユニットテスト
- pyproject.tomlによるパッケージインストール対応

### 技術詳細
- Python 3.9以上で動作
- 外部ライブラリに依存しない（標準ライブラリのみ使用）
- 行番号フォーマット: `   1: `（4桁右寄せ + コロン + スペース）

## リンク

- [リポジトリ](https://github.com/elvezjp/add-line-numbers)
- [Issueトラッカー](https://github.com/elvezjp/add-line-numbers/issues)

## バージョン比較

| バージョン | 主な機能 |
|------------|------------|
| 0.1.3      | PyPI 公開を手動実行のみに変更、`cryptography`（開発依存）の下限引き上げ |
| 0.1.2      | PyPI 公開対応、最小 Python バージョンを 3.11 に引き上げ |
| 0.1.1      | 最小 Python バージョンを 3.9 に引き上げ |
| 0.1.0      | 基本機能公開 |