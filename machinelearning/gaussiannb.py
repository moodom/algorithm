import numpy as np
import math  
from collections import Counter
from naivebayes import NaiveBaysBase
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
class GaussianNB(NaiveBaysBase):
    """
    高斯朴素贝叶斯,假设各维度特征为正太分布
    一般用于连续型数据
    """
    def fit(self,x,y):
        self.n_samples,self.n_features=x.shape
        self.countCate,self.priorPro=self.priorProCaculate(y)
        self.mus,self.sigmas=self.muSigma(x,y)
    def muSigma(self,x,y):
        mus={}
        sigmas={}
        for c in self.countCate.keys():
            xc=x[np.where(y==c)]
            mu=list(np.mean(xc,axis=0))
            mus[c]=mu
            sigma=list(np.std(xc,axis=0))
            sigmas[c]=sigma
        return mus,sigmas
    def condiProCaculate_(self,xi,mu,sigma):
        p=math.exp((-(xi-mu)**2)/(2*sigma**2))/math.sqrt(2*math.pi*sigma**2)
        return p
    def predict(self,xi):
        maxscore,maxc=float("-inf"),float("-inf")
        for c in self.priorPro.keys():
            score=self.priorPro[c]
            for i in range(len(xi)):
                score*=self.condiProCaculate_(xi[i],self.mus[c][i],self.sigmas[c][i])
            (maxscore,maxc)=(score,c) if (score>maxscore) else (maxscore,maxc)
        return maxc
if __name__=="__main__":
    iris=load_iris()
    x=iris.data[:100,[0,3]]
    y=iris.target[:100]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    bayes=GaussianNB()
    bayes.fit(x_train,y_train)
    print(bayes.test(x_train,y_train))
    print(bayes.test(x_test,y_test))  

    # x = np.array([[1, 1], [1, 2], [1, 2], [1, 1], [1, 1], [2, 1],[2,2],[2,2],[2,3],[2,3],[3,3],[3,2],[3,2],[3,3],[3,3]])
    # y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    # bayes=GaussianNB()
    # bayes.fit(x,y) 
    # print(bayes.predict(np.array([2,1])))