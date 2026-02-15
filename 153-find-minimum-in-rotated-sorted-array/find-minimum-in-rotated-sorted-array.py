class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Minimum is in the right half
                left = mid + 1
            else:
                # Mid could be the minimum
                right = mid

        return nums[left]