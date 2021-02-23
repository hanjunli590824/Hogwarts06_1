#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 13:50
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : sent.py
# @software: PyCharm

# from...import...与import...区别：
# 1.from...import...是复制了一份到本地
# 2.import...是引用了变量的地址

# from gift import have_gift
# print(id(have_gift))
import gift


# 发礼物方法
def send():
    print("发礼物啦")
    # have_gift = True
    # print(id(have_gift))
    gift.have_gift = True
    # print(id(gift.have_gift))
