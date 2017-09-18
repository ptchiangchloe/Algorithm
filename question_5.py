# Question 5
# Find the element in a singly linked list that's m elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end
# is the 3rd element. The function definition should look like question5(ll, m),
# where ll is the first node of a linked list and m is the "mth number from the end".
# You should copy/paste the Node class below to use as a representation of a node in
# the linked list. Return the value of the node at that position.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the begining of the Linked LinkedList
    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def nthFromLast(ll, m):
        if m < 1:
            return None
        main_pointer = ll.head
        ref_pointer = ll.head

        count = 0
        if(ll.head is not None):
            while(count < m):
                if(ref_pointer is None):
                    return None
                ref_pointer = ref_pointer.next
                count += 1

        while(ref_pointer is not None):
            main_pointer = main_pointer.next
            ref_pointer = ref_pointer.next

        return main_pointer.value

llist = LinkedList()
llist.push(40)
llist.push(35)
llist.push(78)
llist.push(5)
llist.push(89)
llist.push(124)
llist.push(400)
llist.push(22)
llist.push(1000)

print llist.nthFromLast(1)
# 40
print llist.nthFromLast(0)
# None
print llist.nthFromLast(23)
# None
