"""Test class of MyClassAbstract

This is a basic unit test class.
It is not possible to instantiate a class with an abstract method,
so missing the method for testing the other method.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details
"""

import pytest
from simple_sample.myClassAbstract import MyClassAbstract


def test_my_class_abstract_can_be_created():
    """Verifies if the class MyClassAbstract raises an exception"""
    with pytest.raises(TypeError):
        MyClassAbstract()
