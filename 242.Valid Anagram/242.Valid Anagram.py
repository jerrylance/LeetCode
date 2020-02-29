# LeetCode Solution
# Zeyu Liu
# 2019.2.22
# 242.Valid Anagram

from typing import List
# method 1 利用replace(),很慢，不推荐
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s) != len(t):
    		return False
    	for i in t:
    		if i in s:
    			s = s.replace(i,'',1)
    		else:
    			return False
    	return s == ''
       
# transfer method
solve = Solution()
print(solve.isAnagram("rat","cat"))

# method 2 利用sorted排序性质
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	if len(s) != len(t):
    		return False
    	return sorted(s) == sorted(t)     
# transfer method
solve = Solution()
print(solve.isAnagram("rat","cat"))

# method 3 API Counter()
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    	from collections import Counter
    	return Counter(s) == Counter(t)  
# transfer method
solve = Solution()
print(solve.isAnagram("rat","cat"))

