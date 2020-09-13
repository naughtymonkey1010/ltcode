#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        number = 0
        l1 = l2 = l3 = head

        # while not (l1 == l2 and number != 0):
        # 仅仅是while 这一句条件的判断， 排名就提高了30%-40% 。。。。
        while l1 != l2 or number == 0:
            number += 1

            if l2 and l2.next:
                l2 = l2.next.next
            else:
                return None

            l1 = l1.next

        while l1 != l3:
            l1 = l1.next
            l3 = l3.next

        return l1





