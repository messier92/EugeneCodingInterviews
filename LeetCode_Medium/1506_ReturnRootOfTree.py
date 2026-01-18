"""
You are given all the nodes of an N-ary tree as an array of Node objects, where each node has a unique value.

Return the root of the N-ary tree.

Custom testing:

An N-ary tree can be serialized as represented in its level order traversal where each group of children is separated by the null value (see examples).

For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        children_values = set()

        for node in tree:
            for child in node.children:
                children_values.add(child.val)
        
        for node in tree:
            if node.val not in children_values:
                return node
