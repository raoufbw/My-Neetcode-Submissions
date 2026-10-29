class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        hash[0] = 1
        currSum = 0
        count = 0

        for e in nums:
            currSum += e

            if hash[currSum - k]:
                count += hash[currSum - k]

            hash[currSum] += 1
        
        return count