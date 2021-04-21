class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        last = None
        mid = (len(nums1) + len(nums2))/2.0
        n1 = 0
        n2 = 0
        c = 0
        while n1 < len(nums1) or n2 < len(nums2):
            if n1 < len(nums1):
                one = nums1[n1]
            else:
                one = None
            if n2 < len(nums2):
                two = nums2[n2]
            else:
                two = None
            if one != None and two != None:
                if one < two:
                    n1 += 1
                    curr = one
                    c += 1
                else:
                    n2 += 1
                    curr = two
                    c += 1
            elif one != None:
                n1 += 1
                curr = one
                c += 1
            else:
                n2 += 1
                curr = two
                c += 1
            if c == mid+1:
                return (curr + last)/2.0
            if c > mid:
                return float(curr)
            last = curr