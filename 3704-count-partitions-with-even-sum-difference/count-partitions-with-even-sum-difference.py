class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        partitions = 0
        for i in range(len(nums)-1):
            sum1 = sum(nums[:i+1])
            sum2 = sum(nums[i+1:])
            diff = sum2 - sum1
            if diff % 2 == 0:
                partitions += 1
        return partitions
                