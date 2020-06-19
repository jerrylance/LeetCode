# LeetCode Solution
# Zeyu Liu
# 2019.4.16
# 1108.Defanging an IP Address

from typing import List
# method 1 split(),join(),快
class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = address.split('.')
        return '[.]'.join(l)
# transfer method
solve = Solution()
print(solve.defangIPaddr("255.100.50.0"))

# method 2 replace()
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
# transfer method
solve = Solution()
print(solve.defangIPaddr("255.100.50.0"))

# method 3 常规法,最快
class Solution:
    def defangIPaddr(self, address: str) -> str:
        s = ''
        for i in address:
        	if i == '.':
        		s += '[' + i + ']'
        	else:
        		s += i
        return s
# transfer method
solve = Solution()
print(solve.defangIPaddr("255.100.50.0"))

