# 逆序对问题 (归并排序)
# 在一个数组中,左边的数如果比右边的数大,则这两个数构成一个逆序对,请答应所有的逆对序.
class ReversePairs:
    def reversePairs(self, nums):
        self.nums=nums.copy()
        return self.sortPairs(self.nums,0,len(self.nums))
    def sortPairs(self,nums,L,R):
        if L>=R-1:return []
        mid=L+((R-L)>>1)
        return self.sortPairs(nums,L,mid)+self.sortPairs(nums,mid,R)+self.merge(nums,L,mid,R)
    def merge(self,nums,L,mid,R):
        tmp=[0]*(R-L)
        i,res=0,[]
        L_start,L_end=L,mid
        while L<L_end and mid<R:
            if nums[L]>nums[mid]:
                tmp[i]=nums[mid]
                for l in range(L,L_end):
                    res.append([nums[l],nums[mid]])
                i+=1;mid+=1
            else:
                tmp[i]=nums[L]
                i+=1;L+=1
        tmp[i:]=nums[L:L_end] if mid==R else nums[mid:R]
        nums[L_start:R]=tmp
        return res

if __name__=="__main__":
    a=[7,5,6,4]
    print(ReversePairs().reversePairs(a))