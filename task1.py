"""
Exam 1 Take-Home Project

Suppose a particle starts out at an x position of xpos = 0, with an initial velocity towards the right at yvel=1.0. Everything is kept unitless for simplicity.
We want to simulate its movement starting from time t=0 as t increases.

We'll do this in discrete steps. After a short time of dt passes, the particle will move right by a tiny amount. 
By how much? Since xvel = d(xpos)/dt, the change in xpos will be xvel*dt. 
So in python we can write xpos = xpos + xvel*dt
After this time step, the state of xpos will be updated, the state of xvel will remain the same.
A move() function is provided below that achieves exactly this, advancing time by one small step.

We will advance time by taking one time step like this after another - like taking snapshots of the particles motion. 
This means we will call the move() function many times to continually update xpos and xvel.


TASK 1 (35 pts): 
    This program will perform a simulation of a single particle moving in one dimension inside a box. 
    The box limits the movement of the particle between 0 and 1, with hard reflecting walls. 

    If you run the following program, you'll see a a plot 
    showing that the particle's x position (vertical axis) increases with time (horizontal axis) 
    until it reachs the other end of the box at 1.

    1. Modify just the move() function so that if the particle hits a wall, its velocity will be reversed.
    2. Add xlabel "timestep"
    3. Add ylabel "x position"
 
EXPECTED OUTCOME: A figure plotting the x position of a single particle against time, showing that the particle bounces back,
                  similar to the attached "1-sample.png" file.

Parameters and variables
 
    dt: length of the timestep (in arbitrary units)
    xbox: size of box along the x axis (in arbitrary units)
    xpos: x component of particles positions (in arbitrary units)
    xvel: x component of particles velocities (in arbitrary units)
"""

import matplotlib.pyplot as plt

dt = 0.02 # This is our time step
xbox = 1.0 # The upper bound of our box

# Setup starting configuration of the system
xpos = 0.0 # we start with the particle at the origin
xvel = 1.0 # we start with some positive velocity along the x axis.

# The following is the function responsible of describing the motion of a particle during a short timestep
def move(dt,xpos,xvel,xbox):
    xpos = xpos + xvel*dt
    #if xpos ... 
        # do something to xvel
    return xpos, xvel

t_total = 80 #total timesteps we are simulating
t_range = range(t_total)

for t in t_range:
    xpos, xvel = move(dt, xpos, xvel, xbox)  #move the particle by advancing one timestep
    plt.plot(t, xpos, 'b.')  # plot a single blue dot at (t,xpos)
    #end of loop

#add xlabel and ylabel here
plt.ylim(0,1)
plt.show()
