class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while r >= l:
            k = (l+r)//2
            if nums[k] == target:
                return k
            elif nums[k] < target:
                l = k+1
            else:
                r = k-1
        return l
