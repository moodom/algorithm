class Graph:
    def __init__(self):
        self.nodes=dict() # {Node.val:Node}
        self.edges=set() # {Edge}
class Node:
    def __init__(self,value:int):
        self.value=value
        self.in_=0
        self.out=0
        self.nexts=[]
        self.edges=[]
class Edge:
    def __init__(self,weight:int,fro:Node,to:Node):
        self.weight=weight
        self.fro=fro
        self.to=to
class GraphGenerator:
    def createGraph(self,matrix):
        graph=Graph()
        for i in range(len(matrix)):
            weight=matrix[i][0]
            fro=matrix[i][1]
            to=matrix[i][2]
            if fro not in graph.nodes:
                graph.nodes[fro]=Node(fro)
            if to not in graph.nodes:
                graph.nodes[to]=Node(to)
            froNode=graph.nodes[fro]
            toNode=graph.nodes[to]
            newEdge=Edge(weight,froNode,toNode)
            froNode.nexts.append(toNode)
            froNode.out+=1
            froNode.in_+=1
            froNode.edges.append(newEdge)
            graph.edges.add(newEdge)
        return graph
            
if __name__=="__main__":
    case=[[5,0,1],[2,2,0],[2,2,1],[7,1,2]]
    g=GraphGenerator().createGraph(case)
    print(g.edges)


