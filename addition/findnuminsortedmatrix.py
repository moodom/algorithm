# 在行列都排好序的矩阵中找数 (算法的最优解存在于数据的规律或者题目的问法)
# 题目
# 给定一个有N*M的整型矩阵matrix和一个整数K,matrix的每一行和每一列都是排好序的。实现一个函数，判断K是否在matrix中。
# 例如：
# [[0,1,2,5],
# [2,3,4,7],
# [4,4,4,8],
# [5,7,7,9]]
# 如果k为7,返回ture;如果k为6,返回false
class FindNumInSortedMatrix:
    def findnuminsortedmatrix(self,arr,num):
        if not arr:return False
        i,j=0,len(arr[0])-1
        while i<len(arr) and j>=0:
            if arr[i][j]==num:
                return True
            elif arr[i][j]>num:
                j-=1
            else:
                i+=1
        return False
if __name__=="__main__":
    arr=[[0,1,2,5],
        [2,3,4,7],
        [4,4,4,8],
        [5,7,7,9]]
    res=FindNumInSortedMatrix().findnuminsortedmatrix(arr,7)
    print(res)
