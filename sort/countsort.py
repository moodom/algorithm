class CountSort: # 计数排序 时间复杂度O(N), 空间复杂度O(N)
    def __init__(self,arr):
        self.arr=arr
        self._bucketsort(self.arr)
    def _countsort(self,arr): #only for 有限数组
        if len(arr)<2:return
        maxNum=max(arr)
        minNum=min(arr)
        bucket=[0]*(maxNum-minNum+1)
        for num in arr:
            bucket[num-minNum]+=1
        index=0
        for i in range(maxNum-minNum+1):
            while bucket[i]:
                arr[index]=i+minNum
                bucket[i]-=1;index+=1
def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,CountSort)
if __name__=="__main__":
    main()