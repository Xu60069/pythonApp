
def moveOnce(arr, d, avg):
    total=0
    done=True
    for i in range (len(arr)-d):
        if arr[i]==avg:
            continue
        elif arr[i]>avg:
            total+=arr[i]-avg
            arr[i+d]+=arr[i]-avg
            arr[i]=avg
        else:
            moves = avg-arr[i]
            if moves > arr[i+d]:
                moves=arr[i+d]
            total += moves
            arr[i] += moves
            arr[i+d] -= moves
            if arr[i] != avg:
                done=False
    for i in range(len(arr)-d, len(arr)):
        if arr[i] != avg:
            done=False
            break
    return (total, done) 
            
def mover(arr, d):
    s=sum(arr)
    avg=s//len(arr)
    if avg * len(arr) != s:
        return -1
    total=0
    done=False
    while done==False:
        s, done=moveOnce(arr, d, avg)
        total += s
        #print(total)
        #print(done)
        if done:
            return total
        elif s==0:
            return -1

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
            elif arr[j]>avg:
                ans += arr[j]-avg
                arr[j+d] += arr[j]-avg
                arr[j]=avg
            else:
                diff=avg-arr[j]
                ans += diff
                arr[j+d] -= diff
                arr[j]=avg
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
