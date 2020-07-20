# LeetCode Solution
# Zeyu Liu
# 2019.4.20
# 961.N-Repeated Element in Size 2N Array

from typing import List
# method 1 hash table
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = []
        for i in A:
        	if i in dic:
        		return i
        	else:
        		dic.append(i)
        dic = {}
        #for i in A:
        #	if i in dic:
        #		return i
        #	else:
        #		dic[i] = i
# transfer method
solve = Solution()
print(solve.repeatedNTimes([5,1,5,2,5,3,5,4]))

# method 2 set()
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
    	B = set(A)
    	return (sum(A)-sum(B)) // (len(A)-len(B))
# transfer method
solve = Solution()
print(solve.repeatedNTimes([5,1,5,2,5,3,5,4]))

# method 3 API，random.sample(A,2)，由于同一个数占总数的0.5，使用概率论，随机抽样，抽到两个相同的数返回
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
    	import random
    	while True:
    		s = random.sample(A, 2)
    		if s[0] == s[1]:
    			return s[0]
# transfer method
solve = Solution()
print(solve.repeatedNTimes([5,1,5,2,5,3,5,4]))