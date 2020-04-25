# LeetCode Solution
# Zeyu Liu
# 2019.4.1
# 709.To Lower Case

from typing import List
# method 1 lower(), oneline
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
# transfer method
solve = Solution()
print(solve.toLowerCase("LOVELY"))

# method 2 ord() convert to ASCII value, chr() convert ASCII to character
class Solution:
    def toLowerCase(self, str: str) -> str:
    	s = ''
    	for i in str:
    		if ord(i) >= 65 and ord(i) <= 90:
    			s += chr(ord(i)+32)
    		else:
    			s += i
    	return s
# transfer method
solve = Solution()
print(solve.toLowerCase("LOVELY"))
