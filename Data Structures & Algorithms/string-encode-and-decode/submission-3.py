class Solution:
    def encode(self, strs: List[str]) -> str:
        _sizes = []
        if strs is None:
            return ""
        for i in range(len(strs)):
            _sizes.append(f'{len(strs[i])}#{strs[i]}')
        return ''.join(_sizes)
    
    def decode(self, s: str) -> List[str]:
        res = []
        if s is None:
            return []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res

