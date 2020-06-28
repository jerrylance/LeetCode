# LeetCode Solution
# Zeyu Liu
# 2019.6.3
# 541.Reverse String II

from typing import List
# method 1 stright forward, 转化为list
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), 2*k):
        	s[i:i+k] = s[i:i+k][::-1]
        	#s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
# transfer method
solve = Solution()
print(solve.reverseStr("abcdefg", 2))

# method 2 方法1优化
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Divide s into an array of substrings length k
        s = [s[i:i+k] for i in range(0, len(s), k)]
        # Reverse every other substring, beginning with s[0]
        for i in range(0, len(s), 2):
            s[i] = s[i][::-1]
        return ''.join(s)
# transfer method
solve = Solution()
print(solve.reverseStr("abcdefg", 2))