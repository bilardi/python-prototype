"""An example of interface class.

An example of interface class, but interfaces are not necessary in Python.
There are two examples of methods without implementation:
bar returns None and qux returns an exception.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details
# cite https://stackoverflow.com/questions/2124190/how-do-i-implement-interfaces-in-python/2124415#2124415

Interfaces are not necessary in Python. This is because Python has proper multiple inheritance,
and also ducktyping, which means that the places where you must have interfaces in Java,
you don't have to have them in Python.
"""


class MyClassInterface:
    """An example of interface class.

    Interfaces are not necessary in Python.
    There are two examples of methods without implementation:
    get_boolean returns None
    and method_with_not_implemented_error returns an exception.
    """

    def get_boolean(self) -> bool:
        """Get boolean.

        Method without implementation

        Returns:
            A boolean value
        """

    def method_with_not_implemented_error(self) -> bool:
        """Not implemented method.

        Returns:
            A boolean value
        """
        raise NotImplementedError
