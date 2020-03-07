# LeetCode Solution
# Zeyu Liu
# 2019.2.29
# 205.Isomorphic Strings

from typing import List
# method 1 zip(),这里注意到需要判断两次映射
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dic1 = {}
            dic2 = {}
            for i,k in zip(s,t):
                if (i in dic1 and dic1[i] != k) or (k in dic2 and dic2[k] != i):
                    return False
                dic1[i] = k
                dic2[k] = i
            return True
# transfer method
solve = Solution()
print(solve.isIsomorphic("paper","title"))

# method 2 利用zip和集合性质，映射数量和每个子集数量相当即为同构，快
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))
# transfer method
solve = Solution()
print(solve.isIsomorphic("paper","title"))

# method 3 利用find方法，相同字符返回相同的系数，进一步用map缩减代码
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.find,s)) == list(map(t.find,t))
        # return [s.find(i) for i in s] == [t.find(j) for j in t]
# transfer method
solve = Solution()
print(solve.isIsomorphic("paper","title"))

# method 4 少用一个字典，多了一步elif判断，是否会有非一一映射的出现，快
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] in dic: 
                if dic[s[i]] != t[i]:
                    return False
            elif t[i] in dic.values():
                return False
            else:
                dic[s[i]] = t[i]
        return True
# transfer method
solve = Solution()
print(solve.isIsomorphic("paper","title"))