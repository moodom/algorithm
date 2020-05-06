# 逻辑回归
import math
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# cancer=load_breast_cancer()
# x=cancer.data
# y=cancer.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# model=LogisticRegression()
# model.fit(x_train,y_train)
# print(model.score(x_test,y_test))

class MaxEntropyIIS(object):
    def __init__(self,eps=0.005,max_iter=1000):
        self.eps=eps   # 收敛条件
        self.max_iter=max_iter
    def initial(self,x,y):
        self.samples=x
        self.n_samples,self.n_features=len(x),len(x[0])
        self.c=set(y)
        self.xy_num={}   # 记录以键值为(xi,yi)出现的样本个数
        for xi,yi in zip(x,y):
            for xij in xi:
                if (xij,yi) not in self.xy_num.keys():
                    self.xy_num[(xij,yi)]=1
                else:
                    self.xy_num[(xij,yi)]+=1
        self.n=len(self.xy_num) # 记录键值(x,y)的个数目    
        self.w,self.last_w=[0]*self.n,[] 
        self.id_xy={}
        self.xy_id={}    #
        self.Ep=[0]*self.n       # 计算特征函数fi关于经验分布的期望
        for i, xy in enumerate(self.xy_num):
            self.Ep[i]=self.xy_num[xy]/self.n_samples
            self.xy_id[xy]=i
            self.id_xy[i]=xy
    def calculateZx(self,xi):    # 计算每个z(x)值
        zx=0
        for c in self.c:
            ss=0
            for xij in xi:
                if (xij,c) in self.xy_num:
                    ss+=self.w[self.xy_id[(xij,c)]]
            zx+=math.exp(ss)
        return zx
    def calculatePyx(self,yi,xi):  # 计算每个P(y|x)
        zx=self.calculateZx(xi)
        ss=0
        for xij in xi:
            if (xij,yi) in self.xy_num:
                ss+=self.w[self.xy_id[(xij,yi)]]
        pyx=math.exp(ss)/zx
        return pyx  
    def modelEp(self,index):   #计算特征函数fi关于模型的期望
        xij,yi=self.id_xy[index]
        ep=0
        for xi in self.samples:
            if xij not in xi:
                continue
            pyx=self.calculatePyx(yi,xi)
            ep+=pyx/self.n_samples 
        return ep
    def fit(self,x,y):
        self.initial(x,y)
        for _ in range(self.max_iter):
            self.last_w=self.w[:]
            for i in range(self.n):
                ep=self.modelEp(i)      #计算第i个特征的模型期望
                self.w[i]+=math.log(self.Ep[i]/ep)/self.n_features             # 更新参数
            if self.isConvergence():    # 判断是否收敛
                break
    def isConvergence(self): # 判断是否收敛
        for last,now in zip(self.last_w,self.w):
            if abs(last-now)>=self.eps:
                return False
        return True

    def predict(self,xi):       # 计算预测概率
        z=self.calculateZx(xi)
        result={}
        for c in self.c:
            ss=0
            for xij in xi:
                if (xij,c) in self.xy_num:
                    ss+=self.w[self.xy_id[(xij,c)]]
            pyx=math.exp(ss)/z
            result[c]=pyx
        return result

if __name__=="__main__":
    x = [['no', 'sunny', 'hot', 'high', 'FALSE'],
           ['no', 'sunny', 'hot', 'high', 'TRUE'],
           ['yes', 'overcast', 'hot', 'high', 'FALSE'],
           ['yes', 'rainy', 'mild', 'high', 'FALSE'],
           ['yes', 'rainy', 'cool', 'normal', 'FALSE'],
           ['no', 'rainy', 'cool', 'normal', 'TRUE'],
           ['yes', 'overcast', 'cool', 'normal', 'TRUE'],
           ['no', 'sunny', 'mild', 'high', 'FALSE'],
           ['yes', 'sunny', 'cool', 'normal', 'FALSE'],
           ['yes', 'rainy', 'mild', 'normal', 'FALSE'],
           ['yes', 'sunny', 'mild', 'normal', 'TRUE'],
           ['yes', 'overcast', 'mild', 'high', 'TRUE'],
           ['yes', 'overcast', 'hot', 'normal', 'FALSE'],
           ['no', 'rainy', 'mild', 'high', 'TRUE']]
    y=['no','no','yes','yes', 'yes', 'no', 'yes', 'no', 'yes','yes', 'yes', 'yes', 'yes', 'no']
    iis=MaxEntropyIIS()
    iis.fit(x,y)
    x = ['overcast', 'mild', 'high', 'FALSE']
    print('predict:', iis.predict(x))



        