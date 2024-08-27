"""
Problem Statement
You are given the positions and speeds of n people. All the people are currently at different positions and moving at different speeds. 
You want to get all the people together at the same position. You can choose any position and all the people will move towards that position with their respective speeds.
You want to know the minimum time needed to get all the people together.
"""
def solve():
    # Read the number of people
    n = int(input())
    position_speed = []
    
    # Read the position and speed for each person
    for _ in range(n):
        position, speed = map(int, input().split())
        position_speed.append([position, speed])
    
    # Helper function to determine if everyone can meet at a single point in 'mid' time
    def can_meet(mid):
        # Initialize the allowable range for meeting at a point
        meeting_range = [float("-inf"), float("inf")]
        
        for pos, spd in position_speed:
            # Calculate the new range each person can reach in 'mid' time
            current_range = [pos - mid * spd, pos + mid * spd]
            
            # Check if the current range overlaps with the previous meeting range
            if not (current_range[0] <= meeting_range[1] and current_range[1] >= meeting_range[0]):
                return False
            
            # Update the meeting range to the intersection of the current and previous ranges
            meeting_range = [max(current_range[0], meeting_range[0]), min(current_range[1], meeting_range[1])]
        
        return True
    
    # Binary search to find the minimum time needed
    left = 0
    right = 10**9
    minimum_time = right
    
    for _ in range(55):  # Perform a binary search with fixed iterations
        mid = left + (right - left) / 2
        if can_meet(mid):
            minimum_time = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return minimum_time

# Execute the solve function and print the result
print(solve())
