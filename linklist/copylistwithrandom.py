# 复制含有随机指针节点的链表 (leetcode138. 复制带随机指针的链表)
# class randomNode:
#     def __init__(self,val):
#         self.val=val
#         self.next=None
#         self.random=None
# 一个链表里的节点如randomNode,random指针可能指向链表中的任意一个节点，也可能指向None
# 请实现一个函数完成这个链表中所有结构的复制,并返回复制的新链表的头节点。
# 进阶: 不适用额外的数据结构,只用有限几个变量,且在时间复杂度为O(N)内完成原问题要实现的函数
class randomNode:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.random=None
class CopyListWithRandom:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return head
        cur=head
        while cur:              # 将新增的节点每一个挂在原节点后面
            tmp=cur.next
            cur.next=randomNode(cur.val)
            cur.next.next=tmp
            cur=tmp
        cur=head
        while cur:              # 将random的节点连接好
            tmp=cur.next
            tmp.random=cur.random.next if cur.random else None
            cur=cur.next.next
        cur=head
        newcur=newHead=Node(0)
        while cur:              # 分离两个链表
            newcur.next=cur.next
            newcur=newcur.next
            cur.next=newcur.next
            cur=cur.next
        return newHead.next
def rightMethod(head): # 使用哈希表,空间复杂度为O(N)
    if not head:return head
    hashtable={}
    cur=head
    while cur:
        hashtable[cur]=randomNode(cur.val)
        cur=cur.next
    cur=head
    while cur:
        hashtable[cur].next=hashtable[cur.next] if cur.next else None
        hashtable[cur].random=hashtable[cur.random] if cur.random else None
        cur=cur.next
    return hashtable[head]
