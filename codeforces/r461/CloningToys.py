def cloing(copy, orig):
    if orig < 1:
        return False
    copyOrig=orig-1
    if copyOrig > copy:
        return False
    copy = copy-copyOrig
    return copy%2 ==0

def test():
    print(cloing(6,3))
    print(cloing(4,2))
    print(cloing(1000, 1001))

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
