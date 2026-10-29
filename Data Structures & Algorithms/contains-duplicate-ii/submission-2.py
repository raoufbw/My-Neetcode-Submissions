class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hash = defaultdict(list)
        for i in range(n):
            hash[nums[i]].append(i)
        for L in hash.values():
            if len(L) > 1:
                if L[-1] - L[-2] <= k:
                    return True
        return False
