class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        L = []

        for e in strs:
            e_sorted = tuple(sorted(e))
            hash[e_sorted].append(e)
        
        for e in hash.values():
            L.append(e)
        
        return L