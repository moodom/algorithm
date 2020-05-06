# 全排列   leetcode46. 全排列
#给定一个 没有重复数字的序列，返回其所有可能的全排列。
# 示例:
# 输入: [1,2,3]
# 输出:
# [[1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]]
class Permute:
    # def permute(self,arr):
    #     self.res=[]
    #     self.cursion(arr,0,[])
    #     return self.res
    # def cursion(self,arr,i,tmp):     #递归
    #     if len(arr)==i:
    #         self.res.append(tmp.copy())
    #     else:
    #         for j in range(i+1):
    #             tmp.insert(j,arr[i])
    #             self.cursion(arr,i+1,tmp)
    #             tmp.pop(j)
    def permute(self,arr):
        res=[]
        cur=[[]]
        for i in range(len(arr)):
            for j in range(len(cur)):
                tmp=cur[j].copy()
                for k in range(len(tmp)+1):
                    tmp.insert(k,arr[i])
                    res.append(tmp)
            cur=res
        return res
if __name__=="__main__":
    a=[1,2,3]
    res=Permute().permute(a)
    print(res)

               
            