class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums

    def sumRange(self, left: int, right: int) -> int:
        a = self.array[left]
        for i in range(left+1,right+1):
            a += self.array[i]
        return a



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)