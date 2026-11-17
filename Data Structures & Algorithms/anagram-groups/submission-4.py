class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for e in strs:
            hash[str(sorted(e))].append(e)
        
        L = []
        for e in hash.values():
            L.append(e)
        
        return L

        