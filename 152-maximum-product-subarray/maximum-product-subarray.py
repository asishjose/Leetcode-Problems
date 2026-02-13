class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxi , mini = 1,1

        for n in nums:
            posmax = maxi * n
            negmax = mini * n
            
            maxi = max(posmax, negmax, n)
            mini = min(posmax, negmax, n)

            res = max(maxi, res)
        return res