How to use
==========

In this section you can find some tips & tricks for learning to use any code.

For the full story of the refactoring from ``unittest`` / ``setup.py`` to ``pytest`` / ``pyproject.toml``, see the `refactoring <https://simple-sample.readthedocs.io/en/latest/refactoring.html>`_ page.

Unit tests
##########

The branch ``unittest`` keeps the package state before the refactoring, so you can run the original tests with the Python standard library.

When you change something on your code, you can run one unit test about the class you changed:

.. code-block:: bash

    $ cd python-prototype
    $ git fetch origin
    $ git checkout unittest
    $ python3 -m unittest -v tests/testMyClass.py

And when you are ready for the commit, you can run all unit tests:

.. code-block:: bash

    $ cd python-prototype
    $ git checkout unittest
    $ python3 -m unittest discover -v

To learn how to use a class in your code, read its unit test file: you find the import, the initialization, and the main public methods.

PyTest
######

On the branch ``master``, the tests use `pytest <https://pypi.org/project/pytest/>`_.
Unlike ``unittest``, pytest is a third-party library, so you need to install the dependencies first:

.. code-block:: bash

    $ cd python-prototype
    $ git checkout master
    $ uv sync
    $ uv run pytest tests/test_my_class.py

And for running all tests:

.. code-block:: bash

    $ uv run pytest

Documentation
#############

Another approach is to read the documentation in the class file. When you install a package, you can also read its documentation by shell:

.. code-block:: bash

    $ python3
    >>> import simple_sample
    >>> print(simple_sample.__doc__)  # description like overview of the package
    >>> help(simple_sample)  # description of the package contents, and if there are, classes and functions
    >>> quit()

In the description, you can find an example for a command that you can use for each package element:

.. code-block:: bash

    $ python3
    >>> import simple_sample.my_class
    >>> print(simple_sample.my_class.__doc__)  # description like overview of the element
    >>> help(simple_sample.my_class)  # description of the element contents: classes and functions
    >>> quit()

If there are more classes in a package element, you can import a specific class to read all its methods:

.. code-block:: bash

    $ python3
    >>> from simple_sample.my_class import MyClass
    >>> print(MyClass.__doc__)  # description like overview of the class
    >>> help(MyClass)  # description of the class contents: methods, and if there are, functions
    >>> quit()

MyClass
#######

The previous approaches are the best practice for learning something about a specific package.

Sometimes, the package is so complex, that it is also necessary a "Quick start" where a developer can learn the main classes or methods to start from:

.. code-block:: bash

    $ python3
    >>> from simple_sample.my_class import MyClass
    >>> mc = MyClass()  # initialization with or without boolean argument
    >>> mc.get_param_processing(True)  # returns the reverse value of the argument
    >>> mc.get_boolean()  # returns the boolean initialized
    >>> mc.get_reverse_protected_param()  # returns the reverse value of the boolean initialized
    >>> quit()
