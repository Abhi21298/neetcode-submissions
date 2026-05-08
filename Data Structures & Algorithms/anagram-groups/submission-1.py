class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        track = {}

        for s in strs:

            idx = [0]*26
            for ch in s:
                idx[ord(ch) - ord('a')] += 1
            
            track[tuple(idx)] = track.get(tuple(idx), []) + [s]
        
        for key in track:
            res.append(track[key])
        
        return res