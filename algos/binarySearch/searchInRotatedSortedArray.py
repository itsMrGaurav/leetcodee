class Solution:
    def binarySearch(self, nums, start, end, target):
        if start == end:
            return -1
        elif end-start == 1:
            return start if nums[start] == target else -1
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        return self.binarySearch(nums, start, mid, target) if nums[mid] > target else self.binarySearch(nums, mid+1, end, target)

    def search(self, nums, target):
    	pivot = 0
    	l = len(nums)
    	for i in range(l):
    		if nums[i] == target: return i
    		if i+1 < l and nums[i] < nums[i+1]:
    			pivot = i
    	s1 = self.binarySearch(nums, 0, pivot+1, target)
    	if s1 != -1: return s1
    	return self.binarySearch(nums, pivot+1, l, target)

s = Solution()
print(s.search([4,5,6,7,0,1,2], 2))

        