class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        track = defaultdict(list)       
        for s in strs:

            key = [0]*26

            for ch in s:
                ch = ch.lower()
                key[ord(ch) - ord('a')] += 1
            
            track[tuple(key)].append(s)

        return list(track.values())

        
        