"""Test class of MyClassInterface

There are basic unit tests. There is a test for each public function.
If the functions contained conditions, there would be more tests for each public function.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details

Only with unittest we need a class: pytest works with methods.

$ uv run pytest
"""

import pytest
from simple_sample.my_class_interface import MyClassInterface


@pytest.fixture
def mci():
    """Instantiates the class"""
    return MyClassInterface()


def test_my_class_interface_can_be_created(mci):
    """Verifies if the class MyClassInterface can be created"""
    assert isinstance(mci, MyClassInterface)


def test_my_class_interface_gets_get_boolean_value(mci):
    """Verifies if the class MyClassInterface get_boolean method return None"""
    assert mci.get_boolean() is None


def test_my_class_interface_gets_method_with_not_implemented_error_value(mci):
    """Verifies if the class MyClassInterface
    method_with_not_implemented_error method raises an exception"""
    with pytest.raises(NotImplementedError):
        mci.method_with_not_implemented_error()
