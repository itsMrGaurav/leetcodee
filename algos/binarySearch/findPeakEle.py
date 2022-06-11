class Solution:
	def checkForPeak(self, idx, nums):
		l = len(nums)
		if l == 1: 
		    return True 
		if idx == 0: 
		    return True if nums[idx] > nums[idx+1] else False
		elif idx == l-1: 
		    return True if nums[idx-1] < nums[idx] else False
		else:
		    return True if (nums[idx] > nums[idx-1] and nums[idx] > nums[idx+1]) else False

	def binarySearch(self, nums, start, end):
		if end-start == 1 or start == end:
			return start if self.checkForPeak(start, nums) else -1
		mid = start + (end-start)//2
		if self.checkForPeak(mid, nums):
			return mid
		res = self.binarySearch(nums, start, mid)
		return res if res != -1 else self.binarySearch(nums, mid+1, end)


	def findPeakElement(self, nums):
		return self.binarySearch(nums, 0, len(nums))

# [1,2,3,1] -> 3 as 3 > 2 and 3 > 1
s = Solution()
print(s.findPeakElement([1,2,3,4]))