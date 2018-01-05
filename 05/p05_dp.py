'''
-------------------------------------------------------------------------------
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

Algorithm : Dynamic Programming

Time complexity  : O(n^2)
Space complexity : O(n^2)

Accepted. ms

------------------------------------------------------------------------------- '''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        n = len(s)
        dp = [ [False for j in range( n )] for i in range( n ) ]

        for j in range( n ):
            for i in range(j, -1, -1):
                dp[i][j] = (s[i] == s[j]) and ( j - i < 2 or dp[i + 1][j - 1] )
                if dp[i][j] and (end - start) < (j - i):
                    start, end = i, j

        return s[start:end + 1]