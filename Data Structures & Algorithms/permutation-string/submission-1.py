class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        l1 = sorted(s1)
        l2 = list(s2)
        l = 0
        r = n1
        while r<=n2:
            if l1 == sorted(l2[l:r]):
                return True 
            l += 1
            r += 1
        
        return False