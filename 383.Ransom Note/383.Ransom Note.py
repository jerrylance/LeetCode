# LeetCode Solution
# Zeyu Liu
# 2019.3.12
# 383.Ransom Note

from typing import List
# method 1 利用count()和set(), 快
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
# transfer method
solve = Solution()
print(solve.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))

# method 2 O(m+n),Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        import collections
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
# transfer method
solve = Solution()
print(solve.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))

# method 2 O(1)space, replace, 快
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine = magazine.replace(i,' ',1)
        return True
# transfer method
solve = Solution()
print(solve.canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))