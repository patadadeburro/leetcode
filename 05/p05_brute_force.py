'''
-------------------------------------------------------------------------------
problem: 5. Longest Palindromic Substring

Description:
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"

Algorithm: Brute force. Time limit exceeded
------------------------------------------------------------------------------- '''


class Solution:
    def is_palindrome(self, s, size, half):
        for i in range( 0, half + 1):
            #i2 = size -1 -i
            if s[ i ] != s[ size -1 -i ]:
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

        for size in range( n, 1, -1 ):
            if size % 2 == 0:
                half = ( size // 2 ) - 1
            else:
                half = ((size -1) // 2 ) -1
            print( 'size: {}, half: {}'.format( size, half ) )



            #last_i = n - size + 1

            # slidding window
            for i in range( 0, n - size + 1 ):
                #i2 = i + size
                w = s[ i : i + size ]

                #print( 'size:{} i:{} i2:{} w:{}***'.format( size, i, i2, w ) )

                f = self.is_palindrome( w, size, half )
                if f == True:
                    return w

        #print( 'Not palindrome' )
        return ''

# -------------------------------------------------------------------------------
# Unit Test
# -------------------------------------------------------------------------------

#s   = 'hello world'
#s = 'hello arrozalazorra world'
s = "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"

sol = Solution()
p = sol.longestPalindrome( s )
print( 'palindrome: {}'.format( p ) )
