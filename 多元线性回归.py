#!/usr/bin/env python3     	
# -*- coding: utf-8 -*- 

import numpy as np
import pandas as pd

#上面代码修改过写的是读取csv文件 查看开头说明找出y的值列表变矩阵 找出x列表值变矩阵
def readData(way,x_list_logo,y_logo,show = 0,sample_amount = 1): #这是一个取二元自变量和因变量的函数
    data = pd.read_csv(way)
    y=data.loc[:, y_logo].as_matrix(columns=None)#删掉标签,取出标签time的所有数据保存为列表
    y=np.array([y]).T

    x=data.drop(y_logo, 1)  #吧数据库标签time的一列删除保存到x
    x_list = []
    for x_alone_logo in x_list_logo:
        x_list.append(x.loc[:,x_alone_logo].as_matrix(columns=None))  #删掉标签保存为列表
    x = np.array(x_list).T
    m = y.shape[0]
    if show == 1:
        print("X前5个数据" ,x[:][:5]  ,"\n")
        print("Y前5个数据" ,y[:][:5]  ,"\n")
    if sample_amount == 1:
        print('x样本数为:%d \ny样本数为:%d'%(len(x[:][:]),len(y[:][:])) ,"\n")
    return(x,y,data)

#算自变量 Z值均值以及标准差
def featureNormalize(X):
    X_norm = X;
    X_jun = np.zeros((1,X.shape[1]))
    #输出行1,列为x;列值全为0的数组
    S_x = np.zeros((1,X.shape[1]))
    #输出行1,列为x;列值全为0的数组
    for i in range(X.shape[1]):
        X_jun[0,i] = np.mean(X[:,i])       # 均值
        S_x[0,i] = np.std(X[:,i])     # 标准差
    X_Z  = (X - X_jun) / S_x   #X数组的Z值
    return X_Z,X_jun,S_x

#求线性方程各系数值 θ0,θ1,θ2 .....
def exportTheta(X,Y):
    X = np.hstack((np.ones((X.shape[0] , 1)),X))  #给X数组左侧添加一列全1
    X = np.mat(X)  #X数组转为矩阵
    theta = np.dot(X.I,Y) #X的逆矩阵  矩阵乘法 Y = 各系数
    theta = theta.getA()
    return(theta)

#1/2的最小二乘损失函数 和 成本函数   1/2(y冒 - y)^2 求和 * 1/m  =1/2m  ∑上M下i=1(y冒下i - y下i)^2
def computeCost(X, Y, theta):
    m = Y.shape[0] # m = 样本数
    B = np.array([[int(theta[0]) for x in range(0,m)]]).T #生成1*m列值为theta第一行值组成数组
    theta_x = theta[1:,:]
    epsilon = X.dot(theta_x)+ B - Y   # ε = 算残差 = y冒-y = a1*x1+a2*x2+a0 -y
    J_min = (epsilon.T.dot(epsilon))/ (2*m)   #残差平方之和/样本数
    return J_min

#梯度下降
def gradientDescent(X, Y, theta, alpha, iterations, show = 0, show_a_time = 1):
    theta_new = theta.copy()
    m = Y.shape[0]       #样本数
    # 存储历史误差
    J_history = np.zeros((iterations, 1)) #梯度次数 * 1 的全0数组
    for a in range(iterations):
        B = np.array([[theta[0].tolist()[0] for x in range(0,m)]]).T #生成1*m列值为theta第一行值组成数组
        # θ = θ - α / m * X^T 矩阵乘法 (X矩阵乘法θ+B-Y)    单元素为θ下j = θ下j - α / m * ε下i *X下ij
        theta_new[1:,:] = theta_new[1:,:] - (alpha/m) * np.dot( X.T, np.dot( X, theta_new[1:,:])+B -Y) 
        # θ0 = θ0 - α / m *   求和上m下1(单样本残差)
        theta_new[:1,:] = theta_new[:1,:] - (alpha/m) * (X.dot(theta_new[1:,:]) + B - Y).sum()
        J_history[a] = computeCost(X, Y, theta_new)
        if show == 1 and a%show_a_time == 0:
            print( "偏差导数系数:",np.dot( X.T, np.dot( X, theta_new[1:,:])+B -Y) , (X.dot(theta_new[1:,:]) + B - Y).sum() )
    return J_history,theta_new

#算估计的标准误差
def sampleYStandardDeviation( X, Y, theta_new ):
    X = np.hstack([np.ones((X.shape[0], 1)), X]) #数组左侧添加一列全1
    #1)误差平方 2)求和 3)除 4)分母为样本量-2 5)算完开根
    s_sample = ( ((X.dot(theta_new) - Y)**2).sum() / (X.shape[0]-2) )**0.5
    return s_sample

#预测y值得范围
def predict(data, s_sample):
    data = np.array(data) #全部数据 输出成数组
    data = np.hstack([np.ones((data.shape[0], 1)), data]) #数组左侧添加一列全1
    Y_mao = data.dot(theta_new) #算出y冒值
    Y_95 = [Y_mao - 1.65*s_sample ,Y_mao + 1.65*s_sample]
    Y_98 = [Y_mao - 2.06*s_sample ,Y_mao + 2.06*s_sample]
    Y_99 = [Y_mao - 2.33*s_sample ,Y_mao + 2.33*s_sample]
    print("预测均值:", Y_mao, "\n预测95%可能性数值范围" , Y_95, '\n预测98%可能性数值范围' , Y_98,"\n预测99%可能性数值范围", Y_99)

    

    

#路径,x标签列表,y标签, show 0,1表示是否显示x和y前五行,sample_amount显示x,y样本数
X,Y,data =readData('E:\\ml.csv',['lucheng','cishu'],'time',show = 1,sample_amount = 1)
#读取csv文件

#求特征值: 求X数组的Z值, X每列均值, X每列标准差
X_Z,X_jun,S_x = featureNormalize(X)

#求theta的值 :θ
theta = exportTheta(X,Y) #分别为多元回归公式θ0,θ1,θ2 ...  theta中文为Θ θ
print('这是个线性系数的值:' , theta ,"\n")

J_min = computeCost(X,Y,theta)   #j = 残差平方之和/ 2样本数
print('显示残差^2 /样本量:' , J_min*2 ,"\n")

#这里有个注意的地方 学习率写的过大会导致 偏差成指数形式增长 多次迭代偏差越来越大
#alpha学习率  iterations迭代次数  show是否显示偏差导数系数0不1是 show_a_time多少次迭代显示一次
J_history,theta_new = gradientDescent(X, Y, theta, alpha = 0.0001, iterations = 10, show = 1, show_a_time = 1) 
print('梯度下降更新后 新的theta的值',theta_new ,"\n")

#算估计的标准误差
s_sample = sampleYStandardDeviation( X, Y, theta_new )

#给出x值和估计的标准误差 求y范围
predict([[75,3],[100,4]],s_sample)

 
''' 想写的公式
#log损失函数标准形式  二分法 y只有0或1
单个损失: F(y冒,y) = -(y * log下未知上y冒 + (1-y) * log下未知上(1-y冒) )
平均损失: J(w,b) = 1/m m之和 F(y冒,y)
w为各自变量生成的矩阵 b为所有a0矩阵
'''

''' 
txt加载数据没看
#加载数据
def load_exdata(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [int(item) for item in line]
            #5.5277,9.1302
            data.append(current)
    return data
 
data = load_exdata('ex1data2.txt');
data = np.array(data,np.int64)
 
x = data[:,(0,1)].reshape((-1,2))
y = data[:,2].reshape((-1,1))
m = y.shape[0]
 
# Print out some data points
print('First 10 examples from the dataset: \n')
print(' x = ',x[range(10),:],'\ny=',y[range(10),:])
'''
