class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for e in s:
            if e.isalnum():
                clean += e.lower()
        l = 0
        r = len(clean) - 1
        while r >= l:
            if clean[r] != clean[l]:
                return False

            l += 1
            r -= 1
        return True