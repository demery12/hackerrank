# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            new_head = ListNode(l1.val)
            c1 = l1.next
            c2 = l2
        else:
            new_head = ListNode(l2.val)
            c2 = l2.next
            c1 = l1
        cur_node = new_head
        while c1 or c2:
            if not c1:
                cur_node.next = ListNode(c2.val)
                c2 = c2.next
            elif not c2:
                cur_node.next = ListNode(c1.val)
                c1 = c1.next
            elif c1.val < c2.val:
                cur_node.next = ListNode(c1.val)
                c1 = c1.next
            else:
                cur_node.next = ListNode(c2.val)
                c2 = c2.next
            cur_node = cur_node.next
        return new_head

    def print_list(self, l1):
        list_to_print = []
        while l1:
            list_to_print.append(str(l1.val))
            l1 = l1.next
        print('->'.join(list_to_print))


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

d.next = e
e.next = f


sol = Solution()
sol.print_list(sol.mergeTwoLists(a, d))
