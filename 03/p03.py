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

from collections import OrderedDict
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

    def get_candidates( self, counts, a ):
        '''
        create a list of candidates. Each candidate is a tuple
            ( size, substring, start_index, end_index )
        :param counts:
        :param a: string
        :return:
        '''
        candidates = list()
        for ch, indexes in counts.items():
            previous = indexes[ 0 ]
            if len( indexes ) == 1:
                continue

            for i in indexes:
                if previous != i:
                    t = ( i - previous, a[ previous : i ], previous, i )
                    candidates.append( t )

                previous = i

        candidates = sorted( candidates, key = lambda t: -t[0] )
        return candidates

    def get_solutions( self, candidates ):
        print( 'todo: code this' )


    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''



        return  result


#-------------------------------------------------------------------------------

a = 'abcabcbb'
print( 'input: {}'.format( a ) )

s = Solution()
counts = s.get_counts( a )

print( 'counts' )
for ch, ind in counts.items():
    print( '{} \t {}'.format( ch, ind ) )

print( '\ncandidates' )
candidates = s.get_candidates( counts, a )
for c in candidates:
    print( c )

print( 'end.' )
