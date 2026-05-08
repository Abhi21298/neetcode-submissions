class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## edge cases - none
        currMin = 1001 
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                currMin = min(currMin, nums[left])
                break

            mid = (left + right) // 2
            currMin = min(currMin, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return currMin


        