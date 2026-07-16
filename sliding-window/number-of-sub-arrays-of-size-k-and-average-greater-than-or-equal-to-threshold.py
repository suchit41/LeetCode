class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left =0
        n=len(arr)
        answer =0
        count=0

        for right in range(n):
           count+=arr[right]
           if right - left+1 ==k:
            if count >= k*threshold:
                answer += 1
            count-=arr[left]
            left+=1
        return answer
        

