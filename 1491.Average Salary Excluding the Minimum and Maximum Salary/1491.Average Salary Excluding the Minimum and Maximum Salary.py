# LeetCode Solution
# Zeyu Liu
# 2019.7.6
# 1491.Average Salary Excluding the Minimum and Maximum Salary

from typing import List
# method 1 '%.5f' % a保留5位小数, sorted(), pop()
class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        salary.pop(0)
        salary.pop()
        return (sum(salary) / len(salary))
# transfer method
solve = Solution()
print(solve.average([8000,9000,2000,3000,6000,1000]))

# method 2 oneline, max(), min()
class Solution:
    def average(self, salary: List[int]) -> float:
    	return (sum(salary)-max(salary)-min(salary)) / (len(salary)-2)
# transfer method
solve = Solution()
print(solve.average([8000,9000,2000,3000,6000,1000]))