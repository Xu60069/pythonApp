#edu round 34, C
#cubic boxes, box i can be packed inside j if side ai<aj
#find minimum visible boxes
# 1 ≤ n ≤ 5000, 1 ≤ ai ≤ 10^9
# strategy:
# sort all boxes by side
# find a smaller number in answer list and replace with next box if possible
# else, add box to answer list if it is not bigger
# sort answer list to improve performance
def packing(a):
    a.sort()
    ans=[]
    for i in range(len(a)):
        found=False
        if len(ans)>0 and ans[0]<a[i]:  # check first in answer as it is sorted
                ans[0]=a[i]  # replace answer
                ans.sort()   # sort again
        else:
            ans.append(a[i]) # add new box that cannot pack smaller ones
            ans.sort()       # sort to improve performance
    return len(ans)

# better idea from editorial
# find the max boxes of the same size, that should determine the result
def packing2(a):
    a.sort()
    ans=1  #assume at least one box
    last=a[0]
    lastIndex=0
    for i in range(1,len(a)):
        if a[i]==last:
            continue
        count=i-lastIndex  #find next size
        if count>ans:
            ans=count
        last=a[i]
        lastIndex=i
    count=len(a)-lastIndex  #check last box too
    if count>ans:
        ans=count
    return ans
    
#print (packing2([1,2,3])==1)
#print (packing2([4,2,4,3,5,6,7,9,9,9,7,6,3,1,8,8])==3)


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

n=ni()
print (packing2(nia()))
