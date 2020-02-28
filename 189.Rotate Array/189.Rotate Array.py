# LeetCode Solution
# Zeyu Liu
# 2019.2.22
# 189.Rotate Array

from typing import List
# method 1 list循环替代,O(k*n)，较慢
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    	for i in range(k):
    		nums.insert(0,nums.pop())
    	#return nums
# transfer method
solve = Solution()
print(solve.rotate([1,2,3,4,5,6,7],3))

# method 2 slice 要注意k有可能大于nums长度n的情况，如果k = n，那么排列没变化
# nums[:] can truly change the value of old nums, 
# but nums just changes its reference to a new nums not the value of old nums.
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    	n = len(nums)
    	k = k % n
    	nums[:] = nums[-k:] + nums[:-k] #important
    	# return nums
# transfer method
solve = Solution()
print(solve.rotate([1,2],3))

# method 3 reverse 常规三段
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    	if len(nums) > 0:
    		k %= len(nums)
    	self.reverse(nums,0,len(nums)-1)  #[7,6,5,4,3,2,1]
    	self.reverse(nums,0, k-1)         #[5,6,7,4,3,2,1]
    	self.reverse(nums,k, len(nums)-1) #[5,6,7,1,2,3,4]
    	# return nums
    def reverse(self,nums,i,j):# 定义一个反转函数reverse
    	while i < j:
    		nums[i], nums[j] = nums[j], nums[i]
    		i += 1
    		j -= 1
# transfer method
solve = Solution()
print(solve.rotate([1,2,3,4,5,6,7],3))
