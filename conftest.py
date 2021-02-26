#!/user/bin/env python
# -*- coding:utf-8 -*-
from pytest_test.pytest_shizhan.python_code.daic import Calculator
import pytest

@pytest.fixture(scope='module')
def init_calc():
    print('开始计算')
    calc = Calculator()
    yield(calc)
    print('计算结束')