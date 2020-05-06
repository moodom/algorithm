# 二叉树的先序遍历          leetcode145. 二叉树的后序遍历
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class PosTraversal:
    def postraversal_1(self,root):   # 递归
        if not root: return []
        else:
            return self.postraversal_1(root.left)+self.postraversal_1(root.right)+[root.val]
    def postraversal_2(self,root):  # 非递归
        if not root: return []
        res=[]
        stack=[root]
        while stack:
            tmp=stack.pop()
            res.append(tmp.val)
            if tmp.left:stack.append(tmp.left)
            if tmp.right:stack.append(tmp.right)
        return res[::-1]
