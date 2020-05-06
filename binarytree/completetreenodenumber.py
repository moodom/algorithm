# 已知一顆完全二叉樹，求其節點的個數  leetcode222. 完全二叉树的节点个数
# 要求: 時間複雜度低於O(N),N為這棵樹的節點個數

# 一種簡單的遞歸便利,每次加1,時間複雜度為 O(N)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class CompleteTreeNodeNumber:  #利用完全二叉樹和滿二叉樹的性質,時間複雜度O(NlogN)
    def nodenumber(self,root):
        if not root:return 0
        res=0
        while root:
            Len,Rlen=self.isFullTree(root)
            if Len==Rlen:
                res+=2**Len-1;break
            else:
                Len,Rlen=self.isFullTree(root.left)
                if Len==Rlen:
                    res+=2**Len
                    root=root.right
                else:
                    res+=2**Rlen
                    root=root.left
        return res
    def isFullTree(self,root):
        Llen,Rlen=0,0
        leftroot=root
        rightroot=root
        while leftroot:
            Llen+=1
            leftroot=leftroot.left
        while rightroot:
            Rlen+=1
            rightroot=rightroot.right
        return Llen,Rlen

