def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0
    
def solve():
    n=ni()
    pos=0
    neg=0
    for i in range(n):
        s=input()
        xy=s.split()
        if int(xy[0])<0:
            neg +=1
        else:
            pos += 1
    if pos<=1 or neg<=1:
        print("Yes")
    else:
        print("No")

solve()
