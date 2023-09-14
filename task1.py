"""

TASK 1 (35 pts):  Consider a single particle moving in two dimensions. 
        The 2D box limits the movement of the particle between 0 and 1 in both the x and y directions, 
        with hard reflecting walls on all sides. 
        1. Complete the following code to simulated motion in 2D.
           Careful of the number of variables entering as arguments and the variables returned, 
           as well as their ordering! 
           Use the move() function call in the for loop as your hint.
           
        2. Implement the reflecting walls: if the particle hits any of the four walls, it should bounce back.
        
        3. Add xlabel "x position [m]" and ylabel "y position [m]"
        
        4. Comment on the trajectory of the particle you see. Where did it start and end?
            How many times did it hit the walls?
 
EXPECTED OUTCOME:   Here we will plot xpos against ypos, 
                    so that we can show a trajectory of a particle moving and bouncing inside a 2D box.
                    You should see the particle hit the walls of the 2D box many times, 
                    similar to the attached "1-sample.png" file.
 
Parameters and variables

    dt: length of the timestep (in seconds)
    xbox: size of box along the x axis (in meters)
    xpos: x component of particles positions (in meters)
    xvel: x component of particles velocities (in meters/second)
    ybox: size of box along the y axis (in meters)
    ypos: y component of particles positions (in meters)
    yvel: y component of particles velocities (in meters/second)
"""
import matplotlib.pyplot as plt
import numpy as np

# Setup simulation parameters
dt = 0.02 
t_range = np.arange(0,5,dt)

xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos=0.0 # initial x position
xvel=1.0 # initial x velocity
ypos=0.0 # initial y position
yvel=0.3 # initial y velocity

def move(xpos,xvel): 
    xpos = xpos + xvel * dt
    return xpos, xvel

for t in t_range:
    xpos, xvel, ypos, yvel = move(xpos, xvel, ypos, yvel)
    

plt.ylim(0,1)
plt.xlim(0,1)
plt.show()