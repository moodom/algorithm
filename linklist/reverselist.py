# 反转单向和双向链表
# 题目:分别实现反转单向链表和反转双向链表的函数
# 如果链表长度为N,时间复杂度要求为O(N),额外空间复杂度要求为O(1)
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
# 反转单向链表
class ReverseSinglyList:
    def reversesinglylist(self,head):
        last=None
        while head and head.next:
            cur=head
            head=cur.next
            cur.next=last
            last=cur
        head.next=last
        return head
# 反转双向链表
class DoubleNode:
    def __init__(self,val):
        self.val=val
        self.last=None
        self.next=None
class ReverseDoublyList:
    def reversedoublylist(self,head):
        pre=None
        while head and head.next:
            cur=head
            head=cur.next
            cur.next=pre
            cur.last=head
            pre=cur
        head.next=pre
        head.last=None
        return head
def main():
    import sys
    sys.path.append('./test/')
    from D1linklist import D1LinkList
    head=D1LinkList().generateRandomLinkList(Node=DoubleNode)
    D1LinkList().display(head)
    res=ReverseDoublyList().reversedoublylist(head)
    D1LinkList().display(res)

if __name__=="__main__":
    main()