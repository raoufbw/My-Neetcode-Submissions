class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for e in nums:
            hash[e] += 1
        keys = list(hash.keys())
        values = list(hash.values())
        L = []
        for i in range(len(keys)):
            L.append(keys[i])
            if values[i] > 1:
                L.append(keys[i])
            else:
                continue
        for i in range(len(L)):
            nums[i] = L[i]
        return len(L)