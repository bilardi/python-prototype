# Python prototype makefile

PACKAGE_NAME = "simple-sample"
LIBRARY_NAME = "simple_sample"

.PHONY: help # print this help list
help:
	grep PHONY Makefile | sed 's/.PHONY: /make /' | grep -v grep

.PHONY: unittest # run unit tests
unittest:
	python3 -m unittest discover -v

.PHONY: clean # remove packaging files
clean:
	rm -rf build dist *.egg-info; rm -rf */*pyc; rm -rf */*/*pyc; rm -rf */__pycache__

.PHONY: doc # build documentation
doc: 
	cd docs; make html; cd -

.PHONY: buildtest # build package on testpypi
buildtest: clean
	python3 -m build; python3 -m twine upload --repository testpypi dist/*

.PHONY: installtest # install package from testpypi
installtest:
	mkdir -p test; cd test; uv pip install --upgrade --index-url https://test.pypi.org/simple/ --no-deps $(PACKAGE_NAME); cd -

.PHONY: build # build package on pypi
build: clean
	python3 -m build; python3 -m twine upload dist/*

.PHONY: install # install package from pypi
install:
	uv pip install --upgrade $(PACKAGE_NAME)

.PHONY: major minor patch # update version, CHANGELOG.md and push with also tags
major:
	$(MAKE) release PART=major

minor:
	$(MAKE) release PART=minor

patch:
	$(MAKE) release PART=patch

release:
	bump-my-version bump $(PART)
	$(MAKE) changelog
	git tag -f v$$(python -c "from simple_sample import __version__; print(__version__)")
	git push && git push --tags --force

.PHONY: changelog # update CHANGELOG.md and amend it on the commit
changelog:
	git-cliff --config pyproject.toml --output CHANGELOG.md
	sed -i 's/<!-- [0-9]* -->//g' CHANGELOG.md
	git add CHANGELOG.md
	git commit --amend --no-edit
