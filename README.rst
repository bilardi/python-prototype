Python prototype
================

This package contains a simple sample of a Python package prototype.
It is part of the `educational repositories <https://github.com/pandle/materials>`_ to learn how to write stardard code and common uses of the TDD.

See the documentation and how to do it on `readthedocs <https://simple-sample.readthedocs.io/en/latest/>`_.
And see the development of this code step by step

* with `see-git-steps <https://github.com/bilardi/see-git-steps>`_ on `readthedocs / step by step <https://simple-sample.readthedocs.io/en/latest/stepbystep.html>`_
    * this page is old style: you can learn the concepts about to create before unit test and then the code
    * but now a Python package is handled differently 
* you can find the refactoring on  `readthedocs / refactoring <https://simple-sample.readthedocs.io/en/latest/refactoring.html>`_

Installation
###############

The package is self-consistent. So you can download the package by github:

.. code-block:: bash

    $ git clone https://github.com/bilardi/python-prototype

Or you can install by python3-pip:

.. code-block:: bash

    $ pip3 install simple_sample

Usage
#####

Read the unit tests in `tests/testMyClass.py <https://github.com/bilardi/python-prototype/blob/master/tests/testMyClass.py>`_ file to use it. This is a best practice.
You can read also the documentation by command line,

.. code-block:: bash

    $ python3
    >>> from simple_sample.myClass import MyClass
    >>> print(MyClass.__doc__)
    >>> help(MyClass)
    >>> quit()

If you want to see the local documentation, that you have downloaded by github, you can use the same steps but before you must to change the directory

.. code-block:: bash

    $ cd python-prototype

Development
###########

It is common use to test the code step by step and unittest module is a good beginning for unit test and functional test.

With the need to mock so many libraries that call external APIs, the need arose to use simpler test libraries for this part, such as pytest.

* you can find tests with unittest module on `Unit tests <https://simple-sample.readthedocs.io/en/latest/howtouse.html#unit-tests>`_ section
* you can find tests with pytest module on `PyTest <https://simple-sample.readthedocs.io/en/latest/howtouse.html#pytest>`_ section

Change Log
##########

See `CHANGELOG.md <https://github.com/bilardi/python-prototype/blob/master/CHANGELOG.md>`_ for details.
This file is updated by `Makefile <https://github.com/bilardi/python-prototype/blob/master/Makefile>`_ command:

```sh
make changelog
```

You can find the versioning management on  `readthedocs / versioning <https://simple-sample.readthedocs.io/en/latest/versioning.html>`_,
because before to run the make command, you have to install dependences by `readthedocs / howtomake <https://simple-sample.readthedocs.io/en/latest/howtomake.html>`_ guide.

License
#######

This package is released under the MIT license.  See `LICENSE <https://github.com/bilardi/python-prototype/blob/master/LICENSE>`_ for details.
