# 在二叉樹中找到一個后继节点 leetcode510. 二叉搜索树中的中序后继 II
# 题目
# 现在有一种新的二叉树节点类型如下:
# class Node:     
#     def __init__(self,val):
#         self.val=val
#         self.parent=None 
#         self.left=None
#         self.right=None
# 该结构比普通二叉树节点结构多了一个指向父节点的parent指针。头节点的parent指向None
# 只给一个在二叉树中的某个节点node,请实现返回node的后继节点的函数。
# 在二叉树的中序遍历的序列中，node的下一个节点叫做node的后继节点。

class Node:     
    def __init__(self,val):
        self.val=val
        self.parent=None 
        self.left=None
        self.right=None
class SuccessorNode:
    def successornode(self,node):
        if node.right:             #如果该节点的右孩子存在,则在右子数的最左边
            node=node.right
            while node and node.left:
                node=node.left
            return node
        else:
            while node.parent:     #如果该节点的右孩子不存在
                if node.parent.right==node:
                    node=node.parent
                else:break
            return node.parent
            

                
