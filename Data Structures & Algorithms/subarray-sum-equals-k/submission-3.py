class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currsum = 0
        prefix_sum = {0:1}

        for num in nums:
            currsum += num
            diff = currsum - k

            res += prefix_sum.get(diff,0)
            prefix_sum[currsum] = 1 + prefix_sum.get(currsum,0)
        return res