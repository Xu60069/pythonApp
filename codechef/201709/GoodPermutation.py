def goodPermuEven(n):
    arr=[]
    for i in range(1,n+1):
        if i%2==1:
            arr.append(2*(i//2+1))
        else:
            arr.append(2*(i//2)-1)
    return arr
    
def goodPermu(n):
    if n%2==0:
        return goodPermuEven(n)
    arr=goodPermuEven(n-2)
    arr.append(n)
    arr.append(n-2)
    return arr

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def solve():
    T=ni()
    for t in range(T):
        arr = goodPermu(ni())
        for elem in arr:
            print("{0} ".format(elem), end="")
        print();
        
solve()
        
