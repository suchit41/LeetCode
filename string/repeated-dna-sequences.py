class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left =0
        n = len(s)
        seen = set()
        result = set()

        for right in range(n):

            if right -left+1==10:
                substring = s[left:right+1]
                if substring in seen:
                    result.add(substring)
                else:
                    seen.add(substring)
                left += 1
        return list(result)

        