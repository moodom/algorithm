# 零钱兑换 leetcode322 零钱兑换
# 给定不同面额的硬币coins和一个总金额amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 示例 1:
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 示例 2:
# 输入: coins = [2], amount = 3
# 输出: -1
class Solution:
    #------------------暴力-----------------------------------
    # def coinChange(self, coins,amount):
    #     length=len(coins)
    #     def dfs(index,remain,num):
    #         res=-1
    #         if index==length:
    #             return num if remain==0 else -1
    #         count=remain//coins[index]
    #         for i in range(count+1):
    #             tmp=dfs(index+1,remain-coins[index]*i,num+i)
    #             res=tmp if res==-1 or (tmp<res and tmp!=-1) else res
    #         return res
    #     return dfs(0,amount,0) 
    #-------------------记忆化搜索------------------------------
    def coinChange(self, coins,amount):
        length=len(coins)
        remainMap=dict()
        def dfs(index,remain,num):
            res=-1
            if index==length:
                return num if remain==0 else -1
            for index in range(len(coins)):
                count=remain//coins[index]
                for i in range(count+1):
                    nextAim=remain-coins[index]*i
                    if nextAim in remainMap.keys():
                        tmp=remainMap[nextAim]+i if remainMap[nextAim]!=-1 else -1
                    else:
                        tmp=dfs(index+1,nextAim,num+i)
                    if tmp!=-1:
                        res=min(tmp,res) if res!=-1 else tmp
            remainMap[remain]=res
            return res
        return dfs(0,amount,0) 
    #--------------------动态规划-------------------------------
    # def coinChange(self, coins,amount):
    #     dp=[-1]*(amount+1)
    #     dp[0]=0
    #     for coin in coins:
    #         for i in range(coin,amount+1):
    #             tmp=dp[i-coin]+1 if dp[i-coin]!=-1 else -1
    #             if tmp!=-1:
    #                 dp[i]=min(dp[i],tmp) if dp[i]!=-1 else tmp
    #     return dp[-1]

if __name__=="__main__":
    coins=[1,2,5,10]
    amount=18
    print(Solution().coinChange(coins,amount))

