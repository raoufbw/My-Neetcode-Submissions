class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = list(word1)
        l2 = list(word2)
        l = []
        n1, n2 = len(l1), len(l2)
        if n1 > n2:
            for i in range(n2):
                l.append(l1[i])
                l.append(l2[i])
            for i in range(n2,n1):
                l.append(l1[i])
        else:
            for i in range(n1):
                l.append(l1[i])
                l.append(l2[i])
            for i in range(n1,n2):
                l.append(l2[i])
        res = ''.join([s for s in l])
        return res