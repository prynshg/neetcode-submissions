class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxLen=0
        freq={}
        maxFreq=0
        for r in range(len(s)):
            freq[s[r]]=1+freq.get(s[r],0)
            maxFreq=max(maxFreq,freq[s[r]])
            req=(r-l+1)-maxFreq
            if req>k:
                freq[s[l]]-=1
                l+=1
            else:
                maxLen=max(maxLen,r-l+1)

        return maxLen
