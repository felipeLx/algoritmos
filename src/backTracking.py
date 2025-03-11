# let code Backtracking
"""
Given a string contains digitas from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
# problema de permutação são resolvidos com 
phone_keyboard = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'] 
}

from typing import List

class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []

        def backtrack(idx, path):
            if idx == len(digits):
                res.append(path)
                return

            for letter in phone_keyboard[digits[idx]]:
                backtrack(idx + 1, path + letter)
                
        backtrack(0, "")
        return res


print(Solution2().letterCombinations("23"))

class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []

        def bt(permutation, digits):
           if not digits:
                res.append(permutation)
                return
           for letter in phone_keyboard[digits[0]]:
               bt(permutation+letter, digits[1:])
            
        bt("", digits)
        return res

print(Solution3().letterCombinations("23"))