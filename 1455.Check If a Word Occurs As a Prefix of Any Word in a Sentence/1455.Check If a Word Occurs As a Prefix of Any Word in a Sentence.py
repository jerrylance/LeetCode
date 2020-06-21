# LeetCode Solution
# Zeyu Liu
# 2019.5.26
# 

from typing import List
# method 1 split(), slice, 快
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        s = sentence.split()
        for i,num in enumerate(s):
        	if num[:n] == searchWord:
        		return i+1
        return -1
# transfer method
solve = Solution()
print(solve.isPrefixOfWord("i use triple pillow", "pill"))

# method 2 startswith()
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split()
        for i,num in enumerate(s):
        	if num.startswith(searchWord):
        		return i+1
        return -1
# transfer method
solve = Solution()
print(solve.isPrefixOfWord("i use triple pillow", "pill"))