class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        runningSum = [0]*(n+1)
        for i in range(n):
            runningSum[i+1] = runningSum[i] + nums[i]
        runningSum.pop(0)
        return runningSum