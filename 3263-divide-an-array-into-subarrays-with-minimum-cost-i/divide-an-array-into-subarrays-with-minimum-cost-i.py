class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        fnum = nums[0]
        nums.pop(0)
        nums.sort()
        return nums[0]+nums[1]+fnum
