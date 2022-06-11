from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    
    def minOperations(self, nums: List[int], x: int) -> int:
        result = int(1e9)
        
        psumA = self.getPsum(nums)
        psumB = self.getPsum(nums[::-1])
        
        result = min(result, self.getResult(psumA, psumB, x))
        result = min(result, self.getResult(psumB, psumA, x))
            
        return result if result != int(1e9) else -1

    def getResult(self, source: List[int], dest: List[int], x: int) -> int:
        result = int(1e9)
        for idx, i in enumerate(source):
            if x - i == 0:
                result = min(result, idx + 1)
            if x - i < 0:
                break
                
            findIdx = self.getIdx(dest, x - i)
            if findIdx and findIdx + idx + 1 <= len(source):
                result = min(result, idx + 1 + findIdx)
        return result

    def getPsum(self, lst: List[int]) -> List[int]:
        psum = []
        value = 0
        for i in lst:
            value += i
            psum.append(value)
        
        return psum
        
    def getIdx(self, lst: List[int], x: int) -> int:
        r = bisect_right(lst, x)
        l = bisect_left(lst, x)
        
        return l + 1 if r - l else 0
