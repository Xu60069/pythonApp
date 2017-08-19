#Aug 2017 long challenge
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

class HiringMatch:
    def __init__(self):
        self.minSalary =[]      #min salary of student
        self.offeredSalary=[]   # salary offer from each company
        self.maxJobs=[]         # max job offers from each company
        self.offers=[]          # job offer from company to student
        self.N=0                # No of students
        self.M=0                # No of companies

    def test1(self):
        self.minSalary=[5000, 10000, 3000, 20, 100]
        self.offeredSalary=[10000,800,600,10,1000,2000]
        self.maxJobs=[2,2,1,8,9,10]
        #self.offers=[[1,1,1,1,1,1],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,1],[1,0,0,1,0,0]]
        self.offers=["111111","100000","000000","000001","100100"]
        self.N=5
        self.M=6
        self.solve()

    def solve(self):
        accepted=[0]*self.M
        totalS=0 #total salary
        numAccepted=0 # No of students got jobs
        for i in range(self.N):
            bestoffer=-1
            for j in range (self.M):
                if self.offers[i][j]=='0':
                    continue
                elif self.offeredSalary[j]<self.minSalary[i]:
                    continue
                elif self.maxJobs[j]==accepted[j]:
                    continue
                if bestoffer<0:
                    bestoffer=j
                elif self.offeredSalary[j]>self.offeredSalary[bestoffer]:
                    bestoffer=j
            if bestoffer>=0:
                numAccepted += 1
                totalS += self.offeredSalary[bestoffer]
                accepted[bestoffer] += 1
        noHire=0
        for i in range(self.M):
            if accepted[i]==0:
                noHire +=1
        print("{0} {1} {2}".format(numAccepted, totalS, noHire))

    def read(self):
        NM=nia()
        self.N=NM[0]
        self.M=NM[1]
        self.minSalary=nia()
        for i in range(self.M):
            s=nia()
            self.offeredSalary.append(s[0])
            self.maxJobs.append(s[1])
        self.offers=[""]*self.N
        for i in range(self.N):
            self.offers[i]=input()
        
def main():
    T=ni()
    for t in range (T):
        hiring = HiringMatch()
        hiring.read()
        hiring.solve()

main()            
