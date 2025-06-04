"""
Link: https://leetcode.com/problems/copy-list-with-random-pointer
Difficulty: med

Problem:
make a deep copy of a existing Linked List with pointers to next / random

Input / Output:


Notes:


Solution Approaches:
Create a mapping cache 
Then iterate over original while seeding map nodes for next/random
Fill in as you iterate

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        cache = {}
        res = ListNode(head.val)
        cache[head] = res
        curr_original, curr_copy = head, res
        while curr_original:
            if curr_original.next and curr_original.next not in cache:
                cache[curr_original.next] = ListNode(curr_original.next.val)
            if curr_original.random and curr_original.random not in cache:
                cache[curr_original.random] = ListNode(curr_original.random.val)
            curr_copy.next = cache[curr_original.next] if curr_original.next else None
            curr_copy.random = cache[curr_original.random] if curr_original.random else None
            curr_original = curr_original.next
            curr_copy = curr_copy.next
        return res