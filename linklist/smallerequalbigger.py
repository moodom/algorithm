# 链表partition问题
# 将单向链表按某值划分为左边小，中间相等，右边大的形式
# 题目
# 给定一个单向链表的的头节点head,节点的值类型是整型。给定一个整数pivot。
#进阶:调整后的partion满足有序性，时间复杂度达到O(N),额外空间复杂度达到O(1)
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SmallerEqualBigger:
    def smallerequalbigger(self,head,pivot):
        if not head: return head
        cur=head
        lessHead,equHead,moreHead=Node(None),Node(None),Node(None) # 用三个指针分别来指向划分的数
        less,equ,more=lessHead,equHead,moreHead
        while cur:
            tmp=cur
            cur=cur.next
            tmp.next=None
            if tmp.val<pivot:
                less.next=tmp
                less=less.next
            elif tmp.val==pivot:
                equ.next=tmp
                equ=equ.next
            else:
                more.next=tmp
                more=more.next
        if moreHead.next:
            equ.next=moreHead.next
        if equHead.next:
            less.next=equHead.next
        return lessHead.next
def rightMethod(head,pivot): #转换为数组的荷兰国旗问题,不满足有序性,时间复杂度为O(N),空间复杂度O(N)
    num=[]
    while head:
        num.append(head)
        head=head.next
    less,cur,more=-1,0,len(num)
    while cur<more:
        if num[cur].val<pivot:
            less+=1
            num[less],num[cur]=num[cur],num[less]
            cur+=1
        elif num[cur].val==pivot:
            cur+=1
        else:
            more-=1
            num[more],num[cur]=num[cur],num[more]
    head=cur=num[0]
    for i in range(1,len(num)):
        cur.next=num[i]
        cur=cur.next
    cur.next=None
    return head
def main():
    import sys
    sys.path.append('./test/')
    from D1linklist import D1LinkList,D1Test
    head=D1LinkList().generateRandomLinkList(size=10)
    D1LinkList().display(head)

    head1=D1LinkList().copyLinkList(head)
    res1=rightMethod(head1,0)
    D1LinkList().display(res1)

    head2=D1LinkList().copyLinkList(head)
    res2=SmallerEqualBigger().smallerequalbigger(head2,0)
    D1LinkList().display(res2)

if __name__=="__main__":
    main()

