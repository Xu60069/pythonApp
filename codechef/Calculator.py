# a is N%B, initial push of first button
# b=N/B, max push for second button, x actual push of second button
# N is total energy, B is energy need to push second button.
# return # of second button
def eval(a, b, x, B):
    return x * (a+ (b-x) * B)

def brutforceCalc(low, hi, a, b, B):
    max=0
    for x in range (hi-low+1):
        val=eval(a, b, x+low, B)
        if ( val==0 ):
            continue
        if (max<val):
            max=val
        else:
            break
    #print("b buttons {0} max {1} a={2} B={3}".format(x-1, b, a, B))
    return max

def maximizeBrute(N, B):
    b=N//B
    a=N%B
    low= 0 if a==0 else 1
    return brutforceCalc(low, b, a, b, B)

# upsidedown parabola, pick 5 points to find the vertex
def binaryCalc(low, hi, a, b, B, lowVal, hiVal):
    if hi-low<=10:
        return brutforceCalc(low, hi, a, b, B)
    mid = (low+hi)//2
    midLow = (low+mid)//2
    midHi = (mid+hi)//2
    midVal= eval(a, b, mid, B)
    midLowVal= eval(a, b, midLow, B)
    midHiVal = eval(a, b, midHi, B)
    if ( midVal>midLowVal and midVal>midHiVal ):
        return binaryCalc(midLow, midHi, a, b, B, midLowVal, midHiVal)
    elif midVal<midHiVal:
        return binaryCalc(mid, hi, a, b, B, midVal, hiVal)
    elif midVal<midLowVal:
        return binaryCalc(low, mid, a, b, B, lowVal, midVal)
    elif midVal==midHiVal:  # watch oout for two special edge cases
        return binaryCalc(mid, midHi, a, b, B, midVal, midHiVal)
    elif midVal==midLowVal:
        return binaryCalc(midLow, mid, a, b, B, midLowVal, midVal)
    else:
        print("low {0}, {1}".format(low, lowVal))
        print("midlow {0}, {1}".format(midLow, midLowVal))
        print("mid {0}, {1}".format(mid, midVal))
        print("midHi {0}, {1}".format(midHi, midHiVal))
        print("hi {0}, {1}".format(hi, hiVal))
        return 0

def maximize(N, B):
    b=N//B
    a=N%B
    low= 0 if a==0 else 1
    lowVal=eval(a, b, low, B)
    hiVal=eval(a, b, b, B)
    return binaryCalc(low, b, a, b, B, lowVal, hiVal)

def test():
    print(maximize(10,2))
    print(maximize(8,5))
    print(maximize(6,1))
    print(maximizeBrute(1000000, 500))
    print(maximize(1000000, 500))
    
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

def solve():
    T=ni()
    for t in range(T):
        NB=nia()
        print(maximize(NB[0], NB[1]))

solve()
