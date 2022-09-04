class Solution(object):
    def findMedianSortedArrays( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=nums1+nums2
        nums1.sort()
        l=len(nums1)%2
        if len(nums1)<2:
            
            return nums1[0]
        elif l==0:
            print(int(len(nums1)/2)-1,int(len(nums1)/2))
            print((float(nums1[int(len(nums1)/2)-1])+float(nums1[int(len(nums1)/2)]))/2)
            return (float(nums1[int(len(nums1)/2)-1])+float(nums1[int(len(nums1)/2)]))/2
        elif l==1:
            print(nums1[int(len(nums1)/2)])
            return nums1[int(len(nums1)/2)]

s=Solution
s.findMedianSortedArrays([],[1,2,3,4,5])