import random
class D2Array:
    def generateRandomArray(self,sizes,value):
        #生成长度随机的数组
        arr=[[random.random()]*sizes[0] for j in range(sizes[1])]   # random.random() [0,1)
        for i in range(sizes[0]):
            for j in range(sizes[1]):
                arr[i][j]=int((value+1)*random.random())-int(value*random.random()) #两数相减能产生负数
        return arr
class D2Test:
    def __init__(self,testTime=5000,sizes=[5,5],seed=100):
        self.testTime=testTime
        self.sizes=sizes
        self.seed=seed
        self.succeed=True
    def compare(self,rightMethod,testMethod):
        for i in range(self.testTime):
            arr1=D2Array().generateRandomArray(self.sizes,self.seed)
            arr2=arr1.copy()
            arr3=arr1.copy()
            rightMethod(arr1)
            testMethod(arr2)
            if arr1!=arr2:
                print(arr3)
                self.succeed=False
                break
        print(self.succeed)
    def compareRes(self,rightMethod,testMethod):
        for i in range(self.testTime):
            arr1=D2Array().generateRandomArray(self.sizes,self.seed)
            arr2=arr1.copy()
            arr3=arr1.copy()
            res1=rightMethod(arr1)
            res2=testMethod(arr2)
            if res1!=res2:
                print(arr3)
                self.succeed=False
                break
        print(self.succeed)