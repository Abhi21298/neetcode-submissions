class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        length = len(s)
        if length < k:
            return k
        res = 0
        freq = 0
        l = 0

        track = {}

        for r in range(length):
            track[s[r]] = track.get(s[r], 0) + 1
            freq = max(freq, track[s[r]])

            while (r - l + 1) - freq > k:
                track[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            

        return r - l + 1