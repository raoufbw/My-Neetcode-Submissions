class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0]
        for i in range(n):
            left.append(left[i]+nums[i])
        for i in range(n):
            right = left[n] - left[i+1]
            if left[i] == right:
                return i
        return -1