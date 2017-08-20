# Aug 2017 challenge, RAINBOWA, easy
# detect array in patter 1234567654321, # of same digit must be same on either side
# two strategies: check 4 rules for half of the array
#                 symmetrical, and unique number is in order of 1234567
def rainbow(arr):
    mid=(len(arr)+1)//2  #ceiling
    last=len(arr)-1
    if arr[0] != 1:     #must start from 1
        return False
    if arr[mid-1] != 7: #highest at middle is 7
        return False
    for i in range(mid):
        if arr[i] != arr[last-i]: #symmetrical
            return False
        if i<0:
            continue
        if arr[i]<arr[i-1] or arr[i]-arr[i-1]>1: #none decreasing, increment at most 1
            return False
    return True

def solve(arr):
    if rainbow(arr):
        print("yes")
    else:
        print("no")

def unique(arr):
    s=set()
    uni=[]
    for i in range(len(arr)):
        if arr[i] not in s:
            s.add(arr[i])
            uni.append(arr[i])
    return uni
            
def solve2(arr):
    r=arr[:]
    r.reverse()
    if r != arr:
        print("no")
        return
    uarr=unique(arr)
    if uarr==[1,2,3,4,5,6,7]:
        print("yes")
    else:
        print("no")

def test():
    solve([1,2,3,4,5,6,7,6,5,4,3,2,1])
    solve([1,2,3,4,4,5,6,6,6,7,6,6,6,5,4,4,3,2,1])
    solve([1,2,3,4,5,6,7,6,5,4,3,2,1,1])
    solve([1,2,3,4,5,6,8,6,5,4,3,2,1])
    solve([2,3,4,5,6,7,6,5,4,3,2])
    solve([1,2,3,4,5,6,7,7,6,5,4,3,2,1])
    solve([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])

def test2():
    solve2([1,2,3,4,5,6,7,6,5,4,3,2,1])
    solve2([1,2,3,4,4,5,6,6,6,7,6,6,6,5,4,4,3,2,1])
    solve2([1,2,3,4,5,6,7,6,5,4,3,2,1,1])
    solve2([1,2,3,4,5,6,8,6,5,4,3,2,1])
    solve2([2,3,4,5,6,7,6,5,4,3,2])
    solve2([1,2,3,4,5,6,7,7,6,5,4,3,2,1])
    solve2([1,2,3,4,5,6,7,8,7,6,5,4,3,2,1])
    
def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def main():
    T=ni()
    for t in range(T):
        n=ni()
        NB=nia()
        solve2(NB)

main()
