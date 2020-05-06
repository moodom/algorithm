# LFU 缓存
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。
# get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
# put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
# 「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

from collections import OrderedDict
from collections import defaultdict
class LFUCache:
    def __init__(self, capacity: int):
        self.mincount=0
        self.visited={}
        self.capacity=capacity
        self.cache_dict=defaultdict(OrderedDict)
        # 默认字典嵌套一个有序字典，外层字典的键是访问次数，有序字典会根据放入元素的先后次序进行排序
    def get(self, key: int) -> int:
        if key not in self.visited.keys():
            return -1
        count=self.visited[key]
        self.visited[key]+=1
        value=self.cache_dict[count][key]
        del self.cache_dict[count][key]
        self.cache_dict[count+1][key]=value
        # 如果访问次数等于最小访问次数，且该次数下已经没有值了，则最小访问次数+1
        if count == self.mincount and len(self.cache_dict[count]) == 0:
            self.mincount += 1
        return value
    def put(self, key: int, value: int) -> None:
        if key in self.visited.keys():
            self.get(key)
            count=self.visited[key]
            self.cache_dict[count][key]=value
            return
        if self.capacity and len(self.visited)>=self.capacity:
            tmp_key,tmp_val=self.cache_dict[self.mincount].popitem(last=False)
            del self.visited[tmp_key]
        if self.capacity:
            self.visited[key]=1
            self.mincount=1
            self.cache_dict[1][key]=value
if __name__=="__main__":
    cache =LFUCache(0)
    cache.put(0, 0)
    print(cache.get(0))     
        
        

        
