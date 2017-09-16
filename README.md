### Algorithm Practice

## 1 Anagram

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

## 



Write up an explanation for each question in a single separate text file (called "explanations.txt"). Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code. For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.
