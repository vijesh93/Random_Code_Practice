"""
200. Number of Islands
Attempted
Medium
Topics
premium lock icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

from typing import List


class Solution:

    def flip_all_neighbouring(self, y, x, grid, num_rows, num_cols):
        if grid[y][x] == "0":
            return
    
        # Flipping
        grid[y][x] = "0"

        # Checking if not top boundary, then check top values
        if y - 1 >= 0 and y - 1 < num_rows:
            if grid[y - 1][x] == "1": self.flip_all_neighbouring(y - 1, x, grid, num_rows, num_cols)
        # Checking if not bottom boundary, then check bottom values
        if y + 1 >= 0 and y + 1 < num_rows:
            if grid[y + 1][x] == "1": self.flip_all_neighbouring(y + 1, x, grid, num_rows, num_cols)
        
        # Checking if not left boundary, then check left values
        if x - 1 >= 0 and x - 1 < num_cols:
            if grid[y][x - 1] == "1": self.flip_all_neighbouring(y, x - 1, grid, num_rows, num_cols)
        # Checking if not right boundary, then check right values
        if x + 1 >= 0 and x + 1 < num_cols:
            if grid[y][x + 1] == "1": self.flip_all_neighbouring(y, x + 1, grid, num_rows, num_cols)


    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_rows = len(grid)    # y
        num_cols = len(grid[0]) # x
        island_counter = 0
        for y in range(num_rows):
            for x in range(num_cols):

                if grid[y][x] == "1":
                    island_counter = island_counter + 1
                    self.flip_all_neighbouring(y, x, grid, num_rows, num_cols)
        return island_counter


if __name__ == "__main__":
    print('Starting')
    print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print("Expected: 1 ****************************")
    print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print("Expected: 3 ****************************")
    print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
    print("Expected: 1 ****************************")
    