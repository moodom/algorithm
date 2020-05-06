# 朴素贝叶斯
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from collections import Counter

# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# Y = np.array([1, 1, 1, 2, 2, 2])
# clf = MultinomialNB()  #拟合数据
# clf.fit(X,Y)
# print(clf.predict([[-0.8, -1]]))
# print(clf.predict_proba([[-0.8, -1]]))
# print(clf.predict_log_proba([[-0.8, -1]]))

class NaiveBaysBase(object):
    """
    朴素贝叶斯, "朴素"指特征之间相互独立
    """
    def __init__(self):
        pass
    def fit(self,x,y):
        self.n_samples,self.n_features=x.shape
        self.countCate,self.priorPro=self.priorProCaculate(y)
        self.condiPro=self.condiProCaculate(x,y)
    def feaNumCount(self,x):
        features_counters=[Counter(x[:,col]) for col in range(self.n_features)]
        features=[[f for f in features_counters[col].keys()] for col in range(self.n_features)]
        return features        
    def priorProCaculate(self,y):   #先验概率,统计个数
        count=Counter(y)
        num=len(y)
        prior={key:count[key]/num for key in count.keys()}           
        return count,prior
    def condiProCaculate(self,x,y):              #条件概率,统计个数 
        self.features=self.feaNumCount(x)
        condition={}
        for c in self.countCate.keys():
            condition[c]=[ [0]*len(fea) for fea in self.features]
        for xi,yi in zip(x,y):
            for i in range(len(xi)):
                index=self.features[i].index(xi[i])
                condition[yi][i][index]+=1/self.countCate[yi]
        return condition
    def predict(self,xi):
        maxscore,maxc=float("-inf"),float("-inf")
        for c in self.priorPro.keys():
            score=self.priorPro[c]
            for i in range(len(xi)):
                    index=self.features[i].index(xi[i])
                    score*=self.condiPro[c][i][index]
            (maxscore,maxc)=(score,c) if (score>maxscore) else (maxscore,maxc)
        return maxc
    def test(self,x,y):
        res=sum([self.predict(xi)==yi for xi,yi in zip(x,y)])
        return res/len(y)
        
if __name__=="__main__":
    # iris=load_iris()
    # x=iris.data[:100,[0,2]]
    # y=iris.target[:100]
    # y=np.where(y==1,1,-1)  #np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    # bayes=NaiveBaysBase()
    # bayes.fit(x_train,y_train)
    # print(bayes.test(x_train,y_train))
    # bayes.test(x_test,y_test)

    x = np.array([[1, 1], [1, 2], [1, 2], [1, 1], [1, 1], [2, 1],[2,2],[2,2],[2,3],[2,3],[3,3],[3,2],[3,2],[3,3],[3,3]])
    y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    bayes=NaiveBaysBase()
    bayes.fit(x,y)
    print(bayes.predict(np.array([2,1])))