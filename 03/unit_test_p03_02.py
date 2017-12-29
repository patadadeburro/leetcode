'''
------------------------------------------------------------------------------------
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



------------------------------------------------------------------------------------
'''

import p03_02

class test_case:
    desc     = ''
    a_string = ''
    len      = 3
    expected = ''
# ------------------------------------------------------------------------------------

test_cases = []

t = test_case()
t.desc     = 'example 1.'
t.a_string = 'abcabcbb'
t.bigest   = 'abc'
t.expected = 3
test_cases.append(t)

t = test_case()
t.desc     = 'example 2.'
t.a_string = 'bbbbb'
t.bigest   = 'b'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 3.'
t.a_string = 'pwwkew'
t.bigest   = 'wke'
t.expected = 3
test_cases.append(t)

t = test_case()
t.desc     = 'example 4.'
t.a_string = 'c'
t.bigest   = 'c'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 5.'
t.a_string = 'au'
t.bigest   = 'au'
t.expected = 2
test_cases.append(t)

t = test_case()
t.desc     = 'example 6.'
t.a_string = 'aa'
t.bigest   = 'aa'
t.expected = 1
test_cases.append(t)

t = test_case()
t.desc     = 'example 7.'
t.a_string = 'aab'
t.bigest   = 'a'
t.expected = 2
test_cases.append(t)

t = test_case()
t.desc     = 'example 8.'
t.a_string = 'pwwkew'
t.bigest   = 'wke'
t.expected = 3
test_cases.append(t)

t = test_case()
t.desc     = 'example 9.'
t.a_string = 'nfpdmpi'
t.bigest   = 'nfpdm'
t.expected = 5
test_cases.append(t)

t = test_case()
t.desc     = 'example 10.'
t.a_string = 'ckilbkd'
t.bigest   = 'ckilb'
t.expected = 5
test_cases.append(t)

# ------------------------------------------------------------------------------------
r = 0
s = p03_02.Solution()
print('-' * 69)

print( 'desc       input             expected  result  passed')
print( '---------- ----------------- -------- -------- ------')

for i in test_cases:
    r =  s.lengthOfLongestSubstring( i.a_string )
    print( '{: <12} {: >15} {: >4} {: >8} {:>8}'
            .format(i.desc, i.a_string, i.expected, r, str(i.expected == r) ))
