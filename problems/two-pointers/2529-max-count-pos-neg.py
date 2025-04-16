"""
Link: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer
Difficulty: easy

Problem:
given list of ints, find max of positive and negative numbers
0s count as neither

Input / Output:
[-2,-1,-1,1,2,3] => 3

Notes:


Solution Approaches:
2 x BST

"""
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg, pos = 0,0 
        lo, hi = 0, len(nums)-1
        # BST for neg
        while(lo<=hi):
            mid = lo + ((hi-lo)/2)
            if mid-1>=0 and nums[mid] >= 0 and nums[mid-1]<0:
                neg = mid
                break
            elif mid==len(nums)-1 and nums[mid] < 0:
                neg = len(nums)
                break
            elif nums[mid] >= 0:
                hi = mid - 1
            else:
                lo = mid+1

        # BST for pos
        lo, hi = 0, len(nums)-1
        while(lo<=hi):
            mid = lo + ((hi-lo)/2)
            if mid+1<len(nums) and 0 >= nums[mid] and nums[mid+1]>0:
                pos = len(nums) - (mid+1)
                break
            elif mid==0 and nums[mid] > 0:
                pos = len(nums)
                break
            elif 0 >= nums[mid]:
                lo = mid+1
            else:
                hi = mid-1
        
        return max(pos,neg)
        