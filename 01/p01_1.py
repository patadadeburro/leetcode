'''
-------------------------------------------------------------------------------
Description:

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Author: Arturo Alatriste Trujillo.
------------------------------------------------------------------------------- '''

def twoSum( a, target ):
    found        = False
    i            = 0
    j            = 0
    num_elements = len( a )

    for i in range(0, num_elements ):
        for j in range( i+1, num_elements ):
            s = a[ i ] + a[ j ]
            if s == target:
                found = True
                break

        if found == True:
            break

    if found == True:
        print( 'The solution is' )
        print( 'i   : {0}, j   : {1}'.format( i, j ) )
        print( 'a[ {0} ]: {1}, a[ {2} ]: {3}'.format( i, a[i], j, a[j] ) )
    else:
        print( 'This array does not have solution' )


    return [ i, j ]

# -------------------------------------------------------------------------------
# test
# -------------------------------------------------------------------------------

#data   = [ 15, 11, 7,  2 ]
#target = 9
#found  = False

data = [-1,-2,-3,-4,-5]
target = -8

print( 'original data: {0}'.format( data ) )
print( 'target: {0}'.format( target ) )

a = []
a = twoSum( data, target )
print( 'a: {0}'.format( a ) )


