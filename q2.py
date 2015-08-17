##补齐以简化成统一循环；两数来保存前后进位
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(7)
l1.next = ListNode(7)

l2 = ListNode(3)
l2.next = ListNode(2)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

class Solution:

    def show(self, l):
        if l == None:
            print "Null"
        else:
            print "--" + str(l.val),
        while l.next != None:
            l = l.next
            print "--" + str(l.val),

    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
  
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3

        # make up the same long list
        while (p1.next != None or p2.next != None):
            if (p1.next == None):
                p1.next = ListNode(0)
            
            if (p2.next == None):
                p2.next = ListNode(0)
            
            p1 = p1.next
            p2 = p2.next
        
        p1 = l1
        p2 = l2

        tmp_p = 0
        tmp_a = 0
        sum_tmp = 0
    
        # tackle the intersection
        while (p1 != None):
            tmp_p = tmp_a
            tmp_a = 0
            sum_tmp = p1.val + p2.val + tmp_p
            if sum_tmp >= 10:
                sum_tmp = sum_tmp - 10
                tmp_a = 1
            p3.next = ListNode(sum_tmp)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next

        # tackle the rest
        if tmp_a == 1:
            p3.next = ListNode(1)

        self.show(l3.next)
        return l3.next

Solution().addTwoNumbers(l1,l2)  
