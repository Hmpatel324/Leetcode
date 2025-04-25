"""
Link: https://leetcode.com/problems/remove-nodes-from-linked-list
Difficulty: medium

Problem:
remove nodes with downstream nodes that are higher

Input / Output:


Notes:


Solution Approaches:
Step 1: reverse the LL Step 2: iterate from tail to head tracking highest and updating pointers Step 3: revert point to head to tail

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head: return head
        # reverse LL
        slow, fast = head, head.next
        head.next = None
        while fast.next:
            temp = fast
            fast = fast.next
            temp.next = slow
            slow = temp
        fast.next = slow

        # traverse tail to head + tracking max
        res = ListNode()
        curr_res = res
        curr, curr_max = fast, fast.val
        while curr:
            if curr.val >= curr_max:
                curr_res.next = curr
                curr_res = curr
            curr_max = max(curr_max, curr.val)
            curr = curr.next
        curr_res.next = None
        
        # reverse
        slow, fast = res.next, res.next.next
        slow.next = None
        while fast:
            temp = fast
            fast = fast.next
            temp.next = slow
            slow = temp
        return slow