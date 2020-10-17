"""
Maintain a head and a tail pointer on the merged linked list. Then choose the head of the merged linked list by comparing the first node of both linked lists. For all subsequent nodes in both lists, you choose the smaller current node and link it to the tail of the merged list, and moving the current pointer of that list one step forward.

Continue this while there are some remaining elements in both the lists. If there are still some elements in only one of the lists, you link this remaining list to the tail of the merged list. Initially, the merged linked list is NULL.

Compare the value of the first two nodes and make the node with the smaller value the head node of the merged linked list. In this example, it is 4 from head1. Since it’s the first and only node in the merged list, it will also be the tail. Then move head1 one step forward.
"""

def merge_sorted(head1, head2):
  if head1 == None: # if first ll is empty, returns complete second ll
    return head2
  elif head2 == None: # if second ll is empty, returns complete first ll
    return head1

  mergedHead = None
  if head1.data <= head2.data: #For adding first mergedHead, lowest value from first element of both the list will be considered as mergedHead
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead

  while head1 != None and head2 != None: # From second value till both the ll have values
    temp = None
    if head1.next <= head2.next:
      temp = head1
      head1 = head1.next

    else:
      temp = head2
      head2 = head2.next

  mergedTail.next = temp
  mergedTail = temp

  if head1 != None: #if only first ll have remaining values
    mergedTail.next = head1

  elif head2 != None: #if only second ll have remaining values
    mergedTail.next = head2

  return mergedHead


