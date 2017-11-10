#888B
#robot move in 4 directions, U D L R
#Given a sequence, this robot always come back to where it started (0,0)
#Assume it skipped some moves, find the manimum commands robot could take
#Easy
#count total moves to each of the 4 directions
#difference between L and R, and  between U and D are the commands skipped
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
