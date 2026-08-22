class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _dict = {}

        for i in range(len(nums)):
            if nums[i] in _dict:
                _dict[nums[i]] += 1
            else:
                _dict[nums[i]] = 1

        if len(nums) == len(_dict.keys()):
            return False
        
        return True
        
            