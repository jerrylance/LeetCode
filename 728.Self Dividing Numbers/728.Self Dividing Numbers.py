# LeetCode Solution
# Zeyu Liu
# 2019.6.1
# 728.Self Dividing Numbers

from typing import List
# method 1 straight forward, str(), int()
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
        	res.append(i)
        	for j in (str(i)):
        		if j == '0':
        			res.pop()
        			break
        		else:
        			if i % int(j) != 0:
        				res.pop()
        				break
        return res
# transfer method
solve = Solution()
print(solve.selfDividingNumbers(1, 22))

# method 2 方法1优化，不转化为字符串，进位除法，最快
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
        	num = i
        	while num:
        		if (num % 10) and i % (num % 10) == 0:
        			num //= 10
        		else:
        			break
        	if num == 0:
        		res.append(i)
        return res
# transfer method
solve = Solution()
print(solve.selfDividingNumbers(1, 22))