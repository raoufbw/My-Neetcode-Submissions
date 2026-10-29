class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        l = list(s)
        i = 0
        while l[-1] == " ":
            l.pop()
        while len(l) > 0 and l[-1] != " " :
            i += 1
            l.pop()
        return i