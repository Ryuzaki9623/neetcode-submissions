class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]

        for i in range(len(strs[0])):
            char = first_word[i]

            for j in strs[1:]:
                if i == len(j) or j[i] != char:
                    return first_word[:i]
        return first_word
        

