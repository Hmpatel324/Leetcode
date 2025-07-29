"""
Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node
Difficulty: medium

Problem:
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 

The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Input / Output:


Notes:


Solution Approaches:
Breadth First Exploration - passing through tuple (node, right node)
seed in (root, None)

for left child - the right is always the curr.right
for right child - the right is either the curr_node right.left OR None (if the curr_node right is None)

"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return root
        queue = [(root,None)]
        while queue:
            curr_node, right_node = queue.pop(0)
            curr_node.next = right_node
            if curr_node.left:
                queue.append((curr_node.left, curr_node.right))
                queue.append((curr_node.right, right_node.left if right_node else None))
        return root