class Solution:
    def longestPalindrome(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            # set palindrome length
            P[i] = (R > i) and min(R - i, P[2 * C - i])

            # expand
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # move C and R
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        max_len, center_index = max((n, i) for i, n in enumerate(P))
        return s[(center_index - max_len) // 2: (center_index + max_len) // 2]