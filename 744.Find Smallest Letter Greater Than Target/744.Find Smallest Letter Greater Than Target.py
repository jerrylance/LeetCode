# LeetCode Solution
# Zeyu Liu
# 2019.4.12
# 744.Find Smallest Letter Greater Than Target

from typing import List
# method 1 ord()
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(target) >= ord(letters[-1]):
        	return letters[0]
        for i in letters:
        	if ord(i) > ord(target):
        		return i
# transfer method
solve = Solution()
print(solve.nextGreatestLetter(["c", "f", "j"],"k"))

# method 2 方法1优化，都是小写字母可以不用ord，直接比较大小
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
        	if i > target:
        		return i
        return letters[0]
# transfer method
solve = Solution()
print(solve.nextGreatestLetter(["c", "f", "j"],"k"))

# method 3 binary search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    	if target >= letters[-1]:
    		return letters[0]
    	l, r = 0, len(letters)-1
    	while l < r:
    		m = (l+r) // 2
    		if letters[m] > target:
    			r = m
    		else:
    			l = m + 1
    	return letters[l]
# transfer method
solve = Solution()
print(solve.nextGreatestLetter(["c", "f", "j"],"k"))