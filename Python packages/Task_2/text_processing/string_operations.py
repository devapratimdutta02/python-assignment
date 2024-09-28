def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]