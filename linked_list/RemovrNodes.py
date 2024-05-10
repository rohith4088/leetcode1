class ListNode():
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
class solution():
    def RemveNode(self,head:Optional[ListNode])->Optional[ListNode]:
        stack = []
        cur = head
        while stack:
            while stack and cur.val > stack[-1]:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next
        dummy = ListNode()
        cur = dummy
        for n in stack:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(11)
    head.next.next.next.next.next = ListNode(10)
    head.next.next.next.next.next.next = ListNode(15)
    head.next.next.next.next.next.next.next = ListNode(12)
    sol = solution()
    print(sol.RemveNode(head))
