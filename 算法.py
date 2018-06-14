#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#只能解一元一次方程 实质是它把未知数换成虚数然后求解
def solve(eq,variable='x'): #variable 变量
  eq1 = eq.replace("=","-(") + ")" #吧'=' 换成'-(' 字符尾部加')'
  c = eval(eq1,{variable:1j})  #变量变为1单位虚数
  return -c.real/c.imag  #-实数值/虚数值 = x值

#冒泡排序
def maopaopaixu(list1):
    for a in range(len(list1)-1):
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i] ,list1[i+1] = list1[i+1],list1[i]
    return list1
list_0 = [9,8,7,6,5,4,3,2,1,0]
maopaopaixu(list_0)

