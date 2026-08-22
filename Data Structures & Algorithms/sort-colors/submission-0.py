class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j =0,len(nums) - 1
        point = 0
        while point <= j:
            if nums[point] == 0:
                nums[i],nums[point] = nums[point],nums[i]
                i += 1
                point += 1
            
            elif nums[point] == 2:
                nums[point],nums[j] = nums[j],nums[point]
                j -= 1
            else:
                point += 1
        return nums

