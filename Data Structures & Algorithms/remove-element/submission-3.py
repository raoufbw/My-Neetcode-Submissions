class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i] == val:
                    tmp = nums[i+1]
                    nums[i+1] = val
                    nums[i] = tmp
        k=0
        for e in nums:
            if e != val:
                k += 1
        return k