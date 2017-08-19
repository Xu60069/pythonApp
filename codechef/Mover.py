# Aug 2017 challenge, CHEFMOVR
# a mover of size D can move 1 from i to i+D
# How many moves required to make all elements of array equal
#
# strategey: average of the array should be integer
# if D>1, average of avery other d elements should also be integer, 1<=d<=D
# Observe the fact that move happen only among element, i, i+D, i+2D, i+3D, etc, when i is from 1 to D
# count from left to right, moves += |A[i]-avg|, update A[i+D] = A[i]-avg
def validate(arr, d):
    avg=-1 #compute average of each range of move
    for i in range (d):
        count=0
        total=0
        for j in range (i, len(arr), d):
            count += 1
            total += arr[j]
        avg1 = total//count
        #print("{0} / {1} = {2}".format(total, count, avg1))
        if avg1 * count!=total: # not divisible
            return False
        if avg<0:
            avg = avg1
        elif avg != avg1:
            return False
    return True

def mover2(arr, d):
    if validate(arr, d)==False:
        return -1
    s=sum(arr)
    avg=s//len(arr)
    ans=0
    for i in range (d):
        for j in range (i, len(arr), d):
            if arr[j]==avg:
                continue
            else:
                ans += arr[j]-avg if arr[j]>avg else avg-arr[j]
                arr[j+d] += arr[j]-avg
        #print(arr)
    return ans
          
def test():
    print(mover2([1, 4, 5, 2, 3], 2))#3
    print(mover2([11, 4, 5, 2, 3], 1))#18
    print(mover2([1, 4, 1], 1))      #2
    print(mover2([4, 1, 1], 1))      #3
    print(mover2([3, 4, 3, 5], 2))   #-1
    print(mover2([1,2,5,2,5], 2))    #-1
    print(mover2([1,1,5,3,5], 1))    #10
    print(mover2([1,3,3,3,5], 4))    #2
    print(mover2([2100000000,2000000000,2000000001,30,4], 1)) #6199999962
    print(mover2([1,3], 1))      #1
    print(mover2([1,1], 1))      #0
    print(mover2([1,1,1], 2))    #0
    print(mover2([1,2,3], 2))    #1
    print(mover2([1,2,6], 2))    #-1
    print(mover2([1,5,6], 2))    #-1
    print(mover2([100000000,500000000,800000000,700000000,600000000,400000000,1000000000,700000000,600000000], 3))    #13


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
        ND=nia()
        arr=nia()
        print(mover2(arr, ND[1]))

solve()
