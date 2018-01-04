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
Complexity: O(N) time and O(N) Space.

references:
    https://en.wikipedia.org/wiki/Longest_palindromic_substring

    https://leetcode.com/problems/longest-palindromic-substring/solution/
    https://articles.leetcode.com/longest-palindromic-substring-part-ii/

    Manacher algorithm in Python O(n)
    https://leetcode.com/problems/longest-palindromic-substring/discuss/3337

Accepted: 172 ms
------------------------------------------------------------------------------- '''

class Solution:

    def longestPalindrome(self, s):
        '''
        Find the longest palindrome using Manacher Algorithm.
        :param s: a string

        T = is a Transform S with.
        n = length of T
        P = collection of palindrome sizes
        C = Center
        R = right limit of the last palindrome
        :return:
        '''

        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            # set palindrome size
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)

            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]
