#842B, round 430 div 2
import math

def distance(x1,y1,x2,y2):
    dx=(x2-x1);
    dx *= dx
    dy=y2-y1
    dy *= dy
    return math.sqrt(dx+dy)

class Pizza:
    def __init__(self, r, d):
        self.r=r  # radius of whole pizza
        self.d=d  # width of crust, pizza edge without cheese and source

    def onCrust(self, x, y, r):
        dist=distance(0,0,x,y) # distance from origin of sausage to center of pizza
        if dist-r<self.r-self.d:  # sausage touch pizza none crust
            return False
        if dist+r>self.r:    # sausage partially outside of pizza
            return False
        return True

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

def test():
    pizza = Pizza(8, 4)
    print(pizza.onCrust(7,8,1)==False)
    print(pizza.onCrust(-7,3,2)==False)
    print(pizza.onCrust(0,2,1)==False)
    print(pizza.onCrust(0,-2,2)==False)
    print(pizza.onCrust(-3,-3,1)==False)
    print(pizza.onCrust(0,6,2)==True)
    print(pizza.onCrust(5,3,1)==True)
    
def solve():
    rd=nia()
    T=ni()
    pizza = Pizza(rd[0], rd[1])
    count=0;
    for i in range(T):
        sausage = nia()
        if pizza.onCrust(sausage[0], sausage[1],sausage[2]):
            count +=1
    print(count)

solve()

