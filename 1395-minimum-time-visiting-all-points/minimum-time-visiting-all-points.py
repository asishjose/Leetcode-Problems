class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        for i in range(len(points)-1):
            x = abs(points[i+1][0] - points[i][0])
            y = abs(points[i+1][1] - points[i][1])
            print(points[i])
            if x == y:
                seconds += x
            else:
                seconds = seconds + min(x,y) + abs(x-y)

        return seconds