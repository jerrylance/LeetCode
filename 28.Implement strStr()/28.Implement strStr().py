# LeetCode Solution
# Zeyu Liu
# 2019.1.31
# 28.Implement strStr()
from typing import List

# method 1 find应用
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	if needle in haystack:
    		return haystack.find(needle)
    	elif needle == "":
    		return 0
    	else:
    		return -1        
# transfer method
solve = Solution()
print(solve.strStr("hello","ll"))

# method 2 方法1优化其实find命令返回的三个值正好是题目要求的
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    	#只需要一行代码
    	return haystack.find(needle)       
# transfer method
solve = Solution()
print(solve.strStr("hello","ll"))

# method 3 自己编写个find命令
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
            else:
                continue
        return -1
# transfer method
solve = Solution()
print(solve.strStr("aaaaa","dfd"))


