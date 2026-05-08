class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if not word1 and not word2:
            return ""
        if not word1:
            return word2
        elif not word2:
            return word1

        x, y = len(word1), len(word2)
        res = []

        for idx in range(min(x, y)):
            res.extend([word1[idx], word2[idx]])
        
        if x != y:
            if x < y:
                res.append(word2[x:])
            else:
                res.append(word1[y:])

        return "".join(res)
        