import random
class D1Str:
    def RandomMode(self,mode):
        if mode==0:
            return random.choice('abcdefghijklmnopqrstuvwxyz')
        if mode==1:
            return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if mode==3:
            return random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
    def generateRandomStr(self,sizes,mode):
        #生成长度随机的字符串
        res=[]
        for size in sizes:
            strlist=""
            for i in range(size):
                strlist+=self.RandomMode(mode=mode)
            res.append(strlist)
        return res
class D1Test:
    def __init__(self,testTime=5000,sizes=[10],mode=0):
        self.testTime=testTime
        self.sizes=sizes
        self.mode=mode
        self.succeed=True
    def compare(self,rightMethod,testMethod):
        for i in range(self.testTime):
            str1=D1Str().generateRandomStr(self.sizes,self.mode)
            str2=str1.copy()
            str3=str1.copy()
            rightMethod(*str1)
            testMethod(*str2)
            if str1!=str2:
                print(str3)
                self.succeed=False
                break
        print(self.succeed)
    def compareRes(self,rightMethod,testMethod):
        for i in range(self.testTime):
            str1=D1Str().generateRandomStr(self.sizes,self.mode)
            str2=str1.copy()
            str3=str1.copy()
            res1=rightMethod(*str1)
            res2=testMethod(*str2)
            if res1!=res2:
                print(str3)
                self.succeed=False
                break
        print(self.succeed)

if __name__=="__main__":
    ret=D1Str().generateRandomStr(sizes=[10,5])
    print(ret)