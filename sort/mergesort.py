class MergeSort: # 归并排序 时间复杂度O(N*logN) 空间复杂度(N)
    def __init__(self,arr):
        self.arr=arr
        self.sortProcess(self.arr,0,len(self.arr))
    def sortProcess(self,arr,L,R): # 左闭右开
        if L>=R-1:return
        mid=L+((R-L)>>1)
        self.sortProcess(arr,L,mid)
        self.sortProcess(arr,mid,R)
        self.merge(arr,L,mid,R)
    def merge(self,arr,L,mid,R):
        tmp=[0]*(R-L)
        i,L_start,L_end=0,L,mid
        while L<L_end and mid<R:
            if arr[L]<arr[mid]:
                tmp[i]=arr[L]
                L+=1;i+=1
            else:
                tmp[i]=arr[mid]
                mid+=1;i+=1
        tmp[i:]=arr[L:L_end] if mid==R else arr[mid:R]
        arr[L_start:R]=tmp
def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test(size=5).compare(rightMethod,MergeSort)
if __name__=="__main__":
    main()