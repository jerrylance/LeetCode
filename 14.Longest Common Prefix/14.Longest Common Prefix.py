# LeetCode Solution
# Zeyu Liu
# 2019.2.19
# 14.Longest Common Prefix

from typing import List
# method 1 取第一项切片，从右往左缩小切片范围
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	if strs == []:
    		return ''
    	l = len(strs[0])
    	i = 0
    	while l > 0 and i < len(strs):
    		if strs[0][0:l] != strs[i][0:l]:
    			l -= 1
    		else:
    			i += 1
    	return strs[0][0:l]
        
# transfer method
solve = Solution()
print(solve.longestCommonPrefix(["flower","flow","flight"]))

# method 2 利用sorted性质，会按照字母表顺序排序，只用比较最短和最大的元素中的前缀即可,快
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	if strs == []:
    		return ''
    	strs = sorted(strs)
    	s1 = strs[0]
    	s2 = strs[-1]
    	for i,num in enumerate(s1):
    		if num != s2[i]:
    			return s1[:i]
    	return s1
        
# transfer method
solve = Solution()
print(solve.longestCommonPrefix(["flower","flow","flight"]))