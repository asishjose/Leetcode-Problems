class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        nums.append(nums[-1]+2)
        arr = []
        lr,hr = nums[0],nums[0]
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                hr = nums[i+1]
            else:
                if hr <= lr:
                    arr.append(f'{lr}')
                    lr = nums[i+1]
                else:
                    arr.append(f'{lr}->{hr}')
                    lr = nums[i+1]
        return arr