class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _dict = defaultdict(list)

        for i in strs:
            x = ''.join(sorted(i))
            _dict[x].append(i)
        return list(_dict.values())