# LeetCode Solution
# Zeyu Liu
# 2019.1.23
# 3.Longest Substring Without Repeating Characters

from typing import List

# method 1 我的方法：利用切片在字符串上水平遍历，根据下一个字符改变切片大小，速度快
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	n = 0
    	m = 0
    	maxlengh = 0
    	for i, item in enumerate(s):
    		substring = s[n:m]
    		# 分两种情况讨论，要仔细尤其第一种
    		if s[i] in substring:
    			n += 1 + substring.find(s[i])
    			m += 1
#    			substring = s[n:m]
#    			maxlengh1 = len(substring)
#    			maxlengh = max(maxlengh,maxlengh1)
    		else:
    			m += 1
    			substring = s[n:m]
    			maxlengh1 = len(substring)
    			maxlengh = max(maxlengh,maxlengh1)
    	return maxlengh
# transfer method
solve = Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))

# method 2 网络上的一般方法，原理和我的一样，但是没有优化，速度稍微慢一点。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = []
        max_length = 0
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
            str_list.append(x)    
            max_length = max(max_length, len(str_list))       
        return max_length
# transfer method
solve = Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))

# method 2 哈希表，best，参考了第一题。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength
# transfer method
solve = Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))