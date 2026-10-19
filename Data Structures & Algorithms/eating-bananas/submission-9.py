class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)
        k = m #guaranteed value
        l = 1
        r = m
        ans = 0
        while r>=l and k>0:
            k = (r+l)//2
            total_hours = sum(math.ceil(e / k) for e in piles)
            if total_hours <= h:
                r = k-1
                ans = k
            elif total_hours > h:
                l = k+1
        return ans
