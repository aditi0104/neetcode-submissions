class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #time complexity = m*n(number of rows time number of columns)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        
        #We need time complexity log(m*n). 
        #which means we have to use binary search clearly

        #first we will apply binary search to find the correct row
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            mid_val = (top + bot) //2
            if target > matrix[mid_val][-1]:
                top = mid_val + 1
            elif target < matrix[mid_val][0]:
                bot = mid_val - 1
            else:
                break
        if not (top <= bot):
            return False
        
        row = (top + bot)//2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        return False
        