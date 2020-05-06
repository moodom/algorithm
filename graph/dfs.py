# 深度优先搜索
class DFS:
    def dfs(self,node):
        if not node:return
        res=[]
        stack=[node]
        seen=set(node)
        res.append(node.value)
        while stack:
            tmp=stack.pop()
            for cur in tmp.nexts:
                if cur not in seen:
                    seen.add(cur)
                    stack.append(tmp)
                    stack.append(cur)
                    res.append(cur.value)      #
                    break                      #
        return res