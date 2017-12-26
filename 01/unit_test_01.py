import p01_3 as p01

class test_case:
    desc      = ''
    nums      = ''
    target    = ''
    expected  = []
# ------------------------------------------------------------------------------------

test_cases = []

t = test_case()
t.desc      = 'example 1.'
t.nums      = [ 15, 11, 7,  2 ]
t.target    = 9
t.expected  = [ 2, 3 ]
test_cases.append(t)

t = test_case()
t.desc      = 'example 2.'
t.nums      = [ -1, -2, -3, -4, -5 ]
t.target    = -8
t.expected  = [ 2, 4 ]
test_cases.append(t)

t = test_case()
t.desc      = 'example 3.'
t.nums      = [ 3, 2, 4 ]
t.target    = 6
t.expected  = [ 1, 2 ]
test_cases.append(t)


t = test_case()
t.desc      = 'example 4.'
t.nums      = [ 3, 3 ]
t.target    = 6
t.expected  = [ 0, 1 ]
test_cases.append(t)

# ------------------------------------------------------------------------------------

s = p01.Solution()

for i in test_cases:
    #print( '{} \t{} \t{}'.format( i.desc, i.inputList, i.output ) )
    r = 0
    print( '-' * 69 )
    print( i.desc )
    print( 'nums     = {}'.format( i.nums     ) )
    print( 'target   = {}'.format( i.target   ) )
    print( 'expected = {}'.format( i.expected ) )
    r =  s.twoSum ( i.nums, i.target )
    print( 'result   = {}'.format( r ))
    if i.expected == r:
        print( 'passed: \t\t\t Correct!' )
    else:
        print( 'passed: \t\t\t wrong' )
