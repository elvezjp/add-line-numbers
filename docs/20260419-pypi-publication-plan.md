# PyPI 公開対応 計画書

- 作成日: 2026-04-19
- 対象バージョン: v0.1.1（現在の最新）
- 関連 Issue: [#10 PyPIにパッケージを公開する](https://github.com/elvezjp/add-line-numbers/issues/10)
- 作業ブランチ: `claude/pypi-publication-setup-vM3jZ`

## 1. 背景と目的

`add-line-numbers` を他の Python プロジェクトから `pip install add-line-numbers` で
インストールできるようにするため、現在のリポジトリを PyPI 公開可能な構成へ整備する。

関連情報:

- `md2map`（`elvezjp/md2map#14`）が本パッケージを git 依存で参照しており、
  PyPI 公開により依存解決が容易になる。
- PyPI 上で `add-line-numbers` の名前が未使用であることを Issue 起票者が確認済み
  （2026-03-25 時点）。

## 2. 現状のリポジトリ構成と課題

```
add-line-numbers/
├── add_line_numbers.py   # 本体（main() はすでに切り出し済み）
├── test.py               # pytest ベースのユニットテスト
├── pyproject.toml        # 最小構成（メタデータ不足）
├── LICENSE               # MIT License
├── README.md / README_ja.md
├── CHANGELOG.md / CONTRIBUTING.md / SECURITY.md / spec.md
└── .github/workflows/ci.yml  # pytest を走らせる CI
```

`pyproject.toml` は以下のように必要最小限で、PyPI 公開に必要なメタデータが不足している。

```toml
[project]
name = "add-line-numbers"
version = "0.1.1"
description = "ファイルに行番号を追加するツール"
requires-python = ">=3.9"
```

不足している要素:

- ライセンス宣言 (`license`, `license-files`)
- 長文説明 (`readme`)
- 著者情報 (`authors`)
- キーワード (`keywords`) と分類子 (`classifiers`)
- プロジェクト URL (`[project.urls]`)
- CLI エントリポイント (`[project.scripts]`)
- 任意依存（テスト用）(`[project.optional-dependencies]`)
- uv の lock ファイル (`uv.lock` が未生成)
- ビルド対象ファイルの明示（現状は `packages = ["."]` と広めに指定）

## 3. 公開ライブラリとしての仕様

| 項目 | 内容 |
| ---- | ---- |
| 配布名 (distribution) | `add-line-numbers` |
| インポート名 (import) | `add_line_numbers`（単一モジュール） |
| バージョン | `0.1.1`（本 PR では更新しない） |
| ライセンス | MIT |
| 対応 Python | `>=3.9` |
| 実行時依存 | なし（標準ライブラリのみ） |
| 任意依存 (dev) | `pytest` |
| ビルドバックエンド | `hatchling` |
| 同梱ファイル | `add_line_numbers.py`, `README.md`, `LICENSE` |
| CLI コマンド | `add-line-numbers`（= `add_line_numbers:main`） |
| 公開 API | `add_line_numbers_to_content` / `add_line_numbers_to_file` / `generate_directory_tree` / `generate_readme` / `process_directory` / `main` |

## 4. PyPI 公開までの全体計画

1. **メタデータ整備**（本 PR の対象）
   - `pyproject.toml` に PyPI 公開に必要な項目を追加
   - 単一モジュール構成のまま wheel ビルド対象を明示
   - CLI エントリポイントを追加
2. **開発環境の再現性確保**（本 PR の対象）
   - `uv.lock` を再生成しリポジトリにコミット
3. **ビルド検証**（本 PR の対象）
   - `python -m build` 相当の処理でソース配布物 / wheel を生成
   - wheel に想定ファイルが含まれることを確認
4. **テスト**（本 PR の対象）
   - 既存の `pytest test.py` がパッケージインストール後も通ることを確認
5. **TestPyPI への公開検証**（本 PR の対象外・管理者作業）
   - `twine upload --repository testpypi` で TestPyPI に上げ、
     `pip install -i ...` で他プロジェクトから参照できることを確認
6. **PyPI 本番公開**（本 PR の対象外・管理者作業）
   - API トークンで `twine upload`（または GitHub Actions の
     Trusted Publisher を別途設定）
7. **CI 拡張**（本 PR では最小限、必要に応じて追加 Issue）
   - ビルド成果物検証や自動公開ワークフローは将来的に別途検討

## 5. 本 PR で対応するタスク

- [x] `docs/20260419-pypi-publication-plan.md` を作成
- [x] `pyproject.toml` にメタデータを追加
  - `license` / `license-files`
  - `readme`
  - `authors` / `maintainers`
  - `keywords`
  - `classifiers`（License, Python バージョン, 開発ステータス, OS など）
  - `[project.urls]`（Homepage, Repository, Issues, Changelog）
  - `[project.scripts]` に `add-line-numbers = "add_line_numbers:main"`
  - `[project.optional-dependencies].dev = ["pytest"]`
- [x] `[tool.hatch.build.targets.wheel]` を単一モジュール向けに調整
      （`add_line_numbers.py` のみを wheel / sdist に含める）
- [x] `uv.lock` を再生成してコミット
- [x] ビルドを実行して wheel の中身を確認
- [x] `pytest test.py` が通ることを確認
- [x] PR を Issue #10 に紐付けて作成

## 6. 本 PR の対象外（残タスク）

管理者側での確認・追加対応として以下を想定する。

- TestPyPI への実アップロードと、`pip install -i https://test.pypi.org/simple/ add-line-numbers`
  による動作確認
- PyPI 本番への公開（API トークン or Trusted Publisher 設定）
- PyPI 公開自動化用 GitHub Actions ワークフローの追加（例: タグ push で
  `pypa/gh-action-pypi-publish` を実行する）
- リリースに合わせた `CHANGELOG.md` 更新（本 PR ではバージョン据え置きのため変更しない）
- `md2map` 側で git 依存から PyPI 依存への切り替え（`elvezjp/md2map#14` 側作業）

## 7. 受け入れ確認項目（管理者向け）

以下を確認していただきたい。

### 7.1 リポジトリ構成

- [ ] `docs/20260419-pypi-publication-plan.md` が追加されている
- [ ] `pyproject.toml` に不足メタデータが追加されている
- [ ] `uv.lock` が追加／最新化されている
- [ ] 旧バージョン用のコードは変更されていない（本リポジトリは単一バージョン構成）

### 7.2 ビルド成果物の確認

ローカルで次を実行し、sdist / wheel が生成できること。

```bash
uv sync --all-extras
uv run python -m build   # もしくは `uvx --from build pyproject-build`
```

- [ ] `dist/add_line_numbers-0.1.1-py3-none-any.whl` が生成される
- [ ] `dist/add_line_numbers-0.1.1.tar.gz` が生成される
- [ ] wheel を `unzip -l` で確認し、`add_line_numbers.py` / `*.dist-info/METADATA` /
      `*.dist-info/entry_points.txt` / `LICENSE` 相当のファイルが含まれる
- [ ] METADATA に `License`, `Author`, `Project-URL`, `Classifier` 等が書かれている

### 7.3 インストールと CLI 動作確認

クリーンな仮想環境で次を実行。

```bash
python -m venv .venv-check
.venv-check/bin/pip install dist/add_line_numbers-0.1.1-py3-none-any.whl
.venv-check/bin/add-line-numbers --help  # 使い方が表示される
.venv-check/bin/python -c "from add_line_numbers import add_line_numbers_to_content; print(add_line_numbers_to_content('a\nb\n'))"
```

- [ ] `add-line-numbers` コマンドが PATH 上で実行可能
- [ ] 実引数なしで実行したときの挙動が従来通り（`inputs/` → `outputs/`）
- [ ] `from add_line_numbers import ...` で関数がインポートできる

### 7.4 テスト

- [ ] `pytest test.py -v` がローカルで通る
- [ ] GitHub Actions（`.github/workflows/ci.yml`）がこの PR に対して成功する

### 7.5 PyPI 公開前の最終チェック（参考）

- [ ] `twine check dist/*` でメタデータ検証が通る
- [ ] TestPyPI にアップロードして `pip install` が成功する
- [ ] README.md が PyPI 上で正しくレンダリングされる

## 8. 実装記録

本セクションは実装と並行して更新する。

- 2026-04-19: 計画書作成
- 2026-04-19: `pyproject.toml` を PyPI 公開向けに刷新
  - `license = "MIT"` / `license-files = ["LICENSE"]`
  - `readme = "README.md"`
  - `authors`, `maintainers`, `keywords`, `classifiers`, `[project.urls]`
  - `[project.scripts]` に `add-line-numbers = "add_line_numbers:main"` を追加
  - `[project.optional-dependencies].dev = ["pytest>=7"]`
  - `[tool.hatch.build.targets.wheel]` を `only-include = ["add_line_numbers.py"]` に変更し、
    単一モジュールだけを wheel に含める
  - `[tool.hatch.build.targets.sdist]` で `add_line_numbers.py`, `README.md`,
    `README_ja.md`, `LICENSE`, `CHANGELOG.md`, `test.py`, `pyproject.toml` を同梱
- 2026-04-19: `uv lock` で `uv.lock` を新規生成
- 2026-04-19: `uv run python -m build` で sdist / wheel を生成、`twine check` が成功
- 2026-04-19: `uv run pytest test.py -v` が全件成功
