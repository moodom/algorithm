# 决策树
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from collections import Counter
import math
# iris=load_iris()
# x=iris.data[:100,[0,2]]
# y=iris.target[:100]
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
# dtree=DecisionTreeClassifier()
# dtree.fit(x_train,y_train)
class InfoGain(object):
    def infoGain(self,x,y):            #信息增益
        if not x.size:return None,None
        n_samples,n_features=x.shape
        category_count=Counter(y)
        entropy_y=self.empiricalEntropy(y)
        gain=[0]*n_features
        for i in range(n_features):
            entropy_xi_y=self.conditionEntropy(x[:,i],y)
            gain[i]=entropy_y-entropy_xi_y
        return max(gain),gain.index(max(gain))
    def conditionEntropy(self,x,y):     #条件熵
        condEntropy=0
        n_samples=x.shape[0]
        feature_count=Counter(x)
        for fea in feature_count.keys():
            entropy=(feature_count[fea]/n_samples)*self.empiricalEntropy(y[np.where(x==fea)])
            condEntropy+=entropy
        return condEntropy
    def empiricalEntropy(self,x):        #经验熵
        entropy=0
        n_samples=x.shape[0]
        category_count=Counter(x)                     
        for key in category_count.keys():
            p=category_count[key]/n_samples
            entropy-=p*math.log2(p)
        return entropy
class Node:
    def __init__(self,x=None,label=None,y=None):
        self.x=x        # 特征
        self.label=label # 子节点分类依据的特征
        self.child=[]   # 子节点
        self.y=y        # 类标记(叶节点才有)  
    def append(self,node):
        self.child.append(node)
    def predict(self,feature):
        if self.y is not None:
            return self.y
        else:
            for c in self.child:
                if c.x==feature[self.label]:
                    return c.predict(feature)
class ID3(object):
    def __init__(self,sita=0.1): #sita为阈值
        self.sita=sita 
    def fit(self,x,y):
        self.root=Node()
        self.createTree(self.root,x,y)
    def predict(self,xi):
        return self.root.predict(xi)
    def test(self,x,y):
        res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
        return sum(res)/len(y)
    def maxCategory(self,y):
        max_y,max_y=0,-1
        count_y=Counter(y)
        for key in count_y.keys():
            (max_y,max_key)=(count_y[key],key) if count_y[key]>max_y else (max_y,max_key)
        return max_key
    def getInfoGain(self,x,y):
        return InfoGain().infoGain(x,y)
    def createTree(self,node,x,y):
        if len(set(y))==1:   #所有示例属于同一类
            node.y=y[0]
            return 
        if x.shape[0]==0:        # 没有训练集
            node.y=self.maxCategory(y)
            return 
        max_gain,index=self.getInfoGain(x,y)
        if max_gain is None or max_gain<self.sita:
            node.y=self.maxCategory(y)
            return 
        else:
            node.label=index
            xi_set=set(x[:,index])
            next_x = np.delete(x, index, axis=1)
            for xi in xi_set:
                tmp=Node(x=xi)
                node.append(tmp)
                self.createTree(tmp,next_x[x[:,index]==xi],y[x[:,index]==xi])
            return 

if __name__=="__main__":
    # x 年龄 有工作 有自己的房子 信贷情况  y 类别
    # 1 青年   否      否         一般      否
    # 2 中年   是      是          好       是
    # 3 老年                     非常好
    # x=np.array([[1,1,1,1],[1,1,1,2],[1,2,1,2],[1,2,2,1],[1,1,1,1],
    # [2,1,1,1],[2,1,1,2],[2,2,2,2],[2,1,2,3],[2,1,2,3],
    # [3,1,2,3],[3,1,2,2],[3,2,1,2],[3,2,1,3],[3,1,1,1],[1,1,1,1]])
    # y=np.array([1,1,2,2,1,1,1,2,2,2,2,2,2,2,1,2])
    # id3=ID3()
    # id3.fit(x,y)
    # print(id3.predict([1,1,1,1]))
    # print(id3.test(x,y))

    iris=load_iris()
    x=iris.data[:100,[0,3]]
    y=iris.target[:100]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    id3=ID3()
    id3.fit(x,y)
    print(id3.test(x_train,y_train))
    print(id3.test(x_test,y_test))
    