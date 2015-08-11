class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l1.next = ListNode(2)

l2 = ListNode(2)
l2.next = ListNode(3)

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 == null:
            return l2
        if l2 == null:
            return l1
        l3 = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = l3

        tmp_p = 0
        tmp_a = 0
        sum_tmp = 0
        len1 = len(l1)
        len2 = len(l2)
        i = 0
        for i in range(min(len1, len2)):
            tmp_p = tmp_a
            tmp_a = 0
            sum_tmp = p1.val + p2.val
            if sum_tmp >= 10:
                sum_tmp = sum_tmp - 10
                tmp_a = 1
            p3.val = sum_tmp + tmp_p
            
            p1 = p1.next
            p2 = p2.next
            
