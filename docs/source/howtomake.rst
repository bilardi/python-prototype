How to make
===========

In this section you can find how to generate or publish that helps you with managing your code.

Virtual environment
###################

When you have to install specific requirements.txt, you can use a `virtual environment <https://docs.python.org/3/tutorial/venv.html>`_: this method is important to test different packages versions without to install them on your local.

The main commands are

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m venv .env # create virtual environment
    $ source .env/bin/activate # enter in the virtual environment
    $ pip install --upgrade -r requirements.txt # install your dependences
    $ deactivate # exit when you will have finished the job
    $ rm -rf .env # remove the virtual environment it is a best practice

Documentation
#############

The Python language is permissive, but if you use a basic documentation like `Python Enhancement Proposals 8 <https://www.python.org/dev/peps/pep-0008/>`_ (PEP-8) and unit / functional test, everyone can easily read your code. There are many style to write `Python documentation <https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format>`_. 

If you load your package on `GitHub <https://github.com/>`_, `GitLab <https://gitlab.com/>`_, or `BitBucket <https://bitbucket.org/>`_, you can also use `sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html>`_ for creating docs folder like in this package. It can help you to organize concepts in an unique place without duplicates: the README.rst is the homepage on Github and Pypi repositories and it is also one of these pages (see `overview.rst <https://simple-sample.readthedocs.io/en/latest/overview.html>`_). 

The main commands for building documentation are

.. code-block:: bash

    $ pip3 install sphinx
    $ pip3 install sphinx_rtd_theme # it is necessary only if you want the theme sphinx_rtd_theme
    $ cd python-prototype/docs/
    $ sphinx-quickstart
    $ make html

And you can open build/html/index.html in your web browser to see your docs.

Instead, for uploading documentation on readthedocs, you have to follow `this guide <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.

TDD
###

Before write code, it is important to verbalize the concepts by documentation and to create Test Driven Development (TDD) for your code. Then, it is important to use unit test for finding the issues and before to update change log file and package version.

See the development of this code step by step on `readthedocs / step by step <https://simple-sample.readthedocs.io/en/latest/stepbystep.html>`_ for learning how to make a unit test.

Packaging
#########

The tutorial for `packaging your projects <https://packaging.python.org/tutorials/packaging-projects/>`_ is standard. And then your package is public on `PyPI <https://pypi.org/>`_.

The main commands for testing are

.. code-block:: bash

    $ rm -rf build dist *.egg-info
    $ python3 setup.py sdist bdist_wheel # create source archive
    $ python3 -m twine upload --repository testpypi dist/* # upload source archive on testpypi
    $ python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps simple-sample-bilardi # install package from testpypi

The main commands for the production environment are

.. code-block:: bash

    $ rm -rf build dist *.egg-info
    $ python3 setup.py sdist bdist_wheel # create source archive
    $ python3 -m twine upload dist/* # upload source archive on pypi
    $ python3 -m pip install simple-sample # install package from pypi
    $ pip3 install simple-sample # slim command for installing the package
