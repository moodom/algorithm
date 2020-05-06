# 二叉樹的序列化和反序列化    leetcode297. 二叉树的序列化与反序列化
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SerializeTree:
    def preSerializeTree(self, root):   # 前序序列化
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:return []
        res,stack="",[root]
        while stack:
            tmp=stack.pop()
            if not tmp:
                res+="#!"
                continue
            res+=str(tmp.val)+"!"
            stack.append(tmp.right)
            stack.append(tmp.left)
        print(res)
        return res

class ReconstructTree:
    def transforDidit(self,string):
        res=[]
        Nodes=string.split("!")
        for Node in Nodes:
            if Node=="#":res.append(None)
            elif Node=="":continue 
            else:res.append(int(Node))
        print(res)
        return res
    def preReconstructTree(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        nums=self.transforDidit(data)
        cur=root=TreeNode(nums.pop(0))
        stack=[root]
        last=cur
        Rlast=None
        while nums:
            num=nums.pop(0)
            if num is not None:
                cur=TreeNode(num)
                if cur and not Rlast:
                    stack.append(cur)
                    last.left=cur
                    last=cur
                else:
                    stack.append(cur)
                    Rlast.right=cur
                    last=cur
                    Rlast=None
            else:
                Rlast=stack.pop() if stack else None
        return root 
        
def testTree():
    node1=TreeNode(1)
    node2=node1.left=TreeNode(2)
    node3=node1.right=TreeNode(3)
    node4=node3.left=TreeNode(4)
    node5=node3.right=TreeNode(5)
    return node1
if __name__=="__main__":
    root=testTree()
    res=SerializeTree().preSerializeTree(root)
    print(res)
    ReconstructTree().preReconstructTree(res)