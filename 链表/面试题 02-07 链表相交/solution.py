#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        adda = {}
        numbera, numberb = 0, 0
        while headA:
            adda[id(headA)] = numbera
            headA = headA.next
            numbera += 1

        while headB:
            if id(headB) in adda:
                return headB
            headB = headB.next
            numberb += 1

        return None


# 利用双指针同路径， 时间复杂度n， 空间复杂度为1
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB

        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA

        return l1


if __name__ == '__main__':
    a = None
    b = None
    print(a == b)
    print(id(a) == id(b))
