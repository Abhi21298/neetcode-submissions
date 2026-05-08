class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        nums.sort()
        res = []
        for i in range(0, l - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, l - 1

            while j < k:

                inter_sum = nums[i] + nums[j] + nums[k]
                if inter_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                
                elif inter_sum < 0:
                    j += 1
                else:
                    k -= 1
            
        return res
                    

        