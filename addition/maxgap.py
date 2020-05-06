# 相邻两数最大差值问题 (桶排序)
# 问题
# 给定一个数组,求如果排序之后,相邻两数的最大差值,要求时间复杂度O(N),且要求不能用基于排序比较的排序
class MaxGap:
    def maxgap(self,arr):
        if len(arr)<2:return 0
        length=len(arr)
        minNum=min(arr)
        maxNum=max(arr)
        hashNums=[False]*(length+1)
        mins=[float("inf")]*(length+1)
        maxs=[float("-inf")]*(length+1)
        for num in arr:
            bid=self.bucket(num,length,minNum,maxNum)
            hashNums[bid]=True
            mins[bid]=min(mins[bid],num)
            maxs[bid]=max(maxs[bid],num)
        res=0
        i,j=0,1
        while j<=length:
            if hashNums[j]==False:
                j+=1;continue
            if hashNums[i]==False:
                i+=1;continue
            res=max(res,mins[j]-maxs[i])
            j+=1;i+=1
        return res
    def bucket(self,num,length,minNum,maxNum):
        return (num-minNum)*length//(maxNum-minNum)

def rightMethod(arr):
    if len(arr)<2:return 0
    sortedArr=sorted(arr)
    res=0
    for i in range(len(arr)-1):
        res=max(res,sortedArr[i+1]-sortedArr[i])
    return res
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test(size=20).compareRes(rightMethod,MaxGap().maxgap)
if __name__=="__main__":
    main()