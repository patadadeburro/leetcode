'''
-------------------------------------------------------------------------------
Description: Hash table with one pass.
             we use a dictionary  key value, where
             key is the number from array nums, and
             value is a list of indexes.

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Test: Solution Accepted!

Author: Arturo Alatriste Trujillo.

references: leetcode.com
            Algorithms.
            1. Two sum.
            https://leetcode.com/problems/two-sum/description/

------------------------------------------------------------------------------- '''

from collections import OrderedDict
from collections import defaultdict

class Solution( object):

    def twoSum( self, nums, target ):
        found        = False
        i            = 0
        j            = 0
        num_elements = len( nums )

        d = defaultdict(list)

        #print( 'd: {0}'.format( d ) )

        for i in range(0, num_elements ):
            d[ nums[ i ] ].append(i)
            j_val = target - nums[ i ]

            if j_val in d:
                indexes = d[ j_val ]

                if nums[ i ] != j_val :
                    found = True
                    j     = indexes[ 0 ]
                    break

                if nums[ i ] == j_val and len(indexes) > 1:
                    found = True
                    j     = indexes[ 0 ]
                    break



        '''
        if found == True:
            print( 'The solution is' )
            print( 'i   : {0}, j   : {1}'.format( i, j ) )
            print( 'nums[ {0} ]: {1}, nums[ {2} ]: {3}'.format( i, nums[i], j, nums[j] ) )
        else:
            print( 'This array does not have solution' )
        '''

        return [ j, i ]




# -------------------------------------------------------------------------------
# test
# -------------------------------------------------------------------------------

#data   = [ 15, 11, 7,  2 ]
#target = 9
#found  = False

#data = [-1,-2,-3,-4,-5]
#target = -8

#data = [ 3, 2, 4 ]
#target = 6

data = [ 3, 3 ]
target = 6


print( 'original data: {0}'.format( data ) )
print( 'target: {0}'.format( target ) )

a = []
s = Solution()

a = s.twoSum( data, target )
print( 'Solution: {0}'.format( a ) )


