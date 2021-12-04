def isPalindrome(s):
    s.lower()
    if s.lower() == s.lower()[::-1]:
        return True    
    else:
        return False

print(isPalindrome(input("Palavra: ")))