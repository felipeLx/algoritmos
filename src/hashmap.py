# Hashmap algorithm implementation
# temporal O(1)
# spatial O(n)
class Hashmap:
    def __init__(self):
        self.hashmap = {}

    def put(self, key, value):
        self.hashmap[key] = value

    def get(self, key):
        return self.hashmap.get(key, -1)

    def remove(self, key):
        if key in self.hashmap:
            del self.hashmap[key]
        else:
            return -1

# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, ch in enumerate(s):
            if not d.get(ch):
                d[ch] = [idx, 1]
            else:
                d[ch][1] +=1

        for ch, val in d.items():
            if val[1] == 1:
                return val[0]
        
        return -1

# let code - two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], idx]
            d[num] = idx
        return []

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        for idx, num in enumerate(nums):
            if hasher.get(num) is not None:
                return [hasher.get(num), idx]
            hasher[target - num] = idx