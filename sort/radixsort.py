class RadixSort: # 基数排序  时间复杂度O(N) 空间复杂度O(N)
    def __init__(self,arr):
        self.arr=arr 
        self._radixsort(self.arr)
    def _radixsort(self,arr):
        


def rightMethod(arr):
    arr.sort()
def main():
    import sys
    sys.path.append('./test/')
    from D1array import D1Test
    D1Test().compare(rightMethod,RadixSort)
if __name__=="__main__":
    main()