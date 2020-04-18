# LeetCode Solution
# Zeyu Liu
# 2019.3.28
# 485.Max Consecutive Ones

from typing import List
# method 1 O(n)方法，max()
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        count = 0
        for i in nums:
        	if i == 1:
        		count += 1
        	else:
        		count = 0
        	max1 = max(max1,count)
        return max1
# transfer method
solve = Solution()
print(solve.findMaxConsecutiveOnes([1,1,0,1,1,1]))

# method 2 利用索引和序列为1，0的性质，一种聪明的方法，较快
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i] == 1:
                nums[i] = nums[i] + nums[i-1]
        return max(nums)
# transfer method
solve = Solution()
print(solve.findMaxConsecutiveOnes([1,1,0,1,1,1]))

# method 3 转换成字符串利用split()
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(lambda x: len(x), ''.join([str(num) for num in nums]).split('0')))
# transfer method
solve = Solution()
print(solve.findMaxConsecutiveOnes([1,1,0,1,1,1]))