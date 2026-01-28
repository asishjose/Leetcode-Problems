class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diffs = dict()
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff not in diffs:
                diffs[diff] = [[arr[i], arr[i+1]]]
            else:
                diffs[diff].append([arr[i], arr[i+1]])
        min_diff = min(diffs.keys())
        return diffs[min_diff]