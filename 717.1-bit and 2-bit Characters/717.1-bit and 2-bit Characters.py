# LeetCode Solution
# Zeyu Liu
# 2019.5.25
# 717.1-bit and 2-bit Characters

from typing import List
# method 1 找规律，索引值为0时，索引奇偶性影响结果
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #if bits[-2] == 0:
        #	return True
        #if bits[-3] == 0:
        #	return False
        #if bits[-4] == 0:
        #	return True
        #if bits[-5] == 0:
        #	return False
        for i in range(-2, -len(bits)-1, -1):
        	if bits[i] == 0:
        		if i % 2 == 0:
        			return True
        		else:
        			return False
        if len(bits) % 2 == 0:
        	return False
        return True
# transfer method
solve = Solution()
print(solve.isOneBitCharacter([1, 1, 1, 0]))

# method 2 bits[i] == 0 means it's a 1-bit char, bits[i] == 1 means a start of a 2-bit char
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
    	i = 0
    	while i < len(bits) - 1:
    		if bits[i] == 0:
    			i += 1
    		else:
    			i += 2
    	return i == len(bits) - 1 and bits[i] == 0
# transfer method
solve = Solution()
print(solve.isOneBitCharacter([1, 1, 1, 0]))

# method 3 方法2进一步优化
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
    	i = 0
    	while i < len(bits) - 1:
    		i += 1 + bits[i]
    	return i == len(bits) - 1
# transfer method
solve = Solution()
print(solve.isOneBitCharacter([1, 1, 1, 0]))