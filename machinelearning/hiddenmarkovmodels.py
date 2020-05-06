import numpy as np
import matplotlib.pyplot as plt 
import tushare as ts 
from hmmlearn.hmm import GaussianHMM

class HMM(object):
    def __init__(self,pi,A,b):
        self.pi=pi 
        self.A=A 
        self.b=b 
    def forward(self):
        

if __name__=="__main__":
    A=[[0.5,0.2,0.3],[0.3,0.5,0.2],[0.2,0.3,0.5]]
    B=[[0.5,0.5],[0.4,0.6],[0.7,0.3]]
    pi=[0.2,0.4,0.4]
    hmm=HMM(pi,A,B)
    