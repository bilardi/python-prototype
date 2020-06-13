Step by step
============================

This page is for learning all steps that they are necessary for writing a simple package like simple-sample.

see-git-steps
#############

The package `see-git-steps <https://github.com/bilardi/see-git-steps>`_ has been written for reading piece by piece the commits of a git repository.

If you want to use it, you have to install it following its README.md.

Getting started
###############

The goal of the package simple-sample is to create a Python package prototype. 
So you can use this simple package for downloading a base for your package.

Step 1
******

The first step is to add all the outline files for your package

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps
    6248c90ca6fb91758524addf69a4a179c06baf3d step 1 - add the outline files
    .gitignore
    CHANGELOG.md
    LICENSE
    MANIFEST.in
    Makefile
    README.rst
    setup.py

They are important files and below you can find a link of a guide for each file

* `.gitignore <https://git-scm.com/docs/gitignore>`_, to ignore specific files when you have to commit
* `CHANGELOG.md <https://keepachangelog.com/en/1.0.0/>`_, the  best practise for reading the minor o major change of your code
* `LICENSE <https://help.github.com/en/github/building-a-strong-community/adding-a-license-to-a-repository>`_, the best practise for defining your policy for the public repository
* `MANIFEST.in <https://packaging.python.org/guides/using-manifest-in/>`_, documentation included into your package
* `Makefile <https://www.gnu.org/software/make/manual/make.html>`_, it is not necessary but it is a comfortable way to remember procedures
* `README.rst <https://en.wikipedia.org/wiki/ReStructuredText>`_, documentation visible on your repository homepage
* `setup.py <https://docs.python.org/3/distutils/setupscript.html>`_, it is a best practise for creating or installing your package

The files that you have to customize are

* **.gitignore**, for example, if you use an ide with specific files extension
* **LICENSE**, with year and your name
* **Makefile**, with your PACKAGE_NAME and YOUR_USERNAME of `PyPI <https://pypi.org/>`_
* **README.rst**, with your quick start documentation
* **setup.py**, where you find some variables: name, author, author_email, description and urls

When you have modified, you can commit your first change

.. code-block:: bash

    $ cd python-prototype
    $ git init # for initializing the repository
    $ git add .gitignore CHANGELOG.md LICENSE MANIFEST.in Makefile README.rst setup.py
    $ git commit -m "step 1 - add the outline files"

Step 2
******

The second step is to add the first files that you need for creating your package

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps
    57e2d766fbdea1d6a3862676f6f3a28e5ab5746c step 2 - add the empty package version
    setup.py
    simple_sample/__init__.py
    tests/__init__.py

The files `__init__.py <https://docs.python.org/3/reference/import.html#regular-packages>`_ are the base of a regular package.

It can be empty, like **tests/__init__.py**, and it will say anyway that folder is a package.

It can contain some code, like `simple_sample/__init__.py <https://github.com/bilardi/python-prototype/simple_sample/__init__.py>`_, and it is sufficient for importing it in setup.py for recovering author and version of the package.

See the changes of **setup.py** by `GitHub <https://github.com/bilardi/python-prototype/commit/57e2d766fbdea1d6a3862676f6f3a28e5ab5746c>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c 57e2d766fbdea1d6a3862676f6f3a28e5ab5746c -v

When you have modified **setup.py** and added the new files, you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add setup.py tests/__init__.py simple_sample/__init__.py
    $ git commit -m "step 2 - add the empty package version"

Step 3
******

Before write code, it is important to verbalize the concepts by documentation:
so the documentation is important to learn a package as to plan how to write the code.

You can write your documentation as you want: you can create docs folder like in this package, by `sphinx <https://simple-sample.readthedocs.io/en/latest/howtomake.html#documentation>`_.

When you have created your documentation, you can add the new folder and you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add docs
    $ git commit -m "step 3 - add documentation by sphinx"

When a commit completes one feature or a set of fixies, you can tag that commit as a release.
The standard behaviour is to add changes in a CHANGELOG file: see the changes of **CHANGELOG.md** by `GitHub <https://github.com/bilardi/python-prototype/commit/20b91ae691f29c96059dc3d3b355ab7c91eb9928>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c 20b91ae691f29c96059dc3d3b355ab7c91eb9928 -v | head -n 21

So you can add CHANGELOG.md on your last commit, or you can create one commit for changelog, and then you can add the tag.

.. code-block:: bash

    $ cd python-prototype
    $ git add CHANGELOG.md
    $ git commit --amend # add file on your last commit
    $ git tag -d v0.0.1 -m "Empty package and documentation by sphinx" # create a tag with that version name
    $ git tag -n # show the tag list with description
    $ git push origin --tags # load the tag on repository

Step 4
******

Before write code, it is important to verbalize the methods by create Test Driven Development (TDD) for your code.
Then, it is important to use unit test for finding the issues and before to update change log file and package version.

In Python, a standard TDD is offered by unittest module: see the unit tests of MyClassInterface by `GitHub <https://github.com/bilardi/python-prototype/commit/b31157739997841621968440f970778059a41946>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c b31157739997841621968440f970778059a41946 -v

In Python, the interface is not necessary, but this is a simple sample with a bit of everything.
The MyClassInterface will have only 2 methods not defined in two different ways: one using **pass** and one using **raise**.

When you have created **tests/testMyClassInterface.py** and added the new file, you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add tests/testMyClassInterface.py
    $ git commit -m "step 4 - add the unit test for MyClassInterface"

Step 5
******

Now you can write your first class: see MyClassInterface by `GitHub <https://github.com/bilardi/python-prototype/commit/31b35d60e49878aa01fd8d7d6c47200d8696523b>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c 31b35d60e49878aa01fd8d7d6c47200d8696523b -v

When you have created **simple_sample/myClassInterface.py**, you can run the unit tests of MyClassInterface

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m unittest discover -v
    test_my_class_interface_can_be_created (tests.testMyClassInterface.TestMyClassInterface) ... ok
    test_my_class_interface_gets_bar_value (tests.testMyClassInterface.TestMyClassInterface) ... ok
    test_my_class_interface_gets_qux_value (tests.testMyClassInterface.TestMyClassInterface) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

It is a best practise to run unit tests after a change and before a commit.
If the result is like the example (all tests are OK), you can add the new file and you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add simple_sample/myClassInterface.py
    $ git commit -m "step 5 - add MyClassInterface and unit tests works properly"

Step 6
******

If you need to use a framework, abstract class is a good method. The peculiarity of this is that it cannot be imported.
So the unit tests are simple: see the unit tests of MyClassAbstract by `GitHub <https://github.com/bilardi/python-prototype/commit/fcec3fca61c7860a63969c6b6e56d951ab187489>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c fcec3fca61c7860a63969c6b6e56d951ab187489 -v

When you have created **tests/testMyClassAbstract.py** and added the new file, you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add tests/testMyClassAbstract.py
    $ git commit -m "step 6 - add the unit test for MyClassAbstract"

Step 7
******

Now you can write your second class: see MyClassAbstract by `GitHub <https://github.com/bilardi/python-prototype/commit/ddb120bd0c14528b0c8b0caf223b387588725c50>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c ddb120bd0c14528b0c8b0caf223b387588725c50 -v

When you have created **simple_sample/myClassAbstract.py**, you can run all unit tests like the command of step 5, or you can run only the unit tests of MyClassAbstract

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m unittest -v tests/testMyClassAbstract.py
    test_my_class_abstract_can_be_created (tests.testMyClassAbstract.TestMyClassAbstract) ... ok

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

If the test is OK, you can add the new file and you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add simple_sample/myClassAbstract.py
    $ git commit -m "step 7 - add MyClassAbstract and unit tests works properly"

Step 8
******

Now you can write the unit tests for a class can extend the interface class and the abstract class: note that it has been also added a unit test for the public method of the abstract class.
See the unit tests of MyClass by `GitHub <https://github.com/bilardi/python-prototype/commit/d78aacd6f3ef99d119b8ceb45d2378b1344d5f27>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c d78aacd6f3ef99d119b8ceb45d2378b1344d5f27 -v

When you have created **tests/testMyClass.py** and added the new file, you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add tests/testMyClass.py
    $ git commit -m "step 8 - add the unit test for MyClass"

Step 9
******

After verbalizing all MyClass methods by the unit tests, you are ready to write the methods: see MyClass by `GitHub <https://github.com/bilardi/python-prototype/commit/84ce869d3ea3c5737d99b7b596be3fe4b3d826a4>`_ or by command line with see-git-steps

.. code-block:: bash

    $ cd python-prototype
    $ see-git-steps -c 84ce869d3ea3c5737d99b7b596be3fe4b3d826a4 -v

When you have created **simple_sample/myClass.py**, you can run all unit tests

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m unittest discover -v
    test_my_class_can_be_created (tests.testMyClass.TestMyClass) ... ok
    test_my_class_gets_bar_value (tests.testMyClass.TestMyClass) ... ok
    test_my_class_gets_baz_value (tests.testMyClass.TestMyClass) ... ok
    test_my_class_gets_foo_value (tests.testMyClass.TestMyClass) ... ok
    test_my_class_gets_fooquux_value (tests.testMyClass.TestMyClass) ... ok
    test_my_class_gets_qux_value (tests.testMyClass.TestMyClass) ... ok
    test_my_class_abstract_can_be_created (tests.testMyClassAbstract.TestMyClassAbstract) ... ok
    test_my_class_interface_can_be_created (tests.testMyClassInterface.TestMyClassInterface) ... ok
    test_my_class_interface_gets_bar_value (tests.testMyClassInterface.TestMyClassInterface) ... ok
    test_my_class_interface_gets_qux_value (tests.testMyClassInterface.TestMyClassInterface) ... ok

    ----------------------------------------------------------------------
    Ran 10 tests in 0.001s

    OK

If all test is OK, you can add the new file and you can commit your changes

.. code-block:: bash

    $ cd python-prototype
    $ git add simple_sample/myClass.py
    $ git commit -m "step 9 - add MyClass and unit tests works properly"

Step 10
******

To be continued ..