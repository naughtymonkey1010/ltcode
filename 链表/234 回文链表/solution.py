#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        arr_length = len(arr)
        for i in range(arr_length):
            if arr[i] != arr[arr_length - i - 1]:
                return False
        return True


# 快慢指针有点复杂,还好
class Solution2:
    pass
    # todo  快慢指针