import math
import datetime
import numpy as np
from time import time
from sklearn.svm import SVC
from cvxopt import matrix,solvers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
#**********************sklearn****************************************
# from sklearn.linear_model import LogisticRegression
# cancer=load_breast_cancer()
# x=cancer.data
# y=cancer.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# kernel = ["linear","poly","rbf", "sigmoid"]
# for kernel in kernel:
#     time0 = time()
#     clf = SVC(kernel = kernel, 
#               degree = 1, #degree默认值是3，所以poly核函数跑的非常慢，
#               gamma = "auto", 
#               cache_size=5000).fit(x_train,y_train) #cache_size default=200 默认使用200MB内存
#     print("The accuracy under kernel %s is %f" % (kernel, clf.score(x_test, y_test)))
#****************************************************************************
#*******************cvxopt试用*************************************
# minimize 2*x1+x2   LP(Linear Programming)(线性规划问题)
# subject to -x1+x2<=1
#            x1+x2>=2
#            x2>=0
#            x1-2*x2<=4
# A=matrix([[-1.0,-1.0,0.0,1.0],[1.0,-1.0,-1.0,-2.0]])
# b=matrix([1.0,-2.0,0.0,4.0])
# c=matrix([2.0,1.0])
# sol=solvers.lp(c,A,b)
# print(sol['x'])
# print(np.dot(sol['x'].T,c))
# print(sol['primal objective'])

# minimize 1/2*(w1^2+w2^2)   QP(Quadratic Programming)(二次规划问题)
# subject to  3*w1+3*w2+b>=1
#             4*w1+3*w2+b>=1
#             -w1-w2-b>=1
# P=matrix([[1.,0.,0.],[0.,1.,0.],[0.,0.,0.]])
# q=matrix([0.,0.,0.])
# G=matrix([[-3.,-4.,-1.],[-3.,-3.,-1.],[1.,1.,1.]])
# h=matrix([-1.,-1.,-1.])
# sol=solvers.qp(P, q, G, h)
# print(sol['x'])
# print(sol['primal objective'])

# min 1/2*x.T*P*x+q.T*x
# s.t.    Gx<=h
#         Ax=b
#**********************************************************************
# min 1/2*||w||^2
# s.t. yi(w*xi+b)-1>0   i=1,2,...,N
# 求得最优解 w*,b*
class HardSVM(object):
    def fit(self,x,y):
        wb=self.solveQP(x,y)
        self.w,self.b=wb[:-1],wb[-1]
        print(self.w,self.b)
    def solveQP(self,x,y):
        n_samples,n_features=x.shape
        P=[[1.0*(i==j) for j in range(n_features+1)]for i in range(n_features+1)]
        P[-1][-1]=0.
        q=[0.0 for i in range(n_features+1)]
        h=[-1.0 for i in range(n_samples)]
        G=[[0.]*(n_samples) for _ in range(n_features+1)]
        for i in range(n_features+1):
            for j in range(n_samples):
                if i==n_features:
                    G[i][j]=-1.0*(y[j])
                else:
                    G[i][j]=-1.0*y[j]*x[j][i]
        P_=matrix(P)
        q_=matrix(q)
        G_=matrix(G)
        h_=matrix(h)      
        sol=solvers.qp(P_,q_,G_,h_)
        return sol['x']  
    def predict(self,xi):
        res=0
        for i in range(len(xi)):
            res+=self.w[i]*xi[i]
        res+=self.b
        return 1 if res>=0 else -1
    def test(self,x,y):
        res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
        return sum(res)/len(y) 
if __name__=="__main__":
    # x=np.array([[3,3],[4,3],[1,1]])
    # y=np.array([1,1,-1])

    # x=np.array([[1,1,1,1],[1,1,1,2],[1,2,1,2],[1,2,2,1],[1,1,1,1],
    # [2,1,1,1],[2,1,1,2],[2,2,2,2],[2,1,2,3],[2,1,2,3],
    # [3,1,2,3],[3,1,2,2],[3,2,1,2],[3,2,1,3],[3,1,1,1]])
    # y=np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])

    cancer=load_breast_cancer()
    x=cancer.data
    y=cancer.target
    y[y==0]=-1
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    svm=HardSVM()
    svm.fit(x_train,y_train)
    print(svm.test(x_train,y_train))
    print(svm.test(x_test,y_test))