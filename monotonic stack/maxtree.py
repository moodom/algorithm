# 构造数组的MaxTree   
# 题目
# 一个数组的MaxTree定义如下:
# 数组必须没有重复元素
# maxTree是一棵二叉树，数组的每一个值对应一个二叉树节点
# 包括maxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头
# 有重复元素的数组arr,写出生成这个数组的MaxTree的函数,要求如果数组长度为N,则时间复杂度为O(N),空间复杂度为O(N)

# 建大根堆
# 1.使用大根堆的heapInsert调整
# 2.用层次遍历赋值

# 单调栈
class MaxTree:
    def maxtree(self,arr):
        maxDequeue=[]
        minDequeue=[]7