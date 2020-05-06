# 二叉树的先序遍历  leetcode144. 二叉树的前序遍历
class Node:     
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class PreTraversal:
    def pretraversal_1(self,root):   # 递归
        if not root: return []
        else:
            return [root.val]+self.pretraversal_1(root.left)+self.pretraversal_1(root.right)
    def pretraversal_2(self,root):  # 非递归
        if not root:return []
        res=[]
        stack=[root]
        while stack:
            tmp=stack.pop()
            res.append(tmp.val)
            if tmp.right:stack.append(tmp.right)
            if tmp.left:stack.append(tmp.left)
        return res






