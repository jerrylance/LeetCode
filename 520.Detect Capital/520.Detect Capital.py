# LeetCode Solution
# Zeyu Liu
# 2019.3.28
# 520.Detect Capital

from typing import List
# method 1 lower(), upper(), slice直接判断
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.lower() or word == word.upper():
        	return True
        elif word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True
        return False
# transfer method
solve = Solution()
print(solve.detectCapitalUse("USA"))

# method 2 方法1优化,oneline
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    	return word.isupper() or word[1:].islower() or len(word) == 1
# transfer method
solve = Solution()
print(solve.detectCapitalUse("USA"))