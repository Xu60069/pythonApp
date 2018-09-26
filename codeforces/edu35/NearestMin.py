# smallest distance of 2 minimum numbers in an array
def solve (arr):
    minPos=0  #position of current min val
    minDist=999999999 #distance between 2 min val, set to MAX
    minVal=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minVal:
            minVal=arr[i]  # new min
            minDist=999999999
            minPos=i
        elif arr[i]==minVal:
            dist=i-minPos   #find next minVal, calc dist
            if dist < minDist:
                minDist=dist
            minPos=i
    return minDist

def test():
    print(solve([3,3,4,3])==1)
    print(solve([5,6,5])==2)
    print(solve([5,5,6,5,4,5,6,4])==3)
    print(solve([2, 1, 3, 5, 4, 1, 2, 3, 1])==3)

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

#test()
n=ni()
print(solve(nia()))
