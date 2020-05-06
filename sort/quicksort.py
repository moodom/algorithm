import random
class QuickSort:  # 快速排序 时间复杂度O(N*logN) 空间复杂度O(logN)
    def __init__(self,arr):
        self.arr=arr
        self._quicksort(self.arr,0,len(arr))
    def _quicksort(self,arr,L,R): # 荷兰国旗问题改进版快速排序
        if L>=R-1:return
        p=self.partition(arr,L,R)
        self._quicksort(arr,L,p[0]) # 左闭右开
        self._quicksort(arr,p[1],R)
    def partition(self,arr,L,R):
        less,cur,more=L,L+1,R
        while cur<more:
            if arr[cur]<arr[L]:
                less+=1
                arr[cur],arr[less]=arr[less],arr[cur]
                cur+=1
            elif arr[cur]>arr[L]:
                more-=1 
                arr[cur],arr[more]=arr[more],arr[cur]
            else:
                cur+=1
        arr[less],arr[L]=arr[L],arr[less]
        return less+1,more
# def quickSort(arr,left,right): # 简单版快排
#         if left>right:
#             return 
#         key=L[left]
#         i,j=left,right
#         while i<j:
#             while i<j and key<=arr[j]:
#                 j-=1
#             arr[i]=arr[j]
#             while i<j and L[i]<key:
#                 i+=1
#             arr[j]=arr[i]
#         arr[i]=key
#         quick_sort(arr,left,i-1)
#         quick_sort(arr,i+1,right)
#     quick_sort(arr,0,len(arr)-1)
        
def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,QuickSort)
if __name__=="__main__":
    main()

    

    