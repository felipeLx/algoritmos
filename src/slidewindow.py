# Sliding Window Algorithm
# Given a string s, find the length of the longest substring without repeating characters.

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for idx, num in enumerate(nums):
            if not d.get(num):
                d[num] = idx
            else:
                if idx - d[num] <= k:
                    return True
                d[num] = idx
        return False
class Skidewindow:
    def __init__(self):
        self.counter = {}
        self.l = 0
        self.r = 0
        self._max = 1

    def maximumLengthSubstring(self, s: str) -> int:
        self.counter[s[0]] = 1

        while self.r < len(s) -1:
            self.r+=1
            if self.counter.get(s[self.r]):
                self.counter[s[self.r]] += 1
            else:
                self.counter[s[self.r]] = 1

            while self.counter[s[self.r]] == 3:
                self.counter[s[self.l]] -= 1
                self.l += 1
            self._max = max(self._max, self.r-self.l+1)
        
        return self._max

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {}

        counter[s[0]] = 1

        while r < len(s) -1:
            r+=1
            if counter.get(s[r]):
                counter[s[r]] += 1
            else:
                counter[s[r]] = 1

            while counter[s[r]] == 3:
                counter[s[l]] -= 1
                l += 1
            _max = max(_max, r-l+1)
        
        return _max