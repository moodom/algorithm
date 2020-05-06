class Node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class KDNode(Node):
    def __init__(self,data=None,left=None,right=None,axis=None,sel_axis=None,dimensions=None):
        super(KDNode,self).__init__(data,left,right)
         """为KD树创建一个新的节点

        如果该节点在树中被使用，axis和sel_axis必须被提供。
        sel_axis(axis)在创建当前节点的子节点中将被使用，
        输入为父节点的axis，输出为子节点的axis"""
        self.axis=axis
        self.sel_axis=sel_axis
        self.dimensions=dimensions
    def create(point_list=None,dimensions=None,axis=0,sel_axis=None):
         """从一个列表输入中创建一个kd树
        列表中的所有点必须有相同的维度。
        如果输入的point_list为空，一颗空树将被创建，这时必须提供dimensions的值
        如果point_list和dimensions都提供了，那么必须保证前者维度为dimensions
        axis表示根节点切分数据的位置，sel_axis(axis)在创建子节点时将被使用，
        它将返回子节点的axis"""
        if not point_list and not dimensions:
            raise ValueError("either point_list or dimension should be provide")
        elif point_list:
            dimensions=check_dimensionality(point_list,dimensions)

        sel_axis=sel_axis or (lambda pre_axis:(pre_axis+1)%dimensions)

        if not point_list:
            return KDNode(sel_axis=sel_axis,axis=axis,dimensions=dimensions)
        point_list=list(point_list)
        point_list.sort(key=lambda point:point[axis])
        median=len(point_list)//2
        loc=point_list[median]
        left=create(point_list=[:median],dimensions,sel_axis(axis))
        right=create(point_list=[median+1:],dimensions,sel_axis(axis))
        return KDNode(loc,left,rigth,axis,sel_axis=sel_axis,dimensions=dimensions)
    def check_dimensionality(point_list,dimensions=None):
        dimensions=dimensions or len(point_list[0])
        for p in point_list:
            if len(p)!=dimensions:
                raise ValueError("All Points in the point_list must have the same dimensionality")
        return dimensions
    class BoundedPriorityQueue:
        def __init__(self,k):
            self.heap=[]
            self.k=k
        def items(self):
            return self.heap
        def parent(self,index):
            return int(index/2)
        def left_child(self,index):
            return 2*index+1
        def right_child(self,index):
            return 2*index+2
        def _dist(self,index):
            return self.heap[index][3]
        def max_heapify(self,index):
            left_index=self.left_child(index)
            right_index=self.right_child(index)
        def max_heapify(self,index):
            left_index=self.left_child(index)
            right_index=self.right_child(index)
            largest=index
            if left_index<len(self.heap)
def _search_node(self,point,k,results,get_dist):
    if not self:
        return
    nodeDist=get_dist(self)
    results.add((self,nodeDist))
    split_plane=self.data[self.axis]
    plane_dist=point[self.axis]-split_plane
    plane_dist2=plane_dist**2

    if point[self.axis]<split_plane:
        if self.left is not None:
            self.left._search_node(point,k,r)
        
    if point[self.axis]<split_plane:
        if self.left is not None:
            self.left._search_node(point,k,results,get_dist)
    else:
        if self.rigth is not None:
            self.right._search_node(point,k,results,get_dist)
    if plane_dist2<results.max() or results.size()<k:
        if point[self.axis]<self.data[self.axis]:
            if self.rigtht is not None:
                self.right._search_node(point,k,results,get_dist)
            else:
                if self.left is not None:
                    self.left._search_node(point,k,results,get_dist)
def search_knn(self,point,k,dist=None):
    if dist is None:
        get_dist=lambda n:n.dist(point)
    else:
        gen_dist=lambda n:dist(n.data,point)
    results=BounderdPriorityQueue(k)
    self._search_node(point,k,results,get_dist)
    BY_VALUE=lambda kv:kv[1]
    return sorted(results.items(),key=BY_VALUE)

