# LeetCode Solution
# Zeyu Liu
# 2019.4.9
# 53.Maximum Subarray

from typing import List
# method 1 dict, sorted(,reverse=Ture)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        l = []
        dic = {}
        for i,num in enumerate(sorted(nums, reverse = True)):
        	dic[num] = i+1
        for num in nums:
        	if dic[num] == 1:
        		l.append('Gold Medal')
        	elif dic[num] == 2:
        		l.append('Silver Medal')
        	elif dic[num] == 3:
        		l.append('Bronze Medal')
        	else:
        		l.append(str(dic[num]))
        return l
# transfer method
solve = Solution()
print(solve.findRelativeRanks([5, 4, 3, 2, 1]))

# method 2 利用list(map(dict(zip(sort, rank)).get, nums)), 最快
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        sort = sorted(nums, reverse=True)
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1))) #这里的4是因为排序是要系数加1
        return list(map(dict(zip(sort, rank)).get, nums))
# transfer method
solve = Solution()
print(solve.findRelativeRanks([5, 4, 3, 2, 1]))