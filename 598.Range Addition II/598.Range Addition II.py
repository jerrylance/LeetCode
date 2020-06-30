# LeetCode Solution
# Zeyu Liu
# 2019.6.9
# 598.Range Addition II

from typing import List
# method 1 min()，找出最小的行列数
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    	if ops == []:
    		return m * n
    	return min(i[0] for i in ops) * min(j[1] for j in ops)
# transfer method
solve = Solution()
print(solve.maxCount(3, 3, [[2,2],[3,3]]))

# method 2 zip(*)
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    	if ops == []:
    		return m * n
    	a, b = zip(*ops)
    	return min(a) * min(b)
# transfer method
solve = Solution()
print(solve.maxCount(3, 3, [[2,2],[3,3]]))

# method 3 方法1优化
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for i in ops:
            m = min(m,i[0])
            n = min(n,i[1])
        return m * n
# transfer method
solve = Solution()
print(solve.maxCount(3, 3, [[2,2],[3,3]]))