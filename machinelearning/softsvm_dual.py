import math
import datetime
import numpy as np
from time import time
from sklearn.svm import SVC
from cvxopt import matrix,solvers
from hardsvm_dual import HardSVMDual
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
# min 1/2 sum_i(sum_j(alpha_i*alpha_j*yi*yj(xi*xj)))- sum_i(alpha_i)
# s.t. sum_i(alpha_i*yi)=0
# 0<=alpha_i<=C, i=1,2,...,Na

class SoftSVMDual(HardSVMDual):
    def __init__(self,c=0.1):
        super(SoftSVMDual,self).__init__()
        self.c=c
    def solveQP(self,k,x,y):
        n_samples=x.shape[0]      
        P=[[1.*y[i]*y[j]*k[i][j] for j in range(n_samples)] for i in range(n_samples)]
        q=[-1. for _ in range(n_samples)]
        A=[[1.*y[i]] for i in range(n_samples)]
        b=0.0
        G=[[0]*(2*n_samples) for _ in range(n_samples)]
        for i in range(n_samples):
            for j in range(2*n_samples):
                if i==j:
                    G[i][j]=-1.
                elif j-i==i:
                    G[i][j]=1
        h1=[0. for _ in range(n_samples)]
        h2=[1.*self.c for _ in range(n_samples)]
        h=h1+h2
        P_,q_=matrix(P),matrix(q)
        G_,h_=matrix(G),matrix(h)
        A_,b_=matrix(A),matrix(b)
        sol=solvers.qp(P_,q_,G_,h_,A_,b_)
        return sol['x']
if __name__=="__main__":
    # x=np.array([[3,3],[4,3],[1,1]])
    # y=np.array([1,1,-1])
    # svm=HardSVMDual()
    # svm.fit(x,y)
    # print(svm.w,svm.b)
    cancer=load_breast_cancer()
    x=cancer.data
    y=cancer.target
    y[y==0]=-1
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
    svm=SoftSVMDual()
    svm.fit(x_train,y_train)
    print(svm.test(x_train,y_train))
    print(svm.test(x_test,y_test))