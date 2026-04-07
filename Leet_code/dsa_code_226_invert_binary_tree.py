# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    temp_node = TreeNode()

    def swap_nodes(self, node_1: TreeNode, node_2: TreeNode):
        self.temp_node = node_1
        node_1 = node_2
        node_2 = self.temp_node
        return node_1, node_2

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        root.left, root.right = self.swap_nodes(root.left, root.right)
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    