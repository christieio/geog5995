# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:23:48 2021

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
#import the module agentframework5 we created
import agentframework5

#create a function to return distance between agents_row_a and agents_row_b
def distance_between(agents_row_a, agents_row_b):
    #return the pythagorean distance
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

#assign the random seed for repeatability
#ensures same random numbers generated on each run
random.seed(0)
    
#creation of ten agents
#assign the value "10" to the label "num_of_agents"
num_of_agents = 10

#creation of number of iterations 
#assign the value "100" to the label "num_of_iterations"
num_of_iterations = 100

#create an empty list an assign it to the label "agents"
agents = [] 

#start timing execution of code from here:
start = time.time() 

#make the agents
#for the range of number of agents 
for i in range(num_of_agents):
    #assign value to agents from agentframework5 (random number)
    agents.append(agentframework5.Agent())

#move the agents
#for the number of iterations
for j in range(num_of_iterations):
    #for the range of the number of agents
    for i in range(num_of_agents):
        #move the agents (refer to agentframework5)
        agents[i].move()
       
#create plot y and x axis
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
#for the range of the number of agents
for i in range(num_of_agents):
    #plot the agents
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#show plot
matplotlib.pyplot.show()

#calling on distance_between function from top of code:
#for the agents in row a
for agents_row_a in agents:
    #for the agents in row b
    for agents_row_b in agents:
        #return the pythagorean distance
        distance = distance_between(agents_row_a, agents_row_b)
        #turn on line directly below to return values for pythagorean dist
        #print("pythagorean distance", distance_between)

#assign the value "3" to x
x = 3
#'.' accesses code inside object (agent)
#assign agentframework5.Agent() to the label "a"
a = agentframework5.Agent()
#go to a (agentframework5.py), look inside and find the y variable \
#inside it and print
print(a.y) 
#go to a (agentframework5.py), look inside and find the x variable \ 
#inside it and print
print(a.x)
#prints values for y and x
print(a.y, a.x)
print(x)

#calling on move function (defined in agentframework)
a.move()

#print coordinates 
#prints after move
print(a.y, a.x)
#prints "81, 83" in output

#end timing code execution time from here
end = time.time()

#print the execution time 
print("time = " + str(end - start))