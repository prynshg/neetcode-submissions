class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for ch in strs:
            key=tuple(sorted(ch))
            res[key].append(ch)

        return list(res.values())