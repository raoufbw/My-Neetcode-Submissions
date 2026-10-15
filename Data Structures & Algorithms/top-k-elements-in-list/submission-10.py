class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)
        for e in nums:
            hash[e] += 1
        L = []
        l = []
        result = []
        for e in hash.keys():
            L.append(e)
        for e in hash.values():
            l.append(e)
        for i in range(k):
            a = max(l)
            b = l.index(a)
            result.append(L[b])
            l.remove(a)
            L.remove(L[b])
        return result

