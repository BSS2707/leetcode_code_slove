# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper function to check if there are at least k nodes left
        def hasKNodes(cur, k):
            count = 0
            while cur and count < k:
                cur = cur.next
                count += 1
            return count == k

        # Helper function to reverse k nodes
        def reverseK(cur, k):
            prev = None
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while hasKNodes(prev_group.next, k):
            start = prev_group.next
            end = start
            for _ in range(k - 1):
                end = end.next
            next_group = end.next

            # Reverse k nodes
            new_head = reverseK(start, k)

            # Connect previous group to new head
            prev_group.next = new_head
            start.next = next_group

            # Move prev_group pointer forward
            prev_group = start

        return dummy.next
