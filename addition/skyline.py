# 大楼轮廓问题   # leetcode 218 天际线问题
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。
# 每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。
# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。
import heapq
class Solution:
    def getSkyline(self, buildings):
        events=[[L,-H,R] for L,R,H in buildings]+[[R,0,0] for L,R,H in buildings]
        events.sort()
        res=[[0,0]]
        heap=[[0,float("inf")]]
        heapq.heapify(heap)
        for event in events:
            while event[0]>=heap[0][1]:
                heapq.heappop(heap)
            heapq.heappush(heap,event[1:])
            if -heap[0][0]!=res[-1][1]:
                res.append([event[0],-heap[0][0]])
        return res[1:]            
if __name__=="__main__":
    #buildings=[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings=[[0,2,3],[2,5,3]]
    print(Solution().getSkyline(buildings))