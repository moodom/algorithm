# 零钱兑换  leetcode518. 零钱兑换 II
#给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
#示例 1:
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2:
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 示例 3:
# 输入: amount = 10, coins = [10] 
# 输出: 1
class Solution:
    #------------------- 暴力------------------------
    #def change(self, amount,coins):
        # if amount==0 and coins==[]:return 1
        # length=len(coins)
        # remainMap=dict()
        # def dfs(remain,index):
        #     res=0
        #     if index==length:
        #         res=1 if remain==0 else 0
        #     else:
        #         count=remain//coins[index]
        #         for i in range(count+1):
        #             res+=dfs(remain-coins[index]*i,index+1)
        #     return res
        # return dfs(amount,0)
    #--------------------记忆化搜索-------------------------
    # def change(self,amount,coins):
    #     if amount==0 and coins==[]:return 1
    #     length=len(coins)
    #     remainMap=dict()
    #     def dfs(remain,index):
    #         res=0
    #         if index==length:
    #             res=1 if remain==0 else 0
    #         else:
    #             count=remain//coins[index]
    #             for i in range(count+1):
    #                 nextAim=remain-coins[index]*i
    #                 if (nextAim,index+1) in remainMap.keys():
    #                     res+=remainMap[(nextAim,index+1)]
    #                 else:
    #                     res+=dfs(nextAim,index+1)
    #         remainMap[(remain,index)]=res
    #         return res
    #     return dfs(amount,0)
    #------------------- 动态规划-------------------------------
    def change(self,amount,coins):
        if amount==0 and coins==[]:return 1
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for i in range(coin,amount+1):
                    dp[i]+=dp[i-coin]
        return dp[-1]

if __name__=="__main__":
    amount=500
    coins=[1,2,5]
    print(Solution().change(amount,coins))