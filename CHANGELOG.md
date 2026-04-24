# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.2] - 2026-04-24
### 🐛 Bug Fixes
- Enable sphinx docs build locally and on Read the Docs

### 📚 Documentation
- Add Step 11 on migration of dev dependencies to pyproject.toml
- Extend Step 11 with sphinx dev-dep and Read the Docs configuration

### ⚡ Performance
- Declare dev-deps in pyproject.toml and prefix uv run in Makefile

### ⚙️ Miscellaneous Tasks
- Remove tests/requirements-test.txt (replaced by [dependency-groups].dev)

## [1.5.1] - 2026-04-24
### 🚀 Features
- Added ruff for linting, format e isort

### 📚 Documentation
- Close documentation before release

### ⚡ Performance
- Changed docstring format
- Added type hints and all others ruff controls
- Added pyright
- Added pre-commit
- Fix release workflow and refine pre-commit hooks

### ⚙️ Miscellaneous Tasks
- Update .gitignore and add uv.lock

## [1.5.0] - 2026-03-02
### 🚀 Features
- Changed packaging method
- Changed naming convention test files for pytest
- Added requirements for testing and building

### 🚜 Refactor
- Changed all disallowed variable and method names

### 📚 Documentation
- Added CHANGELOG.md management and updated stepbystep

### ⚡ Performance
- Changed MyClassInterface unittests in pytest
- Changed MyClassAbstract unittests in pytest
- Changed MyClass unittests in pytest
- Changed the format by black
- Changed the syntax by pylint suggestions

## [1.4.0] - 2026-02-22
### 🚀 Features
- Added pyproject.toml and versioning management, updated license's year

### 🐛 Bug Fixes
- Fixed some links and docs syntax

### 📚 Documentation
- Updated license's year
- Updated license's year

## [1.3.1] - 2026-02-22
### 📚 Documentation
- Updated documentation
- Updated documentation

### ⚡ Performance
- Updated changelog and version of the simple-sample package

## [1.3.0] - 2026-02-22
### 🚀 Features
- Added the unit test for MyClass
- Added MyClass and unit tests works properly

### 📚 Documentation
- Updated documentation
- Updated documentation

## [1.2.0] - 2026-02-22
### 🚀 Features
- Added the unit test for MyClassAbstract
- Added MyClassAbstract and unit tests works properly

### 📚 Documentation
- Updated documentation
- Updated documentation

## [1.1.0] - 2026-02-22
### 🚀 Features
- Added the unit test for MyClassInterface
- Added MyClassInterface and unit tests works properly

### 📚 Documentation
- Updated documentation
- Updated documentation

## [1.0.0] - 2026-02-22
### 🚀 Features
- Added the outline files
- Added the empty package version
- Added documentation by sphinx

[1.5.2]: https://github.com/bilardi/python-prototype/compare/v1.5.1...v1.5.2
[1.5.1]: https://github.com/bilardi/python-prototype/compare/v1.5.0...v1.5.1
[1.5.0]: https://github.com/bilardi/python-prototype/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/bilardi/python-prototype/compare/v1.3.1...v1.4.0
[1.3.1]: https://github.com/bilardi/python-prototype/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/bilardi/python-prototype/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/bilardi/python-prototype/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/bilardi/python-prototype/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/bilardi/python-prototype/compare/...v1.0.0

