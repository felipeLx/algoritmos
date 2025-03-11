# let code: dynamic programming
"""
House Robber: you are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
# é quando a execusão do algorigmo vai depender de uma solução anterior
# temporal O(n)
from typing import List

class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

print(Solution().rob([2, 7, 9, 3, 1]))

class Solution2:
    def rob(self, nums: List[int]) -> int:
        one_before, two_before = 0, 0
        for num in nums:
            one_before, two_before = max(one_before, two_before + num), one_before
        return one_before

print(Solution2().rob([1,2,3,1]))