class Node:
    def __init__(self):
        self.name=None
        self.next=[]

class Trie26:
    def __init__(self):
        self.R =26
        self.base='a'
        self.root=None

    def put(self, key):
        self.root=self.put_(self.root, key, 0)

    def put_(self, n, k, d):
        if (n==None):
            n= Node()
        if (d==len(k)):
            n.name=k
            return n
        ind=ord(self.base)
        ind=ord(k[d])-ind
        n.next[ind]=self.put_(n.next[ind], k, d+1)
        return n

    def prefixMatch_(self,n,k,d):
        if (n==None):
            return 0
        if (d==len(k)):
            return d
        if (n.next[k[d]-self.base]==None):
            return d
        return self.prefixMatch_(n.next[k[d]-self.base], k, d+1)

    def prefixMatch(self,key):
        return self.prefixMatch_(self.root, key, 0)

test="test"
print(test[0])
tr=Trie26()
tr.put("google")
print(tr.prefixMatch("goo"));
