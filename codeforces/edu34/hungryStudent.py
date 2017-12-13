#edu round 34, A
#A small portion contains 3 chunks; a large one — 7 chunks
#Ivan wants to eat exactly x chunks.
# solve 3*a+7*b=x

def solve(x):  #brute force to check all possible b
    maxB=x//7+1
    for b in range(maxB):
        if (x-b*7)%3==0:  #if a is integer, done
            return True
    return False

def test():
    print(solve(1))
    print(solve(3))
    print(solve(6))
    print(solve(5))
    print(solve(7))
    print(solve(10))
    print(solve(27))
    print(solve(39))

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

t=ni()
while t>0:
    t -= 1
    n=ni()
    print("YES" if solve(n) else "NO")
