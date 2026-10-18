class MinStack:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr = self.arr[:-1]

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        a = float('inf')
        for e in self.arr:
            if e < a:
                a = e
        return a


