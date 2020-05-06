# 判斷一棵樹是否是完全二叉樹 leetcode958. 二叉树的完全性检验
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class isValidCBT:
    def isvalidcbt(self,root):
        #层次遍历时，叶子节点为空。一但出现空，那么后续的值都必须时空。
        q = [root]
        has_none = False # 是否出现过空
        while q:
            p = q.pop(0) # 出队
            if not has_none and not p: # 第一次出现空
                has_none = True
            elif has_none and p: # 空后面出现了非空
                return False
            if p: # 子节点入队列，无论是否空
                q.extend([p.left, p.right])
        return True
