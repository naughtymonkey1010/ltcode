#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        l = None

        while head:
            tmp = ListNode(head.val)
            tmp.next = l
            l = tmp
            head = head.next

        return l