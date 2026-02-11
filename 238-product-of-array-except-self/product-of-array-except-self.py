class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1] * len(nums)
        n = len(nums)
        for i in range(n-1):
            p = prefix[i]*nums[i]
            prefix.append(p)
        for i in range(n-1, 0, -1):
            s = suffix[i]*nums[i]
            suffix[i-1] = s
        answer = []
        for i in range(n):
            answer.append(prefix[i]*suffix[i])
        return answer