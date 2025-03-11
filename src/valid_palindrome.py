# let code: valid Palindrome
"""
A phrase is a palindrome if it reads the same backward as forward. For example, "madam" is a palindrome.
Write a function that takes a string as input and returns True if the string is a palindrome and False if it is not.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

class SolutionPonteiro:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1

        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        
        return True