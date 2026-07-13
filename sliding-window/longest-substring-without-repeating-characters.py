class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left =0
        n=len(s)
        freq ={}
        answer =0

        for right in range(n):
            freq[s[right]] = freq.get(s[right],0)+1

            while freq[s[right]] > 1:
                freq[s[left]]-=1
                left+=1
            answer = max(answer,right-left+1)
        return answer






        