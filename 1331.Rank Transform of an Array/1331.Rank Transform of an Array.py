# LeetCode Solution
# Zeyu Liu
# 2019.2.9
# 1331.Rank Transform of an Array

from typing import List
# method 1 hash map, 排序set建立最小rank
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    	rankarr = sorted(set(arr))
    	hashmap = {}
    	rank = 1
    	for i in rankarr:
    		hashmap[i] = rank #这一步理解是关键, 使得hashmap[i]一一对应不同的rank
    		rank += 1
    	ranklist = []
    	for item in arr:
    		ranklist.append(hashmap[item]) #这里就可以调用hashmap[?], 返回对应的rank
    	return ranklist

# transfer method    
solve = Solution()
print(solve.arrayRankTransform([37,12,28,9,100,56,80,5,12]))

# method 2 方法1的简化写法
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    	temp = {num:i+1 for i,num in enumerate(sorted(set(arr)))}
    	#return map(temp.get, arr)
    	#return [temp[num] for num in arr]
    	ranklist = []
    	for item in arr:
    		ranklist.append(temp[item])
    	return ranklist

# transfer method    
solve = Solution()
print(solve.arrayRankTransform([37,12,28,9,100,56,80,5,12]))

# 解释哈希表的例子
#        dic = dict()
#        for ind, num in enumerate(sa):
#            dic[num] = ind
# 因此，当输入dic[num]时，就会返回相应的ind