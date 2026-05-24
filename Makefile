# Python prototype makefile

PACKAGE_NAME = "simple-sample"
LIBRARY_NAME = "simple_sample"

.PHONY: help # print this help list
help:
	grep PHONY Makefile | sed 's/.PHONY: /make /' | grep -v grep

.PHONY: clean # remove packaging files
clean:
	rm -rf build dist *.egg-info; rm -rf */*pyc; rm -rf */*/*pyc; rm -rf */__pycache__

.PHONY: sync # install/refresh dev dependencies via uv sync
sync:
	uv sync

.PHONY: test # run unit tests
test:
	uv run pytest

.PHONY: lint # run ruff check
lint:
	uv run ruff check --no-fix .

.PHONY: format # run ruff format
format:
	uv run ruff format .

.PHONY: typecheck # run pyright
typecheck:
	uv run pyright

.PHONY: doc # build documentation
doc:
	cd docs; make html SPHINXBUILD="uv run sphinx-build"; cd -

.PHONY: buildtest # build package and upload on testpypi
buildtest: clean
	uv build && uv run python -m twine upload --repository testpypi dist/*

.PHONY: installtest # install package from testpypi in a sandbox venv and verify
installtest:
	uv venv --clear .installtest
	uv pip install --python .installtest/bin/python --upgrade --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME)
	.installtest/bin/python -c "import $(LIBRARY_NAME); print($(LIBRARY_NAME).__version__)"
	rm -rf .installtest

.PHONY: build # build package and upload on pypi
build: clean
	uv build && uv run python -m twine upload dist/*

.PHONY: install # install package from pypi in a sandbox venv and verify
install:
	uv venv --clear .install
	uv pip install --python .install/bin/python --upgrade $(PACKAGE_NAME)
	.install/bin/python -c "import $(LIBRARY_NAME); print($(LIBRARY_NAME).__version__)"
	rm -rf .install

.PHONY: major minor patch # update version, CHANGELOG.md and push with also tags
major:
	$(MAKE) release PART=major

minor:
	$(MAKE) release PART=minor

patch:
	$(MAKE) release PART=patch

release:
	uv run bump-my-version bump $(PART)
	$(MAKE) changelog
	@echo "To publish the release to remote, run:"
	@echo "  git push && git push --tags --force"

.PHONY: changelog # update CHANGELOG.md and amend it on the commit
changelog:
	uv run git-cliff --config pyproject.toml --output CHANGELOG.md
	sed -i 's/<!-- [0-9]* -->//g' CHANGELOG.md
	git add CHANGELOG.md uv.lock
	TAG=$$(git tag --points-at HEAD); \
	git commit --amend --no-edit; \
	[ -n "$$TAG" ] && git tag -f $$TAG $$(git rev-parse HEAD) || true
