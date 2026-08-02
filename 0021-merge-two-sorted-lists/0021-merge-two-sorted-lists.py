# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # Attach the remaining nodes
        cur.next = list1 if list1 else list2

        return dummy.next


# Helper function to print linked list
def printList(node):
    while node:
        # Works in both Python 2 and 3
        sys.stdout.write(str(node.val) + " ")
        node = node.next
    print()


# Example usage
import sys

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
res = sol.mergeTwoLists(l1, l2)

printList(res)   # Output: 1 1 2 3 4 4
