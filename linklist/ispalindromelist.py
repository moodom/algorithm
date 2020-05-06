# 判断一个链表是否为回文结构
# 题目
# 给定一个链表的头节点head,请判断该链表是否为回文结构。
# 例如:1->2->1,返回true.1->2->2->1,返回true.
# 进阶:如果链表长度为N,时间复杂度达到O(N),额外空间复杂度达到O(1)
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class IsPalindromeList:
    def ispalindromelist(self,head):
        if not head:return False
        if not head.next:return True
        center=self.findCenterNode(head)
        anotherHead=self.reverseList(center.next)
        headA=head;headB=anotherHead
        while headA and headB:
            if headA.val!=headB.val:
                return False
            else:
                headA=headA.next
                headB=headB.next
        reverse=self.reverseList(anotherHead) #将链表重新连接
        center.next=reverse
        return True
    
    def findCenterNode(self,head):
        slow=fast=head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def reverseList(self,head):
        last=None
        while head and head.next:
            cur=head
            head=head.next
            cur.next=last
            last=cur
        head.next=last
        return head

def rightMethod(head): # O(N)
    if not head: return False
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    return res==res[::-1]
def main():
    import sys
    sys.path.append('./test/')
    from D1linklist import D1Test
    D1Test(size=5).compareRes(rightMethod,IsPalindromeList().ispalindromelist)
if __name__=="__main__":
    # main()
    a=[-6, 29,1, 3, -6]
    head=cur=Node(-6)
    for i in range(1,len(a)):
        cur.next=Node(a[i])
        cur=cur.next
    res=IsPalindromeList().ispalindromelist(head)
    print(res)
        