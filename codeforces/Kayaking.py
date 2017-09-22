# 2n numbers, 2n-2 pair, 2 singles
# find the minimal sum of difference of all pairs
# sort numbers, skip 2 numbers (n-1)*(n-1) ways
# find minimal of sum of pair difference
def strip2(nums, s1, s2):
    res=[0]*(len(nums)-2)
    j=0
    for i in range(0, len(nums)):
        if i==s1 or i==s2:
            continue
        res[j]=nums[i];
        j += 1
    return res

def countPairwiseDiff(nums):
    total=0
    for i in range(1, len(nums), 2):
        total += nums[i]-nums[i-1]
    return total

def completeSearch(nums):
    nums=sorted(nums)
    ans=1999999999
    # skip two numbers, pair the rest of them in order
    for skip1 in range(len(nums)-1):
        for skip2 in range(skip1+1, len(nums)):
            total=countPairwiseDiff(strip2(nums, skip1,skip2))
            if total<ans:
                ans=total
    print(ans)  # remove the largest

def test():
    completeSearch([101,100,99,5,4,3,2,1]); # 3
    completeSearch([1, 3, 4, 6, 3, 4, 100, 200]); # 5
    completeSearch([1, 2, 3, 40, 50, 99, 100, 101]); #12
    completeSearch([1, 9, 10, 20, 100, 1000, 1001, 10001]); #19

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def solve():
    n=input()
    completeSearch(nia())

solve()
