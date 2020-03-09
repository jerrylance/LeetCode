# LeetCode Solution
# Zeyu Liu
# 2019.3.1
# 290.Word Pattern

from typing import List
# method 1 zip,set
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        return len(set(zip(pattern,str))) == len(set(pattern)) == len(set(str))     
# transfer method
solve = Solution()
print(solve.wordPattern("abba", "dog cat cat dog"))

# method 2 list(map(str.find,str)) 系数对应法
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        return list(map(pattern.find, pattern)) == list(map(str.index, str))
        # return [pattern.find(i) for i in pattern] == [str.find(j) for j in str]
solve = Solution()
print(solve.wordPattern("abba", "dog cat cat dog"))

# method 3 常规字典法，快
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        else:
            dic1 = {}
            dic2 = {}
            for i,k in zip(pattern,str):
                if (i in dic1 and dic1[i] != k) or (k in dic2 and dic2[k] != i):
                    return False
                dic1[i] = k
                dic2[k] = i
            return True
solve = Solution()
print(solve.wordPattern("abba", "dog cat cat dog"))

# method 4 常规字典法优化
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] in dic: 
                if dic[pattern[i]] != str[i]:
                    return False
            elif str[i] in dic.values():
                return False
            else:
                dic[pattern[i]] = str[i]
        return True
solve = Solution()
print(solve.wordPattern("abba", "dog cat cat dog"))