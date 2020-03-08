# LeetCode Solution
# Zeyu Liu
# 2019.3.1
# 263.Ugly Number

from typing import List
# method 1 循环迭代，快
class Solution:
    def isUgly(self, num: int) -> bool:
        s = [2,3,5]
        i = 0
        while num > 0:
            if num % s[i] == 0:
                num = num // s[i]
            else:
                i += 1
                if i == 3 and num != 1:
                    return False
                elif num == 1:
                    return True
# transfer method
solve = Solution()
print(solve.isUgly(34))

# method 2 方法1小优化
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True   
        for i in [2,3,5]:
            while (num % i) == 0:
                num = num // i
            if num == 1:
                return True
        return False
# transfer method
solve = Solution()
print(solve.isUgly(35))