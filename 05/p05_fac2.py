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

Time complexity  : O(n^2)O(n2​​ ). Since expanding a palindrome around its center could take O(n)O(n) time,
                  the overall complexity is O(n^2)O(n​2​​ ).

Space complexity : O(1)O(1).

Accepted. 515 ms

------------------------------------------------------------------------------- '''


class Solution:

    def get_candidates(self, s ):
        '''
        Find all the palindrome candidates. we do not check the size of the palindrome here.
        :param s: string
        :return : a collection of tuples ( size, palindrome, start_index, end_index )
        '''
        n          = len( s )
        candidates = []
        for i in range( 0, n - 2):
            # candidates of len 2
            j = i + 1
            a = s[ i : j +1 ]
            if s[i] == s[j]:
                t = ( 2, a, i, j )
                candidates.append( t )

            # candidates of len 3
            j = i + 2
            a = s[ i : j + 1]
            if s[i] == s[j]:
                t = (3, a, i, j)
                candidates.append(t)

        # add the last candidate of len 2
        i = n-2
        j = n-1
        a = s[ i : j +1 ]
        if s[i] == s[j]:
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
            #if self.is_palindrome_ij( s, i, j ):
            if s[i] == s[j]:
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
        get the biggest palindrome from the candidates collection.
        :param candidates:
        :param s:
        :return: a tuple ( size, palindrome, start_index, end_index ),
                 where
                    start_index is the element at position [2]
                    end_index   is the element at position [3]

        '''
        biggest = ( 0, '', 0, 0)
        for c in candidates:
            t       = self.get_pal_tuple ( s, c[2], c[3] )
            biggest = max( biggest, t, key = lambda x: x[0] )

        return biggest

    def longestPalindrome(self, s):
        '''

        :param s: input string
        :return : a string that is the biggest palindrome
        '''
        n    = len( s )
        if n <= 1:
            return s

        if len( s.replace( s[0], '' ) ) == 0:
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