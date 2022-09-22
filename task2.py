"""

TASK 2 (30 pts):  In this task, we will still consider a single particle but now moving in two dimensions. 
        The 2D box limits the movement of the particle between 0 and 1 in both the x and y directions, 
        with hard reflecting walls on all sides. 
        1. Modify just the move() function so that if the particle hits a wall, its velocity will be reversed.
            Use line 58 (where the move function is called) as your hint.
            Careful of the number of variables entering as arguments and the variables returned, as well as their ordering! 
        2. Add xlabel "x position"
        3. Add ylabel "y position"
        4. Comment on the trajectory of the particle you see. Where did it start and end?
            How many times did it hit the walls?
 
EXPECTED OUTCOME:   Instead of plotting xpos against timestep, here we will plot xpos against ypos, 
                    so that we can show a trajectory of a particle moving and bouncing inside a 2D box.
                    You should see the particle hit the walls of the 2D box many times, 
                    similar to the attached "2-sample.png" file.

Parameters and variables
 
    dt: lenght of the timestep (in arbitrary units)
    xbox: size of box along the x axis (in arbitrary units)
    xpos: x component of particles positions (in arbitrary units)
    xvel: x component of particles velocities (in arbitrary units)
    ybox: size of box along the y axis (in arbitrary units)
    ypos: y component of particles positions (in arbitrary units)
    yvel: y component of particles velocities (in arbitrary units)
    
"""
import matplotlib.pyplot as plt

# Setup simulation parameters
dt = 0.02 
xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos=0.0 # the particle's initial x position
xvel=1.0 # the particle's initial x velocity
ypos=0.0 # the particle's initial y position
yvel=0.3 # the particle's initial y velocity

def move(dt,xpos,xvel,xbox): #you need to add three more arguments here for y
    
    xpos = xpos + dt*xvel
    ypos = #... you need to update ypos
    
    #if xpos ... 
        # do something to xvel
    #if ypos ... 
        # do something to yvel
        
    return xpos, xvel # you need to return two xpos and xvel here

t_total = 250
t_range = range(t_total)

for t in t_range:
    xpos, xvel, ypos, yvel = move(dt, xpos, xvel, xbox, ypos, yvel, ybox)
    plt.plot(xpos, ypos, 'b.')  # plot a single dot at (xpos, ypos)
    

plt.ylim(0,1)
plt.xlim(0,1)
plt.show()