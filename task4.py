"""
Task 4 (5 pts): We will extend the previous program to an arbitrary number of particles. 
                
    1. Copy everything in task 3 here, and replace the initial setup block with the block of code below. 
    Here you'll encounter a new function, np.random.uniform(a,b), which creates a random number between a an b.
    You'll won't need to modify this block.
                
    2. Comment on what this block is trying to achieve.
                
    3. Modify your final t_range block to extend the simulation to 10 particles. 
    Your trajectory plot will probably gets quite messy. Decrease the total simluation time steps from 250 to 20 
    to visualize just a short time after the simulation started.
                
    4. Make sure xlabel is "x position" and ylabel is "y position"
                
EXPECTED OUTCOME: A trajectory plot of 10 particles similar to the attached "4-sample.png" file.

"""


# Setup starting configuration of the system
import numpy as np
nparticles = 10 # for this assignment we only consider one particle 
xpos_all =[np.random.uniform(0, xbox)  for i in range(nparticles)  ] 
xvel_all= [np.random.uniform(-1,1   )  for i in range(nparticles)  ] 
ypos_all =[np.random.uniform(0, ybox)  for i in range(nparticles)  ]
yvel_all =[np.random.uniform(-1,1   )  for i in range(nparticles)  ] 


