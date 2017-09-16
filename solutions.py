# Question 1
# Given two strings s and t, determine whether some anagram of t is
# a substring of s. For example: if s = "udacity" and t = "ad",
# then the function returns True. Your function definition should look like:
# question1(s, t) and return a boolean True or False.

def question1(s, t):
    if s == "" or t == "":
        return False
    t = t[::-1]
    if t in s:
        return True
    return False

# Test cases:
print question1("", "")
# False
print question1("Hello", "llo")
# False
print question1("Hello", "le")
# True


# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def question2(a):
    if a == "":
        return None
    a = a.lower()
    results = []

    for i in range(len(a)):
        for j in range(0, i):
            chunk = a[j : i+1]
            if chunk == chunk[::-1]:
                results.append(chunk)

    return max(results, key=len)

# Test cases:
print question2("")
# ""
print question2("cabbadc")
# "aabb"
print question2("caabdvc")
# "aa"

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
