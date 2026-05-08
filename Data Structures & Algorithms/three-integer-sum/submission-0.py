class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if nums == [] or len(nums) < 3:
            return []

        nums = sorted(nums)
        total = 0
        tracker = []
        for i in range(len(nums) - 2):

            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                inter_sum = nums[i] + nums[j] + nums[k]
                if inter_sum == 0:
                    tracker.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                    


                elif inter_sum < 0:
                    j = j + 1
                else:
                    k = k - 1
        print(tracker)
        return tracker

            
        