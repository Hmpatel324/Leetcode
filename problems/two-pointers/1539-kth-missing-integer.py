"""
Link: https://leetcode.com/problems/kth-missing-positive-number
Difficulty: easy

Problem:
Fnd the kth missing positive value

Input / Output:


Notes:


Solution Approaches:
Two lists then compare
Have overflow

"""
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        actual = range(1,arr[-1]+1)
        i, j = 0,0
        
        while j<len(arr):
            if actual[i]!= arr[j]:
                k-=1
                i+=1
                if k==0: return i
            else:
                j+=1
                i+=1
        overflow = actual[-1]        
        while True:
            overflow+=1
            k-=1
            if k==0: return overflow
        
            