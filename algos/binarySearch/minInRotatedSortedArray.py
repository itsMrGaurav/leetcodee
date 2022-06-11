class Solution:
	def findMin(self, nums):
		start, end = 0, len(nums)-1
		lmin = 5001
		while True:
			if end - start == 0 : return min(lmin, nums[start])
			mid = (start + end) // 2
			if nums[mid] >= nums[start]:
				if nums[mid] < nums[end]:
					return min(lmin,nums[start])
				else: start = mid + 1
			else:
				end = mid-1
				lmin = min(lmin, nums[mid])


	
s = Solution()
print(s.findMin([3,4,5]))

