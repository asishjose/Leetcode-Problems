class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])/k
        max_avg = avg
        for i in range(k, len(nums)):
            avg = avg - (nums[i-k]/k) + (nums[i]/k)
            max_avg = max(avg, max_avg)
        return max_avg
