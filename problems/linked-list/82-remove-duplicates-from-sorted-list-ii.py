"""
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
Difficulty: medium

Problem:
Remove duplicate nodes in a sorted linked list - only distinct numbers should remain

Input / Output:
1-2-3-3-3-4-4-5
1-2-5

Notes:


Solution Approaches:
2p approach - 
detect a duplicate via fast/fast.next
    on duplicate - move fast fwd until not duplicate value
    else move slow and fast fwd

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        res.next = head
        slow = res
        fast = slow.next
        while fast and fast.next:
            # duplicate detected
            if fast.val == fast.next.val:
                dup_val = fast.val
                while fast and fast.val == dup_val:
                    fast = fast.next
                slow.next = fast
            else:
                slow = slow.next
                fast = fast.next
        return res.next
