"""Test class of MyClassInterface

This is a basic unit test class. There is a test for each public function.
If the functions contained conditions, there would be more tests for each public function.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details
"""

import pytest
from simple_sample.myClassInterface import MyClassInterface


@pytest.fixture
def mci():
    return MyClassInterface()


def test_my_class_interface_can_be_created(mci):
    """Verifies if the class MyClassInterface can be created"""
    assert isinstance(mci, MyClassInterface)


def test_my_class_interface_gets_bar_value(mci):
    """Verifies if the class MyClassInterface bar method return None"""
    assert mci.bar() is None


def test_my_class_interface_gets_qux_value(mci):
    """Verifies if the class MyClassInterface qux method raises an exception"""
    with pytest.raises(NotImplementedError):
        mci.qux()
