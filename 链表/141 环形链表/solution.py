#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        l1 = l2 = head
        number = 0

        while l1 != l2 or number == 0:

            if l2 and l2.next:
                l2 = l2.next.next
            else:
                return False

            l1 = l1.next

            number += 1

        return True