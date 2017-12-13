#edu round 33, B
#The number is called beautiful iff its binary representation consists of
# k consecutive ones, and then k-1 consecutive zeroes
# e.g: 1, 110
# formally, (2^k - 1) * (2^(k - 1)), geometry series from 2^(k-1) to 2^(2k-2)

def pow2(k):
    p=1
    while k>0:
        p *= 2
        k -= 1
    return p

def beau(k):
    return (pow2(k)-1)*pow2(k-1)

def maxBeauDivisor(n):  #brute force
    b=1
    for k in range(1,32):  #iterate all beauti number
        temp=beau(k)
        if temp>n:
            break
        if n%temp==0:  # check =devisibility
            b=temp
    return b

#print(maxBeauDivisor(992))
#print(maxBeauDivisor(81142))

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

n=ni()
print(maxBeauDivisor(n))
