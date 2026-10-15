class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            a = max(arr[i+1:])
            arr[i] = a
        arr[-1] = -1
        return arr