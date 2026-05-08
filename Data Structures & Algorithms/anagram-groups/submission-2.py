class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        if not strs or len(strs) == 0:
            return []

        track = {}
        for element in strs:
            key = [0] * 26

            for ch in element:
                key[ord(str(ch)) - ord('a')] += 1
            
            track[tuple(key)] = track.get(tuple(key) , []) + [element]

        res = list()
        for item in track.keys():
            res.append(track[item])
        
        return res


        
        