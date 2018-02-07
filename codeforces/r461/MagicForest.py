#A xorangle of order n is such a non-degenerate triangle, that lengths of
# its sides are integers not exceeding n, and the xor-sum of the lengths is
# equal to zero
# output: Print the number of xorangles of order n
# idea:
# find such xorangles with the longest side is k, k is from 1 to n
# with each k, try len from 1 to k for the middle lenght side
# third side should equal to xor of other 2
def magicOne(longest):
    count=0
    for side2 in range (2,longest+1): # middle len cannot be 1, if so, third must be 1 too, no solution
        other = longest ^ side2
        if other <= side2 and other+side2>longest: # third side myst be shortest, and form legal triangle
            count += 1
    return count

def magicXor(n):
    count=0;
    for i in range(1, n+1):
        count += magicOne(i)
    return count

def test():
    print(magicXor(6)==1)
    print(magicXor(10)==2)

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

print(magicXor(ni()))
