# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        lsum = ListNode(None)
        flag = 0
        tmp = lsum
        while l1 and l2:
            tmp.next = ListNode(None)
            tmp = tmp.next
            v = (l1.val + l2.val + flag) % 10
            flag = (l1.val + l2.val + flag) // 10

            tmp.val = v

            l1 = l1.next
            l2 = l2.next

        while l1:
            tmp.next = ListNode(None)
            tmp = tmp.next
            tmp.val = (l1.val + flag) % 10
            flag = (l1.val + flag) // 10
            l1 = l1.next
        while l2:
            tmp.next = ListNode(None)
            tmp = tmp.next
            tmp.val = (l2.val + flag) % 10
            flag = (l2.val + flag) // 10
            l2 = l2.next

        if flag:
            tmp.next = ListNode(flag)

        return lsum.next


# 把循环放到一起
class Solution2():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        lsum = ListNode(None)
        flag = 0
        tmp = lsum
        while l1 or l2:
            tmp.next = ListNode(None)
            tmp = tmp.next

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            tmp.val = (val1 + val2 + flag) % 10
            flag = (val1 + val2 + flag) // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if flag:
            tmp.next = ListNode(flag)

        return lsum.next

#