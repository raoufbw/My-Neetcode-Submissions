class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = defaultdict(list)
        for i in range(n):
            hash[nums[i]].append(i)
        sort = sorted(nums)
        l = 0
        r = n-1
        while r > l:
            tot = sort[l] + sort[r]
            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                break
        if sort[l] == sort[r]:
            return sorted([hash[sort[l]][0], hash[sort[r]][1]])
        else:
            return sorted([hash[sort[l]][0], hash[sort[r]][0]])