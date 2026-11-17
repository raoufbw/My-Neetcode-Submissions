class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
                
        for e in strs:
            temp = tuple(sorted(e))
            hash[temp].append(e)
                 
        L = []    
        for e in hash.values():
            L.append(e)
                    
        return(L)