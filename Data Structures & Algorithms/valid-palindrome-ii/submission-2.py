class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        def isPalindrome(s):
            return s == s[::-1]
        
        l = 0
        r = n-1
        while r > l:
            if s[l] != s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            r -= 1
            l += 1
        return True