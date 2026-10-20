class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        sep=0
        mini = 1001
        while r>=l:
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                #clean until mid, maybe messed after
                mini = min(mini,nums[l])
                l = mid+1
            else:
                #dirty until mid, clean after
                mini = min(mini,nums[mid])
                l += 1
        return mini