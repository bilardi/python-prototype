"""Test class of MyClassAbstract

There are basic unit tests.
It is not possible to instantiate a class with an abstract method,
so missing the method for testing the other method.

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/python-prototype for details

Only with unittest we need a class: pytest works with methods.

$ uv run pytest
"""

import pytest

from simple_sample.my_class_abstract import MyClassAbstract


def test_my_class_abstract_can_be_created():
    """Verifies if the class MyClassAbstract raises an exception"""
    with pytest.raises(TypeError):
        MyClassAbstract()
