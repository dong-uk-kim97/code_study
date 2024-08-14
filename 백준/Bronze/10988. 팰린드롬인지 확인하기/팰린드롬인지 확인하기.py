s = input()
def isPalindrome(s):
    if s.lower()== s.lower()[::-1]:
        return 1
    else:
        return 0
print(isPalindrome(s))