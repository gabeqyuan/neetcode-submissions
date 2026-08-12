class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows): # iterating through the rows 
            L = 0 
            R = columns - 1
            while L <= R:
                mid = L + (R - L) // 2
                if matrix[i][mid] == target:
                    return True 
                elif matrix[i][mid] < target:
                    L = mid + 1
                else:
                    R = mid - 1
                
        return False
                

