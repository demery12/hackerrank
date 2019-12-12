def reverse(head):
    if (head==None):
        return None
    cur = head
    while(cur.next):
        next = cur.next
        cur.next = cur.prev
        cur.prev = cur.next  
        cur = next 
    head = cur
    cur.next = cur.prev
    return head
