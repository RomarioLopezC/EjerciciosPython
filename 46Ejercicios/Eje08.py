__author__ = 'romarinpc'


# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome("rassdar"))
