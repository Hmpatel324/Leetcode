"""
Link: https://leetcode.com/problems/design-hashmap
Difficulty: easy

Problem:
design a hashmap

Input / Output:


Notes:


Solution Approaches:
use a dictionary

"""
class MyHashMap(object):

    def __init__(self):
        self.map = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.map[key] if key in self.map.keys() else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.map.keys():
            del self.map[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)