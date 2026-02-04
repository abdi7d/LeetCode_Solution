class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        # Sort balloons by their ending coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points:
            # If the current balloon starts after the last arrow position
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows
