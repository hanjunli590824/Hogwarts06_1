#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 13:05
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : demo.py
# @software: PyCharm

# 总结：
# 1.python允许在模块里定义 变量和方法的
# 2.函数里可以调用外部的变量
# 3.函数里不允许改变外部变量
# 4.把外部变量设置为global全局的，就可以改变
# 5.通过id（）方法可以打印对象的内存地址
# 6.方法默认返回值是None
# 7.if __name__ == '__main__':是一个执行入口

a = 1


def fun():
    global a
    a = 2
    # 打印a的内存地址
    print(id(a))
    print(f"变量a的值:{a}")
    print("这是一个方法")
    # return True


# print(a)
# fun()
# print(id(a))
# print(a)

# print(fun())

if __name__ == '__main__':
    fun()
