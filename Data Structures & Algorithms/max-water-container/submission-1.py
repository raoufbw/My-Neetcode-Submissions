class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        m = -1
        l = 0
        r = n-1
        while r-l>0:
            q = (r-l)*min(heights[r],heights[l])
            if q > m:
                m = q
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return m




