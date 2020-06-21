# LeetCode Solution
# Zeyu Liu
# 2019.5.18
# 1450.Number of Students Doing Homework at a Given Time

from typing import List
# method 1 straight forward
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
        	if startTime[i] <= queryTime and endTime[i] >= queryTime:
        		count += 1
        return count
# transfer method
solve = Solution()
print(solve.busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))

# method 2 oneline, zip()
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))
# transfer method
solve = Solution()
print(solve.busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5))