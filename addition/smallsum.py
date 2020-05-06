# 小和问题 (归并排序)
# 在一个数组中,每一个数左边比当前数小的数累加起来,叫做这个数组的小和.求一个数组的小和.
# 例子:
# [1,3,4,2,5]
# 左边比1小的数,没有;
# 左边比3小的数,1;
# 左边比4小的数,1,3;
# 左边比2小的数,1;
# 左边比5小的数,1,3,4,2;
# 所以小和为 1+1+3+1+1+3+4+2=16
class SmallSum:
    def smallSum(self,arr):
        self.arr=arr.copy()
        return self.sortMerge(self.arr,0,len(self.arr))
    def sortMerge(self,arr,L,R):
        if L>=R-1:return 0
        mid=L+((R-L)>>1)
        return self.sortMerge(arr,L,mid)+self.sortMerge(arr,mid,R)+self.merge(arr,L,mid,R)
    def merge(self,arr,L,mid,R):
        tmp=[0]*(R-L)
        i,res=0,0
        L_start,L_end=L,mid
        while L<L_end and mid<R:
            if arr[L]<arr[mid]:
                tmp[i]=arr[L]
                res+=arr[L]*(R-mid)
                i+=1;L+=1
            else:
                tmp[i]=arr[mid]
                i+=1;mid+=1
        tmp[i:]=arr[L:L_end] if mid==R else arr[mid:R]
        arr[L_start:R]=tmp
        return res
def rightMethod(arr):
    res=0
    for end in range(len(arr)):
        for i in range(end):
            if arr[i]<arr[end]:
                res+=arr[i]
    return res
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compareRes(rightMethod,SmallSum().smallSum)
if __name__=="__main__":
    main()

