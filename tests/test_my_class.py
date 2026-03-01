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
from simple_sample.myClass import MyClass


@pytest.fixture
def mc():
    return MyClass()


def test_my_class_can_be_created(mc):
    """Verifies if the class MyClass can be created"""
    assert isinstance(mc, MyClass)


def test_my_class_gets_bar_value(mc):
    """Verifies if the class MyClass gets the bar value correctly"""
    assert mc.bar()

    assert MyClass(True).bar()
    assert not MyClass(False).bar()


def test_my_class_gets_baz_value(mc):
    """Verifies if the class MyClass gets the baz value correctly"""
    for _ in range(10):
        assert mc.baz() in [True, False]


def test_my_class_gets_foo_value(mc):
    """Verifies if the class MyClass gets the foo value correctly"""
    assert not mc.foo(True)
    assert mc.foo(False)


def test_my_class_gets_qux_value(mc):
    """Verifies if the class MyClass qux method raises an exception"""
    with pytest.raises(NotImplementedError):
        mc.qux()


def test_my_class_gets_fooquux_value(mc):
    """Verifies if the class MyClass gets the fooquux value correctly"""
    for _ in range(10):
        assert mc.fooquux() in [True, False]
