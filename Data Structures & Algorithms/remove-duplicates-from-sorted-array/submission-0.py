class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for e in nums:
            hash[e] += 1
        L_unique = list(hash.keys())
        for i in range(len(L_unique)):
            nums[i] = L_unique[i]
        return len(L_unique)
