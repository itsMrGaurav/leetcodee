"""
Solution to three sum problem 
"""


class Solution:
    
    def threeSum(self, nums: list) -> list:
        n = len(nums)

        # base cases , n <= 3
        if not n or n == 1 or n == 2: return []
        elif n == 3: return [nums] if not sum(nums) else [] 

        # n > 3
        nums.sort()
        results = []
        for i,e in enumerate(nums):

            # find two elements whose sum is -e
            k,j = n-1, i + 1
            temp = []
            while k > j:
                if (nums[j] + nums[k]) == -e:
                    if [e,nums[j], nums[k]] not in results:
                        results.append([e,nums[j], nums[k]])
                    k -= 1
                    j += 1
                elif (nums[j] + nums[k]) > -e:
                    k -= 1
                else:
                    j += 1
        return results


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))  #[-2,-1,0,1,2,3]