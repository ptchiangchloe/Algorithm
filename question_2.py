# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

# @param {string} s input string
# @return {string}

def get_palindrome_length(string, index):
    """
    Return the half length of the longest palindromic substring based on the
    index of the center character of the string
    """
    length = 1
    while index + length < len(string) and index - length >= 0:
        # index - length >= 0 is to make sure the length is within the string
        if string[index + length] == string[index -length]:
            # the comparision is to elvaluate the how far the center could expand as palindrome
            length += 1
        else:
            break
    # print 'length{0}'.format(length)
    return length - 1

def get_palindrome(string, the_highest_value_index, palindrome_length):
    return string[the_highest_value_index-palindrome_length : the_highest_value_index+palindrome_length]

def interleave(string):
    result = []
    for s in string:
        result.extend(['#', s])
    result.append('#')

    return ''.join(result)

# @parame {string} s input string
# @return {string} the longest palindromic substring
def question2(string):
    right = 0
    center = 0
    # center represents the center spot of the current lps
    string = interleave(string)
    P = map(lambda e: 0, xrange(len(string)))
    # P is for tracking the each element's longest palindrome value. so P is list with all the longest
    # palindrome values.
    for i in xrange(1, len(string)):
        mirror = 2*center - i
        # mirror repesents the left responding point of the current pointer
        if right - i >= P[mirror] and mirror >= len(string) - i:
            # P[mirror] repesents the longest palindrome in the mirror index position and
            # i repesents the current pointer's location
            # as long as the number of elements between current pointer i and the right edge
            # location for the larger palindrome set. Then we could reuse the P value from the
            # mirror postion for current pointer i since. Because that section has been validated by the
            # larger palindrome
            P[i] = P[mirror]
        # This part is reuse
        else:
            plength = get_palindrome_length(string, i)
            P[i] = plength
            if plength > 1:
                center = int(i)
                right = center + plength
        # This part is compute
    the_highest_value_index = P.index(max(P))
    palindrome_length = get_palindrome_length(string, the_highest_value_index)
    palindrome = get_palindrome(string, the_highest_value_index, palindrome_length)
    palindrome_list = list(palindrome)
    filter_list = list(filter(lambda x: x != '#', palindrome_list))
    # get rid of the "#"
    return ''.join(filter_list)

# Test cases:
# Test case 1 -> ""
print question2("")
# Empty string
# Test case 2 -> "abba"
print question2("cabbadc")
# Odd number of characters in a string
# Test case 3 -> "dvccvd"
print question2("caabdvccvdaacebbe")
# Test case 4 -> "aa"
print question2("caabdv")
# Even number of characters in a string
# Test case 5 -> "abccba"
print question2("abccba")
# The whole string is a palindrome
