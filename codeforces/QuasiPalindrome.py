#educational round 29, 863A
#a number is palindrome if we can pad some 0 from left
#determin if a number is quasi palindrome
def palindrome(s):
    s=s.strip("0")
    s1=s[::-1]
    if s==s1:
        print("YES")
    else:
        print("NO")

palindrome(input())
