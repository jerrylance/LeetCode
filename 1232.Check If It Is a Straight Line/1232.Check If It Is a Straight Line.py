# LeetCode Solution
# Zeyu Liu
# 2019.5.3
# 1232.Check If It Is a Straight Line

from typing import List
# method 1 数学公式法，寻找k = dx/dy,遍历第三个点之后与前两点的斜率k是否一致，需要注意的是，使用乘法代替除法，避免除数为0
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(2,len(coordinates)):
        	if (coordinates[i][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[1][0]) != (coordinates[i][1] - coordinates[1][1]) * (coordinates[i][0] - coordinates[0][0]):
        		return False
        return True
# transfer method
solve = Solution()
print(solve.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))

# method 2 直接套公式y = kx + b
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x2 - x1 != 0:
            k = (y2 - y1) / (x2 - x1)
        else:
            k = 0
        b = y1 - k*x1
        for i in coordinates:
            if i[1] != k * i[0] + b: 
                return False
        return True
# transfer method
solve = Solution()
print(solve.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))