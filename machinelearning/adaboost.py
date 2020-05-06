import math
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


# cancer = load_breast_cancer()
# x=cancer.data
# y=cancer.target
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
# classifier = AdaBoostClassifier(
#     DecisionTreeClassifier(max_depth=1),
#     n_estimators=100
# )
# classifier.fit(x_train, y_train)
# print(classifier.score(x_test,y_test))
class AdaBoostClassifier(object):
    def __init__(self,classifier,n_estimators):
        self.classifier=classifier
        self.n_estimators=n_estimators
    def fit(self,x,y):
        n_samples,n_features=x.shape
        Dm=[1/n_samples]*n_samples
        self.G,self.alpha=[],[]
        for m in range(self.n_estimators):
            Gm=self.classifier
            Gm.fit(x,y)
            self.G.append(Gm)
            alpham=self.calculateAlpha(x,y,Dm,Gm)
            self.alpha.append(alpham)
            Dm=self.updateD(alpham,x,y,Dm,Gm)
    def calculateAlpha(self,x,y,D,G):
        tmp=[G.score([xi],[yi]) for xi,yi in zip(x,y)]
        e=sum([D[i]*(1-tmp[i]) for i in range(len(D))])
        alpha=0.5*math.log((1-e)/e)
        return alpha
    def updateD(sefl,alpha,x,y,D,G):
        updateD=[D[i]*math.exp(-alpha*y[i]*G.predict([x[i]])[0]) for i in range(len(y))]
        z=sum(updateD)
        return [updateD[i]/z for i in range(len(updateD))]
    def predict(self,xi):
        res=[self.alpha[i]*self.G[i].predict([xi]) for i in range(len(self.G))]
        return 1 if sum(res)>0 else -1
    def test(self,x,y):
        res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
        return sum(res)/len(y) 
if __name__=="__main__":
    cancer = load_breast_cancer()
    x=cancer.data
    y=cancer.target
    y[y==0]=-1
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5)
    classifier = AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3),
        n_estimators=50
    )
    classifier.fit(x_train, y_train)
    print(classifier.test(x_train,y_train))
    print(classifier.test(x_test,y_test))

