'''
-------------------------------------------------------------------------------
3. Longest Substring Without Repeating Characters

Description:
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Algorithm Intuition: Using a sliding window.

author: Arturo Alatriste Trujillo.
------------------------------------------------------------------------------- '''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n       = len( s )
        start   = 0
        end     = 0
        longest = 0
        i       = 0
        while start < n and end < n:
            i  = s.find( s[ end ], start, end )
            if i == -1:
                # character is not repeated
                end    += 1
                longest = max( longest, end - start )
            else:
                # repeated character found.
                size  = end - start + 1
                start = i + 1
        return longest
