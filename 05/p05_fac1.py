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

Algorithm Intuition: Find all small palindromes os size 2 or 3.
                     Next get real size of each palindrome.
                     sort the list of candidates with descending by real size.
                     return first candidate.

exceed time limit in test case 89.

------------------------------------------------------------------------------- '''


class Solution:

    def is_palindrome_ij(self, s, i, j ):
        if s[ i ] == s[ j ]:
            return True
        return False

    def get_candidates(self, s ):
        n          = len( s )
        candidates = []
        for i in range( 0, n - 2):
            j = i + 1
            a = s[ i : j +1 ]
            if self.is_palindrome_ij( s, i, j ):
                # tuple = ( size, substring, i, j )
                t = ( 2, a, i, j )
                candidates.append( t )
            j = i + 2
            a = s[ i : j + 1]
            if self.is_palindrome_ij( s, i, j ):
                t = (3, a, i, j)
                candidates.append(t)

        i = n-2
        j = n-1
        a = s[ i : j +1 ]
        if self.is_palindrome_ij( s, i, j ):
            # tuple = ( size, substring, i, j )
            t = ( 2, a, i, j )
            candidates.append( t )

        return candidates

    def get_pal_tuple(self, s, i, j):
        n     = len( s )
        size  = 0
        start = i
        end   = j
        while i >= 0 and j < n:
            if self.is_palindrome_ij( s, i, j ) == True:
                start = i
                end   = j
                size  = j - i + 1
                i    -= 1
                j    += 1
            else:
                break

        return  (size, s[ start : end + 1], start, end )

    def get_candidates_size(self, candidates, s):
        can_sizes = []
        for c in candidates:
            i = c[2]
            j = c[3]
            t = self.get_pal_tuple ( s, i, j)
            can_sizes.append( t )
        if len( can_sizes ) > 0:
            can_sizes = sorted(can_sizes, key=lambda t: -t[0])
        return can_sizes

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n    = len( s )
        if n <= 1:
            return s

        candidates = self.get_candidates( s )
        can_sizes  = self.get_candidates_size( candidates, s )
        if len(can_sizes) == 0:
            return s[0]
        else:
            return can_sizes[0][1]



# -------------------------------------------------------------------------------
# Unit Test
# -------------------------------------------------------------------------------


import datetime
import textwrap
import time


#s   = 'babad'
#s = 'cbbd'
#s = "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
#s = 'aaaa'
s = 'abcda'

sol = Solution()

start_time   = time.time()
p            = sol.longestPalindrome( s )
end_time     = time.time()
process_time = end_time - start_time

#print( '\n input:' )
#for line in textwrap.wrap( s, 79):
#    print( line )

print( '\nbrute force: 0:00:00.278740  ' )
print ( 'process_time: {0} seconds'.format( process_time ) )
print( 'timedelta: {0}'.format( datetime.timedelta( seconds = process_time ) ) )

print( 'palindrome: ***{}***'.format( p ) )

