"""
Solution class to max area problem on leetcode
"""

class Solution:
	def maxArea(self, heights: list) -> int:
		mx_area = 0
		i, j = 0, len(heights) - 1
		while j > i:
			h1, h2 = heights[i], heights[j]

			# area that can be covered using both heights  
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


"""
input = [1,8,6,2,5,4,8,3,7]

Lets run the code for this input data. 

mx_area i  j  
	0	0	8  	# h1 = 1, h2 = 7, area = 1 (=min(1,7)) * 8, updates mx_area, h1 < h2 -> i updates
	8	1 	8	# h1 = 8, ......, area = 7 * 7, ..............., h1 > h2 -> j updates 	
	49	1 	7	# ......, h2 = 3, area = 3 * 6, no update, .............
	49	1 	6	# ......, h2 = 8, area = 8 * 5, .........., both i and j updates
	49	2 	5	# h1 = 6, h2 = 4, area = 4 * 3, .........., h1 > h2 -> j updates
	49 	2 	4 	# ......, h2 = 5, area = 5 * 2, .........., ....................
	49 	2 	3 	# ......, h2 = 2, area = 2 * 1, .........., ....................
	49 	2 	2 	# condition falsifies -> returns 49
 
"""