# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:31:11 2021

@author: Christie
"""

#import matplotlib.pyplot to create visualisations (plot)
import matplotlib.pyplot
#import operator module to access efficient functions
import operator
#import random module to access random functions
import random

#creation of ten agents
#assign the value "10" to the label "num_of_agents"
num_of_agents = 10

#creation of number of iterations 
#assign the value "100" to the label "num_of_iterations"
num_of_iterations = 100

#create an empty list an assign it to the label "agents"
agents = [] 

#assign values to height and width to prevent agents from going off the map
#assign the value "100" to label "height" and "width"
height = 100
width = 100

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0) 


#create an arbitary number of agents using a 'for-loop'

#make the agents
#assigning a random number to coordinates y and x
#for the range of number of agents (10)
for i in range(num_of_agents):
    #assign random number within the defined height and range
     agents.append([random.randint(0, height-1),random.randint(0, width-1)])
#print values for coordinates y and x     
print ("agents", agents) 
#number of agents is defined as "10" so output shows 10 sets of coordinates
  
#neaten the output up
#print agents
print(agents)
#in the range of the length of the list of agents 
for i in range(len(agents)):
    #print values for agents[i]
    print("agents [i]", agents[i]) 
    #prints 10 agents as there is 10 in the range/list

#move agents arbitary number times using num_of_iterations
#for the number of iterations
for j in range(num_of_iterations):
    #print the number of iteration
    print("iteration", j) 
    #for the range of number of agents (10)
    for i in range(num_of_agents): 
        #move y coordinate
        #assign random number
        random_number = random.random() 
        #if this random number is less than 0.5 then:
        if random_number < 0.5: 
            #add "1" to the valueof agents[i][0] ((% height (y axis) to \
            #stop moving off the map))
            agents[i][0] = (agents[i][0] + 1) % height 
        #if random number is not less than 0.5 then:
        else: 
            #subtract "1" from the value of agents[i][0]
            agents[i][0] = (agents[i][0] - 1) % height
            
        #move x coordinate
        #assign random number
        random_number = random.random() 
        #if this random number is less than 0.5 then:
        if random_number < 0.5: 
            #add "1" to the valueof agents[i][1] ((% height (x axis) to \
            #stop moving off the map))
            agents[i][1] = (agents[i][1] + 1) % width 
        #if random number is not less than 0.5 then:
        else: 
            #subtract "1" from the value of agents[i][1]
            agents[i][1] = (agents[i][1] - 1) % width 

#print the coordinates after the move
print("agents after the move", agents) 

#neaten the output up
#in the range of the length of the list of agents
for i in range(len(agents)):
    #print agents
    print("agents [i]", agents[i]) 
    #prints 10 sets of coordinates
    
    
#calculate the pythagorean distance
distance = (((agents[0][0] - agents[1][0])**2) + \
            ((agents[0][1] - agents[1][1])**2))**0.5
#print the value for the pythagorean distance
print("pythagorean distance", distance)


#calculte which agent is furthest east
#print maximum y and x (
print ("max agents", max(agents))
#prints [62, 33]

#calculate which agent is furthest west
#print minimum y and x
print ("min agents", min(agents)) 
#prints [4, 75]


print(max(agents, key=operator.itemgetter(1)))

#create scatterplot axis to be of the previously defined height and width
matplotlib.pyplot.ylim(0, height -1)
matplotlib.pyplot.xlim(0, width -1)

matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(99, 47, color='red')
matplotlib.pyplot.show()

#for the range of the number of agents (10)
for i in range(num_of_agents):
    #create scatter plot
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0]) 
    
#turning top agent black
#defining top agent as the maximum agent in the y dimension
#use of (0) to represent y axis dimension
top = max(agents, key=operator.itemgetter(0)) 
#change the colour of the most north agent black
matplotlib.pyplot.scatter(top[1], top[0], color='black') 

#turning bottom agent red
#defining bottom agent as the minimum agent in y dimension
#use of (0) to represent y axis dimension
bottom = min(agents, key=operator.itemgetter(0)) 
#change the colour of the most south agent red
matplotlib.pyplot.scatter(bottom[1], bottom[0], color='red') 

#turning left agent pink
#defining the left agent as the minimun agent in the x dimension 
#use of (1) ro represent x axis dimension
left = min(agents, key=operator.itemgetter(1))
#change the colour of the most west agent pink
matplotlib.pyplot.scatter(left[1], bottom[0], color='pink') 

#turning right agent yellow
#defining the right agent as the maximum agent in the x dimension
#use of (1) ro represent x axis dimension
right = max(agents, key=operator.itemgetter(1)) 
#change the colour of the most east agent yellow
matplotlib.pyplot.scatter(right[1], right[0], color='yellow') 

#shows plot
matplotlib.pyplot.show() 
















