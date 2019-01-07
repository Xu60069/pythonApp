def partial_reverse(arr, start, end):
    while start<end:
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start += 1
        end -= 1

#966. Vowel Spellchecker
class Solution:
    def replace_vowel(self,w):
        return re.sub(r"[aeiou]", "_", w.lower())
    
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        exact_match=set(wordlist)
        lowercase_match={w.lower():w for w in wordlist[::-1]}
        novowels_match={self.replace_vowel(w):w for w in wordlist[::-1] }
        return [w if w in exact_match else lowercase_match.get(w.lower()) 
                or novowels_match.get(self.replace_vowel(w), "") for w in queries ]

	#967. Numbers With Same Consecutive Differences
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        result=[0,1,2,3,4,5,6,7,8,9]
        if N == 1:
            return result
        result = result[1:]
        for _ in range (N-1):
            result=[10*left+right for left in result for right in {left%10+K, left%10-K} if right>=0 and right <10 ]
        return result

    #969. Pancake Sorting
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        flips=[]
        for max_val in range(len(A), 0, -1):
            i=A.index(max_val)
            #print(f"{max_val} at {i}")
            if i+1<max_val: # max val is not in position
                flips.extend([i+1, max_val])
            A=A[:i:-1]+A[:i]  # chop off the last elem each time
            print(A)
        return flips

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    #971. Flip Binary Tree To Match Preorder Traversal
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        self.i=0
        flips=[]
        def dfs(root):
            if not root:
                return True;
            if root.val != voyage[self.i]:
                return False
            if root.left and root.right and root.right.val==voyage[self.i+1]:
                root.left, root.right=root.right, root.left
                flips.append(root.val)
            self.i += 1
            return dfs(root.left) and dfs(root.right)
        return flips if dfs(root) else [-1]
