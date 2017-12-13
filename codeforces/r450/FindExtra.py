#round 450, A
#n distinct points on a plane, none of them lie on OY axis
#if all remaining points on one side of OY after removing one point
#simply strategy:
#count positive x and negative x of points
#Yes if either count is <=1
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
        if int(xy[0])<0: # check only x
            neg +=1
        else:
            pos += 1
    if pos<=1 or neg<=1:
        print("Yes")
    else:
        print("No")

solve()
