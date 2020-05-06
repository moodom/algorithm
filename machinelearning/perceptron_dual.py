# 对偶形式
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from perceptron import PerceptronBase
class PerceptronDual(PerceptronBase):
    """
    对偶形态感知机
    """
    def __init__(self,lr=0.1,n_iter=50):
        super(PerceptronDual,self).__init__(lr=lr,n_iter=n_iter)

    def fit(self,x,y):
        """
        对偶形态的感知机,一次更新的时间复杂度O(N) N为训练数据
        """
        self.alpha=np.zeros(x.shape[0])
        self.b=0
        self.w=np.zeros(x.shape[1])
        self.gram=self.gramMatrix(x)
        for _ in range(self.n_iter):
            for i in range(len(x)):
                update=self.lr*(y[i]-self.judge(y,i))//2
                self.alpha[i]+=abs(update)
                self.b+=update
        self.w=np.dot(self.alpha*y,x)
    def gramMatrix(self,x):
        return np.dot(x,x.T)
    def judge(self,y,i):
        tmp=sum(self.alpha*y*self.gram[i])+self.b #
        return np.where(tmp<=0,-1,1)
    # def sign(self,xi):
    #     return np.dot(xi,self.w)+self.b
    # def predict(self,xi):
    #     return np.where(self.sign(xi)<=0.0,-1,1)
    # def test(self,x,y):
    #     res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
    #     return sum(res)/len(y)

if __name__=="__main__":
    iris=load_iris()
    x=iris.data[:100,[0,2]]
    y=iris.target[:100]
    y=np.where(y==1,1,-1)  #np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
    ppn=PerceptronDual(lr=1,n_iter=10)
    ppn.fit(x_train,y_train)
    print(ppn.test(x_train,y_train))
    print(ppn.test(x_test,y_test))

    # x=np.array([[3,3],[4,3],[1,1]])
    # y=np.array([1,1,-1])
    # ppn=PerceptronDual(lr=1,n_iter=10)
    # ppn.fit(x,y)
    # print(ppn.test(x,y))
    # print(ppn.w,ppn.b)





