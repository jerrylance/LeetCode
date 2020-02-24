# LeetCode Solution
# Zeyu Liu
# 2019.2.21
# 69.Sqrt(x)

from typing import List
# method 1 数学公式,最快
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
# transfer method
solve = Solution()
print(solve.mySqrt(30))

# method 2 newton's method, 数学公式，注意要用//
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x//r)//2
        return int(r)

# transfer method
solve = Solution()
print(solve.mySqrt(30))

# method 3 binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            if mid*mid > x:
                r = mid - 1
            elif mid*mid < x:
                l = mid + 1
            else:
                return mid
        return l - 1
# transfer method
solve = Solution()
print(solve.mySqrt(30))

# method 4 api,不建议
class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))
# transfer method
solve = Solution()
print(solve.mySqrt(30))

