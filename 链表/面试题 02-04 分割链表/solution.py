#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1 = ListNode(None)
        h2 = ListNode(None)
        l1 = h1
        l2 = h2
        while head:
            if head.val >= x:
                l1.next = ListNode(head.val)
                l1 = l1.next
            else:
                l2.next = ListNode(head.val)
                l2 = l2.next
            head = head.next

        l2.next = h1.next
        return h2.next


if __name__ == '__main__':
    head = ListNode(1)
    l = head
    l.next = ListNode(4)
    l = l.next
    l.next = ListNode(3)
    l = l.next
    l.next = ListNode(2)
    l = l.next
    l.next = ListNode(5)
    l = l.next
    l.next = ListNode(2)

    # while head:
    #     print('l :', head.val)
    #     head = head.next

    s = Solution()
    h = s.partition(head, 3)
    while h:
        print(h.val)
        h = h.next