# 荷兰国旗问题 (快排的partition) 时间复杂度O(N), 空间复杂度O(1)
# 给定一数组，和一个数num，请把小于num的数放在数组的左边，等于num的数放在数组中间，大于num的数放在数组右边
class NetherlandsFlag:
    def __init__(self,arr,num):
        self.arr=arr
        self.num=num
        self._netherlandsflag(self.arr,self.num)
    def _netherlandsflag(self,arr,num):
        less,cur,more=-1,0,len(arr)
        while cur<more:
            if arr[cur]<num:
                less+=1
                arr[cur],arr[less]=arr[less],arr[cur]
                cur+=1                                      # cur只在小于和等于的时候才+1,因为只有左边的是排列好了的
            elif arr[cur]>num:
                more-=1
                arr[cur],arr[more]=arr[more],arr[cur]       
            else:
                cur+=1                                      # 
if __name__=="__main__":
    a=[2,4,5,3,5,6,4]
    NetherlandsFlag(a,4)
    print(a)
