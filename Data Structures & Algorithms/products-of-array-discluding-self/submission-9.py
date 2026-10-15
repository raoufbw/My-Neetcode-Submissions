class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)
        L = []
        for e in nums:
            hash[e] += 1
        if hash[0] > 1:
            return [ 0 for _ in range(len(nums))]
        elif hash[0] == 1:
            output = []
            a = 1
            for e in nums:
                if e != 0:
                    a = a*e
            for i in range(len(nums)):
                if nums[i] != 0:
                    output.append(0)
                else:
                    output.append(a)
            return output
        else:
            output = []
            b = 1
            for e in nums:
                b = b*e
            for e in nums:
                output.append(int(b/e))
            return output
