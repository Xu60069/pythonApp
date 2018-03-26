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

def testTriangle():
    triangle=[[1],[2,3]]
    test=Triangle()
    print(test.minimumTotal(triangle))

#416. Partition Equal Subset Sum
class EqualSubsetSum:  #beat 77%
    def canPartition(self, nums):
        sum=0  # or int(0)
        for n in nums:
            sum += n
        if sum&1 == 1:
            return False
        sum //= 2  # don't use /= float
        dp = [False]*(sum+1)
        dp[0]=True
        for n in nums:
            if sum>=n:
                dp[sum] = dp[sum] or dp[sum-n]
                if dp[sum]:
                    return True
            for j in range(sum-1, 0, -1):
                if j>=n:
                    dp[j] = dp[j] or dp[j-n]
        return dp[sum]

def testEqualSubsetSumPartition():
    test=EqualSubsetSum()
    print(test.canPartition([3,3,3,4,5]))
    print(test.canPartition([1, 2, 3, 5])==False)

class DominoTromino:
    def numTilings(self, N):
        if N<3:
            return N
        dp=[0]*(N+1)
        dp[1]=1
        dp[2]=2
        dp2=[0]*(N+1)
        dp2[1]=1
        dp2[2]=2
        for n in range (3, N+1):
            dp[n] = (dp[n-1] + dp[n-2]) % MOD  # domino to domino
            dp[n] = (dp[n] + dp2[n-1]) % MOD   # tromino+tromino
            dp2[n] = (2 * dp[n-2]) % MOD       # domino + tromino
            dp2[n] = (dp2[n] + dp2[n-1]) % MOD # tromino + domino extend tromino

        return dp[N]
    
class OutBoundaryPaths:
    def findPaths(self, m, n, N, i, j):
        dp3 = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range (2)]
        MOD=1000000007
        prev = 0
        current = 0
        for x in range (1, N+1):
            current = 1 - prev
            for r in range (m):
                for c in range (n):
                    dp3[current][r][ c] = 1 if r == 0 else  dp3[prev][r - 1][c]  # up !ERROR don't use i-- etc
                    dp3[current][r][c] += 1 if r == m - 1 else dp3[prev][r + 1][c]  # down
                    #dp3[current][r][c] %= MOD
                    dp3[current][r][c] += 1 if c == 0 else dp3[prev][r][c - 1]  # left
                    #dp3[current][r][c] %= MOD
                    dp3[current][r][c] += 1 if c == n - 1 else dp3[prev][r][c + 1]  # left
                    dp3[current][r][c] %= MOD
            prev = current; # swap
        return dp3[current][i][j];
                    
        
