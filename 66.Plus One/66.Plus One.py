# LeetCode Solution
# Zeyu Liu
# 2019.2.1
# 66.Plus One
from typing import List

# method 1 反向切片，insert，注意小细节,快
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
        if digits[0] == 0:
            digits.insert(0,1)
#或者   return [1] + digits            
        return digits
# transfer method    
solve = Solution()
print(solve.plusOne([9,9,9,9]))

# method 2 整数转成列表方法 l = [ int(item) for item in str(value) ]
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = 0
        for i,num in enumerate(digits):
            a += 10 **(len(digits)- 1 - i) * num
        a += 1
        return [int(a) for a in str(a)]    
#或者   return map(int,str(num))

# transfer method    
solve = Solution()
print(solve.plusOne([9,9,9,9]))


# method 3 其他人的一行代码方法，join，
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int(''.join([str(j) for j in digits]))+1)]
# transfer method    
solve = Solution()
print(solve.plusOne([9,9,9,9]))

