# LeetCode Solution
# Zeyu Liu
# 2019.5.19
# 1089.Duplicate Zeros

from typing import List
# method 1 insert(), pop(), 较慢
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
    	i = 0
    	while i < len(arr): 
    		if arr[i] == 0:
    			arr.insert(i,0)
    			arr.pop()
    			i += 1
    		i += 1
    	return arr
# transfer method
solve = Solution()
print(solve.duplicateZeros([1,0,2,3,0,4,5,0]))

# method 2 列表操作，较慢
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
    	i = 0
    	l = len(arr)
    	while i < len(arr):
    		arr.append(arr.pop(0))
    		i += 1	
    		if arr[-1] == 0:
    			arr.append(0)
    			i += 1
    	for i in range(len(arr)-l):
    		arr.pop()
    	return arr
# transfer method
solve = Solution()
print(solve.duplicateZeros([1,0,2,3,0,4,5,0]))

# method 3 Start from the back and adjust items to correct locations. If item is zero then duplicate it.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
        return arr
# transfer method
solve = Solution()
print(solve.duplicateZeros([1,0,2,3,0,4,5,0]))