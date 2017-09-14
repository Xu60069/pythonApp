class Fib:
    def __init__(self,size):
        self.dp=[-1]*size
        self.dp[0]=0
        self.dp[1]=1
    def fib(self,n):
        if self.dp[n]>=0:
            return self.dp[n]
        else:
            self.dp[n]=self.fib(n-1)+self.fib(n-2)
            return self.dp[n]

    def zeckendorf(self,num,ans):
        for i in range (len(self.dp)):
            if self.dp[i]==num:
                ans.append(num)
                return ans
            elif self.dp[i]>num:
                ans.append(self.dp[i-1])
                return self.zeckendorf(num-self.dp[i-1], ans)
        return ans
        
    def print(self):
        print(self.dp)

f=Fib(50)
f.fib(14)
f.print()
print(f.zeckendorf(240,[]))
