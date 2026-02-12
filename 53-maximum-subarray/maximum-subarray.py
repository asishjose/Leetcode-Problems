class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currSum = 0
        maxSum = nums[0]
        for i in range(n):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum