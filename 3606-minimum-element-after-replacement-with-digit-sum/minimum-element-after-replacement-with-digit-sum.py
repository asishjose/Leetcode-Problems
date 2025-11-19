class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
            sum = 0
            for n in nums[i]:
                sum += int(n)
            nums[i] = sum
        return min(nums)
        