class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 1 #whatever
        ans = 0 #whatever
        while r>=l and k>0:
            k = (r+l)//2
            total_hours = sum(math.ceil(e / k) for e in piles)
            if total_hours <= h:
                r = k-1
                ans = k
            elif total_hours > h:
                l = k+1
        return ans
