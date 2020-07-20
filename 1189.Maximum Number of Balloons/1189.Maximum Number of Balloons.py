# LeetCode Solution
# Zeyu Liu
# 2019.4.17
# 1189.Maximum Number of Balloons

from typing import List
# method 1 Oneline, count(), min()
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n'))
# transfer method
solve = Solution()
print(solve.maxNumberOfBalloons("loonbalxballpoon"))

# method 2 字典法
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
    	dic = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
    	for i in text:
    		if i in dic:
    			dic[i] += 1
    	dic['l'] //= 2
    	dic['o'] //= 2
    	return min(dic.values())
# transfer method
solve = Solution()
print(solve.maxNumberOfBalloons("loonbalxballpoon"))