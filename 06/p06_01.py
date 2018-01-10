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

Algorithm      : Use a hash table and fill it up-down-up, up-down-up, ...

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
        # create hash table with rows
        d   = defaultdict( list )
        i   = 0
        row = 0

        while i < n:
            row = 0
            while i < n and row <numRows:
                ch = s[i]
                d[ row ].append( ch )
                i   += 1
                row += 1

            row = numRows - 2
            while i < n and 0 < row:
                ch = s[i]
                space = '' * (numRows - row)
                d[ row ].append( ch + space )
                i   += 1
                row -= 1


        # print Zigzag pattern
        for row in range( 0, numRows):
            #d[row] = ' '.join(d[row])
            #if row % 2 == 0:
            #    d[ row ] = ' '.join( d[ row ] )
            print(  ' '.join( d[ row ] ) )


        result = ''
        for row in range( 0, numRows):
            result += ''.join(d[row])

        return result

# -------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------


s       = 'PAYPALISHIRING'
numRows = 3
sol     = Solution()
result  = sol.convert( s, numRows )
print( 's: {}'.format( s ) )
print( 'result: {}'.format( result ) )