"""

Task 3 (30 pts): 
        We will extend the previous program to *two* particles. 
        Here, instead of initializing xpos = some value for one particle, 
        we initialize a list of x positions for two particles,  xpos_all= [xpos of particle 1, xpos of particle 2].
        Same with xvel, ypos, and yvel.

        1. Copy the entire block of the move() function from the previous task. This block will stay the same.
        2. Inside the t_range loop, replace the current contents with a loop over the particles, 
            so that the four lines can be simplified into two lines under this inner loop.
            Hint: list[0] and list[1] refers to the 1st and 2nd element of a list.
        3. Add xlabel "x position"
        4. Add ylabel "y position"
        
        Don't worry about the arguments you haven't seen before inside plt.plot();
        these are for coloring the trajectories so it's easier to tell the direction of time.
        
EXPECTED OUTCOME:   You should see the trajectories of two particles in a 2D box,
                    similar to the attached "3-sample.png" file.

"""

import matplotlib.pyplot as plt

# Setup simulation parameters
dt = 0.02
xbox = 1.0 # The upper bound of our box along x
ybox = 1.0 # The upper bound of our box along y

# Setup starting configuration of the system
xpos_all =[0.0, 1.0]  #initial x position of particle 1 and 2; same below
xvel_all=[1.0, -0.07] 
ypos_all =[0.0, 0.0]
yvel_all =[0.3, 0.09]


########################################################################
# Copy the entire block of move funtion from the previous task here.   #
# It will stay the same in this Task.                                  #
########################################################################

t_total = 250
t_range = range(t_total)

for t in t_range:
    xpos_all[0], xvel_all[0], ypos_all[0], yvel_all[0] = move(dt, xpos_all[0], xvel_all[0], xbox, ypos_all[0], yvel_all[0], ybox)
    xpos_all[1], xvel_all[1], ypos_all[1], yvel_all[1] = move(dt, xpos_all[1], xvel_all[1], xbox, ypos_all[1], yvel_all[1], ybox)
    plt.plot(xpos_all[0], ypos_all[0],  str(1-t/t_total) , marker='o' )
    plt.plot(xpos_all[1], ypos_all[1],  str(1-t/t_total) , marker='o')
    #replace the four lines above with 
    #for i in range(2):
        # action 1
        # action 2

plt.ylim(0,1)
plt.xlim(0,1)
plt.show()