"""Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        final_spiral_len = len(matrix) * len(matrix[0])
        counter = 0
        final_spiral = []
        loops = (min(len(matrix), len(matrix[0])))/2
        
        if isinstance(loops, int):
            loops = loops
        
        else:
            loops = round(loops) + 1

        shift = 0
        for i in range(loops):

            # Go right in currnent array till end
            for j in range(i, len(matrix[0]) - i):
                final_spiral.append(matrix[i][j])
                counter = counter + 1
            
            print("Counter: ", counter)
            if counter >= final_spiral_len:
                return final_spiral
            
            print("Final_spiral after going right: ", final_spiral)

            # Go south/down
            first_value = True
            for j in range(i, len(matrix) - i):
                # Skip first value and append rest
                if first_value:
                    first_value = False
                    continue
                final_spiral.append(matrix[j][len(matrix[0]) - i - 1])
                counter = counter + 1
                                    
            if counter >= final_spiral_len:
                return final_spiral
            
            print("Final_spiral after going down: ", final_spiral)

            # Go left
            first_value = True
            for j in reversed(range(i, len(matrix[0]) - i)):

                # Skip first value and append rest
                if first_value:
                    first_value = False
                    continue
                
                final_spiral.append(matrix[len(matrix) - 1 - i][j])
                counter = counter + 1

            if counter >= final_spiral_len:
                return final_spiral
            
            print("Final_spiral after going left: ", final_spiral)

            # Finally go up 
            first_value = True
            for j in reversed(range(i + 1, len(matrix) - i)):
                
                # Skip first value and append rest
                if first_value:
                    first_value = False
                    continue
                
                final_spiral.append(matrix[j][i])
                counter = counter + 1
            
            print("Final_spiral after going up: ", final_spiral)

            if counter >= final_spiral_len:
                return final_spiral

        return final_spiral
    

if __name__ == "__main__":
    print('Starting')
    print(Solution().spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
    print("[1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13 ****************************")
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print("[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7 ****************************")
    print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    print("[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10 ****************************")
    print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))
    print("[1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8 ****************************")
    print(Solution().spiralOrder([[1,2],[3,4]]))
    print("[1, 2, 4, 3 ****************************")
    