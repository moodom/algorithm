# 设计RandomPool结构
# 题目 设计一种结构,在该结构中有如下三个功能：
# insert(key):将某个key加入到该结构,做到不重复加入
# delete(key):将原来在结构中的某个key移除。
# getRandom():等概率随机返回结构中的任何一个key
# 要求：Inset,delete和getRandom方法的时间复杂度都是O(1)
import random
class RandomPool:
    def __init__(self):
        self.inputDic={}
        self.outDic={}
        self.size=0
    def insert(self,key):
        if key not in self.inputDic:
            self.inputDic[key]=self.size
            self.outDic[self.size]=key
            self.size+=1
    def delelte(self,key):
        if key not in self.inputDic.keys():
            print("error")
            return
        num=self.inputDic[key]
        self.size-=1
        if self.size==0 or self.inputDic[key]==self.size:
            del self.inputDic[key]
            del self.outDic[num]
            
        else:
            del self.inputDic[key]
            tmp=self.outDic[self.size]
            self.inputDic[tmp]=num
            del self.outDic[self.size]
            self.outDic[num]=tmp
    def getRandom(self):
        if not self.size:return None
        num=int(random.random()*self.size)
        return self.outDic[num]
if __name__=="__main__":
    test=RandomPool()
    test.insert('a')
    test.insert('b')
    test.insert('a')
    test.insert('c')
    print(test.inputDic)
    print(test.delelte('d'))
    print(test.inputDic)
    print(test.getRandom())
