"""
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream
Difficulty: easy

Problem:
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. 
This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, 
maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. 
More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

Input / Output:


Notes:


Solution Approaches:

"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = []
        heapq.heapify(self.heap)
        self.k_tracked = k
        for i in nums:
            heapq.heappush(self.heap,i)
            if len(self.heap)>self.k_tracked:
                heapq.heappop(self.heap) 
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap)>self.k_tracked:
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)