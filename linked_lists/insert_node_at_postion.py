def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if(position==0):
        new_node.next = head
        return new_node
    
    i = 0
    cur = head
    while(i<position-1):
        cur = cur.next
        i += 1
    tmp = cur.next
    cur.next = new_node
    new_node.next = tmp 
    return head
