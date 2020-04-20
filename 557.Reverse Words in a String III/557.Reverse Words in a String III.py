# LeetCode Solution
# Zeyu Liu
# 2019.3.29
# 557.Reverse Words in a String III

from typing import List
# method 1 map()
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(map(str,s.split(' ')))
        s1 = ''
        for i in s:
        	s1 += i[::-1] + ' '
        return s1.strip()
# transfer method
solve = Solution()
print(solve.reverseWords("Let's take LeetCode contest"))

# method 2 方法1优化oneline
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(i[::-1] for i in s.split())
# transfer method
solve = Solution()
print(solve.reverseWords("Let's take LeetCode contest"))