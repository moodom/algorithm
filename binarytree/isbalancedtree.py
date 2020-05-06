# 判斷一棵二叉樹是否是平衡二叉樹 leetcode面试题55 - II. 平衡二叉树
# 套路1
# 所需要求的參數放在主函數作爲全局變量
# 再寫個遞歸處理好遞歸每次的數據以及和全局變量的關係
# 套路2
# 所需要求的參數和每次遞歸的數據都作爲變量變量傳遞
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class IsBalancedTree:                                     
    def depthTree(self,root):                         
        if not root: return 0                             
        leftdepth=self.depthTree(root.left)
        if not self.res:return 0
        rightdepth=self.depthTree(root.right)
        if not self.res:return 0
        if abs(leftdepth-rightdepth)>1:
            self.res=False
            return 0
        else:
            depth=max(leftdepth,rightdepth)+1
            return depth
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        self.res=True
        self.depthTree(root)
        return self.res
    # 套路2
    # def isBalanced(self, root: TreeNode) -> bool:
    #     d, s = self.helper(root)
    #     return s
        

    # def helper(self, root):
    #     if root is None: return 0, True
    #     ld, ls = self.helper(root.left)
    #     if not ls:  return None, False
    #     rd, rs = self.helper(root.right)
    #     if not rs:  return None, False

    #     if abs(ld-rd) <= 1:
    #         return max(ld, rd)+1, True
    #     else:
    #         return None, False
def testTree():
    # [1,2,2,3,3,null,null,4,4]
    node1=TreeNode(1)
    node2=node1.left=TreeNode(2)
    node3=node1.right=TreeNode(2)
    node4=node2.left=TreeNode(3)
    node5=node2.right=TreeNode(3)
    node6=node4.left=TreeNode(4)
    node7=node4.right=TreeNode(4)
    return node1
if __name__=="__main__":
    head=testTree()
    res=IsBalancedTree().isBalanced(head)
    print(res)
    