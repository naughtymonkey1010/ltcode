#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        l1 = l2 = head
        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next

        return l1