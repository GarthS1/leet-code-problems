# https://leetcode.com/problems/kth-largest-element-in-an-array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums) # O(n) to heapify
        return heapq.nlargest(k, nums)[-1] # Use pre-defined function that has the runtime O(n * log(k))
