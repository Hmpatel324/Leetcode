"""
Link: https://leetcode.com/problems/remove-element
Difficulty: easy

Problem: 
Given list of ints, remove parameter val from list; however, needs to be done in place. 
Then return back length of new array list. 

Input / Output:
[3,2,2,3], val = 3 => 2, nums = [2,2,_,_]
[0,1,2,2,3,0,4,2], val = 2 =>  5, nums = [0,1,4,0,3,_,_,_]

Notes:
Must be done in place
order may be changed

Solution Approaches:
Two pointer solution - slow pointer for writing index and use fast throwing matches at the back of the list 

"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0] == val: return 0
        head, tail = 0, len(nums)-1
        while head <= tail:
            if(nums[head] == val):
                nums[head] = nums[tail]
                nums[tail] = val
                tail -= 1
            else:
                head += 1
        return head

