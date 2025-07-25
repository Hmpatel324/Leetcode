"""
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii
Difficulty: medium

Problem:
In a once sorted array which now has a rotation, determine if a element exists

Input / Output:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Notes:


Solution Approaches:
Modified Binary Search

"""
class Solution(object):
    def search(self, nums, target):
# The length of the input array
        num_length = len(nums)
      
        # Initialize the left and right pointers
        left, right = 0, num_length - 1
      
        # Binary search with modifications to handle the rotated sorted array
        while left < right:
            # Calculate the middle index
            mid = left+((right-left)/2)
          
            # If the middle element is greater than the rightmost element,
            # it means the smallest element is to the right of mid.
            if nums[mid] > nums[right]:
                # Target is in the left sorted portion
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # If the middle element is less than the rightmost element,
            # it means the smallest element is to the left of mid.
            elif nums[mid] < nums[right]:
                # Target is in the right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            # If the middle element is equal to the rightmost element,
            # we can't determine the smallest element's position,
            # so we reduce the search space by one from the right.
            else:
                right -= 1
      
        # Final comparison to see if the target is at the left index
        return nums[left] == target