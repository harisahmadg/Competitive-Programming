from typing import List


"""
Given nums sorted non decreasing, square it and sort it in non decreasing
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted = []
        for i in range(len(nums)):
            sorted.append(nums[i]*nums[i])
        
        # Use insertion sort, appropriate for data sets which are already partially sorted
        sorted.sort()
        return sorted
        # for i in range(1, len(sorted)):
        #     key = sorted[i]     # Current element we compare all others to
        #     j = i-1
        #     while j >= 0 and sorted[j] > key:
        #         sorted[j+1] = sorted[j]
        #         j -= 1
        #     sorted[j+1] = key

        #return sorted
        

obj = Solution()
nums = [-4,-1,0,3,10]

print(obj.sortedSquares(nums))