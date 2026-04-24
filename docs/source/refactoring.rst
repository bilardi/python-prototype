Refactoring
===========

This page is for learning all steps that are necessary for refactoring a simple package like simple-sample,

* from unittest and setup.py
* to pytest and pyproject.toml

Before following the guide, it is important to follow the guide `how to make <https://simple-sample.readthedocs.io/en/latest/howtomake.html>`_,
because you need to install dependencies for testing, improving and checking your code.

pyproject.toml
##############

This is the core of configuration of a project where you can add all your custom modules configuration.

In this project you can find,

* `bumpversion <https://pypi.org/project/bumpversion/>`_, to manage the versioning update in the files that need it (see details in Makefile)

.. code-block:: bash

    # use one of the following commands according to the guide https://semver.org/
    make patch
    make minor
    make major

* `git-cliff <https://pypi.org/project/git-cliff/>`_, to update the CHANGELOG.md (see details in Makefile)

.. code-block:: bash

    # it also adds the file in the commit
    make changelog

* `pytest <https://pypi.org/project/pytest/>`_, to run the tests.
* `ruff <https://pypi.org/project/ruff/>`_, it is the linter and formatter to automate code styling.
* `pyright <https://pypi.org/project/pyright/>`_, to analyze the code and suggest how it could be refactored.

Getting started
###############

The goal of the refactoring of the package simple-sample is to update some concepts to manage a Python package.
So you can use this simple package or this guide to refactor your package.

Step 1
******

The first step is to change the commits that have an old style described on `readthedocs / step by step <https://simple-sample.readthedocs.io/en/latest/stepbystep.html>`_.

The `conventional commits <https://www.conventionalcommits.org/en/v1.0.0-beta.2/>`_ uses a specific syntax:

* one of the types described in the guide
* colon
* your message, for me, with `keepachangelog style <keepachangelog.com/>`_

To change all commits, we need to use `git-rebase <https://git-scm.com/docs/git-rebase>`_

.. code-block:: bash

    # save the status in a specific branch
    git checkout -b unittest

    # work on another branch
    git checkout -b conventional-commits

    # replace pick with r to rewrite the commit marked
    git rebase -i --root

Step 2
******

The second step is to add new tags:

* now, the commits are different
* so the tags are linked only on the unittest branch commits

To add the tags, it is important to define

* which commits to use
* if you want to use the same versions or new ones

In this case, only to keep the page `readthedocs / step by step <https://simple-sample.readthedocs.io/en/latest/stepbystep.html>`_ working,
we start from a major release.

.. code-block:: bash

    git tag -a v1.0.0 -f -m "Empty package and documentation by sphinx" 714213d7614c2df9007948d51a0c8b5f5789145f
    git tag -a v1.1.0 -f -m "MyClassInterface, unit tests and documentation" b8ac778148da489d654b44e5964258996736dcac
    git tag -a v1.2.0 -f -m "MyClassAbstract, unit tests and documentation" 5f4b830e17798ba71a6d512175c0b41a4d30f9ab
    git tag -a v1.3.0 -f -m "MyClass, unit tests and documentation" b4b4d745857893efde51c0c3d235778f8f127de6
    git tag -a v1.3.1 -f -m "The first full version of the simple-sample package" bb6029414975a84043fd7b8692318269e26511b0

After that, you can merge on the branch master and keep only the branch unittest.

Step 3
******

Before rewriting the code, it is important to test the new approach to package:

* instead of using `setup.py <https://github.com/bilardi/python-prototype/blob/unittest/setup.py>`_ file that is a legacy method
* you can use pyproject.toml to save all that information

You can see the files added or modified in this step in the commit `f131f15 <https://github.com/bilardi/python-prototype/commit/f131f15bd2219edd6e43ff99f90d5a7e83f4f873>`_.

And you can try the build by

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ python -m build

If it works, you can try to load the package on the repository testpypi

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ make buildtest

If it works, and you can load the `test page <https://test.pypi.org/project/simple-sample/1.4.0/>`_, you can try to install it on a new folder

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ make installtest

Step 4
******

Before loading the package on the official repository, it is important to commit and push all:

* not only the code
* but also the documentation
* and the version

So, after the commit with code or documentation, you can version the status of the package: according to the guide `https://semver.org/ <https://semver.org/>`_

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ make patch  # or
    $ make minor  # or
    $ make major  # or

You can see the files added or modified in this step in the commit `545b1b66 <https://github.com/bilardi/python-prototype/compare/v1.3.1...v1.4.0>`_:
it is very useful to create a version because, you can see the commits and the files involved easily.

Only when you have a new version of your package, you can push it on GitHub and you can load it on the official repository

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ make build

Step 5
******

In our refactoring, we want to move from `unittest <https://docs.python.org/3/library/unittest.html>`_ to `pytest <https://pypi.org/project/pytest/>`_ package because it is more modern and easier.

pytest can run unittest methods, but we want to simplify the tests with its syntax.

So, before we can try to run pytest

.. code-block:: bash

    $ cd python-prototype
    $ uv run pytest

It doesn't work

.. code-block:: bash

    ======================================================== test session starts ========================================================
    platform linux -- Python 3.13.3, pytest-9.0.2, pluggy-1.6.0
    rootdir: /home/bilardi/python-prototype
    configfile: pyproject.toml
    testpaths: tests
    plugins: asyncio-1.3.0, anyio-4.12.1
    asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
    collected 0 items                                                                                                                   

    ======================================================= no tests ran in 0.00s =======================================================

Because the files don't have the standard naming convention and they are not identified:

* **tests/testMyClass.py** has to be renamed to **tests/test_my_class.py** (or at least ``test_``)
* **tests/testMyClasAbstract.py** has to be renamed to **tests/test_my_class_abstract.py** (or at least ``test_``)
* **tests/testMyClassInterface.py** has to be renamed to **tests/test_my_class_interface.py** (or at least ``test_``)

Now the command ``uv run pytest`` works

.. code-block:: bash

    ======================================================== test session starts ========================================================
    platform linux -- Python 3.13.3, pytest-9.0.2, pluggy-1.6.0
    rootdir: /home/bilardi/python-prototype
    configfile: pyproject.toml
    testpaths: tests
    plugins: asyncio-1.3.0, anyio-4.12.1
    asyncio: mode=Mode.AUTO, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
    collected 10 items                                                                                                                  

    tests/test_my_class.py ......                                                                                                 [ 60%]
    tests/test_my_class_abstract.py .                                                                                             [ 70%]
    tests/test_my_class_interface.py ...                                                                                          [100%]

    ======================================================== 10 passed in 0.01s =========================================================

So, we can start to convert the syntax:

* in a big project, it is not necessary to convert
* this is only for educational purpose

We can change one file at a time, running ``uv run pytest`` each time to confirm that it works:

* tests/test_my_class_interface.py
* tests/test_my_class_abstract.py
* tests/test_my_class.py

Step 6
******

Now we can try `black <https://pypi.org/project/black/>`_

.. code-block:: bash

    $ cd python-prototype
    $ uv run black .
    reformatted /home/bilardi/python-prototype/simple_sample/myClassInterface.py
    reformatted /home/bilardi/python-prototype/simple_sample/__init__.py
    reformatted /home/bilardi/python-prototype/tests/test_my_class_abstract.py
    reformatted /home/bilardi/python-prototype/docs/source/conf.py
    reformatted /home/bilardi/python-prototype/simple_sample/myClassAbstract.py
    reformatted /home/bilardi/python-prototype/simple_sample/myClass.py

    All done! ✨ 🍰 ✨
    6 files reformatted, 3 files left unchanged.

The formatter changed

* single quotes with double quotes
* removing spaces at the end of lines
* one line break after a docstring and methods
* double line breaks after imports

You can see the files added or modified in this step in the commit `e3dd1e3 <https://github.com/bilardi/python-prototype/commit/e3dd1e32f039f0e8649783c3b4ec0662c00df280>`_.

It is a best practise to run black after a change and before a commit, or using the black extension on your IDE.

Step 7
******

Now we can try `pylint <https://pypi.org/project/pylint/>`_

.. code-block:: bash

    $ cd python-prototype
    $ uv run pylint .
      Built simple-sample @ file:///home/bilardi/python-prototype
    Uninstalled 1 package in 0.23ms
    Installed 1 package in 0.36ms
    ************* Module simple_sample.myClassInterface
    simple_sample/myClassInterface.py:4:0: C0301: Line too long (104/100) (line-too-long)
    simple_sample/myClassInterface.py:9:0: C0301: Line too long (106/100) (line-too-long)
    simple_sample/myClassInterface.py:20:0: C0301: Line too long (108/100) (line-too-long)
    simple_sample/myClassInterface.py:1:0: C0103: Module name "myClassInterface" doesn't conform to snake_case naming style (invalid-name)
    simple_sample/myClassInterface.py:23:4: C0104: Disallowed name "bar" (disallowed-name)
    simple_sample/myClassInterface.py:29:8: W0107: Unnecessary pass statement (unnecessary-pass)
    ************* Module simple_sample.myClassAbstract
    simple_sample/myClassAbstract.py:29:0: C0301: Line too long (103/100) (line-too-long)
    simple_sample/myClassAbstract.py:1:0: C0103: Module name "myClassAbstract" doesn't conform to snake_case naming style (invalid-name)
    simple_sample/myClassAbstract.py:32:4: C0104: Disallowed name "baz" (disallowed-name)
    simple_sample/myClassAbstract.py:41:4: C0104: Disallowed name "foo" (disallowed-name)
    simple_sample/myClassAbstract.py:41:18: C0104: Disallowed name "foo" (disallowed-name)
    ************* Module simple_sample.myClass
    simple_sample/myClass.py:11:0: C0301: Line too long (119/100) (line-too-long)
    simple_sample/myClass.py:19:0: C0301: Line too long (131/100) (line-too-long)
    simple_sample/myClass.py:21:0: C0301: Line too long (121/100) (line-too-long)
    simple_sample/myClass.py:1:0: C0103: Module name "myClass" doesn't conform to snake_case naming style (invalid-name)
    simple_sample/myClass.py:29:0: W0223: Method 'qux' is abstract in class 'MyClassInterface' but is not overridden in child class 'MyClass' (abstract-method)
    simple_sample/myClass.py:41:23: C0104: Disallowed name "bar" (disallowed-name)
    ************* Module conf
    docs/source/conf.py:1:0: C0114: Missing module docstring (missing-module-docstring)
    docs/source/conf.py:21:0: W0622: Redefining built-in 'copyright' (redefined-builtin)
    docs/source/conf.py:20:0: C0103: Constant name "project" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:21:0: C0103: Constant name "copyright" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:22:0: C0103: Constant name "author" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:25:0: C0103: Constant name "version" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:26:0: C0103: Constant name "release" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:29:0: C0103: Constant name "master_doc" doesn't conform to UPPER_CASE naming style (invalid-name)
    docs/source/conf.py:52:0: C0103: Constant name "html_theme" doesn't conform to UPPER_CASE naming style (invalid-name)

    -----------------------------------
    Your code has been rated at 4.35/10

You can see the files added or modified in this step in the commit `b252557 <https://github.com/bilardi/python-prototype/commit/b2525572f502f252d5417b7aa7e1f751ff8adf10>`_.

After the changes the rate improved:

.. code-block:: bash

    $ uv run pylint .
    ************* Module simple_sample.my_class
    my_class.py:32:0: W0223: Method 'qux' is abstract in class 'MyClassInterface' but is not overridden in child class 'MyClass' (abstract-method)
    my_class.py:44:23: C0104: Disallowed name "bar" (disallowed-name)
    ************* Module simple_sample.my_class_abstract
    my_class_abstract.py:33:4: C0104: Disallowed name "baz" (disallowed-name)
    my_class_abstract.py:42:4: C0104: Disallowed name "foo" (disallowed-name)
    my_class_abstract.py:42:18: C0104: Disallowed name "foo" (disallowed-name)
    ************* Module simple_sample.my_class_interface
    my_class_interface.py:9:0: C0301: Line too long (106/100) (line-too-long)
    my_class_interface.py:24:4: C0104: Disallowed name "bar" (disallowed-name)

    ------------------------------------------------------------------
    Your code has been rated at 7.94/10

It's not a given that we want to change everything pylint tells us:

* W0223, we want it to fail when ``qux`` is used in ``MyClass``
* C0301, it is a link: we can't split it
* C0104, the original classes use disallowed names: we can
    * disable **disallowed-name** control adding in pyproject.toml **disallowed-name** in the disable array
    * rename all variables with an intention-revealing name

This must be an example, so we will also change the variable names.

You can see the files added or modified in this step in the commit `e4a831e <https://github.com/bilardi/python-prototype/commit/e4a831e5ec7fa6bfae6de24995fad6c1e5516ff3>`_.

After the changes the rate improved:

.. code-block:: bash

    $ uv run pylint .
    ************* Module simple_sample.my_class
    simple_sample/my_class.py:33:0: W0223: Method 'method_with_not_implemented_error' is abstract in class 'MyClassInterface' but is not overridden in child class 'MyClass' (abstract-method)
    ************* Module simple_sample.my_class_interface
    simple_sample/my_class_interface.py:10:0: C0301: Line too long (106/100) (line-too-long)

    ------------------------------------------------------------------
    Your code has been rated at 9.41/10

If you remove from pyproject.toml "tests" from "ignore"

.. code-block:: bash

    [tool.pylint.main]
    py-version = "3.13"
    recursive = true
    ignore = [".venv", "docs"]

And you try again pylint,

.. code-block:: bash

    $ uv run pylint .
    ************* Module simple_sample.my_class
    simple_sample/my_class.py:33:0: W0223: Method 'method_with_not_implemented_error' is abstract in class 'MyClassInterface' but is not overridden in child class 'MyClass' (abstract-method)
    ************* Module simple_sample.my_class_interface
    simple_sample/my_class_interface.py:10:0: C0301: Line too long (106/100) (line-too-long)
    ************* Module tests.test_my_class_abstract
    tests/test_my_class_abstract.py:23:8: E0110: Abstract class 'MyClassAbstract' with abstract methods instantiated (abstract-class-instantiated)
    ************* Module tests.test_my_class_interface
    tests/test_my_class_interface.py:25:43: W0621: Redefining name 'mci' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class_interface.py:30:51: W0621: Redefining name 'mci' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class_interface.py:35:73: W0621: Redefining name 'mci' from outer scope (line 20) (redefined-outer-name)
    ************* Module tests.test_my_class
    tests/test_my_class.py:25:33: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class.py:30:48: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class.py:38:48: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class.py:44:50: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class.py:50:63: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)
    tests/test_my_class.py:56:49: W0621: Redefining name 'mc' from outer scope (line 20) (redefined-outer-name)

    ------------------------------------------------------------------
    Your code has been rated at 7.78/10

The warning code W0621 is because pylint and pytest are not aligned .. but it is possible to improve without disable **redefined-outer-name** `rule <https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html>`_.

.. code-block:: python

    @pytest.fixture(name="my_class")
    def mc():
        return MyClass()

    def test_my_class_can_be_created(my_class):
        assert isinstance(my_class, MyClass)

And the execution improve the rate:

.. code-block:: bash

    $ uv run pylint .
    ************* Module simple_sample.my_class
    simple_sample/my_class.py:33:0: W0223: Method 'method_with_not_implemented_error' is abstract in class 'MyClassInterface' but is not overridden in child class 'MyClass' (abstract-method)
    ************* Module simple_sample.my_class_interface
    simple_sample/my_class_interface.py:10:0: C0301: Line too long (106/100) (line-too-long)
    ************* Module tests.test_my_class_abstract
    tests/test_my_class_abstract.py:23:8: E0110: Abstract class 'MyClassAbstract' with abstract methods instantiated (abstract-class-instantiated)

    ------------------------------------------------------------------
    Your code has been rated at 9.03/10

But this change would only be to avoid the pylint warning because it doesn't recognise pytest behaviour. So it would be wrong to please it.

Is there something else better on pylint ? Well, I thought not, but I was wrong.

I started my analysis with `ruff <https://pypi.org/project/ruff/>`_ and `mypy <https://pypi.org/project/mypy/>`_.
Then I added to the research `pyright <https://pypi.org/project/pyright/>`_, `pyrefly <https://pypi.org/project/pyrefly/>`_ and `ty <https://pypi.org/project/ty/>`_.

Step 8
******

`pylint <https://pypi.org/project/pylint/>`_ is a “deep analysis” linter (static type inference). It tries to understand the class hierarchy and how objects interact with each other.

`ruff <https://pypi.org/project/ruff/>`_ is a “fast analysis” linter (based on the AST - Abstract Syntax Tree). It's incredibly fast because it analyzes individual files almost in isolation, but for this reason it struggles to "connect the dots" between a parent class in one file and a child class in another.

Currently, ruff doesn't have data flow analysis or class hierarchy analysis deep enough to know that MyClass inherits from MyClassInterface and that you forgot to implement a method.

* pylint "reads" the code almost as if it were executing it,
* while ruff reads it like structured text.

But, **ruff** replace very well **black** and it can modify the code also for *a lot of lint* cases.

You can try it with **check** as linter

.. code-block:: bash

    uv run ruff check .
    # or making explicit --fix, but in the configuration there is fix = true
    uv run ruff check --fix .

The lint issues can be resolved by

.. code-block:: bash

    uv run ruff check --unsafe-fixes .

The format issue can be resolved by

.. code-block:: bash

    uv run ruff format .

You can see the files added or modified in this step in the commits `c77f81c...babe6b3 <https://github.com/bilardi/python-prototype/compare/c77f81c...babe6b3>`_.

ruff changed

* alphabetical order of the package imports
* new line between third package imports and yours
* one point after the first line of the comment
* comments spaces management

Step 9
******

If ruff can modify the code, mypy, pyright, pyrefly and ty can't do it like pylint.

I think that all these tools are very interesting

* `mypy <https://pypi.org/project/mypy/>`_, it recognizes that
    * the empty method is not implemented
    * and the abstract class is not possible to initialize in the test_my_class_abstract.py
* `pyrefly <https://pypi.org/project/pyrefly/>`_, it recognizes that
    * the empty method has a bad return, because it should return a bool instead it is missing
    * and the abstract class is not possible to initialize in the test_my_class_abstract.py
* `ty <https://pypi.org/project/ty/>`_, it recognizes that
    * the empty method is not implemented on the interface class
    * and this method returns None though the type hinting is bool 
* `pyright <https://pypi.org/project/pyright/>`_, it recognizes that
    * the same points of ty
    * and also another point where the empty method is used in the MyClass

So pyright finds the most useful information and it is also a mature tool.
Instead pyrefly and ty are very fast, so they could be already useful for big projects, although they are young tools.

You can see the files added or modified in this step in the commit `1374bcd <https://github.com/bilardi/python-prototype/commit/1374bcd039f78dbbe4bef1ff396f1674f412def8>`_.

After the changes the rate improved:

.. code-block:: bash

    uv run pyright
    simple_sample/my_class.py:88:16 - error: Condition will always evaluate to False since the types "bool"
    and "None" have no overlap (reportUnnecessaryComparison)
    simple_sample/my_class_interface.py:27:30 - error: Function with declared return type "bool" must return value on all code paths 
    "None" is not assignable to "bool" (reportReturnType)
    2 errors, 0 warnings, 0 informations

Step 10
*******

If we want to run ruff and pytest always before a commit, it could be useful to configure a `pre-commit <https://pre-commit.com/>`_ action.

You can configure a git-hook in ``.git/hooks/pre-commit`` with the command ``pre-commit install`` because

* you have already installed the dependencies with `how to make <https://simple-sample.readthedocs.io/en/latest/howtomake.html>`_,
* you have the file ``.pre-commit-config.yaml``

When you try to do a ``git-commit``, git will run for you ruff and pytest.

If you want to try it before, you can run the command,

.. code-block:: bash

    pre-commit run
    ruff-check...............................................................Passed
    ruff-format..............................................................Passed
    pytest...................................................................Passed

If the step fails, the pre-commit package tells you where and why: for example, if you have not committed as in this example

.. code-block:: bash

    pre-commit run
    [WARNING] Unstaged files detected.
    ruff-check...............................................................Passed
    ruff-format..............................................................Failed
    - hook id: ruff-format
    - files were modified by this hook

    2 files reformatted, 6 files left unchanged

    pytest...................................................................Passed

Step 11
*******

Before the refactoring, the dev dependencies were listed in ``tests/requirements-test.txt``:

.. code-block:: bash

    build
    bump-my-version
    git-cliff
    httpx
    pre-commit
    pyright
    pytest
    pytest-asyncio
    ruff
    twine

With `uv <https://pypi.org/project/uv/>`_ and the new `dependency groups <https://peps.python.org/pep-0735/>`_ (PEP 735), the same list lives directly in ``pyproject.toml``. You can migrate the requirements file in one command:

.. code-block:: bash

    $ uv add --dev -r tests/requirements-test.txt

``uv`` reads the requirements file, resolves the versions, writes a ``[dependency-groups]`` section in ``pyproject.toml``, updates ``uv.lock`` and installs everything in ``.venv/``. After this, ``tests/requirements-test.txt`` is redundant and can be removed.

.. note::

    The command fails if ``requires-python`` in ``pyproject.toml`` is lower than what any dev tool requires. In this project, ``git-cliff`` needs Python >= 3.7, while the original ``requires-python = ">=3.6"`` was a pre-refactoring leftover. Align ``requires-python`` to the target version (``>=3.13`` here, matching `target-version <https://docs.astral.sh/ruff/settings/#target-version>`_ for ruff and `pythonVersion <https://microsoft.github.io/pyright/#/configuration?id=main-configuration-options>`_ for pyright) before running ``uv add``.

The same pattern applies to `sphinx <https://pypi.org/project/sphinx/>`_ and its theme, needed to build this documentation. They are added as dev deps in the same way:

.. code-block:: bash

    $ uv add --dev sphinx sphinx_rtd_theme

The Sphinx-generated ``docs/Makefile`` expects a ``sphinx-build`` in the ``PATH``. To make ``make doc`` work without activating the venv, the ``doc`` target in the project ``Makefile`` overrides the ``SPHINXBUILD`` variable with ``uv run sphinx-build``:

.. code-block:: make

    doc:
    	cd docs; make html SPHINXBUILD="uv run sphinx-build"; cd -

This way the binary is resolved through ``uv run`` without touching the auto-generated ``docs/Makefile``.

The story is not finished at local ``make doc``: `Read the Docs <https://readthedocs.org/>`_ builds the documentation on its own infrastructure, and needs to know how to install the dev dependencies before running Sphinx. Without a configuration file, the build on Read the Docs fails (release 1.5.1 failed for this reason).

The file ``.readthedocs.yaml`` in the project root tells Read the Docs which Python version to use, how to install dependencies with ``uv`` and where ``conf.py`` lives. The key entry is ``python.install.method: uv`` with ``command: sync`` and ``groups: [dev]``: this uses the native Read the Docs integration (`docs <https://docs.readthedocs.com/platform/stable/config-file/v2.html>`_) to run ``uv sync --group dev`` on their build machine, the same command that works locally, without ``pip install uv`` workarounds in ``build.jobs``.

Step 12
*******

After tagging a release on GitHub (`Step 4`_), the next step is to publish the package on `PyPI <https://pypi.org/>`_. Before uploading to the production index, it is a good practice to test the upload on `TestPyPI <https://test.pypi.org/>`_: same API and flow, but a separate index for experiments.

The Makefile has four targets for this workflow:

.. code-block:: bash

    $ make buildtest  # build the wheel and upload to TestPyPI
    $ make installtest  # install the package from TestPyPI in a sandbox venv and verify the import
    $ make build  # build the wheel and upload to PyPI
    $ make install  # install the package from PyPI in a sandbox venv and verify the import

All four targets prefix ``uv run`` for the build and twine commands, so they work without activating the project venv.

The ``installtest`` and ``install`` targets use a throwaway venv (``.installtest/`` or ``.install/``) so that the install is tested end-to-end:

* create a clean venv with ``uv venv --clear``
* install the package in that venv with ``uv pip install --python ...``, downloading the wheel from (Test)PyPI
* verify the import by printing the version with ``python -c "import ..."``
* delete the venv

Without the sandbox venv, ``uv pip install`` would just audit the already-installed editable version in the project ``.venv/`` and download nothing from (Test)PyPI.

Conclusion
##########

You have completed the refactoring of the package: the codebase now uses ``pyproject.toml`` (with `dependency-groups <https://peps.python.org/pep-0735/>`_), ``pytest``, ``ruff``, ``pyright`` and ``pre-commit``.

Every time you finish a class with its unit test, you can:

* release with ``make patch`` / ``make minor`` / ``make major`` (see `Step 4`_): updates ``CHANGELOG.md``, bumps the version, pushes commit and tag in one step
* publish on TestPyPI with ``make buildtest`` and verify with ``make installtest`` (see `Step 12`_)
* publish on PyPI with ``make build`` when the release is stable
