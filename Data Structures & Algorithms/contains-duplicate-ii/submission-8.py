class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = defaultdict(int)
        for i in range(n):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True
            
            seen[nums[i]] = i
        return False