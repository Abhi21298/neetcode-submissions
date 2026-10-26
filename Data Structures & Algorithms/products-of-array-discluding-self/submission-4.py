class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        L = len(nums)
        result = [1] * L

        pre = 1
        for i in range(L):
            result[i] = pre
            pre *= nums[i]
        
        post = 1
        for i in range(L - 1, -1, -1):
            result[i] *= post
            post *= nums[i]
        
        return result

