# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base cases
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Compute length and find the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
            
        # Step 2: Handle cases where k >= length
        k = k % length
        if k == 0:
            return head
            
        # Step 3: Connect tail to head to form a circular list
        tail.next = head
        
        # Step 4: Find the new tail at position (length - k - 1)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # Step 5: Set new head and sever the loop
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head