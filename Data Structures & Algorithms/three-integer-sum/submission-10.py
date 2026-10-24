class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
            else:
                return []
        nums.sort()
        L= []
        for k in range(n-2):
            l = k+1
            r = n-1
            while r-l>0 :
                if nums[l] + nums[r] + nums[k] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[k] < 0:
                    l += 1
                else:
                    Lt = [nums[l], nums[r], nums[k]]
                    Lt.sort()
                    if Lt not in L:
                        L.append(Lt)
                    l += 1
                    r -= 1
        return L