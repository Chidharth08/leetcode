class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        grpprev = dummy

        while True:

            kth = grpprev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    break

            if not kth:
                break

            grpnext = kth.next

            prev = grpnext
            curr = grpprev.next

            while curr != grpnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = grpprev.next
            grpprev.next = kth
            grpprev = temp

        return dummy.next