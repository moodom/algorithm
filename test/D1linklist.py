import random
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class DoubleNode:
    def __init__(self,val):
        self.val=val
        self.last=None
        self.next=None
class D1LinkList:
    def generateRandomLinkList(self,size=5,value=5,Node=Node):
        #生成长度随机的数组
        arr=[random.random()]*size   # random.random() [0,1)
        for i in range(size):
            arr[i]=int((value+1)*random.random())-int(value*random.random()) #两数相减能产生负数
        if Node==Node:
            head=cur=Node(arr[0])
            for i in range(1,size):
                cur.next=Node(arr[i])
                cur=cur.next
        if Node==DoubleNode:
            head=cur=DoubleNode(arr[0])
            for i in range(1,size):
                cur.next=Node(arr[i])
                tmp=cur
                cur=cur.next
                cur.last=tmp
        return head
    def copyLinkList(self,head):
        if head: last=newhead=Node(head.val)
        cur=head.next
        while cur:
            newcur=Node(cur.val)
            last.next=newcur
            last=newcur
            cur=cur.next
        return newhead
    def display(self,head):
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        print(res)
class D1Test:
    def __init__(self,testTime=5000,size=10,seed=100):
        self.testTime=testTime
        self.size=size
        self.seed=seed
        self.succeed=True
    def show(self,head):
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        print(res)
    def compareRes(self,rightMethod,testMethod):
        for i in range(self.testTime):
            head1=D1LinkList().generateRandomLinkList(self.size,self.seed)
            head2=D1LinkList().copyLinkList(head1)
            head3=D1LinkList().copyLinkList(head1)
            res1=rightMethod(head1)
            res2=testMethod(head2)
            if res1!=res2:
                self.show(head3)
                self.succeed=False
                break
        print(self.succeed)     