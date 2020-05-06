import math
import datetime
import numpy as np
from time import time
from sklearn.svm import SVC
from cvxopt import matrix,solvers
from hardsvm import HardSVM
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# min 1/2 sum_i(sum_j(alpha_i*alpha_j*yi*yj(xi*xj)))- sum_i(alpha_i)
# s.t. sum_i(alpha_i*yi)=0
# alpha_i>=0, i=1,2,...,Na

class HardSVMDual(HardSVM):
    def fit(self,x,y):
        k=self.calculatek(x)
        alpha=self.solveQP(k,x,y)
        self.alpha=np.ravel(alpha)
        sv_multipliers,support_x,support_y=self.supportvectors(x,y,self.alpha)
        self.sv_w = self.compute_w(sv_multipliers, support_x, support_y)
        self.w = self.compute_w(alpha, x, y)
        self.b = self.compute_b(self.w, support_x, support_y)
    def calculatek(self,x):
        n_samples=x.shape[0]
        k=[[np.dot(x[i],x[j]) for j in range(n_samples)] for i in range(n_samples)]
        return k
    def compute_w(self,multipliers, x, y):
        return np.sum(multipliers[i] * y[i] * x[i]  for i in range(len(y)))
    def compute_b(self,w, x, y):
        return np.sum([y[i] - np.dot(w, x[i]) for i in range(len(x))])/len(x)
    def supportvectors(self,x,y,alpha,sita=1e-7):
        has_positive_multiplier = alpha > sita 
        sv_multipliers = alpha[has_positive_multiplier]
        support_vectors = x[has_positive_multiplier] 
        support_vectors_y = y[has_positive_multiplier]
        return sv_multipliers,support_vectors,support_vectors_y
    def solveQP(self,k,x,y):
        n_samples=x.shape[0]      
        P=[[1.*y[i]*y[j]*k[i][j] for j in range(n_samples)] for i in range(n_samples)]
        q=[-1. for _ in range(n_samples)]
        G=[[-1.*(i==j) for i in range(n_samples)] for j in range(n_samples)]
        h=[0. for _ in range(n_samples)]
        A=[[1.*y[i]] for i in range(n_samples)]
        b=0.0
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
    svm=HardSVMDual()
    svm.fit(x_train,y_train)
    print(svm.test(x_train,y_train))
    print(svm.test(x_test,y_test))
        