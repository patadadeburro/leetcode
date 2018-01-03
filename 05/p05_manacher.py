'''-------------------------------------------------------------------------------
problem    : 5. Longest Palindromic Substring
Description:
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"

Algorithm : Manacher Algorithm

references:
    https://en.wikipedia.org/wiki/Longest_palindromic_substring

    https://leetcode.com/problems/longest-palindromic-substring/solution/
    https://articles.leetcode.com/longest-palindromic-substring-part-ii/

    Manacher algorithm in Python O(n)
    https://leetcode.com/problems/longest-palindromic-substring/discuss/3337
------------------------------------------------------------------------------- '''
s  = "abba"
s1 = '^{}$'.format(s)
T  = '#'.join( '^{}$'.format(s) )

data = [ 'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print( data )

s2 = '_'.join( data )

s3 = 'hello my friends'

r = max( s1, 'eagle', s3, key = len )


print( 'end.' )


