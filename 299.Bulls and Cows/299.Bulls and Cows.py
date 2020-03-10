# LeetCode Solution
# Zeyu Liu
# 2019.3.1
# 299.Bulls and Cows

from typing import List
# method 1 按顺序判断条件，慢
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = len(secret)
        i = 0
        repeat = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                cow -= 1
                repeat.append(guess[i])
            elif guess[i] not in secret:
                cow -= 1
            else:
                repeat.append(guess[i])
        for i in secret:
            if i in repeat:
                repeat.remove(i)
        cow = cow - len(repeat)
        return str(bull) + 'A' + str(cow) + 'B'
# transfer method
solve = Solution()
print(solve.getHint("1122", "2211"))

# method 2 方法1优化，本质是一样的，慢
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = len(secret)
        a = list(secret)
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bull += 1
                cow -= 1
            if guess[i] in a:
                a.remove(guess[i])
        cow = cow - len(a)
        return str(bull) + 'A' + str(cow) + 'B'
# transfer method
solve = Solution()
print(solve.getHint("1122", "2211"))

# method 3 利用与门&求交集,最快
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        import collections
        bull = sum(a==b for a,b in zip(secret, guess))
        cow = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (bull, sum(cow.values()) - bull)
# transfer method
solve = Solution()
print(solve.getHint("1122", "2211"))