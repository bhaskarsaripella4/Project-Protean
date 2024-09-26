import collections
from typing import List

class Islands:
  # def __init__(self, grid):
  #   self.grid = grid

  def numIslands(self, grid: list[list[str]]) -> int:

    if not grid:
      return 0

    num_islands = 0
    rows, cols = len(grid), len(grid[0])
    visited = set()


    def bfs(row, col):
      q = collections.deque()
      visited.add((row,col))
      q.append((row,col))


      while q:
        r,c = q.popleft() # if you use pop(), then it becomes dfs. pop() returns the most recent element added
        # need to check 1 up, left, down and right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
          row,col = r + dr, c + dc
          if (row in range (rows) and col in range(cols) and grid[row][col] == "1" and(row,col) not in visited):
            q.append((row,col))
            visited.add((row,col))

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1" and (r,c) not in visited:
          bfs(r,c)
          num_islands += 1

    return num_islands








# input
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

grid = [
  ["1","0","0","1","0"],
  ["1","0","1","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"]
]

soln = Islands().numIslands(grid) # First instantiate class then call method.
print("Number of islands is {0}".format(soln))