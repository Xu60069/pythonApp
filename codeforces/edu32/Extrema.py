#888A
#a local minimum iff it is strictly less than both of its neighbours
#local maximum iff it is strictly greater than its neighbours
#Since a1 and an have only one neighbour each, they are neither local minima nor local maxima
#An element is called a local extremum iff it is either local maximum or local minimum.
#Your task is to calculate the number of local extrema in the given array.
#Simple count minimum or minimum
def extr(arr):
    count = 0
    for i in range( 1,len(arr)-1 ):
        if arr[i]<arr[i+1] and arr[i]<arr[i-1]:
            count += 1
        elif arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            count += 1
    print (count)

def test():
    extr([1])
    extr([1,2])
    extr([1,2,3])
    extr([1,5,2,5])

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
    n=input()  #1 ≤ n ≤ 1000
    extr(nia())

solve()
