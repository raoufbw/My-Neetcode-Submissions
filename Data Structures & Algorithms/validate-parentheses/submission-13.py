class Solution:
    def isValid(self, s: str) -> bool:
        c = { ")":"(", "}":"{", "]":"["}
        l = list(s)
        o = []
        for e in l:
            if e in c.values():
                o.append(e)
            else:
                if len(o) > 0 and c[e] == o[-1]:
                    o.pop()
                else:
                    return False
        return len(o) == 0