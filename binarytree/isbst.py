# 判斷一棵樹是否是搜索二叉樹 leetcode98. 验证二叉搜索树 
# 注:這種遞歸不太會做，需要加强
# 這道題一種簡單的方法就是中序遍歷，判斷是否是有序數列
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class isBST:
    def isbst(self,root):
        # 递归法，动态缩减上下界范围，关键点是上下界的变化
        def compute_BST(root,max_ = float('inf'),min_ = float('-inf')):
            if not root:
                return True
            cur = root.val
            if cur >= max_ or cur <= min_:
                return False
            if not compute_BST(root.left,cur,min_):
                return False
            if not compute_BST(root.right,max_,cur):
                return False
            return True
        return compute_BST(root)
def testTree():
    node1=TreeNode(10)
    node2=node1.left=TreeNode(5)
    node3=node1.right=TreeNode(15)
    node4=node3.right=TreeNode(6)
    node5=node3.right=TreeNode(20)
    return node1
if __name__=="__main__":
    root=testTree()
    res=isBST().isbst(root)
    print(res)       


    
