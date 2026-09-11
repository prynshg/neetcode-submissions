class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for i in s:
            freq[i]=1+freq.get(i,0)
        for j in t:
            freq[j] = freq.get(j, 0) - 1

        return all(value == 0 for value in freq.values())