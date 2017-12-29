import p04

class test_case:
    desc     = ''
    nums1    = []
    nums2    = []
    expected = 0
# ------------------------------------------------------------------------------------

test_cases = []

t = test_case()
t.desc     = 'example 1.'
t.nums1    = [1, 3]
t.nums2    = [2]
t.expected = 2.0
test_cases.append(t)

t = test_case()
t.desc     = 'example 2.'
t.nums1    = [1, 2]
t.nums2    = [3, 4]
t.expected = 2.5
test_cases.append(t)



# ------------------------------------------------------------------------------------
r = 0
s = p04.Solution()
print('-' * 69)

print( 'desc           nums1    nums2    expected  result  passed')
print( '----------     ------- --------- -------- -------- ------')

for i in test_cases:
    r =  s.findMedianSortedArrays( i.nums1, i.nums2 )
    print( '{: <12} {: >9} {:>9} {: >6} {: >8} {:>8}'
            .format(i.desc, str(i.nums1), str(i.nums2), i.expected, r, str(i.expected == r) ))
