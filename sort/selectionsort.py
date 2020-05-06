class SelectionSort: # 选择排序 时间复杂度 O(N^2) 空间复杂度O(1)
    def __init__(self,arr):
        self.arr=arr
        self._selectionsort(self.arr)
    def _selectionsort(self,arr):
        for start in range(len(arr)):
            index=start
            for i in range(start,len(arr)):
                index=i if arr[i]<arr[index] else index
            arr[start],arr[index]=arr[index],arr[start]


def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,SelectionSort)

if __name__=="__main__":
    main()