class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()

        if len(merge) % 2 == 0:
            return (merge[len(merge) // 2 - 1] + merge[len(merge) // 2]) / 2.0
        else:
            return merge[len(merge) // 2]