# Check if a string is a palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]