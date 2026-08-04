# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteroid in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, 
# and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:

# Input: asteroids = [3,5,-6,2,-1,4]​​​​​​​
# Output: [-6,2,4]
# Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 destroys -1. Since 2 and 4 are both moving right, they never collide.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0


class Solution:
    # Day-0: 04/Aug/2026
    # Recognition Pattern: Objects move in opposite directions and may repeatedly interact with the most recent surviving object. 
    # Pattern: Stack + Simulation
    # Intuition:
        # The stack stores asteroids that have survived all collisions so far.
        # A collision is possible only when:
        #     stack top is moving right (> 0)
        #     current asteroid is moving left (< 0)
        # The current asteroid may collide repeatedly:
        # 1. Current is larger:
        #       pop the stack top and continue.
        # 2. Equal size:
        #       pop the stack top; current also explodes.
        # 3. Stack top is larger:
        #       current explodes.
        # If the current asteroid survives all possible collisions,
        # push it onto the stack.
    # TC = O(n)
    # SC = O(n)
    # Mistakes Made:
        # None
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        collisions = []

        for asteroid in asteroids:
            add_asteroid = True

            while collisions and (collisions[-1]>=0 and asteroid<0):
                if collisions[-1] <= abs(asteroid):
                    popped_asteroid = collisions.pop()
                    if popped_asteroid == abs(asteroid):
                        add_asteroid = False
                        break
                else:
                    add_asteroid = False
                    break

            if add_asteroid:
                collisions.append(asteroid)

        return collisions
        
o = Solution()
asteroids = [3,5,-6,2,-1,4]
# asteroids = [5,10,-5]
# asteroids = [10,2,-5]
# asteroids = [8,-8]
# asteroids = [-2,-2,1,-2]
# asteroids = [-2,1,1,-1]
asteroids = [-2,1,-1,-2]
print(o.asteroidCollision(asteroids))
