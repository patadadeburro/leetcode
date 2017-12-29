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

Algorithm Intuition: create a dictionary 'counts' with char and (i1, i2, i3, ...) indexes.
                     create a dictionary 'repeated' of char
                     create a list       'candidates' of substrings
                        ( size, substring, start_index, end_index )
                     sort 'candidates' by size of substring

                     create a list 'Indexes', with the indexes of repeated chars.

                     sort Indexes by start_index

                     check which substrings in S does not contain another

author: Arturo Alatriste Trujillo.
------------------------------------------------------------------------------- '''
from collections import defaultdict

class Solution(object):

    def get_counts(self, a ):
        '''
        read all the string, count the characters and store the indexes.
        :param a: string
        :return:
        '''
        n = len( a )
        d = defaultdict(list)
        for i in range( 0, n ):
            ch = a[ i ]
            d[ ch ].append( i )

        return d

    def has_repeated_char( self, counts, a, ch, star_index, end_index ):
        '''
        check if char ch is repeated in a
        :param counts:
        :param a:
        :param ch:
        :param star_index:
        :param end_index:
        :return:
        '''
        result = False
        indexes = counts[ ch ]
        if len( indexes ) == 1:
            return False

        s = 0
        i = 0
        while i < len(indexes) and s < 2:
            ind = indexes[ i ]
            if ind >= star_index and ind <= end_index:
                s = s + 1
            i = i + 1

        if s >= 2:
            result = True

        return  result

    def is_unique(self, counts, a, start_index, end_index):
        for ch, indexes in counts.items():
            if indexes[0] > end_index:
                break
            if len(indexes) == 1:
                continue

            if self.has_repeated_char(counts, a, ch, start_index, end_index) == True:
                return False

        return True

    def has_unique_substrings(self, counts, s, size ):
        result = False

        #print( '\n has_unique_substrings, size: {}'.format( size )  )
        for i in range( 0, len(s) - size+1 ):
            a = s[ i : i + size ]
            start_index = i
            end_index   = i + size -1
            r = self.is_unique(counts, a, i, i + size - 1)
            #print('a: {}, start_index: {}, end_index: {}, unique: {}'.format(a, start_index, end_index, r))

            if r == True:
                return True
        return result

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len( s )
        result     = ''
        counts     = self.get_counts( s )


        for size in range( n, 0, -1):
            if self.has_unique_substrings( counts, s, size ) == True:
                return size

        return  0


#-------------------------------------------------------------------------------
# Unit Test
#-------------------------------------------------------------------------------
'''
a = 'abcabcbb'
#a = 'aab'
print( 'input: {}'.format( a ) )

s      = Solution()
output = s.lengthOfLongestSubstring( a )
print( 'output: {}'.format( output ) )




print( 'end.' )
'''