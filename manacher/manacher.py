# 最长回文子串问题  Manacher原型 时间复杂度O(N) 空间复杂度O(1) leetcode5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。

class Manacher:
    def manacher(self,s):
        s= "".join(["#"+s[i] for i in range(len(s))])+"#"
        i,j,length=0,0,len(s)
        radArr=[0]*len(s)      # 回文半径数组
        curright,curcenter=0,0   # 当前最右回文位置，当前最右回文中心
        maxrad,center=0,0
        while curright<length:
            j=min(radArr[2*curcenter-i],curright-i) if j<curright else 1
            while i+j<length and s[i-j]==s[i+j]:
                j+=1
            radArr[i]=j-1
            if i+j>curright:
                curright=i+j
                curcenter=i
            (maxrad,center)=(j-1,i) if j-1>maxrad else (maxrad,center)
            i+=1
        return s[center-maxrad:center+maxrad+1].replace("#","")
def rightMethod(s):  # 普通的中心扩展法
    s= "".join(["#"+s[i] for i in range(len(s))])+"#"
    i,j,length=0,1,len(s)
    maxrad,center=0,0
    while i<length:
        size,j=0,1
        while i-j>=0 and i+j<length:
            if s[i-j]==s[i+j]:
                size+=1;j+=1
            else:break
        (maxrad,center)=(size,i) if size>maxrad else (maxrad,center)
        i+=1
    return s[center-maxrad:center+maxrad+1].replace("#","")
if __name__=="__main__":
    s="babad"
    print(Manacher().manacher(s))

                




