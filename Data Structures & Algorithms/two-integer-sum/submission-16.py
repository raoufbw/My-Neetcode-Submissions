class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff],i]
            hash[num] = i