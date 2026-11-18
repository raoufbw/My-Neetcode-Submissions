class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        h1 = defaultdict(int)
        h2 = defaultdict(int)

        for i in range(n1):
            h1[s1[i]] += 1
            h2[s2[i]] += 1
        
        if h1 == h2:
            return True
        
        l = 0
        for r in range(n1,n2):
            h2[s2[r]] += 1

            h2[s2[l]] -= 1
            if h2[s2[l]] <= 0:
                del h2[s2[l]]
            
            l += 1
 
            if h1 == h2:
                return True
        
        return False