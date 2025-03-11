# binary search
# temporal O(log n)
"""
Quando dobramos o input aumentamos apenas uma unidade de tempo
"""
# spatial O(1)
def binary_search(nums, n):
    lo = 0
    hi = len(nums)
    steps = 0
    while lo < hi:
        steps += 1
    mid = int((lo + hi) / 2)

    if nums(mid) == n:
        print("step: ", steps)
        return mid
    elif nums(mid) < n:
        lo = mid + 1
    else:
        hi = mid
    return -1

# Let Code: Number of 1 Bits
"""
Given a positive integer n, return the number of set bits in its binary representation.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

print(Solution().hammingWeight(2147483645))
print(Solution().hammingWeight(128))
"""
The & operator is a bitwise AND operator. It compares the binary representation of the two numbers and returns a new number where the bits are set to 1 if both bits are 1 in the input numbers. Otherwise, it sets the bit to 0.
The >> operator is a bitwise right shift operator. It shifts the bits of the number to the right by the specified number of positions. In this case, we are shifting the bits of the number n to the right by 1 position in each iteration.
"""