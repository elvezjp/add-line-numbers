# Changelog
[English](https://github.com/elvezjp/add-line-numbers/blob/main/CHANGELOG.md) | [日本語](https://github.com/elvezjp/add-line-numbers/blob/main/CHANGELOG_ja.md)

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.2] - 2026-05-14

### Added
- GitHub Actions workflows for publishing to PyPI / TestPyPI
  - `publish.yml`: publishes to PyPI when a `v*` tag is pushed (Trusted Publisher / OIDC)
  - `publish-testpypi.yml`: publishes to TestPyPI via manual `workflow_dispatch`

### Changed
- Raised the minimum supported Python version from 3.9 to 3.11
  - Development dependencies (pytest 9.x) require Python 3.10+, and pinning to
    the vulnerable pytest 8.x line on 3.9 was undesirable, so the supported
    range was tightened
- Switched internal links and image references in README.md / README_ja.md to
  absolute URLs under `github.com` / `raw.githubusercontent.com`
  - Relative links are not rendered on the PyPI project description page

## [0.1.1] - 2026-03-11

### Changed
- Raised the minimum supported Python version from 3.8 to 3.9
  - Built-in subscripted type hints (PEP 585) require Python 3.9+

## [0.1.0] - 2025-01-25

### Added
- Automatic 4-digit right-aligned line numbering for text files
- Preserves the input directory structure when copying to the output directory
- Auto-generated README in the output directory
- Support for UTF-8 text files (.py, .java, .js, .json, .xml, .md, .txt, and more)
- Automatic skip for binary files and non-UTF-8 files
- Command-line arguments for input and output directories
- `add_line_numbers_to_content()` function for processing strings directly
- Unit tests with pytest
- Package install support via pyproject.toml

### Technical Details
- Runs on Python 3.9 or later
- No external dependencies (standard library only)
- Line number format: `   1: ` (4-digit right-aligned + colon + space)

## Links

- [Repository](https://github.com/elvezjp/add-line-numbers)
- [Issue Tracker](https://github.com/elvezjp/add-line-numbers/issues)

## Version Comparison

| Version | Highlights |
|---------|------------|
| 0.1.2   | PyPI publishing support; minimum Python raised to 3.11 |
| 0.1.1   | Minimum Python raised to 3.9 |
| 0.1.0   | Initial public release |
