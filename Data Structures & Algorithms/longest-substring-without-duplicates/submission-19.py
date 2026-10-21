class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        n = len(s)
        hash = {}
        l = 0
        maxi = 0
        for i in range(n):
            if s[i] in hash and hash[s[i]] >= l:
                l = hash[s[i]]+1

            hash[s[i]] = i
            maxi = max((i-l+1),maxi)
        maxi = max((i-l+1),maxi)
        
        return maxi