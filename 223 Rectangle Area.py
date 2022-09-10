#https://leetcode.com/problems/rectangle-area/
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        intersect_width = ax2 - max(bx1,ax1) if bx2 > ax2 else bx2 - max(bx1,ax1)
        intersect_height = by2 - max(ay1,by1) if ay2 > by2 else ay2 - max(ay1,by1)
        total_area = (ax2 - ax1) * (ay2 - ay1) +  (bx2 - bx1) * (by2 - by1) 
        print(total_area)
        return total_area - (intersect_width * intersect_height) if intersect_width > 0 and intersect_height > 0 else total_area
        
