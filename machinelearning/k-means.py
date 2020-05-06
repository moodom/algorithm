import random
import numpy as np
from sklearn.cluster import KMeans
# data = np.random.rand(100, 3) #生成一个随机数据，样本大小为100, 特征数为3
# #假如我要构造一个聚类数为3的聚类器
# estimator = KMeans(n_clusters=3)#构造聚类器
# estimator.fit(data)#聚类
# label_pred = estimator.labels_ #获取聚类标签
# centroids = estimator.cluster_centers_ #获取聚类中心
# inertia = estimator.inertia_ # 获取聚类准则的总和
# print(label_pred)
# print(centroids)
# print(inertia)

class myKMeans(object):
    def __init__(self,k=3,sita=0.00001,max_iters=300):
        self.k=k
        self.sita=sita
        self.max_iters=max_iters
    def fit(self,x):
        n_samples,n_features=x.shape
        #x=self.normalize(x)
        self.centroids=[x[random.randint(0,n_samples)] for _ in range(self.k)]
        for _ in range(self.max_iters):
            new_centroids=self.updateCenter(x,self.centroids)
            for i in range(len(self.centroids)):
                if sum(abs(new_centroids[i]-self.centroids[i]))>self.sita:
                    self.centroids=new_centroids
                    break 
            else:
                self.centroids=new_centroids
                break
    def updateCenter(self,x,centroids):
        n_samples,n_features=x.shape
        x_center=np.array([self.nearstCentroids(xi,centroids) for xi in x])
        for i in range(self.k):
            x_k=x[x_center==i]
            for j in range(n_features):
                centroids[i][j]=np.mean(x_k[:,j])
        return centroids
    def nearstCentroids(self,xi,centroids):
        dist=[]
        for centroid in centroids:
            dist.append(self.eucliDist(xi,centroid))
        return dist.index(min(dist))
    def eucliDist(self,A,B):
        return np.sqrt(sum(np.power((A - B), 2)))
    def getCentroids(self):
        return self.centroids
if __name__=="__main__":
    data = np.random.rand(100, 3) #生成一个随机数据，样本大小为100, 特征数为3
    kmeans=myKMeans()
    kmeans.fit(data)
    print(kmeans.getCentroids())
    estimator = KMeans(n_clusters=3)#构造聚类器
    estimator.fit(data)#聚类
    centroids = estimator.cluster_centers_ #获取聚类中心
    print(centroids)