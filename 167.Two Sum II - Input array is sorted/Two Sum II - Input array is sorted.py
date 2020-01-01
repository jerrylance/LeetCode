from typing import List
# method 1
# 哈希(速度快，结果好)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    	dictory = {}
    	for i, num in enumerate(numbers):
    		if num in dictory:
    			return[dictory[num]+1, i+1]
    		else:
    			dictory[target - num] = i
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15],9))

# method 2
# 暴力(超时)
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        renums = []
        n = len(numbers)
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i]+numbers[j] == target:
                    renums.append(i+1)
                    renums.append(j+1)
                    return(renums)
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15],9))

# method 3
# 切片
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
        	if target - numbers[i] in numbers[i+1:]:
        		return [i+1, numbers.index(target - numbers[i],i+1)+1]
# 这里return中的i+1，是index函数中的参数，意味着索引起始值从自己下一个数开始，如果不设置，那么如果有相等value时，如(3,3),6这种情况下会返回[1,1]，而不是[1,2]
# 切片占用内存较小
# transfer method
solve = Solution()
print(solve.twoSum([2,7,11,15,-2],9))