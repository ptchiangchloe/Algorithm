# Question 1
# Given two strings s and t, determine whether some anagram of t is
# a substring of s. For example: if s = "udacity" and t = "ad",
# then the function returns True. Your function definition should look like:
# question1(s, t) and return a boolean True or False.

# Find out if s1 and s2 strings are anagram of each other
# @param {string, string} input strings
# @return {bool} if string are anagram of each other or not
def is_anagram(s1, s2):

    s1 = list(s1)
    s2 = list(s2)

    s1.sort()
    # Quick sort O(n*log(n))
    s2.sort()

    return s1 == s2

# Find out sorted(possible substring of s) and compare with sorted(t).
# @params {string, string} input strings
# @return {bool} Question1 answer
def question1(s, t):
    if s == None or t == None:
        return False
    match_length = len(t)
    pattern_length = len(s)

    for i in range(pattern_length - match_length + 1):
        if is_anagram(s[i: i+match_length], t):
            return True
    return False

# Test cases:
# String S
# String t

# Case 1: question1("", "") -> True
print question1("", "")
# two empty strings have the same values

# Case 2: question1("Hello", "llo" -> True
print question1("Hello", "lol")
# string with 3 letters not same as in order as S

# Case 3: question1("Hello", "le") -> True
print question1("Hello", "le")
# string with 2 letters with new letter not in string S

# Case 4: question1("Hello", "Helloo") -> False
print question1("Hello", "Helloobr")
# substring t's length is greater than string S

# Case 5: question1("Hello", "Hello") -> True
print question1("Hello", None)
# String t has the same value as String S
