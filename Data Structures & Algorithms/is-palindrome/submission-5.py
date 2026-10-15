import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = s.translate(str.maketrans("", "", string.punctuation + " ")).lower()
        L = list(r)
        L.reverse()
        return L == list(r)