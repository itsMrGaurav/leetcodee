"""
Solution class to max area problem on leetcode
"""

from input import t

class Solution:
	def maxArea(self, heights: list) -> int:
		mx_area = 0
		i, j = 0, len(heights) - 1
		while j > i:
			h1, h2 = heights[i], heights[j]
			area = min(h1, h2) * (j-i)
			mx_area = max(mx_area, area)
			if h1 > h2:
				j -= 1
			elif h1 < h2:
				i += 1
			else:
				i += 1
				j -= 1
		return mx_area


s = Solution()
print(s.maxArea(t))