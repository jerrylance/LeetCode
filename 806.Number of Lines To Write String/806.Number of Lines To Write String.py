# LeetCode Solution
# Zeyu Liu
# 2019.5.23
# 806.Number of Lines To Write String

from typing import List
# method 1 dic，字典法
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        for i,num in enumerate(alpha):
        	dic[num] = widths[i]
        line = 1
        count = 0
        for i in S:
        	count += dic[i]
        	if count > 100:
        		line += 1
        		count = dic[i]
        return [line, count]
# transfer method
solve = Solution()
print(solve.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))

# method 2 ord(),ASCII码
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        count = 0
        for i in S:
        	count += widths[ord(str(i))-97]
        	if count > 100:
        		line += 1
        		count = widths[ord(str(i))-97]
        return [line, count]
# transfer method
solve = Solution()
print(solve.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))