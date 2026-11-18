import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for e in s:
            if e.isalnum():
                clean += e.lower()
        return clean == clean[::-1]