import random
class D1Array:
    def generateRandomArray(self,size,value):
        #生成长度随机的数组
        arr=[random.random()]*size   # random.random() [0,1)
        for i in range(size):
            arr[i]=int((value+1)*random.random())-int(value*random.random()) #两数相减能产生负数
        return arr
class D1Test:
    def __init__(self,testTime=5000,size=10,seed=100):
        self.testTime=testTime
        self.size=size
        self.seed=seed
        self.succeed=True
    def compare(self,rightMethod,testMethod):
        for i in range(self.testTime):
            arr1=D1Array().generateRandomArray(self.size,self.seed)
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
            arr1=D1Array().generateRandomArray(self.size,self.seed)
            arr2=arr1.copy()
            arr3=arr1.copy()
            res1=rightMethod(arr1)
            res2=testMethod(arr2)
            if res1!=res2:
                print(arr3)
                self.succeed=False
                break
        print(self.succeed)