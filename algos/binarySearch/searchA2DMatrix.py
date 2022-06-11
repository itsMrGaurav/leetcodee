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

    def searchMatrix(self, matrix, target):
        for row in matrix:
            if self.binarySearch(row, 0, len(row), target): return True
        return False
