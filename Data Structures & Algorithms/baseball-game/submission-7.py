class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []
        for e in operations:
            if e == "D":
                rec.append(2*rec[-1])
            elif e == "+":
                rec.append(rec[-1]+rec[-2])
            elif e == "C":
                rec.pop()
            else:
                rec.append(int(e))
        b = 0
        for e in rec:
            b += e
        return b

