#888B
def count(s):
    x=0
    y=0
    steps=0
    maxCount=0;
    for c in s:
        if c=='U':
            y += 1
        elif c=='D':
            y -= 1
        elif c=='L':
            x -= 1
        elif c=='R':
            x += 1
        steps += 1
        if x==0 and y==0:
            maxCount = steps
    print(maxCount)

def count2(s):
    left=0
    right=0
    up=0
    down=0;
    for c in s:
        if c=='U':
            up += 1
        elif c=='D':
            down += 1
        elif c=='L':
            left += 1
        elif c=='R':
            right += 1
    print(len(s)-abs(left-right)-abs(up-down))
    
def test():
    count2("LDUR")
    count2("RRRUU")
    count2("LLRRRR")

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
    n=input()
    count2(input())

solve()
