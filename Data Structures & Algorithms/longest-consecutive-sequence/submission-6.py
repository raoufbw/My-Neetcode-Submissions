class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        l = 0
        L = []
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                l += 1
            elif nums[i+1] == nums[i]:
                continue
            else :
                L.append(l)
                l=0
        L.append(l)
        return max(L)+1