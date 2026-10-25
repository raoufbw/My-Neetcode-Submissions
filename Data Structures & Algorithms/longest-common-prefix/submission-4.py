class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        i = 0
        s = strs[0]
        temp = 0
        while i <= len(strs[0]) and temp == 0:
            for e in strs:
                if e[:i] != s[:i]:
                    temp += 1
            if temp > 0:
                break
            i += 1
        return strs[0][:i-1]
