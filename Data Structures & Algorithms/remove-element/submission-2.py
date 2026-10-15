class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = []
        for e in nums:
            if e != val:
                L.append(e)
            continue
        for i in range(len(L)):
            nums[i] = L[i]
        return len(L)