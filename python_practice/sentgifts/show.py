#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 13:52
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : show.py
# @software: PyCharm

# 注意python中import和from import 的区别：
# 首先明确：尽量不要为了图省事使用from xxx import *
#
# python中有两种导入模块的方式，一种是import xxx，另一种是from xxx import yyy。两者的区别在于：
# 第一种仅仅导入一个模块，并且将该模块执行了一遍（if __main__ =="__main__"里面的没有执行）。
# 同时，有在当前的命名空间中导入变量，需要通过xxx.yyy的方式使用导入模块中的变量、函数、类等；
# 第二种则将模块中的变量yyy导入了当前命名空间，因此使用时可以直接以yyy调用，
# 使用这种导入方法时，需要注意当前的命名空间是否有重名的，from xxx import *这种方式尽量不要使用，因为这样就破坏了对命名空间的管理。
#
# ps：使用from xxx import *时是不能导入以单下划线开头的保护属性和以双下划线开头的私有属性的

# from gift import have_gift
import gift


# 展示礼物
def show():
    have_gift = gift.have_gift
    # print(id(gift.have_gift))
    # print(id(have_gift))
    if have_gift == True:
        print("收到礼物啦，好开心~")
    else:
        print("没有礼物")
