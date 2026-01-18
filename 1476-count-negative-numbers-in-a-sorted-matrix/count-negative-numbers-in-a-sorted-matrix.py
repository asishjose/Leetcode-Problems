class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for m in range(len(grid)):
            for n in grid[m]:
                if n<0:
                    count+=1
        return count