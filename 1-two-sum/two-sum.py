class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if x not in prev_map:
                prev_map[nums[i]] = i
            else:
                return [i, prev_map[x]]
        