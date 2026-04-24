How to make
===========

In this section you can find how to generate or publish that helps you with managing your code.

Virtual environment
###################

When you have to install specific requirements, you can use a `virtual environment <https://docs.python.org/3/tutorial/venv.html>`_: this method is important to test different package versions without installing them on your local.

The main commands are

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m venv .env  # create virtual environment
    $ source .env/bin/activate  # enter in the virtual environment
    $ pip install --upgrade -r requirements.txt  # install your dependencies
    $ deactivate  # exit when you have finished the job
    $ rm -rf .env  # remove the virtual environment: it is a best practice

Now there are many packages that can help in these steps, one is `uv <https://pypi.org/project/uv/>`_

The main commands become

.. code-block:: bash

    $ cd python-prototype
    $ pip install uv
    # you can manage a specific python version
    $ uv python install 3.13
    # create the environment and install all the dependencies (including dev)
    $ uv sync
    # to enter in the virtual environment
    $ source .venv/bin/activate

After `uv sync`, if you use `uv run` and the command you need (ie: `uv run pytest`, to test unit tests),
you don't need to use `source .venv/bin/activate` because `uv` package is the one who takes care of it.

TDD
###

Before writing code, it is important to verbalize the concepts by documentation and to create a Test Driven Development (TDD) for your code. Then, it is important to use unit tests for finding the issues and before updating the change log file and the package version.

See the development of this code step by step on `readthedocs / step by step <https://simple-sample.readthedocs.io/en/latest/stepbystep.html>`_ for learning how to make a unit test.

The ``step by step`` page uses ``unittest`` (on the ``unittest`` branch). For the ``pytest`` equivalent, see Step 5 of the `refactoring <https://simple-sample.readthedocs.io/en/latest/refactoring.html>`_ page, where each ``unittest`` test file is converted to ``pytest`` file by file.

Test tools
##########

Code quality is checked by three tools, all configured in the ``pyproject.toml``:

* `pytest <https://pypi.org/project/pytest/>`_, to run the tests
* `ruff <https://pypi.org/project/ruff/>`_, as linter and formatter (it replaces older tools like ``black``, ``flake8`` and ``isort`` in a single binary)
* `pyright <https://pypi.org/project/pyright/>`_, as static type checker (it validates type hints without running the code)

The main commands are

.. code-block:: bash

    $ cd python-prototype
    $ uv run pytest  # run all tests
    $ uv run ruff check --no-fix .  # lint (do not auto-fix)
    $ uv run ruff format --check .  # check formatting (do not rewrite)
    $ uv run pyright  # type check

See the `refactoring <https://simple-sample.readthedocs.io/en/latest/refactoring.html>`_ page for how these tools were chosen and configured.

Pre-commit hooks
################

To run ruff and pytest automatically before every commit, this project uses `pre-commit <https://pre-commit.com/>`_: a framework that installs a git hook in ``.git/hooks/pre-commit`` and runs a chain of checks against your changes.

The chain is declared in ``.pre-commit-config.yaml``. To install the git hook on your clone:

.. code-block:: bash

    $ cd python-prototype
    $ uv run pre-commit install

From now on, every ``git commit`` will first run ruff (with auto-fix), ruff-format and pytest. If any of them fails, the commit is aborted.

You can also trigger the chain manually, without committing:

.. code-block:: bash

    $ uv run pre-commit run --all-files

Conventional Commits
####################

The commit messages follow the `conventional commits <https://www.conventionalcommits.org/en/v1.0.0-beta.2/>`_ syntax. Each message starts with a type, a colon, and your description:

.. code-block:: bash

    $ git commit -m "feat: add MyClass and its unit tests"

The types used in this project are ``feat``, ``fix``, ``refactor``, ``perf``, ``docs``, ``test`` and ``chore``. The type is not cosmetic: `git-cliff <https://pypi.org/project/git-cliff/>`_ reads it to group the commits in ``CHANGELOG.md`` under "Features", "Bug Fixes", "Performance" and so on, so the changelog is generated automatically from the git history.

Versioning management
#####################

The project version lives in three files: ``simple_sample/__init__.py``, ``pyproject.toml`` and ``docs/source/conf.py``. Keeping them aligned by hand is error-prone, so there is a single command for each release type (see `semver <https://semver.org/>`_ for the difference between patch, minor and major):

.. code-block:: bash

    $ cd python-prototype
    $ make patch  # bump the patch version (e.g. 1.5.0 -> 1.5.1)
    $ make minor  # bump the minor version (e.g. 1.5.0 -> 1.6.0)
    $ make major  # bump the major version (e.g. 1.5.0 -> 2.0.0)

Under the hood, the ``release`` target in the ``Makefile`` runs ``bump-my-version`` (which updates the three files above), regenerates ``CHANGELOG.md`` with ``git-cliff``, amends the last commit, force-moves the tag and pushes both.

Documentation
#############

The Python language is permissive, but if you use a basic documentation like `Python Enhancement Proposals 8 <https://www.python.org/dev/peps/pep-0008/>`_ (PEP-8) and unit / functional test, everyone can easily read your code. There are many styles to write `Python documentation <https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format>`_.

If you load your package on `GitHub <https://github.com/>`_, `GitLab <https://gitlab.com/>`_, or `BitBucket <https://bitbucket.org/>`_, you can also use `sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_ for creating a docs folder like in this package. It can help you to organize concepts in a single place without duplicates: the README.rst is the homepage on Github and Pypi repositories and it is also one of these pages (see `overview.rst <https://simple-sample.readthedocs.io/en/latest/overview.html>`_).

The main commands for building documentation are

.. code-block:: bash

    $ cd python-prototype
    $ make doc

And you can open ``docs/build/html/index.html`` in your web browser to see your docs.

Instead, for uploading documentation on readthedocs, you have to follow `this guide <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.

Packaging
#########

The tutorial for `packaging your projects <https://packaging.python.org/tutorials/packaging-projects/>`_ is standard. And then your package is public on `PyPI <https://pypi.org/>`_.

The main commands for testing are

.. code-block:: bash

    $ make buildtest  # build and upload on testpypi
    $ make installtest  # install from testpypi

The main commands for the production environment are

.. code-block:: bash

    $ make build  # build and upload on pypi
    $ make install  # install from pypi
