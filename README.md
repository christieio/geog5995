# geog5995
 GEOG5995 Online Portfolio

What the code does:
The python files show the development of a model through the practicals 1-9. 
each agentframework5-9.py file corresponds to its matching prac5-9.py file. 
At the top of the code, all modules required for the code to run properly are imported. The random seed is also set at the top of the code in order for the same output to be produced each time the code is ran. 
The code creates ten sets of agents that represent co-ordinates. These co-ordinates can be visualised at points on the plot that is produced in the output. The plot is created using functions from the various imported matplotlib modules. The agents are caused to move using a "move" function that consists of for-loops that change the values of the y and x coordinate. Incorporated in the model is code within the "move" function that ensures the points do not move off the axis of the plot. The agents are able to communicate with eachother and move around an arbitary amount of times according to the number of iterations set. The code also 'eats' using an "eat" function that nibbles away at the environment. This allows a visual representation of the movement of the agents to be seen on the plot. 

The code is split between two .py files: agentframework and the main model. The agentframework body of code stores the functions created under the "Agent" class. The main model file can then communicate with this agentframework file, calling on the functions defined within the "Agent" class. 

What to expect when the model is ran:
When the code is ran, a pop-up window titled 'model' should appear. On clicking the 'model' tab at the top of the pop up window, a drop down menu should appear with the option to 'run model'. When 'run model' is clicked, a raster graph should appear with ten points overlayed on top. These ten points should move around on the plot. You should be able to see a trail showing the movement of the points. 

Evidence of tests and timing:
prac4-7 show evidence of timing the execution of the code. This is done by importing the "time" module and using the "time" function at the beginning and end of the code. 
prac1 shows evidence of testing the code for returning the value for the pythagorean distance. This can be seen at the bottom of the code. 
prac6-7 show evidence of testing whether storing the txt file has been successful, using the following code:
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
This code tests the model by showing a plot; if a raster graph can be seen then the code has worked correctly. 
