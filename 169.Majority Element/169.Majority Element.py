# LeetCode Solution
# Zeyu Liu
# 2019.2.22
# 169.Majority Element

from typing import List
# method 1 sort()利用题目条件，存在大于n/2的主要元素，因此排序后，取中位数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# transfer method
solve = Solution()
print(solve.majorityElement([2,2,1,1,1,2,2]))

# method 2 利用字典性质dic.items()
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key,value in dic.items():
            if value > len(nums)/2:
                return key
# transfer method
solve = Solution()
print(solve.majorityElement([3,3,4]))

# method 3 利用count()
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums)/2:
                return i
# transfer method
solve = Solution()
print(solve.majorityElement([3,3,4]))