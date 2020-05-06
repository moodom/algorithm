# 二叉树的中遍历    leetcode94. 二叉树的中序遍历
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class InTraversal:
    def intraversal_1(self,root):   # 递归
        if not root: return []
        else:
            return self.intraversal_1(root.left)+[root.val]+self.intraversal_1(root.right)
    def intraversal_2(self,root): # 非递归
        if not root: return []
        res=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res




