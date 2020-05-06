# 用数组结构实现大小固定的栈
class Stack:
    def __init__(self,size):
        self.stack=[0]*size
        self.top=-1
        self.size=size        
    def stackPush(self,num): 
        if self.top<self.size-1:
            self.top+=1
            self.stack[self.top]=num
        else:print("The stack is full!")
    def stackPop(self):
        if self.top>=0:
            res=self.stack[self.top]
            self.top-=1
            return res
        else:print("The stack is empty!")
    def show(self):
        print(self.stack)
# 用链表实现实现大小不固定的栈
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None 
class LinkStack:
    def __init__(self):
        self.top=None
    def stackPush(self,num):
        if not self.top: self.top=Node(num)
        else:
            tmp=self.top
            self.top=Node(num)
            self.top.next=tmp
    def stackPop(self):
        if not self.top:
            print("The stack is empty!")
            return
        else:
            res=self.top.val
            self.top=self.top.next
        return res
if __name__=="__main__":
    stack=LinkStack()
    stack.stackPush(1)
    stack.stackPush(2)
    stack.stackPush(3)
    stack.stackPush(4)
    a=stack.stackPop()
    a=stack.stackPop()
    a=stack.stackPop()
    a=stack.stackPop()
    a=stack.stackPop()
    print(a)

