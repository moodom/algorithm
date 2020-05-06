# 二叉树中的最大搜索二叉子树 (树形DP)
# 给定一颗二叉树的头节点head，已知其中所有节点的值都不一样，找到含有节点最多的搜索二叉子树，并返回这棵子树的头节点
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def maxSearchSubTree(self,root):
        res=self.search(root)
        return res["head"]
    def search(self,node):
        if node is None:
            return{'size':0,'head':None,'min':float("-inf"),'max':float("inf")}
        L=self.search(node.left)
        R=self.search(node.right)
        if L['head'] is None and R['head'] is None:
            return {'size':1,'head':node,'min':node.val,'max':node.val}
        elif L['head']==node.left and R['head']==node.right and L['max']<node.val<R['min']:
            return {'size':L['size']+R['size']+1,'head':node,'min':L['min'],'max':R['max']}
        else:
            return L if L['size']>R['size'] else R
def test():
    head=TreeNode(6)
    head.left=TreeNode(1)
    head.left.left=TreeNode(0)
    head.left.right=TreeNode(3)
    head.right=TreeNode(12)
    head.right.left = TreeNode(10)
    head.right.left.left = TreeNode(4)
    head.right.left.left.left = TreeNode(2)
    head.right.left.left.right = TreeNode(5)
    head.right.left.right = TreeNode(14)
    head.right.left.right.left = TreeNode(11)
    head.right.left.right.right = TreeNode(15)
    head.right.right = TreeNode(13)
    head.right.right.left = TreeNode(20)
    head.right.right.right = TreeNode(16)
    print(Solution().maxSearchSubTree(head))
if __name__=="__main__":
    test()
