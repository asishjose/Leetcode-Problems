class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = 0
        min_diff = float('inf')
        for i in range(len(nums)-k+1):
            print(nums[i], nums[i+k-1])
            diff = nums[i+k-1] - nums[i]
            min_diff = min(min_diff, diff)
        return min_diff