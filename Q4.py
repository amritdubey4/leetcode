# LeetCode 4. Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i
            if i < m and j > 0 and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = B[j - 1]
                elif j == 0:
                    left_max = A[i - 1]
                else:
                    left_max = max(A[i - 1], B[j - 1])
                if (m + n) % 2 == 1:
                    return float(left_max)
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                return (left_max + right_min) / 2.0
