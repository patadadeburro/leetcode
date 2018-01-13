'''
-------------------------------------------------------------------------------
Problem    : 8. String to Integer (atoi)

Description:

    Implement atoi to convert a string to an integer.

    Hint: Carefully consider all possible input cases. If you want a challenge,
    please do not see below and ask yourself what are the possible input cases.

    Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
    You are responsible to gather all the input requirements up front.

    Update (2015-02-10):
    The signature of the C++ function had been updated. If you still see your function
    signature accepts a const char * argument, please click the reload button  to reset your code definition.

Author: Arturo Alatriste Trujillo.
__________         __              .___           .___    __________
\______   \_____ _/  |______     __| _/____     __| _/____\______   \__ ________________  ____
 |     ___/\__  \\   __\__  \   / __ |\__  \   / __ |/ __ \|    |  _/  |  \_  __ \_  __ \/  _ \
 |    |     / __ \|  |  / __ \_/ /_/ | / __ \_/ /_/ \  ___/|    |   \  |  /|  | \/|  | \(  <_> )
 |____|    (____  /__| (____  /\____ |(____  /\____ |\___  >______  /____/ |__|   |__|   \____/
                \/          \/      \/     \/      \/    \/       \/
'''

class Solution:
    def myAtoi(self, str):
        """
        We use the ascii code to check if a character is a digit.
        Ascii codes for digits goes from 48 for Zero, and 57 for Nine.

        :type str: str
        :rtype: int
        """
        if str == None or str == '':
            return 0

        n     = 0
        str   = str.strip().replace( ',', '' )
        start = 0
        sign  = 1
        if str[ 0 ] == '-' or  str[ 0 ] == '+':
            start = 1
        if str[0] == '-':
            sign = -1

        for i in range( start, len(str) ):
            a = ord( str[ i ] )
            if a >= 48 and a <= 57:
                # we have a digit
                d = a - 48
                n = n*10 + d
            else:
                # we found a character that is not a digit
                break
        n = sign * n

        if n < -2147483648:
            return -2147483648
        if n > 2147483647:
            return 2147483647

        return n



# -----------------------------------------------------------------------------
# unit test
# -----------------------------------------------------------------------------

#s1 = "  -0012a42"
s1 = "2147483648"
s = Solution()
i = s.myAtoi( s1 )

print( 's1: {}'.format( s1 ) )
print( 'i : ***{}***'.format( i ) )