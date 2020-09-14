#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        l1 = l2 = l3 = head
        number = 0

        while not (l1 == l2 and number > 0):

            if l2 and l2.next:
                l2 = l2.next.next
            else:
                return None

            l1 = l1.next
            number += 1

        while l1 != l3:
            l1 = l1.next
            l3 = l3.next

        return l1
