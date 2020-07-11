# LeetCode Solution
# Zeyu Liu
# 2019.5.29
# 819.Most Common Word

from typing import List
# method 1 dic, replace()，常规
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = 0
        dic = {}
        for c in "!?',;.":
        	paragraph = paragraph.replace(c, " ")
        for i in paragraph.lower().split():
        	if i not in banned:
        		if i not in dic:
        			dic[i] = 1
        		else:
        			dic[i] += 1
        		if dic[i] > count:
        			count = dic[i]
        			res = i
        return res
# transfer method
solve = Solution()
print(solve.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))

# method 2 set()，方法1优化
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        count = 0
        for c in "!?',;.":
        	paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()
        for i in set(paragraph):
        	if i not in banned:
        		count1 = paragraph.count(i)
        		if count1 > count:
        			count = count1
        			res = i
        return res
# transfer method
solve = Solution()
print(solve.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))