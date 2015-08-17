class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(7)
l1.next = ListNode(7)

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next = ListNode(4)

class Solution:

    def show(self, l):
        if l == None:
            print "Null"
        else:
            print "--" + str(l.val),
        while l.next != None:
            l = l.next
            print "--" + str(l.val),

    def len(self, l):
        if l == None:
            return 0
        i = 1
        while l.next != None:
            i += 1
            l = l.next
        return i

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

        tmp_p = 0
        tmp_a = 0
        sum_tmp = 0
        len1 = self.len(l1)
        len2 = self.len(l2)
        i = 0
        # tackle the intersection
        for i in range(min(len1, len2)):
            tmp_p = tmp_a
            tmp_a = 0
            sum_tmp = p1.val + p2.val
            if sum_tmp >= 10:
                sum_tmp = sum_tmp - 10
                tmp_a = 1
            val = sum_tmp + tmp_p
            p3.next = ListNode(val)
            p3 = p3.next
            p1 = p1.next
            p2 = p2.next

    # figure out the longer list
        if self.len(l1) >= self.len(l2):
            longer = p1
        else:
            longer = p2

    # tackle the rest
        for i in range(min(len1, len2)+1, max(len1, len2) +1):
            tmp_p = tmp_a
            tmp_a = 0
            sum_tmp = tmp_p + longer.next.val
            if sum_tmp >= 10:
                sum_tmp = sum_tmp - 10
                tmp_a = 1
            p3.next = ListNode(sum_tmp)
            p3 = p3.next
            long = long.next
            print "Hello"

    # tackle the rest
        if tmp_a == 1:
            p3.next = ListNode(1)

        self.show(l3.next)
        return l3.next

Solution().addTwoNumbers(l1,l2)  
