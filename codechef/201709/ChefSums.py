
def prefixSum(arr):
    psum=[0]*len(arr)
    psum[0]=arr[0]
    for i in range(1, len(arr)):
        psum[i]=psum[i-1]+arr[i]
    return psum

def suffixSum(arr):
    ssum=[0]*len(arr)
    size=len(arr)
    ssum[size-1]=arr[size-1]
    for i in range(size-2, -1, -1):
        ssum[i] = ssum[i+1]+arr[i]
    return ssum

def minSums(arr):
    if len(arr)==1:
        return 1
    psum=prefixSum(arr)
    ssum=suffixSum(arr)
    minVal=psum[0]+ssum[0];
    minPos=0
    for i in range(len(arr)):
        s=psum[i]+ssum[i]
        if minVal>s:
            minVal=s
            minPos=i
    return minPos+1
        
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

def solve():
    T=ni()
    for t in range(T):
        n=ni()
        arr=nia()
        print(minSums(arr))

solve()
