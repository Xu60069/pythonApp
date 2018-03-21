class Leetcode:
    def findMaxForm(self, strs, m, n):
        memo=[[0 for x in range(n+1)] for y in range(m+1)]  #m+1 rows
        for i in range(len(strs)):
            s=strs[i]
            ones=0
            zero=0
            for j in range(len(s)):
                if s[j]=='1':
                    ones += 1
                else:
                    zero += 1
            r=m
            while r>=zero:   # loop is very slow
                c=n
                while c>=ones:
                    memo[r][c]=max(memo[r][c], 1+memo[r-zero][c-ones])
                    c -= 1
                r -= 1
        return memo[m][n]

    def findMaxForm2(self, strs, m, n):
        if not m and not n:
            return 0
    
        dp = [[0] * (n + 1) for _ in range(m + 1)]
    
        for string in strs:
            zeros, ones = string.count('0'), string.count('1')
            for z in range(m, zeros - 1, -1):
                for o in range(n, ones - 1, -1):
                    dp[z][o] = max(dp[z][o], dp[z - zeros][o - ones] + 1)
                
        return dp[m][n]


    def __init__(self):
        self.dp=[]

    def combinationSum4Dp(self, nums, target):
        if self.dp[target]>=0:
            return self.dp[target]
        total=0
        for val in nums:
            if target>=val:
                total += self.combinationSum4Dp(nums, target-val)
        self.dp[target]=total
        return total

    def combinationSum4(self, nums, target):
        self.dp=[-1]*(target+1)
        self.dp[0]=1
        return self.combinationSum4Dp(nums, target)

def testSomboSum4():
    test=Leetcode()
    strs=["10", "0001", "111001", "1", "0"]
    print(test.findMaxForm(strs, 5, 3)==4)
    #strs=["1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","101010100101010100101010010101","10100101010101001001"]*20
    #print(test.findMaxForm2(strs, 100, 100))

    print(test.combinationSum4([1,2,3], 4)==7)

class Triangle:
    def __init__(self):
        self.maxInt32=1<<31-1
    def minimumTotalDp(self, triangle, level, pos, memo):
        if level==len(triangle)-1:
            return triangle[level][pos]
        if memo[level][pos]==self.maxInt32: # not computed yet
            left = self.minimumTotalDp(triangle, level+1, pos, memo)
            right = self.minimumTotalDp(triangle, level+1, pos+1, memo)
            memo[level][pos] = min(left, right)+triangle[level][pos]
        return memo[level][pos]
        
    def minimumTotal(self, triangle):
        n=len(triangle)
        memo=[[self.maxInt32]*n for _ in range(n)]
        return self.minimumTotalDp(triangle, 0, 0, memo)

def testTriangle:
    triangle=[[1],[2,3]]
    test=Triangle()
    print(test.minimumTotal(triangle))
