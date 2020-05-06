# 存在bug
import math
import datetime
import numpy as np
from time import time
from sklearn.svm import SVC
from cvxopt import matrix,solvers
from softsvm_dual import SoftSVMDual
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

class KenelSVMDual(SoftSVMDual):
    def __init__(self,c=1,kernel="gaussian"):
        super(KenelSVMDual,self).__init__(c)
        self.kernel=kernel
    def fit(self,x,y):
        self.n_samples=x.shape[0]
        self.x,self.y=x,y
        k=[[self.calculatek(x[i],x[j],self.kernel) for j in range(self.n_samples)] for i in range(self.n_samples)]
        alpha=self.solveQP(k,x,y)
        self.alpha=np.ravel(alpha)
        sv_multipliers,support_x,support_y=self.supportvectors(x,y,self.alpha)
        self.sv_w = self.compute_w(sv_multipliers, support_x, support_y)
        self.w = self.compute_w(alpha, x, y)
        self.b = self.compute_b(self.w, support_x, support_y)
    def calculatek(self,xi,xj,kernel):
        if kernel==None:
            kij=np.dot(xi,xj)
        if kernel=="poly":
            kij=self.calculatePolyk(xi,xj) 
        if kernel=="gaussian":
            kij=self.calculateGaussiank(xi,xj)
        return kij
    def calculatePolyk(self,xi,xj,p=2):
        return math.pow((np.dot(xi,xj)+1),p) 
    def calculateGaussiank(self,xi,xj,sita=3):
        return math.exp(-sum([(xi[i]-xj[i])**2 for i in range(len(xi))])/2*sita**2)
    def predict(self,xi):
        res=0
        for i in range(self.n_samples):
            res+=self.alpha[i]*self.y[i]*self.calculatek(self.x[i],xi,self.kernel)
        res+=self.b  
        return 1 if res>0 else -1
if __name__=="__main__":
    cancer=load_breast_cancer()
    x=cancer.data
    y=cancer.target
    y[y==0]=-1
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    svm=KenelSVMDual()
    svm.fit(x_train,y_train)
    print(svm.test(x_train,y_train))
    print(svm.test(x_test,y_test))
