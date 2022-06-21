# Used a min heap to keep track of the min distance a ladder had been used. 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_used = []
        heapify(ladders_used)
        index = 0
        
        while index < len(heights) - 1 and bricks >= 0:
            if heights[index] < heights[index + 1]:
                if len(ladders_used) != ladders:
                    heappush(ladders_used, heights[index + 1] - heights[index])
                elif len(ladders_used) != 0 and ladders_used[0] < heights[index + 1] - heights[index]:
                    bricks -= ladders_used[0]
                    heappop(ladders_used)
                    heappush(ladders_used, heights[index + 1] - heights[index])
                else:
                    bricks -= heights[index + 1] - heights[index]
            
            if bricks >= 0:
                index += 1
            
        return index
        
