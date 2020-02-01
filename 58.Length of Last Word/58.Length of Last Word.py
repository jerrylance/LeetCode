# LeetCode Solution
# Zeyu Liu
# 2019.1.30
# 58.Length of Last Word
from typing import List

# method 1 remove 和while 应用
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    	if s:
    		last = s.split(" ")
    		while '' in last:#循环去除空值
    			last.remove('')
    		if last == []:
    			return 0
    		else:
    			return len(last[-1])
    	else:
    		return 0
# transfer method
solve = Solution()
print(solve.lengthOfLastWord(" a "))

# method 2 方法1的优化，strip可以去除首和尾的空白字符.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    	if s:
    		s = s.strip()
    		last = s.split(" ")
    		return len(last[-1])# 注意这里如果返回的是空值，则长度len(last[-1]) = 0
    	else:
    		return 0
# transfer method
solve = Solution()
print(solve.lengthOfLastWord("    "))
