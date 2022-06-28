# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    ans = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1] # 7
    if (ans[version-1] == 0):
        return False
    else:
        return True
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        pivot = 0
        while left <= right:
            pivot = (left + right) // 2
            is_bad = isBadVersion(pivot)
            prev_is_bad = isBadVersion(pivot-1)
            
            if (is_bad and (pivot-1) >=0 and not prev_is_bad): # this is the first bad version
                return pivot
            elif (is_bad and (pivot-1) >= 0 and prev_is_bad):   # bad version but prev is also bad so we check left side
                right = pivot-1
            elif (not is_bad):   # not bad version so then we check the right side
                left = pivot+1
            else:
                return 0


obj = Solution()
n = 20

print(obj.firstBadVersion(n))