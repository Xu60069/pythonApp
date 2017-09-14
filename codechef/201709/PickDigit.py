def countDigit(s):
    count =[0]*10 # count digits from a string
    for a in s:
        idx=ord(a)-ord('0')
        count[idx] +=1
    return count

def pickAZ(count):
    ans=""
    for i in range(65,91): # A to Z
        one=i%10
        ten=i//10
        if count[one]>0 and count[ten]>0:
            if one != ten or count[one]>1:
                ans += chr(i)
    return ans

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0
      
#print(pickAZ(countDigit("123456690")))
def solve():
    T=ni()
    for t in range(T):
        print(pickAZ(countDigit(input())))

solve()
        
