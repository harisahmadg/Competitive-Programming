from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1
        pivot = 0
        
        while left <= right:
            pivot = (left + right) // 2
            
            if (target == nums[pivot]):     # if target equals mid point
                return pivot
            elif (target < nums[pivot]):   # if target is less than mid point 
                right = pivot-1
            else:
                left = pivot+1      # if target is greater than mid point
        
        return -1
        
        
        

obj = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(obj.search(nums, target))