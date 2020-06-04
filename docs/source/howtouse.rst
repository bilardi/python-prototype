How to use
==========

In this section you can find some tips & tricks for learning to use any code.

Unit tests
##########

When you change something on your code, you can run one unit test about that class changed

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m unittest -v tests/testMyClass.py

And when you are ready for the commit, you can use a command for running all unit tests

.. code-block:: bash

    $ cd python-prototype
    $ python3 -m unittest discover -v

But for learning how to use an class in your code, you need to read its unit test file.
You can find the import class, the initialization class, and the main public methods.

Documentation
#############

Another approach is to read the documentation in the class file. When you install a package, you can also read its documentation by shell

.. code-block:: bash

    $ python3
    >>> import simple_sample
    >>> print(simple_sample.__doc__) # description like overview of the package
    >>> help(simple_sample) # description of the package contents, and if there are, classes and functions
    >>> quit()

In the description, you can find an example for a command that you can use for each package element

.. code-block:: bash

    $ python3
    >>> import simple_sample.myClass
    >>> print(simple_sample.myClass.__doc__) # description like overview of the element
    >>> help(simple_sample.myClass) # description of the element contents: classes and functions
    >>> quit()

If there are more classes in an package element, you can import a specific class where to read all methods

.. code-block:: bash

    $ python3
    >>> from simple_sample.myClass import MyClass
    >>> print(MyClass.__doc__) # description like overview of the class
    >>> help(MyClass) # description of the class contents: methods, and if there are, functions
    >>> quit()

MyClass
#######

The precedent approches are the best practice for learning something about a specific package.

Sometimes, the package is so complex, that it is also necessary a "Quick start" where a developer can learn the main classes or methods to start from

.. code-block:: bash

    $ python3
    >>> from simple_sample.myClass import MyClass
    >>> mc = MyClass() # initialization with or without boolean argument
    >>> mc.foo(True); # returns the reverse value
    >>> mc.bar(); # returns the boolean initialized
    >>> mc.foobar(); # returns the reverse value of the boolean initialized
    >>> quit()
    
