class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def countOnes(num):
            count = 0
            for i in range(7, -1 ,-1):
                
                if num & (1 << i):
                    count += 1
                else:
                    break
            return count
        count = 0
        for d in data:
            if not count:
                count = countOnes(d)
                
                if count == 0:
                    continue
                if count == 1 or count > 4:
                    return False
                count -= 1
            else:
                count -= 1
                if countOnes(d) != 1:
                    return False
        return count == 0
        
        