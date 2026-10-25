class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hash = defaultdict(int)
        for e in nums:
            hash[e] += 1
        for key, value in hash.items():
            if value >= n/2:
                return key