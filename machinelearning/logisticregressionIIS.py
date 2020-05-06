# 存在bug

import math
import numpy as np 
from copy import deepcopy
from collections import Counter

class IIS(object):
    def __init__(self,eps=0.005,max_iter=100):
        self.eps=eps  #收敛条件
        self.max_iter=max_iter
    def data_struct(self,x,y):
        counter_x=[Counter(x[:,i]) for i in range(self.n_features)]
        counter_y=Counter(y)
        tmp=[{key:0 for key in counter_x[i].keys()} for i in range(self.n_features)]
        data={c:deepcopy(tmp) for c in counter_y.keys()}
        return deepcopy(data)
    def empiricalDisEp(self,x,y):   # 特征函数f(x,y)关于经验分布P_(X,Y)的期望值
        empirical_ep=self.data_struct(x,y)
        for xi,yi in zip(x,y):
            for i in range(len(xi)):
                empirical_ep[yi][i][xi[i]]+=1/self.n_samples
        return empirical_ep
    def modelDisEp(self,w,x,y):       # 特征函数f(x,y)关于模型P(Y|X)与经验分布P_(X)的期望值
        model_ep=self.data_struct(x,y)
        for xi,yi in zip(x,y):
            for i in range(len(xi)):
                p_y_x=self.calculatePyx(w,yi,xi)
                model_ep[yi][i][xi[i]]+=p_y_x/self.n_samples
        return model_ep
    def calculatePyx(self,w,yi,xi):
        zx=self.calculateZx(xi,w)
        ss=0
        for i in range(len(xi)): 
            ss+=w[yi][i][xi[i]]
        pyx=math.exp(ss)/zx
        return pyx
    def calculateZx(self,xi,w):     
        zx=0
        for c in w.keys():
            ss=0
            for i in range(len(xi)):
                ss+=w[c][i][xi[i]]
            print(ss)
            zx+=math.exp(ss)
        return zx
    def fit(self,x,y):
        self.n_samples,self.n_features=x.shape
        w=self.data_struct(x,y)
        empirical_ep=self.empiricalDisEp(x,y)
        print(empirical_ep)
        for _ in range(self.max_iter):
            last_w=w
            model_ep=self.modelDisEp(w,x,y)
            for xi,yi in zip(x,y):
                for i in range(len(xi)):
                    w[yi][i][xi[i]]+=math.log(empirical_ep[yi][i][xi[i]]/model_ep[yi][i][xi[i]])/self.n_features
            if self.isConvergence(last_w,w):
                break
    def isConvergence(self,last_w,w):
        for c in w.keys():
            for i in range(len(w[c])):
                for j in w[c][i].keys():
                    if last_w[c][i][j]>=w[c][i][j]:
                        return False
        return True

if __name__=="__main__":
    # x 年龄 有工作 有自己的房子 信贷情况  y 类别
    # 1 青年   否      否         一般      否
    # 2 中年   是      是          好       是
    # 3 老年                     非常好
    x=np.array([[1,1,1,1],[1,1,1,2],[1,2,1,2],[1,2,2,1],[1,1,1,1],
    [2,1,1,1],[2,1,1,2],[2,2,2,2],[2,1,2,3],[2,1,2,3],
    [3,1,2,3],[3,1,2,2],[3,2,1,2],[3,2,1,3],[3,1,1,1],[1,1,1,1]])
    y=np.array([1,1,2,2,1,1,1,2,2,2,2,2,2,2,1,2])
    iis=IIS()
    iis.fit(x,y)
    