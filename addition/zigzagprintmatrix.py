# "之"字形打印矩阵 (宏观调度)
# 题目：给定一个矩阵matrix,按照"之"字形的方式打印这个矩阵
# 例如：[[1,2,3,4],
#       [5,6,7,8],
#       [9,10,11,12]]
# "之"字形打印的结果是[1,2,5,9,6,3,4,7,10,11,8,12]
class ZigZagPrintMatrix:
    def __init__(self):
        self.res=[]
    def zigzagprintmatrix(self,arr):
        tR,tC,bR,bC=0,0,0,0
        mode=False
        while bR<len(arr) and tR<len(arr) and tC<len(arr[0]) and bC<len(arr[0]):
            self.zigPrint(arr,tR,tC,bR,bC,mode)
            mode=(mode==False)
            (tR,tC)=(0,tC+1) if (tC+1)<len(arr[0]) else (tR+1,tC)
            (bR,bC)=(bR+1,0) if (bR+1)<len(arr) else (bR,bC+1)
        return self.res
    def zigPrint(self,arr,tR,tC,bR,bC,mode):
        if mode==False:
            while tR<=bR and bC<=tC: 
                self.res.append(arr[bR][bC])
                bR-=1;bC+=1
        else:
            while tR<=bR and bC<=tC:
                self.res.append(arr[tR][tC])
                tR+=1;tC-=1 
                
if __name__=="__main__":
    a=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12]]
    res=ZigZagPrintMatrix().zigzagprintmatrix(a)
    print(res)
    
