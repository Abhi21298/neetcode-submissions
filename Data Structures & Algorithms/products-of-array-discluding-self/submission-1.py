class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        L = len(nums)
        res = [1]*L
        pre = 1
        for i in range(L):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(L-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res

        