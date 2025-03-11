


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value

# Let code
"""
merge two sorted list
You are given the heads of two sorted linked lists. The linked lists must be merged into a single sorted linked list.
"""
from typing import Optional, List
#from linkedlist import ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linkedlist(head):
    current = head
    while current:
        print(List[current.val])
        current = current.next
    #print("None")

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        current = dummy
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next

# Convert lists to linked lists
l1 = list_to_linkedlist([1, 2, 4])
l2 = list_to_linkedlist([1, 3, 4])

# Merge the linked lists
merged_list = Solution().mergeTwoLists([1, 2, 4], [1, 3, 4])

# Print the merged linked list
print_linkedlist(merged_list)