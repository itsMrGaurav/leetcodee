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
        
    
    def searchRange(self, nums, target):
        l = len(nums)
        idx = self.binarySearch(nums, 0, l, target)
        start, end = idx, idx
        while (start - 1) > -1 and nums[start - 1] == target:
            start -= 1
        while (end + 1) < l and nums[end+1] == target:
            end += 1
        return [start, end]

s = Solution()
print(s.searchRange([1,2,3,4,5], 4))