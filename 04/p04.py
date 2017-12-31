'''
Description: 4. Median of Two Sorted Arrays
	There are two sorted arrays nums1 and nums2 of size m and n respectively.

	Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

	Example 1:
	nums1 = [1, 3]
	nums2 = [2]
	The median is 2.0

	Example 2:
	nums1 = [1, 2]
	nums2 = [3, 4]

	The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a    = sorted( nums1 + nums2 )
        size = len( a )
        r    = size % 2
        if r == 1:
            i = (size // 2)
            m = 1.0 * a[ i ]
        else:
            i = (size // 2)
            m = (a[i] + a[ i -1] ) / 2.0

        return m



s = Solution()

#nums1 = [1, 3]
#nums2 = [2]

nums1 = [1, 2]
nums2 = [3, 4]
m = s.findMedianSortedArrays( nums1, nums2 )

print ( 'median: {}'.format( m ) )