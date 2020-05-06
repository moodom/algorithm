# 队列和栈的转换问题

# 队列转换为栈的问题
class QueueConvertStack:
    def __init__(self):
        self.pushQueue=[]
        self.popQueue=[]
    def pop(self):
        if not self.pushQueue:
            print("The stack is empty!")
            return
        while len(self.pushQueue)>1:
            self.popQueue.append(self.pushQueue.pop(0))
        res=self.pushQueue.pop(0)
        self.pushQueue,self.popQueue=self.popQueue,self.pushQueue
        return res
    def push(self,num):
        self.pushQueue.append(num)
    def show(self):
        print(self.pushQueue)
# 栈转换为队列的问题
class StackConvertQueue:
    def __init__(self):
        self.pushStack=[]
        self.popStack=[]
    def push(self,num):
        self.pushStack.append(num)
    def pop(self):
        if not self.popStack:
            while self.pushStack:
                self.popStack.append(self.pushStack.pop())
            if not self.popStack:
                print("The queue is empty!")
                return
        return self.popStack.pop()
if __name__=="__main__":
    queue=StackConvertQueue()
    queue.push(1)
    queue.push(3)
    queue.push(2)
    a=queue.pop()
    print(a)
    a=queue.pop()
    print(a)
    a=queue.pop()
    print(a)
    a=queue.pop()
