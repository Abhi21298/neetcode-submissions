class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []

        arr.sort(key = lambda z: (abs(z - x), z), reverse = False)

        if k >= len(arr):
            return sorted(arr)
        
        return sorted(arr[:k])