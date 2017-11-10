#888C
#given a string s consisting of lowercase Latin letters.
#Character c is called k-dominant iff each substring of s with length at least k contains c
#find minimum k such that there exists at least one k-dominant character
#Easy Medium
#compute max distance per letter, tricky part: need to compute distance to beginning and end too
#find the minimum among all letters
def dominant(s):
    ALPHA_LEN=26
    pos=[-1]*ALPHA_LEN  # store position of 26 letter
    MAX_=10000
    ans=len(s)//2+len(s)%2
    dist=[MAX_]*ALPHA_LEN # store max distance of same letter
    for i in range(len(s)):
        idx = ord(s[i])-ord('a')
        #always measure distance from start
        d=i-pos[idx]
        if dist[idx]==MAX_ or d>dist[idx]:  #update if it is first time or larger
            dist[idx]=d
            #print("{0} at {1} from {2} to {3}".format(s[i], i, dist[i], d))
        pos[idx]=i
    for i in range(ALPHA_LEN):  #update distance to end
        d=len(s)-pos[i]
        if d>dist[i]:
            #print("change at {0} from {1} to {2}".format(i, dist[i], d))
            dist[i]=d
    #print(dist)
    print(min(dist))

def test():
    dominant("abacaba")  #2
    dominant("zzzzz")    #1
    dominant("abcde")    #3
    dominant("abcd")     #3
    dominant("abcded")   #4

def nia():
    s=input()   #1 ≤ |s| ≤ 100000
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal

def solve():
    dominant(input())

solve()
