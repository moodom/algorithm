# 拓扑排序
class sortedTopology:
    def sortedtopology(self,graph):
        inMap={}
        zeroInQueue=[]
        for node in graph.nodes:
            inMap[node]=node.in_
            if node.in_==0:
                zeroInQueue.append(node)
        result=[]
        while zeroInQueue:
            cur=zeroInQueue.pop()
            result.append(cur)
            for node in cur.nexts:
                inMap[node]=inMap[node]-1
                if inMap[node]==0:
                    zeroInQueue.append(node)
        return result