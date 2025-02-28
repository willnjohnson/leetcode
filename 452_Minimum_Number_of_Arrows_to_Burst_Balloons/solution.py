class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: # No balloons == no nArrows required
            return 0
        
        # Sort the balloons by end points for better arrow placement
        points.sort(key=lambda x: x[1])
        
        # Initialize number of nArrows
        # Initialize position of the first shot
        nArrows, last = 1, points[0][1]
        
        for start, end in points[1:]:
            if start > last:
                nArrows += 1 # Shoot new arrow if curr balloon starts after last shot
                last = end  # Update last arrow's position to current end
        
        return nArrows  # Return the total number of arrows required