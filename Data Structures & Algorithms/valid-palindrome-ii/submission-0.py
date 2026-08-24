class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                SkipL = s[l+1:r+1]
                SkipR = s[l:r]
                return SkipL == SkipL[::-1] or SkipR == SkipR[::-1]
            l += 1
            r -= 1
        return True