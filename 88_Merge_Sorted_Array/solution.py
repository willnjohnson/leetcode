class Solution:
    def merge(self, nums1, m, nums2, n):
        # Initialize bookkeeping "pointers":
        # 'i' is the pointer for the last valid element in nums1 (before the trailing zeros).
        # 'j' is the pointer for the last element in nums2.
        # 'k' is the pointer for the last position in nums1 (where the merged result will be placed).
        i, j, k = m - 1, n - 1, m + n - 1
        
        # Merge nums1 and nums2 from the back to the front
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If there are any remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
