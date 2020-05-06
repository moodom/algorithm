# 累加和为目标值的最长子数组 leetcode325 和等于k的最长子数组长度
# 奇数偶数长度相等的最长子数组(奇数为1,偶数为-1,求累加和为0的最长子数组)
#给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。
# 注意:
#  nums 数组的总和是一定在 32 位有符号整数范围之内的。
# 示例 1:
# 输入: nums = [1, -1, 5, -2, 3], k = 3
# 输出: 4 
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
# 示例 2:
# 输入: nums = [-2, -1, 2, 1], k = 1
# 输出: 2 
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。
# 进阶:
# 你能使时间复杂度在 O(n) 内完成此题吗?
class Solutiion():
    def maxSubArrayLen(self,nums,k):
        cur_sum=0
        sum_index={0:-1}
        res=0
        for i,num in enumerate(nums):
            cur_sum+=num
            if cur_sum-k in sum_index.keys():
                res=max(res,i-sum_index[cur_sum-k])
            if cur_sum not in sum_index.keys():
                sum_index[cur_sum]=i
        return res 
if __name__=="__main__":
    nums=[-2, -1, 2, 1]
    k=1
    print(Solutiion().maxSubArrayLen(nums,k))    

