class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L = []
        hash = defaultdict(int)
        
        for i in range(n):
            diff = target - nums[i]

            if diff in hash:
                L = [hash[diff],i]
            
            hash[nums[i]] = i

              
        
        return L