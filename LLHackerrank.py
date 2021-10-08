#to reverse printing linked list
def reversePrint(llist):
    # Write your code here

    a=[]
    while llist:
        ele=llist.data
        a.append(ele)
        llist=llist.next
    a.reverse()
    for i in a:
        print(i)

#reverse a linked list
def reverse(llist):
    # Write your code here
    prev = None
    cur = llist
    nxt = llist.next
    while cur != None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    llist = prev
    return llist

#comparing two linked list
def compare_lists(llist1, llist2):
    a = []
    b = []

    count1 = 0
    count2 = 0
    while llist1:
        ele1 = llist1.data
        a.append(ele1)
        count1 += 1
        llist1 = llist1.next

    while llist2:
        ele2 = llist2.data
        b.append(ele2)
        count2 += 1
        llist2 = llist2.next
    if count1 == count2:
        if a == b:
            return 1
        else:
            return 0
    else:
        return 0

#Merge two sorted linked list
def mergeLists(head1, head2):
    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeLists(head1.next, head2)

    else:
        temp = head2
        temp.next = mergeLists(head1, head2.next)

    return temp

#Cycle detection
def has_cycle(head):
    temp1 = temp2 = head
    while temp2 != None and temp2.next != None:
        temp1 = temp1.next
        temp2 = temp2.next.next
        if temp1 == temp2:
            return 1

    return 0
#finding merge point
def findMergeNode(head1, head2):
    while head1:
        temp = head2
        while temp:
            if head1 == temp:
                return head1.data
            temp = temp.next

        head1 = head1.next


#inserting element in sorted doubly linked list
def sortedInsert(llist, data):
    # Write your code here
    nb = DoublyLinkedListNode(data)
    if llist == None:
        llist = node
    elif data < llist.data:
        nb.next = llist
        llist.prev = nb
        llist = nb
    else:
        temp = llist
        while temp.next != None and temp.data < data:
            temp = temp.next
        if temp.next == None and temp.data < data:
            nb.prev = temp
            temp.next = nb
        else:
            prev1 = temp.prev
            prev1.next = nb
            nb.prev = prev1
            nb.next = temp
            temp.prev = nb

    return llist

#reversing doubly linked list
def reverse(llist):
    # Write your code here
    temp=newhead=llist
    while temp:
        temp.next,temp.prev=temp.prev,temp.next
        newhead=temp
        temp=temp.prev
    return newhead


