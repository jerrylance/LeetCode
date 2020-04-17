# LeetCode Solution
# Zeyu Liu
# 2019.3.28
# 496.Next Greater Element I

from typing import List
# method 1 index,列表操作，慢，但是考虑了i右边存在比i大的数，题目是判断右边第一个数即可
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res= []
        for i in nums1:
        	if i == max(nums2):
        		res.append(-1)
        	else:
        		index = nums2.index(i)+1
        		while index < len(nums2):
        			if i < nums2[index]:
        				res.append(nums2[index])
        				break
        			else:
        				index += 1
        		if index == len(nums2):
        			res.append(-1)
        return res
# transfer method
solve = Solution()
print(solve.nextGreaterElement([4,1,2],[1,3,4,2]))

# method 2 stack,get(a,b),如果没有找到a则返回b,快
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	stack = []
    	dic = {}
    	for i in nums2:
    		while stack and stack[-1] < i:
    			j = stack.pop()
    			dic[j] = i
    		stack.append(i)
    	return [dic.get(i,-1) for i in nums1]
# transfer method
solve = Solution()
print(solve.nextGreaterElement([4,1,2],[1,3,4,2]))