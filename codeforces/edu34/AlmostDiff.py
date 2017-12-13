#edu round 34, D
def d(x,y):
    if abs(x-y)>1:
        return y-x
    else:
        return 0

def sumd(a):
    n=len(a)
    total=0
    for i in range(n-1):   # two loops, TLE
        for j in range(i+1,n):
            total += d(a[i], a[j])
    print(total)

def test():
    sumd([1,2,3,1,3])
    sumd([6,6,5,5])
    sumd([6,6,4,4])


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
sumd(nia())
