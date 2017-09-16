### Algorithm Practice

## 1 Anagram Checker

The fist algorithm is to check a string if it's an anagram for another string as its substring.

First, the algorithm will check the edge cases to see if the inputs are empty strings. Then use reverse function to reverse the string. If the string is in the another string. Then it will return True.

The time efficiency is O(n) and the space efficiency is O(1).

## 2 The longest palindromic substring

The second algorithm is to find the longest palindromic substring for the input string.

First, test out the edge case that when the input string is a empty string. It will return None.

Second, make sure the testing string is all lowercase.

Then, create a results list that will contain all the substring combinations in the array by using nested loops.

Last, find out the longest string item in the results list.

The time efficiency is O(n**n) and the space efficiency will be O(n).

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







Write up an explanation for each question in a single separate text file (called "explanations.txt"). Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code. For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.
