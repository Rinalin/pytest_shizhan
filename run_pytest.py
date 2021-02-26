#!/user/bin/env python
# -*- coding:utf-8 -*-
import pytest
import os

if __name__ =='__main__':
    command_line = ['-s','./pytest_calc.py','--alluredir=./result/1']
    pytest.main(command_line)
    os.system ('allure generate ./result/1 -o ./report/1 --clean' )
