# LRU  leetcode146. LRU缓存机制
#设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。当缓存被填满时，它应该删除最近最少使用的项目。
# 它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 示例:
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
class Node:
    def __init__(self,val,p=None,n=None):
        self.val=val
        self.p=p
        self.n=n
class LinkList:
    def __init__(self,capacity):
        self.capacity=capacity
        self.head=Node(None)
        self.bottom=self.head
        self.count=0
    def changeNode(self,node):
        if node.n is None:
            node.p.n=None
            self.bottom=node.p 
        else:
            tmp=node.n 
            node.p.n=tmp
            tmp.p=node.p
        self.count-=1 
        self.addNode(node)
        
    def addNode(self,node):
        if self.head.n is None:
            self.head.n=node
            node.p=self.head
            self.bottom=node
            self.count+=1
        else:
            tmp=self.head.n
            self.head.n=node
            tmp.p=node
            node.p=self.head
            node.n=tmp
            self.count+=1
    def update(self):
        if self.count>self.capacity:
            tmp=self.bottom
            self.bottom=tmp.p
            self.bottom.n=None
            tmp.p=None
            self.count-=1
            return tmp 
        else:
            return None
class LRUCache:
    def __init__(self, capacity):
        self.key_node={}
        self.node_key={}
        self.linklist=LinkList(capacity)
    def get(self, key: int) -> int:
        if key not in self.key_node.keys():
            return -1
        else:
            self.linklist.changeNode(self.key_node[key])
            return self.key_node[key].val
    def put(self, key,value):
        if key in self.key_node.keys():
            self.key_node[key].val=value
            self.linklist.changeNode(self.key_node[key])
        else:
            self.key_node[key]=node=Node(value)
            self.node_key[node]=key
            self.linklist.addNode(node)
            tmp=self.linklist.update()
            if tmp is not None:
                del self.key_node[self.node_key[tmp]]
                del self.node_key[tmp]
#--------------------使用OrderedDict-----------------------
from collections import OrderedDict
class LRUcache:
    def __init__(self,capacity):
        self.maxsize=capacity 
        self.lrucache=OrderedDict()
    def get(self,key):
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key,-1)
    def put(self,key,value):
        if key in self.lrucache:
            del self.lrucache[key]
        self.lrucache[key]=value
        if len(self.lrucache)>self.maxsize:
            self.lrucache.popitem(last=False)        
def main():
   cache=LRUCache(10)
   cache.put(10,13)
   cache.put(3,17)
   cache.put(6,11)
   cache.put(10,5)
   cache.put(9,10)
   cache.get(10)
   cache.put(2,19)
   cache.get(2)
   cache.get(3)
   cache.put(5,25)
   cache.get(8)
   cache.put(9,22)
   cache.put(5,5)
   cache.put(1,30)
   cache.get(11)
   cache.put(9,12)
   cache.get(7)
   cache.get(5)
   cache.get(8)
   cache.get(9)
   cache.put(4,30)
   cache.put(9,3)
   print(cache.get(9))
   print(cache.get(10))
   print(cache.get(10))
if __name__=="__main__":
    main()


