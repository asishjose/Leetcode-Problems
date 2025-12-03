class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map = dict()
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        
        max_val = max(map.values())
        keys_with_max = [k for k,v in map.items() if v==max_val]

        res = 0
        for k in keys_with_max:
            res += map[k]
        
        return res