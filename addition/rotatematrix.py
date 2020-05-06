# 旋转正方形矩阵 (宏观调度问题)
# 给定一个整型正方形matrix,请把该矩阵调整成顺时针旋转90度的样子.
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10,11,12],
# [13,14,15,16]]
# 输出为
# [[13, 9, 5, 1],
# [14, 10, 6, 2],
# [15, 11, 7, 3],
# [16, 12, 8, 4]]
# 要求：空间复杂度为O(1)
class RotateMatrix:
    def rotatematrix(self,arr):
        if not arr: return []
        for i in range((len(arr)+1)//2):
            self.rotateEdge(arr,i,len(arr)-1)
        return arr
    def rotateEdge(self,arr,start,c):
        for i in range(start+1,c-start+1):
            tmp=arr[start][i]
            arr[start][i]=arr[c-i][start]
            arr[c-i][start]=arr[c-start][c-i]
            arr[c-start][c-i]=arr[i][c-start]
            arr[i][c-start]=tmp
def rightMethod(arr): # 无脑转置加反转
    arrT=[list(item) for item in zip(*arr)]
    return [item[::-1] for item in arrT]


def main():
    import sys
    sys.path.append('./test/')
    from D2array import D2Test
    D2Test(sizes=[10,10]).compareRes(rightMethod,RotateMatrix().rotatematrix)
if __name__=="__main__":
    main()
    