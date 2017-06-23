
class Node:
    def __init__(self):
        self.R =26
        self.name=None
        self.next=[None]*self.R

class Trie26:
    def __init__(self):
        self.base='a'
        self.root=None

    def put(self, key):
        self.root=self.put_(self.root, key, 0)

    def getIndex(self, str, d):
        return ord(str[d])-ord(self.base)
        
    def put_(self, n, k, d):
        if (n==None):
            n= Node()
        if (d==len(k)):
            n.name=k
            return n
        ind=self.getIndex(k, d)
        #print(ind);
        n.next[ind]=self.put_(n.next[ind], k, d+1)
        return n

    def prefixMatch_(self,n,k,d):
        if (n==None):
            return 0
        if (d==len(k)):
            return d
        ind=self.getIndex(k, d)
        if (n.next[ind]==None):
            return d
        return self.prefixMatch_(n.next[ind], k, d+1)

    def prefixMatch(self,key):
        return self.prefixMatch_(self.root, key, 0)

def trieTest():
    tr=Trie26()
    tr.put("google")
    print(tr.prefixMatch("goo")==3);
    print(tr.prefixMatch("oog")==0);
    print(tr.prefixMatch("googler")==6);
    print(tr.prefixMatch("g")==1);

def solve(trie, blocked):
    ans=set()
    for site in blocked:
        match=trie.prefixMatch(site)
        if (match==len(site)):
            print(-1)
            return
        ans.add(site[:match+1])
    print(len(ans))
    sorted = list(x for x in ans)
    #print(type(sorted))
    sorted.sort()
    for str in sorted:
        print(str)

def blockedWebTest():
    tr=Trie26()
    tr.put("google");
    tr.put("codechef");
    blocked=["codeforces","codefool"]
    solve(tr, blocked)  #codef
    blocked.append("codechill");
    solve(tr, blocked);
    blocked.append("youtube");
    blocked.append("yoyo");
    solve(tr, blocked);
    tr.put("codechefxyz");
    blocked.append("codechefu");
    solve(tr, blocked);
    blocked.append("codechefx");
    solve(tr, blocked);

def blockedWeb():
    tr=Trie26()
    blocked=[]
    n=int(input())
    for i in range(n):
        cmd,site=input().split(" ")
        if cmd=='+':
            tr.put(site)
            #print("approve "+site)
        else:
            blocked.append(site)
            #print("block"+site)
    solve(tr, blocked)

blockedWeb()
#print("done")

