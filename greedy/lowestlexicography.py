# 最低字典序
# 给定一个字符串类型的数组strs,找到一种拼接方式,使得把所有字符串拼起来形成的字符串具有最低的字典序


class LowestLexicography:
    def lowestlexicograpy(self,strs):
        for end in range(len(strs)):
            for j in range(end):
                if strs[j+1]+strs[j]<strs[j]+strs[j+1]:
                    strs[j],strs[j+1]=strs[j+1],strs[j]
        return "".join(strs)

if __name__=="__main__":
    a=["ab","awefef","e","efra","aa"]
    test=LowestLexicography().lowestlexicograpy(a)
    print(test)