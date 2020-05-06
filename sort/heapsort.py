class HeapSort: # 堆排序 时间复杂度O(N*logN) 空间复杂度O(1)
    def __init__(self,arr):
        self.arr=arr
        for i in range(len(self.arr)): #建立大根堆
            self.heapInsert(self.arr,i)
        for heapsize in reversed(range(len(self.arr))):
            self.swap(self.arr,0,heapsize)
            self.heapify(self.arr,0,heapsize)
    def swap(self,arr,a,b):
        arr[a],arr[b]=arr[b],arr[a]
    def heapInsert(self,arr,i):
        while (i-1)//2 >=0:
            if arr[(i-1)//2]<arr[i]:
                self.swap(arr,(i-1)//2,i)
                i=(i-1)//2
            else:break
    def heapify(self,arr,loc,hepsize): #heapsize没有取到边界值
        while loc*2+1<hepsize:
            largest=loc*2+2 if loc*2+2<hepsize and arr[loc*2+2]>arr[loc*2+1] else loc*2+1
            if arr[largest]>arr[loc]:
                self.swap(arr,largest,loc)
                loc=largest
            else:break
def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,HeapSort)
if __name__=="__main__":
    main()
