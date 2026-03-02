"""An example of class

An example of class that it extends an abstract class and it implements an interface.
There is a boolean pun by not_implemented_and_abstract_method function of abstract class,
get_boolean function of interface class,
and foobar function of this class.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details

Note that the _quux method is not present in the documentation like the other methods because
it is a method protected.

    >>> from simple_sample.my_class import MyClass
    >>> help(MyClass)

# cite https://stackoverflow.com/questions/11483366/protected-method-in-python/11483397#11483397

Python does not support access protection as C++/Java/C# does. Everything is public.
The motto is, "We're all adults here." Document your classes, and insist that your collaborators
read and follow the documentation.
The culture in Python is that names starting with underscores mean,
"don't use these unless you really know you should."
You might choose to begin your "protected" methods with underscores.
But keep in mind, this is just a convention, it doesn't change how the method can be accessed.
"""

from simple_sample.my_class_interface import MyClassInterface
from simple_sample.my_class_abstract import MyClassAbstract


class MyClass(MyClassInterface, MyClassAbstract):
    """
    An example of class that it extends an abstract class and it implements an interface.
    There is a boolean pun by not_implemented_and_abstract_method function of abstract class,
    get_boolean function of interface class,
    and foobar function of this class.
        Args:
            param(bool): a boolean value
    """

    # param(bool): a class boolean variable with default True
    _protected_param = True

    def __init__(self, param=True):
        """
        Initialization of variables
            Args:
                param(bool): a boolean value
        """
        self._protected_param = param

    def get_param_processing(self, param):
        """
        Override of the abstract method gets reverse value of param
            Args:
                param(bool): a boolean value
            Returns:
                The reverse value of param
        """
        return not param

    def get_boolean(self):
        """
        Method override of the class MyClassInterface
            Returns:
                The boolean value of _protected_param
        """
        return self._protected_param

    def get_reverse_protected_param(self):
        """
        Gets reverse value of _protected_param
            Returns:
                The reverse value of _protected_param
        """
        return self.get_param_processing(self._protected_param)

    def _protected_method(self):
        """
        Protected method recalls some methods
            Returns:
                The boolean value
        """
        try:
            if MyClassInterface.get_boolean(self) is None:
                MyClassInterface.method_with_not_implemented_error(self)
        except NotImplementedError:
            return self.get_random_boolean()
        return True

    def get_reverse_boolean(self):
        """
        Gets reverse value of the protected method _protected_method
            Returns:
                The boolean value
        """
        return self.get_param_processing(self._protected_method())
