def findMergeNode(head1, head2):
    list1_set = set()
    cur = head1
    while(cur):
        list1_set.add(cur)
        cur = cur.next
    cur = head2
    while(cur):
        if(cur in list1_set):
            return cur.data
        cur = cur.next
