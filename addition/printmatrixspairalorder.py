# 转圈打印矩阵 (宏观调度)
# 题目
# 给定一个整型矩阵matrix,请按照转圈的方式答应它
# 例:
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10,11,12],
# [13,14,15,16]]
# 打印结果 [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]
# 要求 空间复杂度为 O(1)
class PrintMatrixSpiralOrder:
    def printmatrixspiralorder(self,arr):
        if not arr: return []
        imin,imax=0,len(arr)
        jmin,jmax=0,len(arr[0])
        res=[]
        while jmin<jmax and imin<imax:
            res.extend([arr[imin][j] for j in range(jmin,jmax)]);imin+=1
            if imin>=imax:break
            res.extend([arr[i][jmax-1] for i in range(imin,imax)]);jmax-=1
            if jmin>=jmax:break
            res.extend([arr[imax-1][j] for j in reversed(range(jmin,jmax))]);imax-=1
            if imin>=imax:break
            res.extend([arr[i][jmin] for i in reversed(range(imin,imax))]);jmin+=1
            if jmin>=jmax:break
        return res 
if __name__=="__main__":
    arr=[[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10,11,12],
        [13,14,15,16]]
    res=PrintMatrixSpiralOrder().printmatrixspiralorder(arr)
    print(res)
            




        


