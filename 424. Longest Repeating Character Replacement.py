class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        maxf = 0
        res = 0
        count = {}

        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end],0)
            maxf = max(maxf,count[s[end]])

            while (end-start+1) -maxf > k:
                count[s[start]]-=1
                start+=1
            res = max(res,end-start+1)
        return res
