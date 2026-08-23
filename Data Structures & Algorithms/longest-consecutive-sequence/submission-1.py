class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = list(sorted(set(nums)))
        max_cnt,_cnt = 1,1
        if not nums:
            return 0
        for i in range(1,len(x)):
            if x[i] == x[i-1] + 1:
                _cnt += 1
            else:
                _cnt = 1
            max_cnt = max(max_cnt,_cnt)
        return max_cnt