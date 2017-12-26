'''
-------------------------------------------------------------------------------
Description:

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

references:
    leetcode.com
    algorithms
    02
------------------------------------------------------------------------------- '''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def number_2_linked_list(self, num ):
        first    = None
        previous = None
        n = num

        if num == 0:
            node = ListNode( 0 )
            return  node

        while n > 0:
            r        = n % 10
            n        = n // 10
            node     = ListNode( r )
            node.val = r
            #print( 'r: {}'.format( r ) )

            if first == None:
                first = node
            else:
                previous.next = node

            previous = node
        return first

    def linked_list_2_number( self, first ):
        node = first
        num = 0
        i = 0
        while node != None:
            #print( 'node.val: {} '.format( node.val ) )
            num = (node.val * 10 ** i) + num
            node = node.next
            i += 1
        return num


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = self.linked_list_2_number( l1 )
        n2 = self.linked_list_2_number( l2 )
        n  = n1 + n2
        result = self.number_2_linked_list( n )
        return result


# -------------------------------------------------------------------------------
# test
'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

'''
s  = Solution()
#l1 = s.number_2_linked_list( 12345 )
#n  = s.linked_list_2_number( l1 )
#print( 'n: {}'.format( n ) )

'''
[2,4,3]
[5,6,4]
'''

#l1 = s.number_2_linked_list( 342 )
#l2 = s.number_2_linked_list( 465 )

l1 = s.number_2_linked_list( 0 )
l2 = s.number_2_linked_list( 0 )


r  = s.addTwoNumbers( l1, l2 )
n  = s.linked_list_2_number( r )
print( 'Solution: {}'.format( n ) )



# -------------------------------------------------------------------------------
