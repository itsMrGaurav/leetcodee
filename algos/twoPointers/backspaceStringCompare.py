"""
Solution class for Backspace string compare problem on leetcode
"""


class Solution:

    # stack implementation
    def purifyString(self, s: str) -> str:
        res = []
        for c in s:
            if c == '#':
                if len(res): res.pop()
            else: res.append(c)
        return ''.join(res)


    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.purifyString(s) == self.purifyString(t)






s = "y#fo##f"
t = "y#f#o##f"

sol = Solution()
print(sol.backspaceCompare(s, t))


