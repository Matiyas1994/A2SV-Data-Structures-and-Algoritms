class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        #tp = sorted(map(int, p.split(':')) for p in timePoints)
        tp= sorted(map(int,p.split(":")) for p in timePoints)
        tp += [[tp[0][0] + 24, tp[0][1]]]
        return min((tp[x+1][0] - tp[x][0]) * 60 + tp[x+1][1] - tp[x][1] \
                   for x in range(len(tp) - 1))
