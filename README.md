### Algorithm Practice

## 1 Anagram Checker

The fist algorithm is to check a string if it's an anagram for another string as its substring.

First, create a helper function to check if two strings are anagram.
In the helper function, use the sorting algorithm to sort out two lists that the elements in the each list represents each string. For the helper function, the time efficiency complexity is O(n*log(n)) since we used the sorting algorithm and the n represents the items in a the list, the space algorithm will be O(n) since we will use two lists to store the string data.

Then we conduct our main algorithm, define the lengths of two input strings, then we will use two pointers to navigate the substrings for making comparison in the is_anagram helper function.

In the main operation, the time complexity is O(n) since we need find all the substring combinations in the string S, the space complexity is O(n).

The time efficiency is O(n) and the space efficiency is O(1).

## 2 The longest palindromic substring (Monacher Algorithm)

First, use a helper function called interleave, return a interleaved version of the given string. 'aaa' --> '#a#a#a'.
Thanks to this function, we don't have to deal with even/odd length issue of
palindrome.

Then, computes length of the longest palindromic substring centered on each character
in the given string. The idea behind this algorithm is to reuse previously
computed values whenever possible(palindromic and symmetric).

Example (interleaved string):
```
i 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
s # a # b # c # q # q #  q  #  q  #  q  #  q  #  x  #  y  #
P 0 1 0 1 0 1 0 1 2 3 4  5  6  5  4  ?
                    ^       ^        ^        ^
                  mirror   center  current   right
```
We're at index 15 wondering shall we compute (costly) or reuse. The mirror value
for 15 is (center is in 12 which is defined by the current targeting palindrome). P[mirror] = 3 which means a palindrome of length 3 is
3 is centered at this index. A palindrome of same length would be placed in index 15,
if 15 + 3 <= (right border of large palindrome centered in 12). This condition is satisfied,
so we can reuse value from index 9 and avoid computation.

The time efficiency is O(n) since we only need to loop through the whole list once.
The space efficiency is O(n).

## 3 The minimum spanning tree graph algorithm

The minimum spanning tree of a weighted undirected graph is an algorithm sums up the minimum
weight of the edges that connects all the vertices on the graph.

It needs to use the disjoint sets for this algorithm.

First, all the edges need to be sorted into a nondecreasing order.

Then, use makeSet operation of disjoint sets we create as many disjoint sets as the number of all
the vertices on the graph.

Then, start from the top of the nondecreasing edges list to check if vertices are connected or not by reference of the edge name. If the vertices are not connected, merge the vertices into one big disjoint set until all the vertices merge into one set by using union operation. At the same time, append the edge that used in the merge operation.

The reasoning behind the algorithm is to find the smallest combinations in terms of the weight by using sorting and comparison.

The time efficiency of this algorithm is O(Elog(E) + E), the Elog(E) is for sorting and E is for evaluating each edge when it comes to merge vertices into one big set. The space efficiency of the algorithm is O(V+E+A), V is for storing vertices in a list, E is for storing all the edges and their weight in a list, A is for storing adjacency_list for the return value in the end of this algorithm.

## 4 Find the least common ancestor

The mission of this algorithm is to find the lowest common ancestor in a Binary Tree.

The key point of the algorithm is to have clear understanding on how Binary tree works and how to use a matrix to represent a tree.

The search begin on the root node. Any time we found the input nodes from the left node or right node, we return the parent node as the least common ancestor,

Anytime we found left node and right node are both null, we return the None since the nodes are not exsiting.

Anytime if left node is not None and right is None, we will traverse into the left side and call the whole evaluation again.

Anytime if we found a input from one side and the other side is not None, we still will traverse the other side to see if we can find the another input node.

If the root value is one of the values from the input nodes. we also will return the root value since the root value will be the bigger common factor between those two input nodes.

The space efficiency complexity is O(n), n is for the nodes in the tree. The time efficiency complexity is O(n), n is for the time to traverse the tree.

## Nth number from the End.

This is a algorithm to find the value of the node in a specific location of a linked list.

First, test out the edge case to make sure the input number is not a negative number.

Then, user two pointers at the head to start in different time, when the fast pointer move head to make the distance as input number between the fast pointer and the slower, then the two can move together until the  fast pointer hits to the end of the list. At that moment, the slow pointer will be located at the nth node from the end.

The space efficiency of the operation is O(n), since the only space we need is for storing the linked list. The time efficiency complexity is O(n) as well, since we only need to walkthrough the link once.
