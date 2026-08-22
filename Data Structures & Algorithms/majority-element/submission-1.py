from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return next(iter(dict(sorted(Counter(nums).items(), key=lambda item: item[1], reverse=True))))
    
        