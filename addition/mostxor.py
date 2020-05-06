# 最大异或和问题
# 定义数组的异或和的概念： 数组中所有的数异或起来，得到的结果叫做数组的异或和， 比如数组{3,2,1}的异或和是，3^2^1 = 0
# 给定一个数组arr，你可以任意把arr分成很多不相容的子数组，你的目的是： 分出来的子数组中，异或和为0的子数组最多。
# 请返回：分出来的子数组中，异或和为0的子数组最多是多少

class Solution():
    def mostXOR(self,nums):
        cur_xor=0
        length=len(nums)
        dp=[0]*length
        xor_dict={0:-1}
        for i,num in enumerate(nums):
            cur_xor^=num
            if cur_xor in xor_dict.keys():
                dp[i]=1 if xor_dict[cur_xor]==-1 else dp[xor_dict[cur_xor]]+1
            if i>1:
                dp[i]=max(dp[i],dp[i-1])
            xor_dict[cur_xor]=i
        return dp[-1] 
                
if __name__=="__main__":
    nums=[1,2,3,0,3,2,1,0]
    print(Solution().mostXOR(nums))

