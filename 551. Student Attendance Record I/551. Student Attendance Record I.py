# LeetCode Solution
# Zeyu Liu
# 2019.3.14
# 551.Student Attendance Record I

from typing import List
# method 1 count(), 注意理解题意，转化'LLL'的条件, 快
class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1 or s.count('LLL') > 0:
            return False
        return True
# transfer method
solve = Solution()
print(solve.checkRecord("PPALLL"))

# method 2 iteration
class Solution:
    def checkRecord(self, s: str) -> bool:
        c1 = 0
        for i in s:
            if i == 'A':
                c1 += 1
                if c1 > 1:
                    return False
            elif 'LLL' in s:
                return False
        return True
solve = Solution()
print(solve.checkRecord("PPALLL"))

# method 3 方法2优化
class Solution:
    def checkRecord(self, s: str) -> bool:
        c1 = 0
        c2 = 0
        for i in s:
            if i == 'A':
                c1 += 1
                if c1 > 1:
                    return False
            if i == 'L':
                c2 += 1
            if i != 'L':
                c2 = 0
            if c2 > 2:
                return False
        return True
solve = Solution()
print(solve.checkRecord("PPALLL"))