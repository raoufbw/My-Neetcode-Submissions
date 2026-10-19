class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix[0]) == 0:
            return False
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                if matrix[i][0] == target:
                    return True
                    break
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m-1
        i = (r + l)//2
        while (matrix[i][-1] < target or matrix[i][0] > target) and r>=l: #trouver bonne ligne
            i = (r + l)//2
            if target < matrix[i][0]:
                r = i-1
            elif target > matrix[i][-1]:
                l = i+1
            else:
                break
        l_n = 0
        r_n = n-1
        while l_n <= r_n:
            j = (r_n + l_n) // 2
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l_n = j + 1
            else:
                r_n = j - 1
                
        return False