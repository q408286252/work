#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#冒泡排序
def maopaopaixu(list1):
    for a in range(len(list1)-1):
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i] ,list1[i+1] = list1[i+1],list1[i]
    return list1
list_0 = [9,8,7,6,5,4,3,2,1,0]
maopaopaixu(list_0)

