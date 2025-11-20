class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))

        chosen_points = []
        secondLast = float('-inf')
        last = float('-inf')

        for a,b in intervals:
            if a <= secondLast:
                continue
            elif a <= last:
                chosen_points.append(b)
                secondLast = last
                last = b
            else:
                chosen_points.extend([b-1, b])
                secondLast = b-1
                last = b

        return len(chosen_points)