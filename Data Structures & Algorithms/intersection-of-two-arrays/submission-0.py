class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = set(nums1)
        
        res = []
        for element in nums1:
            if element in nums2:
                res.append(element)

        return res
        