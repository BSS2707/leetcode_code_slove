class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root

        while curr:
            head = None   # first node of next level
            prev = None   # previous node in next level

            while curr:
                if curr.left:
                    if not head:
                        head = curr.left

                    if prev:
                        prev.next = curr.left

                    prev = curr.left

                if curr.right:
                    if not head:
                        head = curr.right

                    if prev:
                        prev.next = curr.right

                    prev = curr.right

                curr = curr.next

            curr = head

        return root