# 单链表相交的一系列问题
# 在本题中,单链表可能有环,也可能无环.给定两个单链表的头节点head1和head2,，这两个链表可能相交，也可能不相交。
# 请实现一个函数， 如果两个链表相交，请返回相交的第一个节点；如果不相交，返回None即可。 
# 要求：如果链表1 的长度为N，链表2的长度为M，时间复杂度请达到 O(N+M)，额外 空间复杂度请达到O(1)。

# 分两种情况
# 1.两个链表都没有环
# 2.连个链表都有环
# 一个有环一个无环的情况不存在

# 针对第2种情况又分三种状况
# 2.1 各自成环不相交
# 2.2 成Y形
#       O
# 2.3 成-O-形
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class FindFistInterSetionNode:
    def findfistintersetionnode(self,head1,head2):
        if not head1 or not head2:return None
        res1=self.hasCycle(head1)
        res2=self.hasCycle(head2)
        if not res1 and not res2:      # 第一种情况 两个链表都没有环
            num1,num2,cur1,cur2=1,1,head1,head2
            while cur1.next:
                cur1=cur1.next;num1+=1
            while cur2.next:
                cur2=cur2.next;num2+=1
            if cur1!=cur2:return None
            (maxcur,num,mincur)=(head1,num1-num2,head2) if num1>=num2 else (head2,num2-num1,head1)
            while num:
                maxcur=maxcur.next;num-=1
            while maxcur:
                if maxcur==mincur:
                    res=maxcur;break
                else:
                    maxcur=maxcur.next
                    mincur=mincur.next
            return res
        elif not res1 or not res2: return None  #一个有环一个无环的情况不存在
        else:
            if res1==res2:             # 2.2 成Y形
                num1,num2,cur1,cur2=0,0,head1,head2
                while cur1!=res1:
                    cur1=cur1.next;num1+=1
                while cur2!=res2:
                    cur2=cur2.next;num2+=1
                (maxcur,num,mincur)=(head1,num1-num2,head2) if num1>=num2 else (head2,num2-num1,head1)
                while num:
                    maxcur=maxcur.next;num-=1
                while maxcur:
                    if maxcur==mincur:
                        res=maxcur;break
                    else:
                        maxcur=maxcur.next
                        mincur=mincur.next
                return res
            else:
                cur1=res1:
                while cur1:
                    cur1=cur1.next
                    if cur1==res2:      # 2.3 成-O-形
                        return cur1
                    if cur1==res1:
                        break           #2.1 各自成环不相交
            return None
# 判断链表是否成环,若没有环返回None,若成环则返回开始入环的第一个节点
    def hasCycle(self,head):                #规律 快指针和慢指针相遇时是环的入口
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow :
                return True
        return Fals
    def hasCycle_1(self,head): # 使用一个哈希表，空间复杂度为O(N)
        seen=set()
        while head:
            if head not in seen:
                seen.add(head)
                head=head.next
            else:
                break
        return head
      