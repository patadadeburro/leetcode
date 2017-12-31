'''
-------------------------------------------------------------------------------
Description: 5. Longest Palindromic Substring
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

    Input: "cbbd"

    Output: "bb"
------------------------------------------------------------------------------- '''


class Solution:

    def is_palindrome(self, s, size, half):
        for i in range( 0, half):
            i2 = size -1 -i
            if s[i] != s[ size - 1 - i]:
                return False
        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n    = len( s )
        size = n
        half = 0

        if n <= 1:
            return s

        for size in range( n, 0, -1 ):
            if size % 2 == 0:
                half = ( size / 2 ) - 1
            else:
                half = (size // 2)
            #print( 'size: {}, half: {}'.format( size, half ) )


            i2 = n - size + 1

            # slidding window
            for i in range( 0, n - size + 1 ):
                w = s[ i : i + size ]
                f = self.is_palindrome( w, size, half )
                if f == True:
                    return w

        print( 'Not palindrome' )
        return ''

# -------------------------------------------------------------------------------
# Unit Test
# -------------------------------------------------------------------------------

s   = 'hello'
sol = Solution()
p = sol.longestPalindrome( s )
print( 'palindrome: {}'.format( p ) )
