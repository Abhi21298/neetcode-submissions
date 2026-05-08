class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        tracker = {}
        long_window = 0
        window_start = 0
        for window_end in range(len(s)):
            while s[window_end] in tracker:
                tracker.pop(s[window_start])
                window_start += 1
            tracker[s[window_end]] = window_end
            long_window = max(long_window, window_end - window_start + 1)
        
        return long_window


            
        