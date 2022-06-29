# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  
        queue, i, j, islands = deque(), 0, 0, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    queue.append([i, j])
                    
                    while queue:
                        cur_pos = queue.pop()
                        grid[cur_pos[0]][cur_pos[1]] = 0
                        
                        if cur_pos[0] + 1 < len(grid) and grid[cur_pos[0] + 1][cur_pos[1]] == '1':
                            queue.append([cur_pos[0] + 1, cur_pos[1]])
                        if cur_pos[1] + 1 < len(grid[0]) and grid[cur_pos[0]][cur_pos[1] + 1] == '1':
                            queue.append([cur_pos[0], cur_pos[1] + 1])
                        if cur_pos[0] - 1 > -1 and grid[cur_pos[0] - 1][cur_pos[1]] == '1':
                            queue.append([cur_pos[0] - 1, cur_pos[1]])
                        if cur_pos[1] - 1 > -1 and grid[cur_pos[0]][cur_pos[1] - 1] == '1':
                            queue.append([cur_pos[0], cur_pos[1] - 1])

        return islands 
            
        
        
