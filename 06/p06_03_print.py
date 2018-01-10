'''
-------------------------------------------------------------------------------

Problem     : 6. ZigZag Conversion
Description :
                The string "PAYPALISHIRING" is written in a zigzag pattern
                on a given number of rows like this:
                    (you may want to display this pattern in a fixed font for better legibility)

                P   A   H   N
                A P L S I I G
                Y   I   R
                And then read line by line: "PAHNAPLSIIGYIR"
                Write the code that will take a string and make this conversion given a number of rows:

                string convert(string text, int nRows);
                convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Algorithm      : Use a list of strings and fill it up-down-up, up-down-up, ...

Author         : Arturo Alatriste Trujillo.
-------------------------------------------------------------------------------
'''

from collections import defaultdict

class Solution:

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n   = len( s )
        # array with zigzag text
        a   = [ '' ] * numRows
        i   = 0
        row = 0
        space = ''

        while i < n:
            row = 0
            while i < n and row <numRows:
                a[ row ] += space + s[i]
                i   += 1
                row += 1
                space = ''

            space   =  ' ' * numRows
            a[row -1 ] += space

            row = numRows - 2
            while i < n and 0 < row:
                space = ' ' * (numRows - row )
                a[ row ] += space + s[i]
                i   += 1
                row -= 1

            space += ' '

        print( '\nZigzag pattern: \n' )
        for i in a:
            print( i )

        print('\n')

        return ''.join( a ).replace( ' ', '' )

# -------------------------------------------------------------------------------
# test
# -------------------------------------------------------------------------------


s       = 'PAYPALISHIRING'
numRows = 3
sol     = Solution()
print( '\n input string: {}'.format( s ) )
result  = sol.convert( s, numRows )
print( 'result: {}'.format( result ) )