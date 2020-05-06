# 实现一个特殊的栈，在实现栈的基本功能上,再实现返回栈中最小元素的操作
# 要求
# 1.pop,push,getMin操作的时间复杂度都是O(1)
# 2.设计的栈类型可以使用现成的栈结构
class GetMinStack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def pop(self):
        if self.stack:
            res=self.stack.pop()
            self.minstack.pop()
            return res
        else:
            print("The stack is empty!")
    def push(self,num):
        self.stack.append(num)
        if not self.minstack:
            self.minstack.append(num)
        else:
            self.minstack.append(min(num,self.minstack[-1]))
    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            print("The stack is empty!")
    def show(self):
        print(self.stack)
        print(self.minstack)
if __name__=="__main__":
    stack=GetMinStack()
    stack.push(8)
    stack.push(5)
    stack.push(3)
    stack.push(4)
    
    minNum=stack.getMin()
    print(minNum)

