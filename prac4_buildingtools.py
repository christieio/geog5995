# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:27:02 2021

@author: Christie
"""

#import matplotlib.pyplot to create visualisations (plot)
import matplotlib.pyplot
#import operator module to access efficient functions
import operator
#import random module to access random functions
import random
#to time how long a set of code takes to run (execution time)
#time takes longer the higher number of agents you have
import time 

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)

#start timing execution of code from here:
start = time.time() 
    
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

#make the agents
#assigning a random number to coordinates y and x
#for the range of number of agents 
for i in range(num_of_agents):
    #assign random number within the defined height and range
     agents.append([random.randint(0, height-1),random.randint(0, width-1)])

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


#create a function to return distance between a and b
#two arguments a & b, pretending that these are lists of coordinates
#agent 0 is a, agent 1 is b  
def distance_between (a, b): 
    #returning the answer for the pythagorean distance
    return (((a[0] - b[0])**2) 
                     + ((a[1] - b[1])**2))**0.5
    
#calling upon function just created (distance_between)
#note how a corresponds to agents[0] and b to agents[1]
max_dist = distance_between(agents[0], agents[1])
min_dist = max_dist


#using a for loop to calculate output for ALL sets of agents
#use -1 to stop us going over the range /out of range as using +1 further down
#for y in range of the number of agents then
for i in range(num_of_agents):
    #for x in range of the number of agents then:
    for j in range(num_of_agents):
        #calls on function to provide answer for distance
        #answer = distance between all agents in list
        answer = distance_between(agents[i], agents[j])
        #maximum distance is the answer with the highest distance
        max_dist = max(max_dist, answer)
        #minimum distance is the answer with the smallest distance
        min_dist = min(min_dist, answer)
        #print iteration number
        print("iteration", [i])
        #prints answers for all iterations
        print("answer", answer)
        #print max distance for each iteration
        print("max dist", max_dist)
        #print min distance for each iteration
        print("min dist", min_dist)



#create scatterplot axis to be of the previously defined height and width
matplotlib.pyplot.ylim(0, height -1)
matplotlib.pyplot.xlim(0, width -1)
#in the range of the number of agents
for i in range(num_of_agents):
    #plot the agents 
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
#show the plot
matplotlib.pyplot.show()

#end timing code execution time from here
end = time.time()

#print the execution time 
print("time = " + str(end - start))

