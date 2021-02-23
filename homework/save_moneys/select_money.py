#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 16:56
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : select_money.py
# @software: PyCharm

import money


# 查询工资
def select():
    if money.saved_money == 2000:
        print("收到工资，很开心！")
    else:
        print("没发工资")
