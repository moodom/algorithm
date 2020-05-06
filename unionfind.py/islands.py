# 岛问题   leetcode200. 岛屿数量
# 一个矩阵中只有0和1两种值,每个位置都可以和自己的上,下,左,右四个位置相连,
# 如果有一片1连在一起,这个部分叫做一个岛,求一个矩阵中有多少个岛？
# 举例
# 11110
# 11010
# 11000
# 00000
class IsLands:
    def islands(self,arr):
        if not arr or not arr[0]:
            return 0
        num=0
        row,col=len(arr),len(arr[0])
        for i in range(row):
            for j in range(col):
                if arr[i][j]==1:
                    num+=1
                    self.detection(arr,i,j,row,col)
        return num
    def detection(self,arr,i,j,row,col):
        if i<0 or i>=row or j<0 or j>=col or arr[i][j]!=1:return
        arr[i][j]=2
        self.detection(arr,i-1,j,row,col)
        self.detection(arr,i+1,j,row,col)
        self.detection(arr,i,j-1,row,col)
        self.detection(arr,i,j+1,row,col)
if __name__=="__main__":
    arr=[[1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,0],
        [0,0,0,0,0]]
    num=IsLands().islands(arr)
    print(num)


