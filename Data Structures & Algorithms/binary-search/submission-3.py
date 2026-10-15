class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        n = len(nums)
        l = 0
        r = n-1
        while r-l > 0:
            m = int((l+r)/2)
            if nums[m] == target:
                return m
            elif r-l == 1:
                if nums[l] == target:
                    return l 
                elif nums[r] == target:
                    return r
                break
            elif nums[m] > target:
                r = m
            else:
                l=m
        return -1