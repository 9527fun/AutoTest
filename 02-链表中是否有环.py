class Solution(object):

    def trycycle(self,head):
        if head == None or head.next == None:
                return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
