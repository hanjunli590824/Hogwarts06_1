#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23 16:19
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : save_money.py
# @software: PyCharm

# 已存金额
saved_money = 1000


# 发工资
def send_money():
    global saved_money
    print("发工资啦！")
    saved_money = 2000


# 查询工资
def select_money():
    if saved_money == 2000:
        print("收到工资，很开心！")
    else:
        print("没发工资")


if __name__ == '__main__':
    send_money()
    select_money()
