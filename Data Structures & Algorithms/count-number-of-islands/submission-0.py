#Task: In a grid, vertical and horizontal alignment of 1s leads to the formation of an island
#Count the no. of islands and return the count
#[
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]

#Optimal Time and Space Complexity => Time: O(m * n) & Space: O(m * n) in worst case due to recursion stack
            #Recursion stack: Memory Py uses to keep track of func calls when a func calls itself (recursion).

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # A DFS function that explores and "sinks" an entire island
        def dfs(r, c):  #rows and columns passed as args here
            # Check boundaries AND ignore water (grid[r][c] == '0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return

            # Mark the current land cell as visited by turning it into water
            # This prevents us from counting the same island more than once
            grid[r][c] = '0'

            # Explore all 4 directions (up, down, left, right)
            dfs(r + 1, c)     # down
            dfs(r - 1, c)     # up
            dfs(r, c + 1)     # right
            dfs(r, c - 1)     # left



        # This will count the total number of islands discovered
        islands = 0

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is land, we have found a new island
                if grid[r][c] == '1':
                    islands += 1      # Count this island
                    dfs(r, c)         # Sink the entire island (mark it visited)

        return islands
        