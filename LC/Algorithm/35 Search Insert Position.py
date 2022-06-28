from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        pivot = 0
        
        while left <= right:
            pivot = (left + right) // 2
            
            if (target == nums[pivot]):
                return pivot
            elif (target < nums[pivot]):
                right = pivot-1
            else:
                left = pivot+1
        
        return left


obj = Solution()
nums = [1,3,5,6]
target = 2

print(obj.searchInsert(nums, target))