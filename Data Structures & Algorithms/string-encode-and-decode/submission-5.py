class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        s = ""
        for e in strs:
            s += e + "ç"
        return s[:-1]
    
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        L = list(s)
        l = []
        a = ''
        for e in L:
            if e != "ç":
                a+= e
            else:
                l.append(a)
                a = ''
        l.append(a)
        return l