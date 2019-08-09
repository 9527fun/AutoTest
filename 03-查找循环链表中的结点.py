class Solution(object):
    def findjiedian(self,slow,fast,nhead):
        if nhead == None or nhead.next == None:
            return False
        slow = fast = nhead
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = nhead
                while (fast and fast.next):
                    slow = slow.next
                    fast = fast.next.next
                    if slow == fast:
                        return fast
        return False



