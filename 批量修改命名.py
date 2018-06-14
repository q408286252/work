
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
mulu = 0
while True:
    if mulu == False:
        mulu = input('输入需要批量修改的目录:')
    else:
        print('重新开始')
        shifouxiugai = input('已有目录是否修改? y/n:')
        if shifouxiugai == 'y':
            mulu = input('输入需要批量修改的目录:')
        elif shifouxiugai == 'q':
            exit()  
        elif shifouxiugai == 'n':
            pass
        
    muluwenjian = os.listdir(mulu)
    mulu = mulu + '/'
    xuanze = input('1.<替换> 用于批量删除 中间内容替换或添加;2.<添加>批量开头或末尾添加:')
    if xuanze == '1':
        beitihuanneirong = input('输入被替换的内容:')
        tihuanneirong = input('输入替换内容:')
        for i in muluwenjian:
            ii = i
            ii = ii.replace(beitihuanneirong,tihuanneirong) 
            os.rename(mulu + i,mulu + ii)
        print('完成')
    elif xuanze == '2':
        kaitoumowei = input('1.请输入屎添加开头;2.添加末尾:')
        if kaitoumowei == '1':
            kaitou = input('添加开头内容输入:')
            for i in muluwenjian:
                os.rename(mulu + i,mulu + kaitou + i)
            print('完成')
        elif kaitoumowei == '2':
            mowei = input('添加末尾内容输入:')
            for i in muluwenjian:
                ii = i
                ii = ii.split('.')
                ii.insert(1,mowei)
                ii.insert(2,'.')
                ii = ''.join(ii)
                os.rename(mulu + i,mulu + ii)
            print('完成')
        else:
            print('输入错误重新开始')
            contiue
    elif xuanze == 'q':
        exit()  
    else:
        print('输入错误重新开始')
        contiue