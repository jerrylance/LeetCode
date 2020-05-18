# LeetCode Solution
# Zeyu Liu
# 2019.4.15
# 836.Rectangle Overlap

from typing import List
# method 1 overlap重叠判, 满足四个条件即可, O(0), 最快
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec2[0] < rec1[2] and rec2[2] > rec1[0] and rec2[1] < rec1[3] and rec2[3] > rec1[1]
# transfer method
solve = Solution()
print(solve.isRectangleOverlap([0,0,2,2], [1,1,3,3]))

# 其他方法大体差不多，有些会用到min(), max()，考虑的太复杂