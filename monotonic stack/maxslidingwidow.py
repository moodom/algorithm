#滑动窗口最大值   leetcode239. 滑动窗口最大值
#给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回滑动窗口中的最大值。
# 进阶：你能在线性时间复杂度内解决此题吗？

class MaxSlidingWindow:
    def maxslidingwidow(self,nums,k):
        dequeue=[]
        res=[]
        for i in range(len(nums)):
            while dequeue and nums[dequeue[-1]]<=nums[i]:
                dequeue.pop()
            dequeue.append(i)
            if dequeue[0]==i-k:
                dequeue.pop(0)
            if i>=k-1:
                res.append(nums[dequeue[0]])
        return res

            
