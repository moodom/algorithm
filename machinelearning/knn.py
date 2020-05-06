# 存在bug

# K近邻模型
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as KNN
from collections import Counter
class Data:
    def __init__(self,xi,yi):
        self.xi=xi
        self.yi=yi
class KDNode:
    def __init__(self,data=[]):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
class BalancedKDTree:
    def getroot(self,x,y):
        self.datas=[Data(xi=xi,yi=yi) for xi,yi in zip(x,y)]
        self.n_samples,self.n_features=x.shape
        mid=self.getMedian(self.datas,0,self.n_samples,0)
        root=KDNode(data=self.datas[mid])
        self.createKDTree(root,0,mid,self.n_samples-1,0)
        return root
    def quicksort(self,datas,left,right,fea_i): #[left,right)
        if left>=right:return
        key=datas[left]
        i,j=left,right-1
        while i<j:
            while i<j and key.xi[fea_i]<=datas[j].xi[fea_i]:
                j-=1
            datas[i]=datas[j]
            while i<j and datas[i].xi[fea_i]<key.xi[fea_i]:
                i+=1
            datas[j]=datas[i]
        datas[i]=key
        self.quicksort(datas,left,i,fea_i)
        self.quicksort(datas,i+1,right,fea_i)
    def getMedian(self,datas,start,end,fea_i): #[start,end)
        self.quicksort(datas,start,end,fea_i)
        mid=start+(end-start)//2
        return mid
    def createKDTree(self,root,start,mid,end,fea_i):#[start,end]
        fea_i=(fea_i+1)%self.n_features
        if start<mid:
            m=self.getMedian(self.datas,start,mid,fea_i)
            leftchild=root.left=KDNode(data=self.datas[m])
            leftchild.parent=root
            self.createKDTree(leftchild,start,m,mid-1,fea_i)
        if mid<end:
            m=self.getMedian(self.datas,mid+1,end+1,fea_i)
            rightchild=root.right=KDNode(data=self.datas[m])
            rightchild.parent=root
            self.createKDTree(rightchild,mid+1,m,end,fea_i)
        return
    

class KNeighborsClassifier(object):
    def __init__(self,k=1):
        self.k=k
    def fit(self,x,y):
        self.n_samples,self.n_features=x.shape
        self.root=BalancedKDTree().getroot(x,y)
    def predict(self,xi):
        leafNode=self.searchLeafNode(xi,self.root,0)
        self.nearst=[]
        for _ in range(self.k):
            nearst=self.searchNearst(xi,leafNode,[None,float("inf")])# [[node,distance]]
            if nearst[0]:self.nearst.append(nearst)
        return self.getMaxC(self.nearst)
    def getMaxC(self,nearst):
        hash_dict={}
        for n in nearst:
            if n[0].yi not in hash_dict.keys():
                hash_dict[n[0].yi]=1
            else:hash_dict[n[0].yi]+=1
        maxC,num=-1,0
        for key in hash_dict.keys():
            (maxC,num)=(key,hash_dict[key]) if hash_dict[key]>num else (maxC,num)
        return maxC
    def searchLeafNode(self,xi,root,fea_i):  
        if not root.left and not root.right:return root
        tmp=root.data.xi
        if xi[fea_i]<=tmp[fea_i] and root.left:
            return self.searchLeafNode(xi,root.left,(fea_i+1)%self.n_features)
        elif xi[fea_i]>tmp[fea_i] and root.right:
            return self.searchLeafNode(xi,root.right,(fea_i+1)%self.n_features)
    def searchNearst(self,xi,node,nearst):
        if not node: return nearst
        s=self.eucliDist(node.data.xi,xi)
        nearst=[node.data,s] if s<nearst[1] and node.data not in self.nearst else nearst
        if node.parent: 
            if node.parent.left==node:
                anotherNode=node.parent.right
            else:anotherNode=node
            if anotherNode:
                s=self.eucliDist(anotherNode.data.xi,xi)
                if s<nearst[1]:
                    nearst=[anotherNode.data.xi,s]
                    nextNode=anotherNode.left if anotherNode.left else anotherNode.right
                    nearst=self.searchNearst(xi,nextNode,nearst)
        nearst=self.searchNearst(xi,node.parent,nearst)
        return nearst
    def eucliDist(self,A,B):
        return np.sqrt(sum(np.power((A - B), 2)))
    def test(self,x,y):
        res=[self.predict(xi)==yi for xi,yi in zip(x,y)]
        return sum(res)/len(y)
def rightMethod(x,y,x_train,y_train):
    knn=KNN(1)
    knn.fit(x_train,y_train)
    res1=[knn.predict([xi])==yi for xi,yi in zip(x_train,y_train)]
    res2=[knn.predict([xi])==yi for xi,yi in zip(x,y)]
    return sum(res1)/len(y_train),sum(res2)/len(y)
if __name__=="__main__":
    iris=load_iris()
    x=iris.data[:100,[0,2]]
    y=iris.target[:100]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    knn=KNeighborsClassifier()
    knn.fit(x_train,y_train)
    print(knn.test(x_train,y_train))
    # print(knn.test(x_test,y_test))  
    # print(rightMethod(x_test,y_test,x_train,y_train))
    # x = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
    # y = np.array([1, 1, 1, 2, 2, 2])
    # root=BalancedKDTree().getroot(x,y)
    



        


        
    



