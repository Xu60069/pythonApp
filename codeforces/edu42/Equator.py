def midSum(arr):
    total=sum(arr)
    total = (total+1)//2
    s=0
    for i in range(len(arr)):
        s += arr[i]
        if s>= total:
            return i+1
    return len(arr)

def test():
    print(midSum([1,3,2,1])==2)
    print(midSum([2,2,2,2,2,2])==3)
    print(midSum([1,3,4,1])==3)

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

n=ni()
print(midSum(nia()))
