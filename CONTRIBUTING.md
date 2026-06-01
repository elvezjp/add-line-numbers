# Contributing to add-line-numbers
[English](https://github.com/elvezjp/add-line-numbers/blob/main/CONTRIBUTING.md) | [日本語](https://github.com/elvezjp/add-line-numbers/blob/main/CONTRIBUTING_ja.md)

This document describes how to contribute to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open a GitHub Issue including the following:

- A clear, descriptive title
- Steps to reproduce the problem
- Expected behavior
- Actual behavior
- A sample file (if possible)
- Python version
- Operating system

### Proposing Enhancements

Feature suggestions are welcome! Please open an Issue with:

- A clear, descriptive title
- A detailed description of the proposed feature
- Use cases and benefits
- Relevant examples or mockups

### Pull Requests

1. **Fork the repository** and create a branch from `main`
   ```bash
   git checkout -b username/YYYYMMDD-description
   ```

2. **Follow the coding style** of the existing codebase
   - Use meaningful variable and function names
   - Add comments for complex logic
   - Follow the PEP 8 style guide

3. **Write tests** for your changes
   ```bash
   pytest test.py -v
   ```

4. **Update documentation** as needed
   - Update README.md for user-facing changes
   - Update spec.md for specification changes

5. **Commit your changes** with clear commit messages
   ```bash
   git commit -m "Add feature: description of your changes"
   ```

6. **Push to your fork** and open a pull request
   ```bash
   git push origin username/YYYYMMDD-description
   ```

7. **Wait for review** — maintainers may request changes during review

## Development Setup

### Prerequisites

- Python 3.11 or later

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/add-line-numbers.git
cd add-line-numbers

# Install pytest for testing (optional)
pip install pytest
```

### Running Tests

```bash
# Run all tests
pytest test.py -v

# Run a specific test
pytest test.py::TestClassName::test_method -v
```

### Verifying Your Changes

Before submitting a PR, please confirm the following:

1. All existing tests pass
2. New tests have been added for new functionality
3. The script works correctly across a variety of text files

## Coding Guidelines

### Python Style

- Follow the PEP 8 style guide
- Use type hints where appropriate
- Maximum line length: 100 characters (be flexible for long strings)
- Use meaningful variable names

### Documentation

- Add docstrings to all public functions and classes
- Use clear, concise language
- Include examples in docstrings where helpful

### Commit Messages

- Use the present tense ("Add feature", not "Added feature")
- Use the imperative mood ("Move cursor to...", not "Moves cursor to...")
- Keep the first line to 72 characters or less
- Reference related issues and pull requests when relevant

Example:
```
Add support for custom line number format

- Add --format option for customizing line number format
- Update README with new option documentation

Closes #123
```

## Code Review Process

1. Maintainers will review the pull request
2. They may ask questions or request changes
3. Once approved, the PR will be merged

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others where you can

## Release

### When to bump the version

Bump the version when there is a meaningful change to the repository — new features, bug fixes, or significant documentation additions. Dependency-only updates (e.g. routine security patches from Dependabot) do **not** trigger a version bump on their own; record them in `[Unreleased]` and include them in the next release that has a meaningful change.

### Tagging a release

After the version-bump commit is merged into `main`, tag it and push:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## Questions

For questions about contributing, please:

- Open an Issue with the `question` label
- See the contact information in the README
