class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while r>=l:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]:
                #clean until mid, maybe messed after
                if target >= nums[l] and target < nums[mid]:
                    r = mid-1
                else: 
                    l = mid+1
                
            else:
                #dirty until mid, clean after
                if target > nums[mid] and target <= nums[r]: #si on est dans la partie triée
                    l = mid+1
                else:
                    r = mid-1
                
        return -1