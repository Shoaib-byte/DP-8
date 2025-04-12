#time complexit o(nlogn)
#space complexity o(n)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0],-x[1]))

        arr = [0] * n
        arr[0] = envelopes[0][1]
        le = 1
        for i in range(1,n):
            if arr[le-1] < envelopes[i][1]:
                arr[le] = envelopes[i][1]
                le += 1
            else:
                bsIdx = self.binarysearch(arr,0,le-1,envelopes[i][1])
                arr[bsIdx] = envelopes[i][1]
        
        return le


        

    
    def binarysearch(self,arr: List[int],low: int, high: int, target:int):

        while low <= high:
            mid = low + (high - low)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        return low 