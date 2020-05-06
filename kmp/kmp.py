# 字符串匹配问题  KMP原型  时间复杂度O(M+N), 空间复杂度O(N)
# 给定一个strA(M)字符串和一个strB(N)字符串，在strA字符串中找出strB字符串出现的第一个位置 (从0开始)。如果不存在，则返回-1。
# 示例 1:
# 输入: strA= "hello", strB = "ll"
# 输出: 2
class KMP:
    def kmp(self,strA,strB):
        if not strB: return 0
        if not strA:return -1
        nextArr=self.next(strB)
        i,j=0,0
        while i<len(strA) and j<len(strB):
            if strA[i]==strB[j]:
                i+=1;j+=1
            elif j>0:
                j=nextArr[j]
            else:
                i+=1
        if j==len(strB):return i-j
        return -1
    def next(self,strB):
        if len(strB)==1:return [-1]
        nextArr=[0]*len(strB)
        nextArr[0]=-1
        i,cn=2,0
        while i<len(strB):
            if strB[i-1]==strB[cn]:
                nextArr[i]=cn+1
                i+=1;cn+=1
            elif cn>0:
                cn=nextArr[cn]
            else:
                nextArr[i]=0
                i+=1
        return nextArr

def rightMethod(strA,strB):
    if not strB: return 0
    if not strA:return -1
    res=-1
    for k in range(len(strA)):
        if k+len(strB)>len(strA):break
        i=0
        while i<len(strB):
            if strA[k+i]!=strB[i]:break
            i+=1
        if i==len(strB):
            res=k;break 
    return res

def main():
    import sys
    sys.path.append('./test/')
    from D1str import D1Test
    D1Test(sizes=[10,3]).compareRes(rightMethod,KMP().kmp)
if __name__=="__main__":
    main()