
from datetime import *

'''全局'''
chushi = datetime.now() 
jixushijian = 0
zantingbianliang = 0

def shijian():
    global jixushijian
    global chushi
    xuexishijian = datetime.now() 
    if jixushijian == 0:
        print(xuexishijian - chushi )
    else:
        print(xuexishijian - chushi + jixushijian)

def zanting(la):
    global jixushijian
    global chushi
    if la == 1:
        zantingshijian = xuexishijian = datetime.now() 
        if jixushijian == 0:
            jixushijian = zantingshijian - chushi
        else:
            jixushijian += zantingshijian - chushi
    elif la == 0:
        chushi = datetime.now()

while True:
    global zantingbianliang
    if zantingbianliang != 1:
        kongzhi = input('输入内容1显示时间 2暂停 3结束')
    elif zantingbianliang == 1:
        input('2继续')
    if kongzhi == '1':
        shijian()
    if kongzhi == '2' and zantingbianliang == 0:
        zantingbianliang = 1
        zanting(1)
    elif kongzhi == '2' and zantingbianliang == 1:
        zantingbianliang = 0
        zanting(0)
    if kongzhi == '3':
        exit()