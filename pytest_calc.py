#!/user/bin/env python
# -*- coding:utf-8 -*-
import yaml
import pytest

with open('./datas/calc.yaml')as test_data:
    datas = yaml.safe_load(test_data)['datas']
    add_datas = datas['add']
    sub_datas = datas['sub']
    mul_datas = datas['mul']
    div_datas = datas['div']

@pytest.fixture(params=add_datas)
def get_add_datas(request):
    data = request.param
    return data

@pytest.fixture(params=sub_datas)
def get_sub_datas(request):
    data = request.param
    return data

@pytest.fixture(params=mul_datas)
def get_mul_datas(request):
    data = request.param
    return data

@pytest.fixture(params=div_datas)
def get_div_datas(request):
    data = request.param
    return data

class TestCalc:

    @pytest.mark.run(ordder=1)
    def test_add(slef,init_calc,get_add_datas):
        result = init_calc.add(get_add_datas[0],get_add_datas[1])
        expect = get_add_datas[2]
        assert result == expect

    @pytest.mark.run(ordder=2)
    def test_sub(slef,init_calc,get_sub_datas):
        result = init_calc.sub(get_sub_datas[0],get_sub_datas[1])
        expect = get_sub_datas[2]
        assert result == expect

    @pytest.mark.run(ordder=3)
    def test_mul(slef, init_calc, get_mul_datas):
        result = init_calc.mul(get_mul_datas[0], get_mul_datas[1])
        expect = get_mul_datas[2]
        assert result == expect

    @pytest.mark.run(ordder=4)
    def test_div(slef, init_calc, get_div_datas):
        result = init_calc.div(get_div_datas[0], get_div_datas[1])
        expect = get_div_datas[2]
        assert result == expect