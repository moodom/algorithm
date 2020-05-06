# 广度优先搜索

class BFS:
    def bfs(self,node):
        if not node:return
        res=[]
        queue=[node]
        seen=set(node)
        while queue:
            tmp=queue.pop(0)
            res.append(tmp.val)
            for cur in tmp.nexts:
                if cur not in seen:
                    seen.add(cur)
                    queue.append(cur)
        return res
