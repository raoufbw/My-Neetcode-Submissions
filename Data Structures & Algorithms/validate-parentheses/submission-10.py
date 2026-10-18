class Solution:
    def isValid(self, s: str) -> bool:
        o = ['(','{','[']
        c = [')','}',']']
        l = list(s)
        n = len(s)
        if len(s)%2 == 1 or l[0] in c:
            return False
        L = [l[0]]
        for e in l[1:]:
            if e in o:
                L.append(e)
            else:
                if e == ')':
                    if len(L) != 0 and L[-1] == '(':
                        L.pop()
                    else:
                        return False
                elif e == ']':
                    if len(L) != 0 and L[-1] == '[':
                        L.pop()
                    else:
                        return False
                else:
                    if len(L) != 0 and L[-1] == '{':
                        L.pop()
                    else:
                        return False
        return len(L) == 0