'''
-----------------------------------------------------------------------------
Problem     : 7. Reverse Integer

Description :

    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
        Input: 123
        Output:  321

    Example 2:
        Input: -123
        Output: -321

    Example 3:
        Input: 120
        Output: 21

    Note:     Assume we are dealing with an environment
    which could only hold integers within the 32-bit signed integer range.
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Author  : Arturo Alatriste Trujillo.
Accepted: 104 ms
-----------------------------------------------------------------------------'''

class Solution:
    def reverse(self, x):
        """ We create the reversed integer using the modulo operator :)
        :type x: int
        :rtype: int
        """
        r = 0
        i = abs( x )
        while i != 0:
            r = r * 10 + i % 10
            i = i // 10

        if x < 0:
            r = -r
        if  r < -2147483648 or 2147483647 < r:
            return 0
        return r


# -----------------------------------------------------------------------------
# unit test
# -----------------------------------------------------------------------------

s = Solution()
x = 1534236469
r = s.reverse( x )
print( 'x: {}'.format( x ) )
print( 'r: {}'.format( r ) )