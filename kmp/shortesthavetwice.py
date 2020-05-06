# 原始串复制成最短两个原始串 (kmp求next数组)
# 问题
# 一个原始串在后面可以在后面增添字符,求解怎么增添字符能够使得原始串可以变为两个原始串
class ShortestHaveTwice:
    def shortesthavetwice(self,s):
        nextArr=self.next(s+'/')
        return s+s[nextArr[len(s)]:]
    def next(self,s):
        if len(s)==1:return [-1]
        nextArr=[0]*len(s)
        nextArr[0]=-1
        i,cn=2,0
        while i<len(s):
            if s[i-1]==s[cn]:
                nextArr[i]=cn+1
                i+=1;cn+=1
            elif cn>0:
                cn=nextArr[cn]
            else:
                nextArr[i]=0
                i+=1
        return nextArr
if __name__=="__main__":
    a="abcabcx"
    ret=ShortestHaveTwice().shortesthavetwice(a)
    print(ret)