def palindrome(s):
    s=s.strip("0")
    s1=s[::-1]
    if s==s1:
        print("YES")
    else:
        print("NO")

palindrome(input())
