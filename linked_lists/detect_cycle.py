def has_cycle(head):
    visited = set()
    cur = head
    while(cur):
        if(cur in visited):
            return True
        visited.add(cur)
        cur = cur.next
    return False 
