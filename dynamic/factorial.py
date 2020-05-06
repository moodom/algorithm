# 求n!

class Factorial:
    # def factorial(self,n): # 递归
    #     if n==1:
    #         return 1
    #     else:
    #         n*self.factorial(n-1)
    def factorial(self,n):  # 动态规划
        res=1
        for i in range(1,n+1):
            res*=i
        return res
if __name__=="__main__":
    res=Factorial().factorial(5)
    print(res)
