# LeetCode Solution
# Zeyu Liu
# 2019.6.11
# 1460.Make Two Arrays Equal by Reversing Sub-arrays

from typing import List
# method 1 Oneline, sorted()
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
# transfer method
solve = Solution()
print(solve.canBeEqual([1,2,3,4], [2,4,1,3]))

# method 2 sum(), set()
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sum(target) == sum(arr) and set(target) == set(arr):
            return True
        return False
# transfer method
solve = Solution()
print(solve.canBeEqual([1,2,3,4], [2,4,1,3]))

# method 3 API, Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        import collections
        c = collections.Counter(target)
        for i in arr:
            c[i] -= 1
            if c[i] < 0:
                return False
        return True  
# transfer method
solve = Solution()
print(solve.canBeEqual([1,2,3,4], [2,4,1,3]))