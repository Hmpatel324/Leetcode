"""
Link: https://leetcode.com/problems/merge-two-sorted-lists
Difficulty: easy

Problem:
merge two linked lists into one

Input / Output:


Notes:


Solution Approaches:
1 pointer per linked list, 1 pointer for new then change .next to manipulate connectivity

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        curr = res
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        curr.next = list2 if list2!=None else list1
        return res.next