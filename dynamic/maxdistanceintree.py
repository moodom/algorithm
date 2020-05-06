# 求一颗二叉树上的最远距离 (树形DP)
# 二叉树中,一个节点可以往上走和往下走,那么从节点A总能走到节点B
# 节点A走到节点B的距离为: A走到B最短路径上的节点个数
# 求一颗二叉树上的最远距离
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def maxDistanceInTree(self,head):
        res=self.search(head)
        return res['maxSize']
    def search(self,node):
        if node is None:
            return {'maxSize':0,'leftSize':0,'rightSize':0}
        L=self.search(node.left)
        R=self.search(node.right)
        leftSize=max(L['leftSize'],L['rightSize'])+1
        rightSize=max(R['leftSize'],R['rightSize'])+1
        maxSize=max(L['maxSize'],R['maxSize'],leftSize+rightSize-1)
        return {'maxSize':maxSize,'leftSize':leftSize,'rightSize':rightSize}
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
    print(Solution().maxDistanceInTree(head))
if __name__=="__main__":
    test()