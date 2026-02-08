from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0
        for x in range(num_cols):
            for y in range(num_rows):
                if grid[y][x] == "1":
                    
                    if x == 0 and y == 0:
                        num_islands = num_islands + 1
                        print("Element found at x = ", x, "and y = ", y)

                    # If first col, check only top and do not check left side
                    elif x == 0 and y > 0:
                        if grid[y - 1][x] == "0":
                            num_islands = num_islands + 1
                            print("Element found at x = ", x, "and y = ", y)
                    
                    # If first row, check only left and do not check left side
                    elif x > 0 and y == 0:
                        if grid[y][x - 1] == "0":
                            num_islands = num_islands + 1
                            print("Element found at x = ", x, "and y = ", y)

                    # For center elements check left and top both
                    else:
                        if grid[y][x - 1] == "0" and grid[y - 1][x] == "0":
                            num_islands = num_islands + 1
                            print("Element found at x = ", x, "and y = ", y)

        return num_islands

if __name__ == "__main__":
    print('Starting')
    """print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
    print("Expected: 1 ****************************")
    print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
    print("Expected: 3 ****************************")"""
    print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))
    print("Expected: 1 ****************************")