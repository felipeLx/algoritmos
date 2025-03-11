class Solution:
    def reverseWords(self, s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                res += s[l:r+1][::-1]
                r += 1
                l = r

        res += ' '
        res += s[l:r + 2][::-1]
        return res[1:]

# let code: two pointers: valid palindrome
"""
A phrase is a palindrome if it reads the same backward as forward. For example, "madam" is a palindrome.
Write a function that takes a string as input and returns True if the string is a palindrome and False if it is not.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]