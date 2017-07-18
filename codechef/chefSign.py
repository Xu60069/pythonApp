# add N+1 number to N signs (<=>) to make it true for all signs
# using # in [1,P] as many time as needed. find the min P
# find the longest segment, either < or >, that wwould decide the min P
def count(_str):
    min=1
    max=1
    val=1
    #print("len {0}".format(len(_str)))
    for i in range (len(_str)):
        if _str[i] == '<':
            val += 1
        elif _str[i]=='>':
            val -= 1
        if val>max:
            max=val
        elif val<min:
            min=val
    print("min={0} max={1}".format(min,max))
    return max-min+1

class CountMaxSegment:
    def __init__(self):
        self.maxCount=0

    def calcMax(self, newMax):
        if newMax>self.maxCount:
            self.maxCount=newMax
            
    def count(self, _str):
        countLT=0;  #max segment of <
        countGT=0;
        for i in range (len(_str)):
            if _str[i] == '<':
                self.calcMax(countGT)
                countGT=0
                countLT += 1
            elif _str[i]=='>':
                self.calcMax(countLT)
                countLT=0
                countGT += 1
        self.calcMax(countGT)
        self.calcMax(countLT)
        if self.maxCount==0:
            return 1
        return self.maxCount+1

def ni():
    s=input()
    while len(s)==0:
        s=input()
    try:
        return int(s)
    except:
        return 0

def ns():
    s=input()
    while len(s)==0:
        s=input()
    return s

def solve():
    T=ni()
    while (T > 0):
        T -= 1
        counter=CountMaxSegment()
        print(counter.count(ns()))

def test():
    print(count(">"))
    print(count("<"))
    print(count("="))
    print(count("=<"))
    print(count(">="))
    print(count(">>>>=<<<"))  #5
    signs=">><>>>"
    print(count(signs))  # wrong val 5
    counter=CountMaxSegment()
    print(counter.count("="))
    print(counter.count("<"))   # lazy test, should create new object
    print(counter.count(signs)) # correct val 4
    
solve()
