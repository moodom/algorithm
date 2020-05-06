import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
import math
from decisiontreeID3 import InfoGain,ID3

class InfoGainRatio(InfoGain):
    def infoGainRatio(self,x,y):
        if not x.size:return None,None
        infogain=self.infoGain(x,y)
        n_samples,n_features=x.shape
        entropy_x=[0]*n_features
        for i in range(n_features):
            entropy_x[i]=self.empiricalEntropy(x[:,i])
        gain_ratio=[infogain[i]/entropy_x[i] for i in range(n_features)]
        return max(gain_ratio),gain_ratio.index(max(gain_ratio))
class C45(ID3):
    def __init__(self,sita=0.1): 
        super(C45,self).__init__(sita=sita) 
    def getInfoGain(self,x,y):
        return InfoGainRatio().infoGainRatio(x,y)

if __name__=="__main__":
    # x 年龄 有工作 有自己的房子 信贷情况  y 类别
    # 1 青年   否      否         一般      否
    # 2 中年   是      是          好       是
    # 3 老年                     非常好
    # x=np.array([[1,1,1,1],[1,1,1,2],[1,2,1,2],[1,2,2,1],[1,1,1,1],
    # [2,1,1,1],[2,1,1,2],[2,2,2,2],[2,1,2,3],[2,1,2,3],
    # [3,1,2,3],[3,1,2,2],[3,2,1,2],[3,2,1,3],[3,1,1,1]])
    # y=np.array([1,1,2,2,1,1,1,2,2,2,2,2,2,2,1])
    # print(InfoGainRatio().infoGainRatio(x,y))
    # c45=C45()
    # c45.fit(x,y)
    # print(c45.predict([1,1,1,1]))
    
    iris=load_iris()
    x=iris.data[:100,[0,3]]
    y=iris.target[:100]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    c45=C45()
    c45.fit(x,y)
    print(c45.test(x_train,y_train))
    print(c45.test(x_test,y_test))