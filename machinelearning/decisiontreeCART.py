# 剪枝还没完成
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
from decisiontreeID3 import ID3
import math
class Gini(object):
    def singleGini(self,x):
        n_samples=x.shape[0]
        count_x=Counter(x)
        g=0
        for key in count_x.keys():
            g+=(count_x[key]/n_samples)**2
        return 1-g 
    def conditionGini(self,x,y):
        n_samples,n_features=x.shape
        g_y_x=[]
        for i in range(n_features):
            xi=x[:,i]
            count_xi=Counter(xi)
            g={}
            for key in count_xi.keys():
                gini=(len(y[xi==key])*self.singleGini(y[xi==key])+len(y[xi!=key])*self.singleGini(y[xi!=key]))/n_samples
                g[key]=gini
            g_y_x.append(g)
        return g_y_x
    def chosebest(self,x,y):
        g_y_x=self.conditionGini(x,y)
        axis,fea,minGini=None,None,float("inf")
        for i in range(len(g_y_x)):
            for key in g_y_x[i].keys():
                if g_y_x[i][key]<minGini:
                    axis,fea,minGini=i,key,g_y_x[i][key]
        return axis,fea
class CARTNode(object):
    def __init__(self,x=None,label=None,left=None,right=None,y=None):
        self.x=x        # 特征
        self.label=label # 子节点分类依据的特征
        self.left=left   # 左边子节点存放最优切分面
        self.right=right # 右边子节点点存放其他的
        self.y=y        # 类标记(叶节点才有)  
    def predict(self,feature):
        if self.y is not None:
            return self.y
        else:
            if self.left.x==feature[self.label]:
                return self.left.predict(feature)
            else:
                return self.right.predict(feature)
class CART(ID3):
    def __init__(self):
        pass
    def fit(self,x,y):
        self.root=CARTNode()
        self.createTree(self.root,x,y)
    def createTree(self,node,x,y):
        if len(set(y))==1:      #所有示例属于同一类
            node.y=y[0]
            return
        if x.shape[0]==0:
            node.y=self.maxCategory(y)
            return 
        axis,fea=Gini().chosebest(x,y)
        if axis is None:
            node.y=self.maxCategory(y)
            return
        else:
            node.label=axis
            next_x = np.delete(x, axis, axis=1)
            tmp=node.left=CARTNode(x=fea)
            self.createTree(tmp,next_x[x[:,axis]==fea],y[x[:,axis]==fea])
            tmp=node.right=CARTNode()
            self.createTree(tmp,next_x[x[:,axis]!=fea],y[x[:,axis]!=fea])
            return
    def pruneTree(self,node):


if __name__=="__main__":
    # x 年龄 有工作 有自己的房子 信贷情况  y 类别
    # 1 青年   否      否         一般      否
    # 2 中年   是      是          好       是
    # 3 老年                     非常好
    # x=np.array([[1,1,1,1],[1,1,1,2],[1,2,1,2],[1,2,2,1],[1,1,1,1],
    # [2,1,1,1],[2,1,1,2],[2,2,2,2],[2,1,2,3],[2,1,2,3],
    # [3,1,2,3],[3,1,2,2],[3,2,1,2],[3,2,1,3],[3,1,1,1],[1,1,1,1]])
    # y=np.array([1,1,2,2,1,1,1,2,2,2,2,2,2,2,1,2])
    # cart=CART()
    # cart.fit(x,y)
    # print(cart.test(x,y))

    iris=load_iris()
    x=iris.data[:100,[0,3]]
    y=iris.target[:100]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    cart=CART()
    cart.fit(x,y)
    print(cart.test(x_train,y_train))
    print(cart.test(x_test,y_test))
    
   