class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = []
        a=0
        for e in nums:
            if e == 1:
                a += 1
            elif e == 0:
                L.append(a)
                a=0
        L.append(a)
        return max(L)
