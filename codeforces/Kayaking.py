def instability(nums):
    nums=sorted(nums)
    total=0
    maxdiff=0
    for i in range(0, len(nums),2):
        diff=nums[i+1]-nums[i]
        total += diff
        if diff>maxdiff:
            maxdiff=diff
    print(total-maxdiff)  # remove the largest

def test():
    instability([101,100,99,5,4,3,2,1]); # 3
    instability([1, 3, 4, 6, 3, 4, 100, 200]); # 5
    instability([1, 2, 3, 40, 50, 99, 100, 101]); #12

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
    instability(nia())

test()
