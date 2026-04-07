"""
141. Linked List Cycle
Attempted
Easy
Topics
premium lock icon
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
                
        runner_1 = head
        runner_2 = head

        while runner_2 and runner_2.next:

            runner_1 = runner_1.next
            runner_2 = runner_2.next.next
            

            if runner_1 == runner_2:
                return True

        return False
        """
        # Set of node values
        node_set = set()
        
        while head.next:
            
            if head in node_set:
                return True
            
            node_set.add(head)
            head = head.next
        return False
        """

        """
        while head.next:
            
            if head.val == "temp":
                return True

            head.val = "temp"
            head = head.next
        
        return False
        """

if __name__ == "__main__":
    # Create the individual nodes
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node_temp = ListNode(15)

    # Link them: 3 -> 2 -> 0 -> -4
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Now, create the CYCLE: -4 points back to 2
    node4.next = node2

    # Test the code
    sol = Solution()
    result = sol.hasCycle(node1)
    print(f"Has Cycle: {result}") # Should print True
