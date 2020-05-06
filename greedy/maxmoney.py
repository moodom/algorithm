# 获得的最大钱数   leetcode502. IPO
# 输入：参数1，正数数组capital 参数2，正数数组profits 参数3， 正数k 参数4，正数w 
# capital[i]表示i号项目的花费 profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润) k表示你不能并行、只能串行的最多做k个项目 w表示你初始的资金 
# 说明：你每做完一个项目，马上获得的收益，可以支持你去做下一个项目
# 你最后获得的最大钱数。
import heapq
class MaxMoney:
    def maxmoney(self,capital,profits,k,w):
        items=[]
        maxres=0
        for i in range(len(capital)):
            item=(capital[i],profits[i])
            items.append(item)
        minCap=items
        heapq.heapify(minCap)
        maxPro=[]
        for _ in range(k):
            while minCap and minCap[0][0]<=w:
                heapq.heappush(maxPro,-heapq.heappop(minCap)[1])
            if maxPro:
                p=heapq.heappop(maxPro)
                maxres-=p
                w-=p
            else:
                break
        return w
if __name__=="__main__":
    k=1
    w=2
    profit=[1,2,3]
    capital=[1,1,2]
    res=MaxMoney().maxmoney(capital,profit,k,w)
    print(res)
            


        
