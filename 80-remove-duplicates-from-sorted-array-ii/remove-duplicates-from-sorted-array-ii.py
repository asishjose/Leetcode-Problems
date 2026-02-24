class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums)-2:
            j=i+1
            if nums[i]==nums[j]:
                if nums[j]==nums[j+1]:
                    nums.remove(nums[j+1])
                else:
                    i=j+1
            else:
                i=j