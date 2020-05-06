# 感知器
# 需要掌握的知识点：
# 1.感知器的算法流程以及推导过程
# 2.感知器对偶形式

# 使用klearn库
# from sklearn.linear_model import Perceptron
# import numpy as np 
# x=np.array([[3,3],[4,3],[1,1]])
# y=np.array([1,1,-1])
# perceptron=Perceptron()
# perceptron.fit(x,y)
# print("w:",perceptron.coef_)
# print("b:",perceptron.intercept_)
# print("n_iter:",perceptron.n_iter_)
# res=perceptron.score(x,y)
# print("correct rate:{:.0%}".format(res))

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
class PerceptronBase(object):
    """
    原始形态感知器，一次更新的时间复杂度O(n) n为特征空间的大小 
    """
    def __init__(self,lr=1,n_iter=50):
        self.lr=lr
        self.n_iter=n_iter
    def fit(self,x,y):
        # 初始化参数w,d
        self.w=np.zeros(x.shape[1])
        self.b=0
        for _ in range(self.n_iter):
            erros=0
            for xi,yi in zip(x,y):
                update=self.lr*(yi-self.predict(xi))//2
                self.w+=update*xi
                self.b+=update
                erros+=int(update!=0.0)
            if erros==0:
                break
    def sign(self,xi):
        return np.dot(xi,self.w)+self.b  #
    def predict(self,xi):
        return np.where(self.sign(xi)<=0.0,-1,1)
    def test(self,x,y):
        res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
        return sum(res)/len(y)

if __name__=="__main__":
    # iris=load_iris()
    # x=iris.data[:100,[0,2]]
    # y=iris.target[:100]
    # y=np.where(y==1,1,-1)  #np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    # ppn=PerceptronBase(lr=1,n_iter=5)
    # ppn.fit(x_train,y_train)
    # print(ppn.test(x_train,y_train))
    # print(ppn.test(x_test,y_test))

    x=np.array([[0,0],[0,1],[1,0],[1,1]])
    y=np.array([-1,1,1,-1])
    ppn=PerceptronBase(lr=1,n_iter=20)
    ppn.fit(x,y)
    print(ppn.test(x,y))
    print(ppn.w,ppn.b)

    

