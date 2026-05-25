# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None): #__init__ is a method/function in a class, it's called immediately when an object (class instance) is created
#         self.val = val #An individual initialised object will have its val = val | i.e. Stores the value of this node
#         self.next = next #An individual initialised object will have its next pointer = next pointer | Stores a reference (pointer) to the next node 

#Task: Given beginning of singly linked list (head), reverse the list and return the new beginning of the list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #'head' is the singly-linked list, reverse the singly-linked list and return the first value of it
        prev, curr = None, head #'head' holds singly linked list, curr will initially hold the first value bc of the pointers
                                # curr = head establishes the blue pointer

        while curr: #i.e. while curr is not empty/NULL
            nxt = curr.next #Here we store the next node of the curr node, this way we dont lose it after we reverse the white pointer
            curr.next = prev #White pointer of 1 -> 2 into NULL <- 1 | curr.next refers to the pointer of current list value to the next 
            prev = curr #curr has not moved yet*** - Shift prev pointer from NULL to where curr is now
            curr = nxt #i.e. curr = curr.next => move the blue pointer from the curr node to point to the next node
            #One loop done
        return prev #Return the beginning of the new list