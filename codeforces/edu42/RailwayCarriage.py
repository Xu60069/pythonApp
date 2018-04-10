def solve(carriage, n, a, b):
    odd=0;
    total=0
    subsum=0;
    for ch in carriage:
        if ch=='.':
            subsum +=1
        elif ch=='*':
            total += subsum
            if subsum%2==1:
                odd += 1
            subsum=0
    total += subsum
    if subsum%2==1:
        odd += 1
    even=(total-odd)//2
    ans=0
    if a<= even:
        ans += a
        a=0
    else:
        ans+=even
        a -= even
    if b<= even:
        ans += b
        b=0
    else:
        ans+=even
        b -= even
    #print(even)
    #print(odd)
    #print(a+b)
    return ans+min(a+b, odd)

def test():
    print(solve("*...*", 5, 1, 1)==2)
    print(solve("*...*.", 6, 2, 3)==4)
    print(solve(".*....**.*.", 11, 3, 10)==7)
    print(solve("***", 3, 2, 3)==0)
    

def nia():
    s=input()
    while len(s)==0:
        s=input()
    s=s.split()
    iVal=[];
    for i in range (len(s)):
        iVal.append(int(s[i]))
    return iVal


n=nia()
arr=input()
print(solve(arr, n[0], n[1], n[2]))

