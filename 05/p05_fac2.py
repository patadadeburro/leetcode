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

Algorithm Intuition:
                     if string s is empty or has one char or has only one char repeated
                     return s

                     Find all small palindromes os size 2 or 3.
                     Next get real size of each palindrome.
                     keep the palindrome with the biggest size.
                     Do not store all palindromes, and do not sort.
                     return biggest candidate.

Accepted.

------------------------------------------------------------------------------- '''


class Solution:

    def is_palindrome_ij(self, s, i, j ):
        '''
        check if characters at index i and j are equal.
        :param s: string
        :param i: start index
        :param j: end   index
        :return : True if characters at index i and j are equal, other case False.
        '''
        if s[ i ] == s[ j ]:
            return True
        return False

    def get_candidates(self, s ):
        '''
        Find all the palindrome candidates. we do not check the size of the palindrome here.
        :param s: string
        :return : a collection of tuples ( size, palindrome, start_index, end_index )
        '''
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
        '''
        calculate the size of the palindrome, and return a tuple with ( size, palindrome, start_index, end_index )
        :param s: input string
        :param i: start index of the candidate palindrome
        :param j: end index   of the candidate palindrome
        :return: a tuple with ( size, palindrome, start_index, end_index )
        '''
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

    def get_biggest_palindrome(self, candidates, s):
        '''
        get the biggest palindrome from the candidates collection
        :param candidates:
        :param s:
        :return:
        '''
        biggest = ( 0, '', 0, 0)
        can_sizes = []
        for c in candidates:
            i = c[2]
            j = c[3]
            t = self.get_pal_tuple ( s, i, j)

            biggest = max( biggest, t, key = lambda x: x[0] )

        return biggest

    def longestPalindrome(self, s):
        '''

        :param s: input string
        :return : a string that is the biggest palindrome
        '''
        n    = len( s )
        if n <= 1 or len( s.replace( s[0], '' ) ) == 0:
            return s

        candidates = self.get_candidates( s )
        biggest    = self.get_biggest_palindrome( candidates, s )

        if biggest[ 1 ] == '':
            return s[0]

        return biggest[ 1 ]



# -------------------------------------------------------------------------------
# Unit Test
# -------------------------------------------------------------------------------

'''
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

'''