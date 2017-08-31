#842A, round 430 div 2
# experience 1 ≤ l ≤ r ≤ 10^7, cost 1 ≤ x ≤ y ≤ 10^7, 1 ≤ k ≤ 10^7
# Print "YES" without quotes if a potion with efficiency exactly k exist
import math

#fast but it is trick to get special cases
def potion(exp1,exp2, cost1,cost2, k):
    # exp= k*cost
    minExp = k*cost1 # minimal exp to get k efficiency
    if minExp>exp2:
        return False
    maxExp = k*cost2 # maximal exp to get k efficiency
    if maxExp < exp1:
        return False
    #4 4 1 2 3 special case
    #99 100 1 100 50
    if exp1 > minExp and exp2 < maxExp:
        if exp1%k==0:
            return True
        if (exp1//k+1)*k<=exp2:
            return True
        return False
    return True

# slow but straight forward solution
def potion2(exp1,exp2, cost1,cost2, k):
    for i in range(cost2-cost1+1):
        exp=(i+cost1)*k
        if exp<=exp2 and exp>=exp1:
            return True
    return False

def test():
    print(potion(1,10,9,10,1)==True)
    print(potion(1,11,6,10,2)==False)
    print(potion(1,10000000,1,10000000,10000000)==True)
    print(potion(1,1000000,1,10000000,10000000)==False)
    print(potion(10000000,10000000,10,10000000,1000000)==True)
    print(potion(10000000,10000000,1,2,1000000)==False)
    print(potion(2000000,10000000,1,2,1000000)==True)
    print(potion(2000001,10000000,1,2,1000000)==False)
    print(potion(4,4,1,2,3)==False)
    print(potion(99,100,1,100,50)==True)


def solve():
    s=input()
    s=s.split()
    ok=potion(int(s[0]), int(s[1]),int(s[2]),int(s[3]),int(s[4]))
    print("YES" if ok else "NO")

solve()
