import numpy as np  
from collections import Counter
from naivebayes import NaiveBaysBase

class MultinomialNB(NaiveBaysBase):
    """
    多项式朴素贝叶斯,先验概率和条件概率都采用贝叶斯估计
    一般用于离散型数据
    """
    def __init__(self,lam=1): # lam=0时表示条件概率最大似然估计,lam>0时表示贝叶斯估计,lam=1时 称为拉普拉斯平滑
        self.lam=lam
    def priorProCaculate(self,y):
        count=Counter(y)
        num=len(y)
        prior={key:(count[key]+self.lam)/(num+len(count)*self.lam) for key in count.keys()}  # 先验概率的贝叶斯估计         
        print(prior)
        return count,prior
    def condiProCaculate(self,x,y):              #条件概率,统计个数 
        self.features=self.feaNumCount(x)
        condition={}
        for c in self.countCate.keys():
            condition[c]=[ [0]*len(fea) for fea in self.features]
        for xi,yi in zip(x,y):
            for i in range(len(xi)):
                index=self.features[i].index(xi[i])
                tmp=self.countCate[yi]+len(self.countCate)*self.lam
                condition[yi][i][index]+=1
        for yi in condition.keys():
            yNum=self.countCate[yi]
            cateNum=len(self.countCate)
            for i in range(len(condition[yi])):
                sj=len(condition[yi][i])
                for j in range(len(condition[yi][i])):
                    condition[yi][i][j]=(condition[yi][i][j]+self.lam)/(yNum+sj*self.lam)
        return condition
if __name__=="__main__":
    x = np.array([[1, 1], [1, 2], [1, 2], [1, 1], [1, 1], [2, 1],[2,2],[2,2],[2,3],[2,3],[3,3],[3,2],[3,2],[3,3],[3,3]])
    y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])
    bayes=MultinomialNB()
    bayes.fit(x,y)
    print(bayes.predict(np.array([2,1])))