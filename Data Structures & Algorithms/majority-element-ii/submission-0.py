class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = int(len(nums) / 3)

        _dict = defaultdict(int)

        for i in nums:
            _dict[i] += 1

        return [k for k,v in _dict.items() if v > target]