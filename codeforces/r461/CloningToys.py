#Each original toy can be cloned to create one additional original and one copy
#Each copy can be cloned to create two additional copies
#Is it possible to have toys of this many copies and original
def cloing(copy, orig):
    if orig < 1:
        return False
    copyOrig=orig-1
    if copyOrig > copy:
        return False
    if copyOrig==0 and copy>0: #special case, original not cloned
        return False
    copy = copy-copyOrig
    return copy%2 ==0

def test():
    print(cloing(6,3))
    print(cloing(4,2)==False)
    print(cloing(1000, 1001))
    print(cloing(2,1)==False)  #failed case
    print(cloing(0,1)) 

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
    arr=nia()
    if cloing(arr[0], arr[1]):
        print("Yes")
    else:
        print("No")

solve()
