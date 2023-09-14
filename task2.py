"""
Task 2 (35 pts): 
        We will extend the previous program to *two* particles. 
        Here, instead of initializing xpos = some value for one particle, 
        we initialize a list of x positions for two particles,  xpos_all= [xpos of particle 1, xpos of particle 2].
        Same with xvel, ypos, and yvel.

        1. Copy the entire block of the move() function from the previous task. This block will stay the same.
        
        2. Complete the rest of the code to implement refective walls. Inspect your plot to make sure the code works.
        
        3. Reconstruct the two t_range loops to simplify them, by adding another layer of loop over the particles.
        
        Hint: One way to do this is (note the indentation)
            
        for i in range(2):
            #initialize empty lists to contain positions
            for t in t_range:
                # update positions and velocities of particle i
                # append xpos to a list and ypos to a list
            # make plots using these lists
           
        4. Add xlabel "x position [m]" and ylabel "y position [m]"
        
        
EXPECTED OUTCOME:   You should see the trajectories of two particles in a 2D box,
                    similar to the attached "2-sample.png" file.

"""

import matplotlib.pyplot as plt
import numpy as np

# Setup simulation parameters
dt = 0.02
t_range = np.arange(0,5,dt)

xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos_all =[0.0, 1.0]  #initial x position of particle 1 and 2; same below
xvel_all= [1.0, -0.07] 
ypos_all =[0.0, 0.0]
yvel_all =[0.3, 0.09]


########################################################################
# Copy the entire block of move funtion from the previous task here.   #
# It will stay the same in this Task.                                  #
########################################################################

for t in t_range:
    xpos_all[0], xvel_all[0], ypos_all[0], yvel_all[0] = move( xpos_all[0], xvel_all[0], ypos_all[0], yvel_all[0])
    #some appending here 
#plot for particle 1 here    
    
for t in t_range:    
    xpos_all[1], xvel_all[1], ypos_all[1], yvel_all[1] = move( xpos_all[1], xvel_all[1], ypos_all[1], yvel_all[1])
    #some appending here 
#plot for particle 2 here    

plt.ylim(0,1)
plt.xlim(0,1)
plt.show()