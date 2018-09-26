# card has letter lower case on one side, digit on the other
# is it true: if a card has vowel (a e i o u) on one side, digit is even
# find minimal cards to flip to verify statement true or false
# string show char of either side, 1<=len<=50
# verify if one side is vowel, other side must be even digit
# verify if one side is odd digit, other side must not be vowel
def count(s):
    target="aeiou13579"
    count=0
    for c in s:
        if c in target:
            count +=1
    return count

def test():
    print(count("ee"))
    print(count("z"))
    print(count("0ay1"))

print(count(input()))
