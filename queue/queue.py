# 用数组实现大小固定的队列
class Queue:
    def __init__(self,size):
        self.arr=[0]*size
        self.size=size
        self.len=0
        self.end=0
        self.start=0
    def queuePush(self,num):
        if self.len<self.size:
            self.arr[self.end]=num
            self.end=(self.end+1)%self.size
            self.len+=1
        else:
            print("The queue is full!")
    def queuePop(self):
        if self.len:
            res=self.arr[self.start]
            self.start=(self.start+1)%self.size
            self.len-=1
            return res
        else:
            print("The queue is empty!")
            return 
    def show(self):
        print(self.arr)
# 用链表实现大小不固定的队列
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkQueue:
    def __init__(self):
        self.head=Node(None)
        self.tail=None
    def queuePush(self,num):
        if not self.tail:
            self.tail=Node(num)
            self.head.next=self.tail
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    def queuePop(self):
        if self.head.next:
            res=self.head.next.val
            self.head=self.head.next
            return res
        else:
            print("The queue is empty!")
if __name__=="__main__":
    queue=LinkQueue()
    queue.queuePush(1)
    queue.queuePush(2)
    queue.queuePush(3)
    queue.queuePush(4)
    a=queue.queuePop()
    print(a)
    a=queue.queuePop()
    print(a)
    a=queue.queuePop()
    print(a)
    a=queue.queuePop()
    queue.queuePush(4)
    a=queue.queuePop()
    a=queue.queuePop()
    print(a)



