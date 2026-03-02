"""Test class of MyClass

There are basic unit tests. There is a test for each public function.
If the functions contained conditions, there would be more tests for each public function.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details

Only with unittest we need a class: pytest works with methods.

$ uv run pytest
"""

import pytest
from simple_sample.my_class import MyClass


@pytest.fixture
def mc():
    """Instantiates the class"""
    return MyClass()


def test_my_class_can_be_created(mc):
    """Verifies if the class MyClass can be created"""
    assert isinstance(mc, MyClass)


def test_my_class_gets_method_get_boolean_value(mc):
    """Verifies if the class MyClass gets the get_boolean value correctly"""
    assert mc.get_boolean()

    assert MyClass(True).get_boolean()
    assert not MyClass(False).get_boolean()


def test_my_class_gets_get_random_boolean_value(mc):
    """Verifies if the class MyClass gets the get_random_boolean value correctly"""
    for _ in range(10):
        assert mc.get_random_boolean() in [True, False]


def test_my_class_gets_get_param_processing_value(mc):
    """Verifies if the class MyClass gets the get_param_processing value correctly"""
    assert not mc.get_param_processing(True)
    assert mc.get_param_processing(False)


def test_my_class_gets_method_with_not_implemented_error_value(mc):
    """Verifies if the class MyClass method_with_not_implemented_error method raises an exception"""
    with pytest.raises(NotImplementedError):
        mc.method_with_not_implemented_error()


def test_my_class_gets_get_reverse_boolean_value(mc):
    """Verifies if the class MyClass gets the get_reverse_boolean value correctly"""
    for _ in range(10):
        assert mc.get_reverse_boolean() in [True, False]
