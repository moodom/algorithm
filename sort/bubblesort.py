class BubbleSort: # 冒泡排序 时间复杂度O(N^2),空间复杂度O(1)
    def __init__(self,arr):
        self.arr=arr
        self._bubblesort(self.arr)
    def _bubblesort(self,arr):
        for end in reversed(range(len(arr))):
            for i in range(end):
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,BubbleSort)
if __name__=="__main__":
    main()