# LeetCode Solution
# Zeyu Liu
# 2019.4.22
# 686.Repeated String Match

from typing import List
# method 1 chosen 3 to be sufficiently large to make sure string will contain B
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        s = ''
        for i in range(len(B)//len(A)+3):  	
        	if B in s:
        		return i
        	s += A
        return -1
# transfer method
solve = Solution()
print(solve.repeatedStringMatch("bb","bbbbbbb"))

# method 2 方法1优化, 快, 关键在于这段代码 if not set(B).issubset(set(A)): return -1 先判断B是否含有A中没有的元素
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
    	if not set(B).issubset(set(A)):
    		return -1
    	for i in range(len(B)//len(A)+3):
    		if B in i*A:
    			return i
    	return -1
# transfer method
solve = Solution()
print(solve.repeatedStringMatch("bb","bbbbbbb"))