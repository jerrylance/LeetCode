# LeetCode Solution
# Zeyu Liu
# 2019.3.17
# 1323.Maximum 69 Number

from typing import List
# method 1 replace()
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in num:
            if i == '6':
                num = num.replace(i,'9',1)
                break
        return int(num)
# transfer method
solve = Solution()
print(solve.maximum69Number(9669))

# method 2 方法1优化
class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))
# transfer method
solve = Solution()
print(solve.maximum69Number(9669))

# method 3 列表法
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        l = []
        count = 0
        for i in num:
            if count == 0 and i =='6':
                l.append('9')
                count = 1
            else:
                l.append(i)
        return int(''.join(l))
# transfer method
solve = Solution()
print(solve.maximum69Number(9669))

# method 3 不转化str，使用math方法
class Solution:
    def maximum69Number (self, num: int) -> int:
        i = 0
        tem = num
        six = -1
        while tem > 0:
            if tem % 10 == 6:
                six = i
            tem = tem // 10
            i += 1
        return (num + 3 * (10**six)) if six != -1 else num
# transfer method
solve = Solution()
print(solve.maximum69Number(9669))