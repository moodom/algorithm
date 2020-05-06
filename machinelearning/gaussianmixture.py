# 有bug 主要多维的高斯分布没考虑清楚
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import math
from sklearn.datasets.samples_generator import make_blobs
#产生实验数据
# from sklearn.datasets.samples_generator import make_blobs
# X, y_true = make_blobs(n_samples=400, centers=4,
#                        cluster_std=0.60, random_state=0)
# from sklearn.mixture import GMM
# gmm = GMM(n_components=4).fit(X)
# labels = gmm.predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
# plt.show()

class GMM(object):
    def __init__(self,n_components=4,sita=0.001,max_iters=300):
        self.n_components=n_components
        self.sita=sita
        self.max_iters=max_iters
    def fit(self,x):
        n_samples,n_features=x.shape
        self.mu=np.zeros((self.n_components,n_features))
        self.square_sigma=np.ones((self.n_components,n_features))
        self.alpha=np.ones((self.n_components,n_features))
        for _ in range(self.max_iters):
            gama=self.stepE(x,self.mu,self.square_sigma,self.alpha)
            new_mu,new_square_sigma,new_alpha=self.stepM(x,gama,self.mu,self.square_sigma,self.alpha)
            for i in range(self.n_components):
                if abs(self.mu[i]-new_alpha[i])>self.sita:
                    self.mu,self.square_sigma,self.alpha=new_mu,new_square_sigma,new_alpha
                    break
            else:
                self.mu,self.square_sigma,self.alpha=new_mu,new_square_sigma,new_alpha
                break 
    def stepE(self,x,mu,square_sigma,alpha):
        n_samples,n_features=x.shape
        gama=np.zeros((self.n_components,n_features))
        for j in range(n_samples):
            tmp=0
            for k in range(self.n_components):
                gama[j][k]=alpha[k]*self.gaussian(x[j],mu[k],square_sigma[k])
                tmp+=gama[j][k]
            for k in range(self.n_components):
                gama[j][k]=gama[j][k]/tmp
        return gama
    def stepM(self,x,gama,mu,square_sigma,alpha):
        n_samples=x.shape[0]
        for k in range(self.n_components):
            tmp_mu=0
            tmp_sigma=0
            tmp_alpha=0
            for j in range(n_samples):
                tmp_mu+=gama[j][k]*x[j]
                tmp_sigma+=gama[j][k]*(x[j]-mu[k])**2
                tmp_alpha+=gama[j]
            mu[k]=tmp_mu/tmp_alpha
            square_sigma[k]=tmp_sigma/tmp_alpha
            alpha[k]=tmp_alpha/n_samples
        return mu,square_sigma,alpha
    def gaussian(self,xi,muk,square_sigmak):
        print(x)
        print(muk)
        print(square_sigmak)
        return math.exp((-(xi-muk)**2)/(2*square_sigmak))/math.sqrt(2*math.pi*muk**2)


if __name__=="__main__":
    x, y_true = make_blobs(n_samples=400, centers=4,
                        cluster_std=0.60, random_state=0)
    gmm=GMM()
    gmm.fit(x)