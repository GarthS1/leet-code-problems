# https://leetcode.com/problems/find-k-closest-elements/
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[len(arr) - k:]
        else: 
            left_index, right_index = 0, len(arr)
            while right_index - left_index != k:
                if abs(arr[left_index] - x) > abs(arr[right_index - 1] - x):
                    left_index += 1
                else:
                    right_index -= 1
            return arr[left_index:right_index]
        
